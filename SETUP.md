# 🚀 Setup Instructions

## Download Dataset

The Telecom Customer Churn dataset needs to be downloaded separately from Kaggle:

### Option 1: Download from Kaggle Web UI (Easiest)
1. Go to: https://www.kaggle.com/blastchar/telco-customer-churn
2. Click **Download** (you'll need a Kaggle account)
3. Extract the CSV file to `data/` folder
4. Rename it to: `WA_Fn-UseC_-Telco_Customer_Churn.csv`

### Option 2: Download via Kaggle API (Advanced)
```bash
# Install Kaggle CLI
pip install kaggle

# Download dataset (requires API credentials)
kaggle datasets download -d blastchar/telco-customer-churn -p ./data/

# Unzip
unzip ./data/telco-customer-churn.zip -d ./data/
```

## Environment Setup

### 1. Create Virtual Environment
```bash
# Navigate to project folder
cd customer-churn-analysis

# Create venv
python -m venv venv

# Activate
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start Jupyter
```bash
jupyter notebook
```

Then open: `notebooks/churn_analysis.ipynb`

## Project Structure
```
customer-churn-analysis/
├── README.md              # Main documentation
├── SETUP.md              # This file
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
├── data/
│   └── WA_Fn-UseC_-Telco_Customer_Churn.csv  ← Download here
├── notebooks/
│   └── churn_analysis.ipynb  # Main analysis notebook
└── visualizations/
    └── (Generated outputs)
```

## Troubleshooting

### "No such file or directory" for CSV
→ Make sure dataset is in `data/` folder with exact name: `WA_Fn-UseC_-Telco_Customer_Churn.csv`

### Jupyter kernel issues
```bash
# Reinstall kernel
python -m ipykernel install --user --name venv --display-name "Python (venv)"
```

### Library import errors
```bash
# Update pip and reinstall
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## Running the Analysis

1. Download the dataset (see above)
2. Open Jupyter: `jupyter notebook`
3. Open `notebooks/churn_analysis.ipynb`
4. Run all cells: **Kernel → Run All**
5. View results, visualizations, and insights

Enjoy! 🎉
