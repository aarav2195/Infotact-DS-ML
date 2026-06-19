# Predictive Maintenance using Industrial IoT Telemetry

## Overview

This project implements a predictive maintenance pipeline using industrial IoT sensor telemetry data.

The objective is to analyze machine operating conditions, process time-series sensor data, integrate contextual information, and prepare a machine learning ready dataset for predicting machine failures.


## Dataset

AI4I 2020 Predictive Maintenance Dataset

The dataset contains machine operational parameters such as:

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
Machine Learning Preparation
```


## Project status

### Week 1: IoT Telemetry Ingestion and Signal Processing

Completed:

- Project setup and data pipeline creation
- Industrial dataset ingestion
- Sensor data exploration
- Time-series signal processing
- Rolling statistical feature generation

Created features:

- Rolling Mean
- Rolling Standard Deviation
- Rolling Variance


### Week 2: Contextual Data Fusion and Feature Engineering

Completed:

- External context simulation
- Timestamp based telemetry and context merging
- Context feature engineering
- Feature interaction creation
- Ablation study between sensor-only and context-enhanced data
- Feature importance analysis
- Final model-ready dataset preparation

### Next Phase:

Machine learning model development and evaluation.


## Project Structure

```
Project-1-Predictive-Maintenance

├── data
│   ├── external
│   │   └── external_context.csv   
│   ├── processed
│   │   ├── signal_features.csv
│   │   ├── baseline_features.csv
│   │   ├── context_fused_dataset.csv
│   │   ├── ablation_results.csv
│   │   ├── week2_final_features.csv
│   │   └── model_ready_dataset.csv
│   └── raw
│       └── ai4i2020.csv
│
├── notebooks
│   ├── 01_data_ingestion.ipynb
│   ├── 02_signal_processing.ipynb
│   ├── 03_context_fusion.ipynb
│   ├── 04_ablation_study.ipynb
│   ├── 05_context_feature_engineering.ipynb
│   ├── 06_feature_selection.ipynb
│   └── 07_week2_validation.ipynb
│
├── reports
│   ├── week-1
│   │   ├── day2_report.md
│   │   ├── day3_signal_analysis.md
│   │   ├── day4_feature_engineering.md
│   │   └── week1_summary.md
│   └── week-2
│       ├── day1_context_fusion.md
│       ├── day2_ablation_study.md
│       ├── day3_context_feature_engineering.md
│       ├── day4_feature_selection.md
│       ├── day5_validation.md
│       └── week2_summary.md
│
├── README.md
└── requirements.txt
```


## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Git & GitHub


## Current Status

Completed:

✅ IoT telemetry processing  
✅ Feature engineering  
✅ Contextual data integration  
✅ Ablation analysis  
✅ Feature selection  
✅ Model-ready dataset preparation  


## Future Work

- Train machine learning models
- Evaluate prediction performance
- Build predictive maintenance application
