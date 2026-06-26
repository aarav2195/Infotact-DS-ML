# Week 3 Summary

## Objective

Implement machine failure prediction using imbalanced classification techniques and LightGBM.

---

## Completed Work

### 1. Imbalance Handling

- Analyzed machine failure class distribution
- Applied SMOTE technique
- Prevented data leakage by applying SMOTE only on training folds

---

### 2. Cross Validation

Implemented:

- Stratified 5-Fold Cross Validation

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1 Score

---

### 3. LightGBM Modeling

Implemented:

- LightGBM classifier
- Baseline model training
- Hyperparameter tuning

Parameters optimized:

- n_estimators
- learning_rate
- num_leaves

---

### 4. Final Model Evaluation

Generated:

- Final predictions
- Classification report
- Confusion matrix

---

### 5. Model Analysis

Performed:

- Feature importance analysis
- Prediction error analysis

---

## Generated Files

- week3_cv_results.csv
- lightgbm_tuning_results.csv
- final_model_results.csv
- feature_importance.csv

---

## Outcome

Successfully developed an imbalanced classification pipeline for predictive maintenance fault detection.