# Week 2 – Day 1 Report
## Standard Tabular Feature Engineering

### Objective

The objective of Week 2 Day 1 was to establish the standard tabular feature set required for baseline real estate price prediction.

The cleaned housing dataset produced during Week 1 was used as the starting point.

### Work Completed

- Loaded the cleaned King County housing dataset.
- Validated the available property attributes.
- Created house-age feature from the construction year.
- Created a renovation indicator.
- Created years-since-renovation feature.
- Calculated distance from each property to Seattle city center using the Haversine distance formula.
- Created additional property-level ratio features.
- Validated numerical features and the target variable.
- Prepared an ML-ready tabular dataset.
- Removed rows containing missing values from the final ML feature set.
- Verified the saved dataset after writing it to disk.

### Engineered Features

The Day 1 feature-engineering pipeline includes:

- `house_age`
- `is_renovated`
- `years_since_renovation`
- `distance_to_city_center_km`
- `sqft_per_bedroom`
- `sqft_per_bathroom`
- `living_lot_ratio`

Additional original housing features were retained where available.

### Output

The final Day 1 dataset was saved as:

`data/processed/week2_tabular_features.csv`

### Week 2 Baseline Preparation

The resulting dataset provides a conventional tabular feature representation of each property.

This dataset will be used in the next stage to establish baseline regression performance using traditional machine learning models.

### Next Step

Week 2 Day 2 will focus on:

- Train/test split
- Linear Regression baseline
- XGBoost Regressor
- RMSE evaluation
- MAPE evaluation
- Baseline performance comparison

### Status

✅ Week 2 Day 1 Completed