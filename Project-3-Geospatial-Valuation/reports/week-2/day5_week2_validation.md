# Week 2 – Day 5: Final Validation and Week 2 Completion

## Objective

The objective of Day 5 was to validate the complete Week 2 baseline machine-learning pipeline and ensure that all datasets, trained models, predictions, evaluation results, and documentation were consistent and ready for the spatial modeling phase.

## Validation Performed

- Verified all required Week 2 datasets and model artifacts.
- Validated the training and holdout datasets.
- Confirmed the 80/20 train-test split.
- Checked for missing values.
- Checked for infinite values.
- Loaded the Linear Regression model successfully.
- Loaded the XGBoost model successfully.
- Regenerated holdout predictions.
- Verified that both models produced predictions for all 4,320 holdout properties.
- Validated the Day-4 evaluation results.
- Recalculated the improvement of XGBoost over Linear Regression.
- Verified prediction-error and price-range analysis outputs.

## Final Baseline Results

| Model | RMSE | MAPE | MAE | R² |
|---|---:|---:|---:|---:|
| Linear Regression | $129,959.74 | 23.50% | $99,623.90 | 0.7274 |
| **XGBoost** | **$103,398.17** | **17.31%** | **$75,525.97** | **0.8274** |

XGBoost achieved:

- 20.44% lower RMSE than Linear Regression.
- 26.34% lower MAPE than Linear Regression.
- Lower MAE.
- Higher R².

## Week 2 Outcome

Week 2 has been successfully completed.

The project now has a validated traditional machine-learning benchmark based on XGBoost Regression.

The completed Week 2 workflow is:

**Tabular Feature Engineering → Train/Test Split → Linear Regression → XGBoost → Model Evaluation → Error Analysis → Final Validation**

The XGBoost model achieved a final MAPE of **17.31%** and will serve as the benchmark for the spatial modeling phase.

## Next Phase

The project will now move to Week 3: **Spatial Embeddings and Graph Construction**.

The next phase will construct a K-Nearest Neighbor graph in which properties are represented as nodes and geographically nearby properties are connected through graph edges.

Spatial and property-level features will then be prepared for spatial embedding and Graph Neural Network modeling.

## Validation Status

**Week 2 – Completed ✅**