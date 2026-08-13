# 🏡 Geospatial Real Estate Valuation using Spatial Feature Engineering

## Project Overview

This project focuses on developing an intelligent **Geospatial Real Estate Valuation System** capable of estimating house prices by combining traditional property attributes with spatial neighborhood information.

Unlike conventional valuation models that rely only on tabular features, this project gradually incorporates spatial relationships between nearby properties using neighborhood analysis, graph construction, and Graph Neural Networks (GNNs).

The project follows a four-week industry-oriented development roadmap as part of the **Infotact Data Science & Machine Learning Internship**.

---

# Dataset

**Dataset:** King County House Sales Dataset

The dataset contains residential property information including:

- Property Price
- Bedrooms
- Bathrooms
- Living Area
- Lot Area
- Floors
- Waterfront
- View Rating
- Condition
- Grade
- Construction Year
- Renovation Year
- Latitude
- Longitude

The availability of precise geographical coordinates enables advanced spatial analysis and neighborhood-based feature engineering.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- BallTree
- Haversine Distance
- Jupyter Notebook
- Git & GitHub

---

# Project Structure

```text
Project-3-Geospatial-Valuation
│
├── app
│
├── data
│   ├── raw
│   │   └── kc_house_data.csv
│   │
│   └── processed
│       ├── week-2
│       │   ├── predictions
│       │   │   ├── model_prediction_comparison.csv
│       │   │   └── xgboost_predictions.csv
│       │   │
│       │   ├── baseline_model_comparison.csv
│       │   ├── linear_regression_features.csv
│       │   ├── model_evaluation.csv
│       │   ├── prediction_error_analysis.csv
│       │   ├── price_range_error_analysis.csv
│       │   ├── X_test.csv
│       │   ├── X_train.csv
│       │   ├── y_test.csv
│       │   └── y_train.csv
│       │   
│       ├── clean_house_data.csv
│       ├── clean_houses.geojson
│       ├── spatial_features.csv
│       └── tabular_features.csv
│
├── models
│   ├── linear_regression_baseline.pkl
│   └── xgboost_baseline.pkl
│
├── notebooks
│   ├── 01_data_acquisition.ipynb
│   ├── 02_spatial_feature_engineering.ipynb
│   ├── 03_geospatial_visualization.ipynb
│   ├── 04_tabular_feature_engineering.ipynb
│   ├── 05_linear_regression_baseline.ipynb
│   ├── 06_xgboost_baseline.ipynb
│   └── 07_model_evaluation.ipynb
│
├── reports
│   ├── week-1
│   │   ├── visualizations
│   │   │   ├── property_locations.html
│   │   │   ├── property_price_distribution.html
│   │   │   └── property_price_heatmap.html
│   │   │
│   │   ├── day1_data_acquisition.md
│   │   ├── day2_geospatial_preprocessing.md
│   │   ├── day3_spatial_feature_engineering.md
│   │   ├── day4_geospatial_visualizations.md
│   │   └── day5_week1_validation.md
│   │
│   └── week-2
│       ├── day1_tabular_feature_engineering.md
│       ├── day2_linear_regression_baseline.md
│       ├── day3_xgboost_baseline.md
│       └── day4_model_evaluation.md
│
├── requirements.txt
└── README.md
```

---

# 🚀 Project Progress

## ✅ Week 1 – Geospatial Data Acquisition and Processing

### ✅ Day 1 – Data Acquisition and Exploration

- Downloaded and organized the King County Housing dataset.
- Performed exploratory data analysis.
- Verified geographical coordinates.
- Analyzed the initial house price distribution.
- Established the foundation for geospatial processing.

---

### ✅ Day 2 – Data Cleaning and Preprocessing

- Cleaned the housing dataset.
- Removed duplicate records.
- Handled extreme property-price values.
- Engineered temporal and housing-age features.
- Prepared the dataset for spatial analysis.

---

### ✅ Day 3 – Spatial Feature Engineering

- Implemented BallTree-based neighbor search.
- Computed Haversine distances.
- Engineered neighborhood-based spatial features.
- Generated neighborhood pricing statistics.
- Created spatial analysis visualizations.
- Prepared the dataset for geospatial visualization and machine learning.

---

### ✅ Day 4 – Geospatial Visualization

