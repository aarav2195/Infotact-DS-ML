# Predictive Maintenance using Industrial IoT Telemetry

## Overview

This project implements an end-to-end predictive maintenance pipeline using industrial IoT sensor telemetry data.

The objective is to analyze machine operating conditions, process time-series sensor data, integrate contextual information, engineer meaningful features, and build machine learning models to predict possible machine failures before breakdown.


## Dataset

AI4I 2020 Predictive Maintenance Dataset

The dataset contains industrial machine operating parameters:

- Air temperature
- Process temperature
- Rotational speed
- Torque
- Tool wear
- Machine failure status


## Project Workflow

```
Data Ingestion
        ↓
Signal Processing
        ↓
Feature Engineering
        ↓
Contextual Data Fusion
        ↓
Feature Selection
        ↓
Imbalanced Classification Handling
        ↓
SMOTE Based Training Pipeline
        ↓
LightGBM Model Training
        ↓
Threshold Tuning
        ↓
Noise Sensitivity Analysis
        ↓
Interactive Dashboard
```


# Project Status


## Week 1: IoT Telemetry Ingestion and Signal Processing

Completed:

- Project setup and data pipeline creation
- Industrial telemetry dataset ingestion
- Sensor data exploration
- Time-series signal processing
- Rolling statistical feature generation


Created features:

- Rolling Mean
- Rolling Standard Deviation
- Rolling Variance



## Week 2: Contextual Data Fusion and Feature Engineering

Completed:

- External context simulation
- Timestamp based telemetry and context merging
- Context feature engineering
- Feature interaction creation
- Ablation study between sensor-only and context-enhanced data
- Feature importance analysis
- Final model-ready dataset preparation


Generated:

- baseline_features.csv
- context_fused_dataset.csv
- ablation_results.csv
- model_ready_dataset.csv



## Week 3: Imbalanced Classification and LightGBM Modeling

Completed:

- Machine failure class imbalance analysis
- Stratified 5-Fold Cross Validation pipeline
- SMOTE implementation inside cross-validation workflow
- LightGBM classifier training
- Hyperparameter tuning
- Final model training
- Model performance evaluation
- Feature importance analysis
- Prediction error analysis


Machine Learning Pipeline:

```
           Dataset
              ↓
   Stratified 5 Fold Split
              ↓
SMOTE applied on training folds
              ↓
      LightGBM Classifier
              ↓
     Performance Evaluation
```


Generated:

- week3_cv_results.csv
- lightgbm_tuning_results.csv
- final_model_results.csv
- feature_importance.csv


## Week 4: Noise Sensitivity Analysis and Deployment

Completed:

- Threshold tuning
- Precision-Recall evaluation
- Noise robustness analysis
- Final model serialization
- Deployment modules
- Interactive Streamlit dashboard

Generated:

- app.py
- dashboard.py

# Project Structure

```
Project-1-Predictive-Maintenance

├── app
│   └── app.py
│
├── data
│   ├── external
│   │   └── external_context.csv
│   │
│   ├── processed
│   │   ├── signal_features.csv
│   │   ├── baseline_features.csv
│   │   ├── context_fused_dataset.csv
│   │   ├── ablation_results.csv
│   │   ├── week2_final_features.csv
│   │   ├── model_ready_dataset.csv
│   │   ├── week3_cv_results.csv
│   │   ├── lightgbm_tuning_results.csv
│   │   ├── final_model_results.csv
│   │   ├── feature_importance.csv
│   │   ├── noise_sensitivity_results.csv
│   │   ├── threshold_tuning_results.csv
│   │   ├── robustness_comparison.csv
│   │   └── deployment_validation_results.csv 
│   │
│   └── raw
│       └── ai4i2020.csv
│
├── models
│   ├── final_lightgbm_model.pkl
│   └── lightgbm_model.pkl
│
├── notebooks
│   ├── 01_data_ingestion.ipynb
│   ├── 02_signal_processing.ipynb
│   ├── 03_context_fusion.ipynb
│   ├── 04_ablation_study.ipynb
│   ├── 05_context_feature_engineering.ipynb
│   ├── 06_feature_selection.ipynb
│   ├── 07_week2_validation.ipynb
│   ├── 08_ml_pipeline_setup.ipynb
│   ├── 09_lightgbm_tuning.ipynb
│   ├── 10_final_lightgbm_evaluation.ipynb
│   ├── 11_model_analysis.ipynb
│   ├── 12_noise_sensitivity_results.ipynb
│   ├── 13_precision_recall_threshold_tuning.ipynb
│   ├── 14_robustness_comparison.ipynb
│   └── 15_deployment_validation.ipynb
│
├── reports
│   ├── week-1
│   │   ├── day2_report.md
│   │   ├── day3_signal_analysis.md
│   │   ├── day4_feature_engineering.md
│   │   └── week1_summary.md
│   │
│   ├── week-2
│   │   ├── day1_context_fusion.md
│   │   ├── day2_ablation_study.md
│   │   ├── day3_context_feature_engineering.md
│   │   ├── day4_feature_selection.md
│   │   ├── day5_validation.md
│   │   └── week2_summary.md
│   │
│   ├── week-3
│   │   ├── day1_ml_setup.md
│   │   ├── day2_smote_lightgbm.md
│   │   ├── day3_lightgbm_tuning.md
│   │   ├── day4_final_model.md
│   │   ├── day5_model_analysis.md
│   │   └── week3_summary.md
│   │
│   ├── week-4
│       ├── day1_noise_analysis.md
│       ├── day2_threshold_tuning.md
│       ├── day3_robustness_analysis.md
│       ├── day4_deployment_validation.md
│       ├── day5_dashboard.md
│       └── week4summary.md
│
├── dashboard.py
├── README.md
└── requirements.txt
```


## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- LightGBM
- Jupyter Notebook
- Matplotlib
- Streamlit
- Git & GitHub

## Interactive Dashboard

An interactive Streamlit dashboard has been developed to demonstrate the predictive maintenance model.

Features include:

- Machine parameter input
- Automatic feature engineering
- Real-time failure prediction
- Failure probability estimation
- Maintenance recommendations

Run the dashboard locally:

```bash
streamlit run dashboard.py
```

## Current Status

Completed:

✅ Industrial IoT telemetry processing  
✅ Time-series feature engineering  
✅ Contextual data integration  
✅ Ablation analysis  
✅ Feature selection  
✅ Machine failure classification pipeline  
✅ SMOTE based imbalance handling  
✅ Stratified Cross Validation  
✅ LightGBM model training  
✅ Model evaluation and analysis
✅ Threshold tuning
✅ Noise sensitivity analysis
✅ Model deployment
✅ Interactive Streamlit dashboard


## Future Work

- Integrate live industrial IoT sensor streams.
- Deploy the dashboard on Streamlit Community Cloud.
- Implement real-time alert notifications.
- Support multiple machine monitoring.
- Explore deep learning models for predictive maintenance.


## How to Run

Install dependencies:

```
pip install -r requirements.txt
```

Launch Jupyter:

```
jupyter notebook
```

Run notebooks in sequence:

```
01_data_ingestion.ipynb
02_signal_processing.ipynb
03_context_fusion.ipynb
04_ablation_study.ipynb
05_context_feature_engineering.ipynb
06_feature_selection.ipynb
07_week2_validation.ipynb
08_ml_pipeline_setup.ipynb
09_lightgbm_tuning.ipynb
10_final_lightgbm_evaluation.ipynb
11_model_analysis.ipynb
```


## Project Goal

To develop an industry-oriented predictive maintenance system capable of identifying early machine failure patterns using IoT telemetry and machine learning.