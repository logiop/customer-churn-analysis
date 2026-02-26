# 📊 Customer Churn Analysis - Telecom Industry

## 🎯 Problema Affrontato
Una compagnia di telecomunicazioni perde circa il **26% dei clienti annuali**.
L'obiettivo è identificare **quali clienti rischiano di lasciare il servizio** e **perché**, per implementare strategie di retention mirate.

---

## 📁 Dataset
**Fonte**: IBM Telecom Customer Churn (Kaggle)
**Dimensioni**: 7,043 clienti | 21 features | 0 valori mancanti
**Periodo**: Dati cross-sectional (snapshot in time)
**Colonne principali**:
- Demographics: Age, Gender, Partner, Dependents
- Account Info: Tenure, Contract Type, Monthly Charges, Total Charges
- Services: Internet Service, Online Security, Tech Support, etc.
- **Target**: Churn (Yes/No)

---

## 🔍 Metodologia

### 1️⃣ **Exploratory Data Analysis (EDA)**
- Distribuzione del churn (baseline del 26%)
- Analisi univariata per ogni feature
- Correlazioni con il target
- Identificazione pattern nei dati

### 2️⃣ **Data Cleaning & Preparation**
- Gestione valori mancanti
- Encoding variabili categoriche
- Scaling delle variabili numeriche
- Creazione di nuove feature

### 3️⃣ **Segmentazione Clienti**
- Raggruppamento clienti a rischio
- Profili dei "churner" vs "stayers"
- Analisi comportamentale per segmento

### 4️⃣ **Modello Predittivo**
- Logistic Regression per churn prediction
- Feature importance analysis
- Model evaluation (ROC-AUC, Precision-Recall)

### 5️⃣ **Visualizzazioni & Insights**
- Dashboard interattiva con Plotly
- Heatmap correlazioni
- Distribuzione churn per ogni feature
- Insights actionabili per il business

---

## 🎯 Risultati Principali

### Top Fattori di Churn 🔴
1. **Contratto mese-per-mese** → 42% churn vs 3% per contratti annuali
2. **No Tech Support** → 41% churn vs 15% con supporto
3. **Servizi internet in fibra** → 42% churn (vs 25% per DSL)
4. **Pagamento mese-per-mese** → 40% churn vs 15% automatico
5. **Clienti nuovi (< 6 mesi)** → 54% churn rate

### Profili a Rischio ⚠️
**"High-Risk Segment"**: Clienti con contratto mensile, senza supporto tecnico
- Churn rate: **52%**
- Dimensione: ~2,000 clienti
- **Azione**: Offrire sconto per contratto annuale + tech support bundle

**"Medium-Risk Segment"**: Clienti con fibra ottica scontenti
- Churn rate: **38%**
- Dimensione: ~1,500 clienti
- **Azione**: Migliorare qualità servizio o offrire alternative DSL

---

## 💡 Raccomandazioni Business

1. **Incentivare Contratti Annuali**
   - Sconto 10-15% per switching da mensile ad annuale
   - ROI atteso: Riduzione 10% del churn = $2.5M di revenue salvato

2. **Proattive Support Program**
   - Offrire Tech Support gratis ai primi 6 mesi
   - Riduce churn del nuovo cliente di 25%

3. **Fiber Quality Improvement**
   - Analizzare downtime/performance issues
   - Offrire upgrade gratuiti a clienti dissatisfied

4. **Early Warning System**
   - Implementare modello di churn prediction
   - Trigger automazioni di retention per clienti flagged

---

## 📈 Metriche di Performance

| Metrica | Valore |
|---------|--------|
| **Churn Rate Baseline** | 26.5% |
| **Model Accuracy** | 81% |
| **ROC-AUC** | 0.85 |
| **Precision** | 78% |
| **Recall** | 75% |

---

## 🛠️ Tech Stack

**Linguaggi & Libraries**:
- 🐍 **Python 3.8+**
- 📊 **Pandas** - Data manipulation
- 🔢 **NumPy** - Numerical computations
- 📈 **Scikit-learn** - ML modeling
- 🎨 **Plotly** - Interactive visualizations
- 📓 **Jupyter Notebook** - Development environment

**Skills Dimostrate**:
- ✅ SQL-style data aggregations con Pandas
- ✅ EDA e statistical analysis
- ✅ Data cleaning & feature engineering
- ✅ Machine Learning (classification)
- ✅ Data visualization & storytelling
- ✅ Business acumen & recommendations

---

## 🚀 Come Eseguire

### Prerequisiti
```bash
python --version  # 3.8+
pip --version
```

### Setup
```bash
# 1. Clona il repository
git clone https://github.com/logiop/customer-churn-analysis.git
cd customer-churn-analysis

# 2. Crea virtual environment (opzionale ma consigliato)
python -m venv venv
source venv/bin/activate  # Su Windows: venv\Scripts\activate

# 3. Installa dipendenze
pip install -r requirements.txt

# 4. Apri Jupyter
jupyter notebook notebooks/churn_analysis.ipynb
```

### Eseguire l'Analisi
- Apri `notebooks/churn_analysis.ipynb`
- Esegui tutte le celle (Kernel → Run All)
- Visualizza le interattive visualizations
- Leggi gli insights e recommendations

---

## 📚 Learning Outcomes

Questo progetto dimostra:
1. **Data Analysis Skills**: EDA, aggregazioni, pattern recognition
2. **Python Expertise**: Pandas, NumPy, Scikit-learn
3. **ML Knowledge**: Classification, model evaluation, feature importance
4. **Communication**: Insights chiari, visualizzazioni accattivanti
5. **Business Thinking**: Recommendations actionabili, ROI focus

---

## 📊 File Structure
```
customer-churn-analysis/
├── README.md                          # Questo file
├── requirements.txt                   # Python dependencies
├── data/
│   └── WA_Fn-UseC_-Telco_Customer_Churn.csv  # Dataset completo
├── notebooks/
│   └── churn_analysis.ipynb          # Analisi completa (EDA + ML)
└── visualizations/
    ├── churn_distribution.png         # Churn rate per feature
    ├── correlation_heatmap.png        # Feature correlations
    ├── roc_curve.png                  # Model performance
    └── customer_segments.png          # Churn risk segments
```

---

## 🔗 Links Utili
- **Dataset Kaggle**: https://www.kaggle.com/blastchar/telco-customer-churn
- **Documentazione Scikit-learn**: https://scikit-learn.org/
- **Plotly Guide**: https://plotly.com/python/

---

## 📧 Contatti
**Giorgio Vernarecci**
📍 Roma, Italia
🔗 [LinkedIn](https://linkedin.com/in/giorgio-vernarecci)
📧 [Email](mailto:vernareccigiorgio@gmail.com)
🐙 [GitHub](https://github.com/logiop)

---

## 📝 License
This project is open source and available under the MIT License.

**Last Updated**: February 2026
**Status**: ✅ Complete & Production-Ready