- Implemented interactive geospatial visualization using Folium.
- Visualized property locations across King County.
- Created property price-based spatial visualizations.
- Generated neighborhood price heatmaps.
- Analyzed spatial patterns and localized pricing trends.

---

### ✅ Day 5 – Final Validation and Week 1 Completion

- Executed and validated all Week 1 notebooks.
- Verified processed datasets and spatial features.
- Validated latitude, longitude, and property-price information.
- Confirmed successful generation of spatial datasets.
- Reviewed the complete geospatial preprocessing pipeline.
- Finalized Week 1 documentation.
- Prepared the project for baseline machine learning in Week 2.

---

## 📌 Week 1 Outcome

Week 1 has been successfully completed.

The project now contains a cleaned and spatially enriched housing dataset with property-level geographic information and neighborhood-based features.

The completed workflow is:

**Data Acquisition → Data Cleaning → Spatial Feature Engineering → KNN/Haversine Analysis → Geospatial Visualization → Final Validation**

The resulting spatial dataset will be used for baseline machine learning and property-price prediction during Week 2.

---

## 🔄 Week 2 – Baseline Machine Learning

### ✅ Day 1 – Standard Tabular Feature Engineering

* Loaded the cleaned Week 1 housing dataset.
* Validated the input dataset and numerical features.
* Engineered house-age features.
* Created renovation-related features.
* Calculated distance to Seattle city center using Haversine distance.
* Created additional property-level ratio features.
* Handled missing and infinite values.
* Prepared an ML-ready tabular dataset.
* Saved the Week 2 feature dataset as `tabular_features.csv`.

---

### ✅ Day 2 – Train/Test Split and Linear Regression Baseline

* Selected baseline property and location features.
* Included `house_age` and `distance_to_city_center_km`.
* Validated feature completeness and missing values.
* Created an 80/20 training and holdout dataset split.
* Implemented a standardized Linear Regression baseline.
* Generated holdout predictions and initial prediction-error analysis.
* Saved the trained model as `linear_regression_baseline.pkl`.
* Saved training and holdout datasets for subsequent evaluation.

---

### ✅ Day 3 – XGBoost Regression Baseline

* Loaded the same train/test split used for Linear Regression.
* Implemented an XGBoost Regressor for nonlinear property-price prediction.
* Generated holdout predictions.
* Calculated initial RMSE and MAPE.
* Compared XGBoost with the Linear Regression baseline.
* Analyzed XGBoost feature importance.
* Saved the trained XGBoost model as `xgboost_baseline.pkl`.

---

### ✅ Day 4 – Model Evaluation and Error Analysis

* Evaluated Linear Regression and XGBoost on the same holdout dataset.
* Calculated RMSE, MAPE, MAE, and R².
* Compared traditional baseline model performance.
* Generated actual-versus-predicted price analysis.
* Generated detailed prediction-error analysis.
* Analyzed XGBoost errors across property-price ranges.
* Identified XGBoost as the stronger traditional ML baseline.

### 📊 Week 2 Day 4 Results

| Model             |            RMSE |       MAPE |            MAE |         R² |
| ----------------- | --------------: | ---------: | -------------: | ---------: |
| Linear Regression |     $129,959.74 |     23.50% |     $99,623.90 |     0.7274 |
| **XGBoost**       | **$103,398.17** | **17.31%** | **$75,525.97** | **0.8274** |

XGBoost achieved:

* **20.44% lower RMSE**
* **26.34% lower MAPE**
* Higher R² than Linear Regression

Therefore, XGBoost is established as the primary traditional ML benchmark for the spatial modeling stages.

---

## 📌 Week 2 Progress

Week 2 is currently in progress.

The project has now established and evaluated the traditional machine-learning benchmark:

**Tabular Feature Engineering → Linear Regression → XGBoost → RMSE/MAPE Evaluation → Error Analysis**

The XGBoost model achieved a MAPE of **17.31%** and will serve as the primary benchmark for evaluating the improvement obtained from spatial embeddings and graph-based models.

---

# 🚀 Upcoming Work

## 🔄 Week 2 – Baseline Machine Learning

### ⏳ Day 5 – Week 2 Validation

* Validate the complete Week 2 ML pipeline.
* Review Linear Regression and XGBoost artifacts.
* Finalize baseline model comparison.
* Review prediction and error-analysis outputs.
* Document Week 2 findings.
* Prepare the project for spatial graph construction.

