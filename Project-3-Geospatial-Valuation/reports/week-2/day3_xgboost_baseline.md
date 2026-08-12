# Week 2 – Day 3: XGBoost Regression Baseline

## Objective

The objective of Day 3 was to develop a stronger nonlinear machine-learning baseline for the Geospatial Real Estate Valuation project using XGBoost Regression.

The XGBoost model was trained using the same train/test split established during Day 2 so that its performance could be compared fairly with the Linear Regression baseline.

## Dataset and Features

The model used the Week 2 tabular feature representation prepared during the feature-engineering stage.

The baseline feature set included conventional property characteristics together with spatially relevant information such as:

* `house_age`
* `distance_to_city_center_km`

The training and holdout datasets generated during Day 2 were reused to maintain a consistent evaluation setup.

## Data Validation

Before training, the following checks were performed:

* Training and test feature sets were verified to be identical.
* Missing values were checked.
* Target data was validated.
* Training and holdout dataset dimensions were verified.

No new random train/test split was created so that Linear Regression and XGBoost would use the same holdout observations.

## XGBoost Model

An XGBoost Regressor was implemented to capture nonlinear relationships between property characteristics and house prices.

The baseline configuration used:

* 500 estimators
* Learning rate: 0.05
* Maximum tree depth: 6
* Subsample ratio: 0.8
* Column sampling ratio: 0.8
* Random state: 42

The model was trained using the training dataset and evaluated initially on the unseen holdout dataset.

## Prediction Analysis

The trained XGBoost model generated house-price predictions for the holdout dataset.

An error table was created containing:

* Actual Price
* Predicted Price
* Absolute Error

This provided an initial inspection of the model's prediction behavior before the formal evaluation stage.

## Baseline Metrics

Initial RMSE and MAPE values were calculated for the XGBoost model.

The Linear Regression model was also loaded and evaluated using the same holdout dataset.

This enabled a direct comparison between:

* Linear Regression
* XGBoost Regression

The final comparative analysis will be documented during Day 4.

## Feature Importance

XGBoost feature importance was calculated to identify which property-level variables contributed most strongly to the model's predictions.

This analysis provides an initial interpretation of the conventional tabular model and will later be contrasted with spatial relationships captured by graph-based models.

## Model Artifacts

The trained XGBoost model was saved as:

`models/xgboost_baseline.pkl`

Holdout predictions were saved as:

`data/processed/week-2/predictions/xgboost_predictions.csv`

The baseline comparison results were saved as:

`data/processed/week-2/baseline_model_comparison.csv`

## Outcome

Day 3 successfully established the XGBoost regression baseline.

The project now has two traditional machine-learning benchmarks:

**Linear Regression → XGBoost Regression**

These models provide the performance reference required before introducing spatial embeddings and graph-based learning.

## Next Step

Day 4 will focus on formal model evaluation using RMSE and MAPE, detailed error analysis, and comparison of the Linear Regression and XGBoost baselines.
