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
│       ├── clean_house_data.csv
│       ├── clean_houses.geojson
│       ├── spatial_features.csv
│       └── tabular_features.csv
│
├── notebooks
│   ├── 01_data_acquisition.ipynb
│   ├── 02_spatial_feature_engineering.ipynb
│   ├── 03_geospatial_visualization.ipynb
│   └── 04_tabular_feature_engineering.ipynb
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
│       └── day1_tabular_feature_engineering.md
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

## 🚀 Week 2 – Baseline Machine Learning

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

### Week 2 Day 1 Outcome

The standard tabular feature-engineering pipeline has been completed.

The resulting dataset provides the conventional property-level feature representation required to establish the baseline machine-learning models.

The generated dataset is:

`data/processed/tabular_features.csv`

This dataset will be used for the baseline regression and XGBoost experiments.

---

# 🚀 Upcoming Work

## 🚀 Week 2 – Baseline Machine Learning

### ⏳ Day 2 – Baseline Regression

- Create train/test split.
- Train Linear Regression baseline.
- Generate initial price predictions.
- Evaluate baseline performance.

### ⏳ Day 3 – XGBoost Regression

- Train XGBoost Regressor.
- Tune the baseline model where appropriate.
- Generate property-price predictions.

### ⏳ Day 4 – Model Evaluation

- Calculate RMSE.
- Calculate MAPE.
- Compare Linear Regression and XGBoost.
- Analyze baseline model limitations.

### ⏳ Day 5 – Week 2 Validation

- Validate the complete baseline ML pipeline.
- Document findings.
- Analyze limitations in spatially complex neighborhoods.
- Complete Week 2 summary.

---

## ⏳ Week 3 – Spatial Embeddings & Graph Construction
- Construct K-Nearest Neighbor Graph.
- Create graph nodes and edges.
- Generate spatial embeddings.
- Prepare graph dataset for Graph Neural Networks.
- Analyze neighborhood connectivity.

---

## ⏳ Week 4 – Graph Neural Network & Deployment
- Train Graph Neural Network (GNN).
- Implement Attention-Based Spatial Modeling.
- Compare GNN against XGBoost baseline.
- Deploy Streamlit dashboard.
- Visualize predicted property prices on interactive maps.
- Final GitHub documentation and project deployment.

---

# Current Status

**Week 1 – Completed ✅**

**Week 2 – Day 1 Completed ✅**

### Completed Work

#### Week 1

* Dataset acquisition
* Data exploration
* Data cleaning and preprocessing
* Spatial feature engineering
* BallTree-based neighbor analysis
* Haversine distance calculation
* Interactive geospatial visualization
* Week 1 validation and documentation

#### Week 2 – Day 1

* Standard tabular feature engineering
* House-age feature
* Renovation features
* Distance-to-city-center feature
* Property-level ratio features
* ML-ready dataset preparation
* Final dataset validation

### Current Output

`data/processed/tabular_features.csv`

### Next Phase

The next stage focuses on establishing the traditional machine-learning benchmark using Linear Regression and XGBoost Regression, followed by RMSE and MAPE evaluation.

---

# Future Goal

Build an end-to-end Geospatial Real Estate Valuation System capable of leveraging neighborhood relationships through Graph Neural Networks to outperform traditional machine learning valuation models.