---

## ⏳ Week 3 – Spatial Embeddings & Graph Construction

* Construct a K-Nearest Neighbor (KNN) graph.
* Represent each property as a graph node.
* Connect properties using geographic proximity.
* Generate spatial embeddings.
* Prepare the graph dataset for Graph Neural Network modeling.
* Analyze neighborhood connectivity.

---

## ⏳ Week 4 – Graph Neural Network & Deployment

* Train a Graph Neural Network (GNN).
* Implement attention-based spatial modeling.
* Aggregate information from neighboring properties.
* Compare GNN performance against the XGBoost baseline.
* Analyze improvement in MAPE.
* Develop the Streamlit valuation dashboard.
* Visualize predicted property prices on interactive maps.
* Display influential neighboring properties.
* Complete final GitHub documentation and deployment.

---

# Current Status

**Week 1 – Completed ✅**

**Week 2 – In Progress 🔄**

### Completed Work

#### Week 1

* Dataset acquisition and exploration
* Data cleaning and preprocessing
* Spatial feature engineering
* BallTree-based neighbor analysis
* Haversine distance calculation
* Neighborhood pricing features
* Interactive geospatial visualization
* Week 1 validation and documentation

#### Week 2 – Day 1

* Standard tabular feature engineering
* House-age feature
* Renovation-related features
* Distance-to-city-center feature
* Property-level ratio features
* ML-ready dataset preparation

#### Week 2 – Day 2

* Baseline feature selection
* 80/20 train/test split
* Linear Regression baseline
* Feature standardization
* Holdout prediction generation
* Initial prediction-error analysis
* Baseline model artifact generation

#### Week 2 – Day 3

* XGBoost Regression baseline
* Nonlinear property-price modeling
* Holdout prediction generation
* Initial RMSE and MAPE calculation
* Linear Regression vs XGBoost comparison
* XGBoost feature importance analysis
* XGBoost model artifact generation

#### Week 2 – Day 4

- Formal baseline evaluation
- RMSE calculation
- MAPE calculation
- MAE and R² calculation
- Linear Regression vs XGBoost comparison
- Prediction error analysis
- Price-range error analysis
- XGBoost benchmark selection

### Current Outputs

* `data/processed/tabular_features.csv`
* `data/processed/week-2/X_train.csv`
* `data/processed/week-2/X_test.csv`
* `data/processed/week-2/y_train.csv`
* `data/processed/week-2/y_test.csv`
* `data/processed/week-2/linear_regression_features.csv`
* `data/processed/week-2/baseline_model_comparison.csv`
* `data/processed/week-2/predictions/xgboost_predictions.csv`
* `models/linear_regression_baseline.pkl`
* `models/xgboost_baseline.pkl`
* `data/processed/week-2/model_evaluation.csv`
* `data/processed/week-2/prediction_error_analysis.csv`
* `data/processed/week-2/price_range_error_analysis.csv`
* `data/processed/week-2/predictions/model_prediction_comparison.csv`

### Next Phase

The immediate next step is **Week 2 Day 5 – Final Validation and Documentation**.

The Week 2 baseline pipeline will be reviewed and finalized, including:

- Linear Regression baseline validation.
- XGBoost baseline validation.
- RMSE and MAPE result verification.
- Prediction and price-range error analysis review.
- Finalization of Week 2 documentation.
- Validation of all generated model artifacts and datasets.

After Week 2 is completed, the project will move to **Week 3 – Spatial Embeddings and Graph Construction**.

Week 3 will introduce spatial dependencies by:

- Constructing a K-Nearest Neighbor (KNN) graph.
- Representing each property as a graph node.
- Connecting geographically nearby properties through graph edges.
- Preparing node features using property and spatial information.
- Generating spatial embeddings.
- Preparing the graph dataset for Graph Neural Network modeling.
- Analyzing neighborhood connectivity.

The finalized **XGBoost MAPE of 17.31%** will serve as the traditional machine-learning benchmark against which the spatial and graph-based models will be evaluated.

---

# Future Goal

Build an end-to-end **Geospatial Real Estate Valuation System** that combines conventional property attributes with neighborhood relationships and spatial dependencies.

The final system will aim to demonstrate that spatially aware models can outperform traditional tabular machine-learning approaches for property valuation.