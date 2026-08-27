# Week 4 – Day 4: Model Comparison and Prediction Analysis

## Objective

Perform a professional comparison of XGBoost, Baseline GNN, and Attention GNN using the same held-out test properties.

## Work Completed

- Created a common 70/15/15 train-validation-test split.
- Retrained XGBoost using the same feature set and split used for the graph models.
- Aligned Baseline GNN and Attention GNN predictions with the common test set.
- Calculated RMSE, MAPE, MAE and R² for all three models.
- Calculated model changes relative to XGBoost.
- Performed property-price prediction error analysis.
- Performed price-range error analysis.
- Selected the best-performing model using test MAPE.
- Created a dashboard-ready prediction dataset.
- Generated model comparison and actual-versus-predicted visualizations.
- Saved the final comparison XGBoost model.

## Final Results

| Model | Test RMSE | Test MAPE | Test R² |
|---|---:|---:|---:|
| **XGBoost** | **$75,232.36** | **11.39%** | **0.9038** |
| Baseline GNN | $80,285.81 | 12.32% | 0.8905 |
| Attention GNN | $121,562.18 | 19.40% | 0.7490 |

## Model Ranking

1. **XGBoost – 11.39% MAPE**
2. **Baseline GNN – 12.32% MAPE**
3. **Attention GNN – 19.40% MAPE**

## Key Findings

The original Week 2 XGBoost benchmark achieved a MAPE of 17.31%.

For a controlled comparison, XGBoost was retrained using the same final feature set and the same test properties used by the GNN models. The common-test XGBoost model achieved a MAPE of **11.39%**.

The Baseline GNN achieved **12.32% MAPE**, while the Attention GNN achieved **19.40% MAPE**.

Therefore, XGBoost is the current best-performing model for deployment based on the common test-set evaluation.

## Generated Outputs

- `data/processed/week-3/gnn/day4/final_model_split.csv`
- `data/processed/week-3/gnn/day4/final_model_comparison.csv`
- `data/processed/week-3/gnn/day4/final_prediction_error_analysis.csv`
- `data/processed/week-3/gnn/day4/final_price_range_analysis.csv`
- `data/processed/week-3/gnn/day4/dashboard_predictions.csv`
- `models/xgboost_comparison.pkl`

## Visualizations

- `reports/week-4/visualizations/final_model_mape_comparison.png`
- `reports/week-4/visualizations/final_actual_vs_predicted.png`

## Notebook

`notebooks/17_model_comparison_analysis.ipynb`

## Outcome

Day 4 established a controlled three-model comparison and identified XGBoost as the best-performing model on the common test set.

The dashboard prediction pipeline will therefore use the selected best model while retaining GNN and Attention GNN predictions for comparison and analysis.

## Next Step

Complete the final Week 4 deployment stage and build the advanced modular Streamlit geospatial valuation dashboard.