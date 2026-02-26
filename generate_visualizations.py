"""
Script to generate missing visualizations for Customer Churn Analysis
Requires: pandas, numpy, matplotlib, seaborn, scikit-learn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix
import warnings
import os

warnings.filterwarnings('ignore')

def load_data():
    """Load and prepare data for visualization"""
    # Check if data exists
    data_path = 'data/WA_Fn-UseC_-Telco_Customer_Churn.csv'
    if not os.path.exists(data_path):
        raise FileNotFoundError(
            f"Dataset not found at {data_path}\n"
            "Please run: python download_dataset.py\n"
            "Or download from: https://www.kaggle.com/blastchar/telco-customer-churn"
        )
    
    df = pd.read_csv(data_path)
    return df

def prepare_model(df):
    """Prepare data and train model"""
    df_model = df.copy()
    df_model['Churn'] = (df_model['Churn'] == 'Yes').astype(int)
    df_model['TotalCharges'] = pd.to_numeric(df_model['TotalCharges'], errors='coerce')
    df_model['TotalCharges'].fillna(df_model['TotalCharges'].median(), inplace=True)
    df_model = df_model.drop('customerID', axis=1)
    
    categorical_columns = df_model.select_dtypes(include=['object']).columns
    df_encoded = pd.get_dummies(df_model, columns=categorical_columns, drop_first=True)
    
    X = df_encoded.drop('Churn', axis=1)
    y = df_encoded['Churn']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    return model, X, X_test_scaled, y_test, scaler

def plot_roc_curve(model, X_test_scaled, y_test):
    """Generate ROC Curve"""
    y_pred_proba = model.predict_proba(X_test_scaled)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    auc_score = roc_auc_score(y_test, y_pred_proba)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(fpr, tpr, linewidth=3, color='#1f77b4', label=f'ROC Curve (AUC = {auc_score:.3f})')
    ax.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Random Classifier')
    ax.set_xlabel('False Positive Rate', fontsize=12, fontweight='bold')
    ax.set_ylabel('True Positive Rate', fontsize=12, fontweight='bold')
    ax.set_title('ROC Curve - Model Performance', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, loc='lower right')
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('visualizations/04_roc_curve.png', dpi=300, bbox_inches='tight')
    print("✅ ROC Curve saved: visualizations/04_roc_curve.png")
    plt.close()

def plot_correlation_heatmap(df_encoded):
    """Generate Correlation Heatmap"""
    correlations = df_encoded.corr()['Churn'].sort_values(ascending=False)
    top_features = pd.concat([correlations.head(8), correlations.tail(7)])[1:]
    
    corr_matrix = df_encoded[top_features.index.tolist() + ['Churn']].corr()
    
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='RdYlGn', center=0,
                cbar_kws={'label': 'Correlation Coefficient'}, ax=ax, linewidths=0.5)
    ax.set_title('Feature Correlation Matrix (Top Features vs Churn)', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('visualizations/05_correlation_heatmap.png', dpi=300, bbox_inches='tight')
    print("✅ Correlation Heatmap saved: visualizations/05_correlation_heatmap.png")
    plt.close()

def plot_feature_importance(model, X):
    """Generate Feature Importance"""
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'coefficient': np.abs(model.coef_[0])
    }).sort_values('coefficient', ascending=True).tail(12)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    colors = ['#d62728' if x > 0 else '#2ca02c' for x in feature_importance['coefficient']]
    ax.barh(feature_importance['feature'], feature_importance['coefficient'], color=colors, alpha=0.7, edgecolor='black')
    ax.set_xlabel('Absolute Coefficient Value', fontsize=12, fontweight='bold')
    ax.set_title('Top 12 Features - Feature Importance (Logistic Regression)', fontsize=14, fontweight='bold')
    ax.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig('visualizations/06_feature_importance.png', dpi=300, bbox_inches='tight')
    print("✅ Feature Importance saved: visualizations/06_feature_importance.png")
    plt.close()

def plot_confusion_matrix(model, X_test_scaled, y_test):
    """Generate Confusion Matrix"""
    y_pred = model.predict(X_test_scaled)
    cm = confusion_matrix(y_test, y_pred)
    
    fig, ax = plt.subplots(figsize=(8, 7))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, ax=ax,
                xticklabels=['No Churn', 'Churn'], yticklabels=['No Churn', 'Churn'],
                annot_kws={'size': 14, 'fontweight': 'bold'})
    ax.set_ylabel('Actual', fontsize=12, fontweight='bold')
    ax.set_xlabel('Predicted', fontsize=12, fontweight='bold')
    ax.set_title('Confusion Matrix', fontsize=14, fontweight='bold', pad=20)
    
    accuracy = (cm[0,0] + cm[1,1]) / cm.sum()
    precision = cm[1,1] / (cm[1,1] + cm[0,1])
    recall = cm[1,1] / (cm[1,1] + cm[1,0])
    
    textstr = f'Accuracy: {accuracy:.1%}\nPrecision: {precision:.1%}\nRecall: {recall:.1%}'
    ax.text(2.5, 0.5, textstr, fontsize=11, fontweight='bold', 
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('visualizations/07_confusion_matrix.png', dpi=300, bbox_inches='tight')
    print("✅ Confusion Matrix saved: visualizations/07_confusion_matrix.png")
    plt.close()

def main():
    """Main execution"""
    print("🚀 Generating visualizations...\n")
    
    try:
        # Load and prepare
        df = load_data()
        print("✅ Dataset loaded")
        
        # Prepare model
        model, X, X_test_scaled, y_test, scaler = prepare_model(df)
        print("✅ Model trained")
        
        # Ensure visualizations directory exists
        os.makedirs('visualizations', exist_ok=True)
        
        # Generate visualizations
        plot_roc_curve(model, X_test_scaled, y_test)
        
        # Need to recreate df_encoded for correlation
        df_model = df.copy()
        df_model['Churn'] = (df_model['Churn'] == 'Yes').astype(int)
        categorical_columns = df_model.select_dtypes(include=['object']).columns
        df_encoded = pd.get_dummies(df_model, columns=categorical_columns, drop_first=True)
        
        plot_correlation_heatmap(df_encoded)
        plot_feature_importance(model, X)
        plot_confusion_matrix(model, X_test_scaled, y_test)
        
        print("\n🎉 All visualizations generated successfully!")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
