# Week 3 Day 2 Report

## Objective

Implement an imbalanced classification pipeline for predictive maintenance using SMOTE and LightGBM.

The main goal was to handle machine failure class imbalance and build a reliable validation workflow.

---

## Tasks Completed

### 1. Data Preparation

- Loaded the final feature dataset generated during Week 2.
- Used:

model_ready_dataset.csv


- Separated:

Features:
- Sensor telemetry features
- Contextual features
- Engineered features


Target:
- Machine failure


---

## 2. Class Imbalance Analysis

Machine failure data contains fewer failure samples compared to normal operation samples.

Performed:

- Class distribution analysis
- Failure percentage calculation


Reason:

Machine failure cases represent a minority class, requiring imbalance handling techniques.

---

## 3. Stratified 5-Fold Cross Validation

Implemented:

StratifiedKFold


Configuration:

- Number of folds: 5
- Shuffle: Enabled
- Random state: 42


Purpose:

Maintain the same failure/normal class distribution in every fold.

---

## 4. SMOTE Implementation

Implemented:

Synthetic Minority Oversampling Technique (SMOTE)


Workflow:

```
             Dataset
                ↓
       Stratified fold split
                ↓
    Apply SMOTE on training data
                ↓
       Balance minority class
                ↓
        Train classifier
                ↓
Validate on original validation data
```


This prevents data leakage during evaluation.

---

## 5. LightGBM Model Training

Implemented:

LightGBM Classifier


Model configuration:

- Random state: 42


The model was trained using SMOTE-balanced training data.

---

## 6. Model Evaluation

Evaluated model performance using:

- Accuracy
- Precision
- Recall
- F1 Score


Generated:

week3_cv_results.csv


Location:

data/processed/week3_cv_results.csv


---

## Final Pipeline
