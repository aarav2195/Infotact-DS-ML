# Week 2 Summary – Baseline Machine Learning

## Overview

Week 2 focused on establishing the traditional machine-learning benchmark for the Real Estate Geospatial Valuation project.

The objective was to engineer standard tabular property features, develop baseline regression models, evaluate their performance, analyze prediction errors, and establish a reliable benchmark for comparison with the spatial and graph-based models planned for the later stages.

---

## Day 1 – Standard Tabular Feature Engineering

- Loaded the cleaned Week 1 housing dataset.
- Validated property-level numerical features.
- Engineered house-age features.
- Created renovation-related features.
- Calculated distance to Seattle city center.
- Created additional property-level ratio features.
- Handled missing and infinite values.
- Prepared the final ML-ready tabular dataset.

### Main Output

`data/processed/tabular_features.csv`

---

## Day 2 – Train/Test Split and Linear Regression Baseline

- Selected standard property and geographic features.
- Included `house_age`.
- Included `distance_to_city_center_km`.
- Created an 80/20 training and holdout split.
- Standardized numerical features.
- Trained a Linear Regression baseline.
- Generated holdout predictions.
- Saved the trained baseline model.

### Main Model

`models/linear_regression_baseline.pkl`

---

## Day 3 – XGBoost Baseline

- Trained an XGBoost Regression model.
- Used the same training and holdout datasets as the Linear Regression baseline.
- Generated holdout predictions.
- Compared XGBoost with Linear Regression.
- Saved the trained XGBoost model.

### Main Model

`models/xgboost_baseline.pkl`

---

## Day 4 – Model Evaluation and Error Analysis

Both baseline models were evaluated using the holdout dataset.

### Evaluation Metrics

- RMSE
- MAPE
- MAE
- R²

### Final Results

| Model | RMSE | MAPE | MAE | R² |
|---|---:|---:|---:|---:|
| Linear Regression | $129,959.74 | 23.50% | $99,623.90 | 0.7274 |
| **XGBoost** | **$103,398.17** | **17.31%** | **$75,525.97** | **0.8274** |

### XGBoost Improvement

Compared with Linear Regression:

- RMSE improved by **20.44%**.
- MAPE improved by **26.34%**.
- MAE decreased from **$99,623.90** to **$75,525.97**.
- R² improved from **0.7274** to **0.8274**.

XGBoost was therefore selected as the primary traditional machine-learning benchmark.

### Price-Range Error Analysis

Prediction errors were also analyzed across different property-price ranges.

The analysis showed that prediction error was not uniform across the housing market, with lower-priced properties showing higher percentage-based prediction error.

---

## Day 5 – Final Validation and Week 2 Completion

The complete Week 2 baseline machine-learning pipeline was validated.

### Validation Performed

- Verified all required Week 2 datasets.
- Verified trained model artifacts.
- Validated the training and holdout datasets.
- Confirmed the 80/20 train-test split.
- Checked missing values.
- Checked infinite values.
- Reloaded the Linear Regression model.
- Reloaded the XGBoost model.
- Regenerated holdout predictions.
- Verified prediction counts.
- Revalidated RMSE, MAPE, MAE and R² results.
- Verified prediction-error analysis outputs.
- Verified price-range analysis outputs.
- Finalized Week 2 documentation.

---

## Week 2 Outcome

Week 2 has been successfully completed.

The completed baseline workflow is:

**Tabular Feature Engineering → Train/Test Split → Linear Regression → XGBoost → Model Evaluation → Error Analysis → Final Validation**

The **XGBoost model achieved a final MAPE of 17.31%** and is now established as the traditional machine-learning benchmark for the project.

This benchmark will be used during the spatial modeling phase to determine whether incorporating neighborhood relationships and spatial dependencies can improve property valuation performance.

---

## Week 2 Deliverables

### Notebooks

- `04_tabular_feature_engineering.ipynb`
- `05_linear_regression_baseline.ipynb`
- `06_xgboost_baseline.ipynb`
- `07_model_evaluation.ipynb`
- `08_week2_validation.ipynb`

### Models

- `models/linear_regression_baseline.pkl`
- `models/xgboost_baseline.pkl`

### Evaluation Outputs

- `data/processed/week-2/model_evaluation.csv`
- `data/processed/week-2/prediction_error_analysis.csv`
- `data/processed/week-2/price_range_error_analysis.csv`
- `data/processed/week-2/predictions/model_prediction_comparison.csv`

---

## Week 2 Status

**Week 2 – Completed ✅**

### Next Phase

**Week 3 – Spatial Embeddings and Graph Construction**

The next phase will introduce spatial dependencies by representing properties as graph nodes and connecting geographically nearby properties through K-Nearest Neighbor relationships.

The spatial graph and embeddings will later be used for Graph Neural Network-based property valuation.