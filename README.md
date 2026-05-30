# Bulldozer Sale Price Prediction

This repository contains a machine learning project focused on predicting bulldozer sale prices using historical auction data from Kaggle's Blue Book for Bulldozers competition. The project applies regression analysis techniques to estimate prices based on various equipment specifications, usage patterns, and sale timing.

## Project Overview

The goal of this project is to build a machine learning model that accurately predicts the future sale price of bulldozers given their characteristics and historical sales data. This is a regression problem where we minimize the Root Mean Squared Logarithmic Error (RMSLE) metric.

## Dataset

- **Source**: Kaggle Blue Book for Bulldozers Competition
- **Training Set**: Historical data through end of 2011
- **Validation Set**: Data from January 1, 2012 - April 30, 2012
- **Features**: Equipment specifications, usage history, auction details, and market conditions

## Project Structure

```
Bulldozer-Sale-Price/
├── Bulldozer.ipynb       # Main Jupyter notebook with complete analysis and modeling
├── README.md             # This file
├── .gitattributes        # Git LFS configuration for large CSV files
└── Data/                 # Dataset files (tracked with Git LFS)
    ├── TrainAndValid.csv # Combined training and validation data
    └── train_tmp.csv     # Temporary training file
```

## Methodology

The project follows a structured machine learning workflow:

1. **Data Exploration**: Analyze features, distributions, and relationships
2. **Data Preprocessing**: Handle missing values, outliers, and feature engineering
3. **Model Development**: Train and evaluate various regression models
4. **Hyperparameter Tuning**: Optimize model performance
5. **Evaluation**: Assess results using RMSLE metric

## Key Features

- Comprehensive exploratory data analysis (EDA)
- Data preprocessing and feature engineering
- Multiple regression model implementations
- Model comparison and evaluation
- Visualization of patterns and insights

## Requirements

- Python 3.7+
- Jupyter Notebook
- pandas, NumPy, scikit-learn
- matplotlib, seaborn for visualization
- Other dependencies specified in notebook imports

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/arnavjaiswal18/Bulldozer-Sale-Price.git
   cd Bulldozer-Sale-Price
   ```

2. Install required packages:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn
   ```

3. Open the Jupyter notebook:
   ```bash
   jupyter notebook Bulldozer.ipynb
   ```

## Large Files

This repository uses Git Large File Storage (Git LFS) to handle large CSV files. Make sure Git LFS is installed:

```bash
git lfs install
```

Large CSV files are tracked with LFS and will be automatically handled when cloning.

## Results

The model evaluation and results are documented in the main notebook. The project demonstrates the application of machine learning to real-world regression problems in the heavy equipment sales domain.

## Author

arnavjaiswal18

## License

This project is based on the Kaggle Blue Book for Bulldozers competition dataset.
