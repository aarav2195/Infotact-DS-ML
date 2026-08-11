# Week 2 – Day 2: Train/Test Split and Linear Regression Baseline

## Objective

The objective of Day 2 was to establish the first traditional machine learning baseline for the Geospatial Real Estate Valuation project.

The tabular features prepared during Day 1 were used to create training and holdout datasets, followed by implementation of a standardized Linear Regression model.

## Dataset Preparation

The processed `tabular_features.csv` dataset was loaded and validated before model development.

The target variable was identified as:

* `price`

The baseline feature set included standard property characteristics together with:

* `house_age`
* `distance_to_city_center_km`

Feature completeness and missing values were checked before model training.

## Train/Test Split

The dataset was divided into:

* 80% training data
* 20% holdout data

A fixed random state of 42 was used to ensure reproducibility.

The holdout dataset was kept separate from model training and will be used for subsequent performance evaluation.

## Linear Regression Baseline

A Linear Regression model was implemented using a Scikit-learn pipeline.

StandardScaler was applied before Linear Regression to standardize the numerical feature space.

The model was trained using the training dataset and predictions were generated for the unseen holdout dataset.

## Prediction Analysis

Initial prediction results were compared against the actual house prices.

Absolute prediction errors were calculated for individual holdout observations.

The prediction results demonstrate that a simple linear model does not perfectly capture the complex relationships present in real estate pricing. These errors will be quantified using formal evaluation metrics in the subsequent evaluation stage.

## Model Artifact

The trained model was saved as:

`models/linear_regression_baseline.pkl`

The train/test datasets and baseline feature configuration were also saved under:

`data/processed/week-2/`

## Outcome

Day 2 successfully established the first traditional machine learning benchmark for the project.

The Linear Regression baseline provides a reference point against which the stronger XGBoost model and later spatial/graph-based models can be evaluated.

## Next Step

The next stage will focus on training the XGBoost regression model as the stronger tabular machine learning baseline.
