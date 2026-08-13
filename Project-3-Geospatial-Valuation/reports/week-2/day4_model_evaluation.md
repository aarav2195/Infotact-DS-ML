# Week 2 – Day 4: Model Evaluation and Error Analysis

## Objective

The objective of Day 4 was to formally evaluate the traditional machine-learning baselines developed during Week 2.

The Linear Regression and XGBoost models were evaluated using the same holdout dataset to ensure a fair comparison. The evaluation focused primarily on RMSE and MAPE, as specified in the project requirements.

Additional MAE, R², prediction-error, and price-range analyses were also performed to understand model behavior.

## Evaluation Setup

The models were evaluated on a common holdout dataset containing **4,320 properties**.

The two evaluated models were:

* Linear Regression
* XGBoost Regression

Using the same holdout observations ensured that the performance comparison was consistent and unbiased.

## Model Performance

| Model             |            RMSE |       MAPE |            MAE |         R² |
| ----------------- | --------------: | ---------: | -------------: | ---------: |
| Linear Regression |     $129,959.74 |     23.50% |     $99,623.90 |     0.7274 |
| **XGBoost**       | **$103,398.17** | **17.31%** | **$75,525.97** | **0.8274** |

Lower RMSE, MAPE, and MAE indicate better prediction performance, while a higher R² indicates better explanatory performance.

## Baseline Model Comparison

XGBoost produced better results than Linear Regression across all primary evaluation measures.

Compared with Linear Regression:

* RMSE improved by **20.44%**.
* MAPE improved by **26.34%**.
* MAE decreased substantially.
* R² increased from **0.7274** to **0.8274**.

Therefore, XGBoost was selected as the stronger traditional machine-learning baseline for the next stages of the project.

## Prediction Error Analysis

A detailed prediction-error dataframe was generated containing:

* Actual property price
* Linear Regression prediction
* XGBoost prediction
* Absolute prediction errors
* Percentage prediction errors

The analysis showed that prediction accuracy varies across individual properties.

Some properties exhibited considerably larger prediction errors than others, demonstrating that conventional tabular models do not capture every factor influencing property valuation.

## Price-Range Error Analysis

XGBoost prediction errors were additionally analyzed across property-price ranges.

| Price Range | Properties | XGBoost MAPE |
| ----------- | ---------: | -----------: |
| Below $300K |        934 |       27.31% |
| $300K–$500K |      1,586 |       16.31% |
| $500K–$750K |      1,106 |       14.29% |
| $750K–$1M   |        401 |       12.15% |
| Above $1M   |        293 |        9.34% |

The highest percentage error was observed for properties below $300K, while the lowest percentage error was observed for properties above $1M.

This indicates that model performance is not uniform across the property-price distribution.

## Actual vs Predicted Analysis

Actual-versus-predicted visualizations were generated for both models.

The visualizations were used to inspect how closely predictions followed the ideal prediction relationship.

XGBoost showed a stronger overall fit than Linear Regression, consistent with its lower RMSE and MAPE and higher R² score.

## Business Interpretation

The results demonstrate that nonlinear machine-learning methods can provide a stronger traditional baseline for real estate valuation than a simple linear model.

However, even the XGBoost model still produces meaningful prediction errors for certain properties and price ranges.

More importantly, the current baseline primarily relies on conventional property-level features. It does not explicitly model the influence of nearby properties and neighborhood relationships.

This limitation is directly relevant to the project's core objective of introducing spatial dependencies into property valuation.

## Generated Outputs

The following evaluation artifacts were generated:

* `data/processed/week-2/model_evaluation.csv`
* `data/processed/week-2/prediction_error_analysis.csv`
* `data/processed/week-2/price_range_error_analysis.csv`
* `data/processed/week-2/predictions/model_prediction_comparison.csv`

The evaluation notebook is:

* `notebooks/07_model_evaluation.ipynb`

## Day 4 Outcome

Day 4 successfully completed the formal evaluation of the traditional machine-learning baselines.

The final benchmark is:

**Linear Regression → XGBoost**

with XGBoost achieving:

* **RMSE: $103,398.17**
* **MAPE: 17.31%**
* **MAE: $75,525.97**
* **R²: 0.8274**

XGBoost will therefore serve as the primary traditional ML benchmark for the spatial modeling stages.

## Next Step

Day 5 will focus on Week 2 validation and documentation.

The completed baseline results will then be carried forward into Week 3, where the project will introduce K-Nearest Neighbor graph construction and spatial embeddings to explicitly model relationships between nearby properties.
