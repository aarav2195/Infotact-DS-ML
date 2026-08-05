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
│       └── spatial_features.csv
│
├── notebooks
│   ├── 01_data_acquisition.ipynb
│   └── 02_spatial_feature_engineering.ipynb
│
├── reports
│   └──week-1
│      ├── day1_data_acquisition.md
│      ├── day2_geospatial_preprocessing.md
│      └── day3_spatial_feature_engineering.md
│
├── requirements.txt
└── README.md
```

---

# 🚀 Project Progress

## ✅ Week 1

### ✅ Day 1 – Data Acquisition and Exploration

- Downloaded and organized the King County Housing dataset.
- Performed exploratory data analysis.
- Verified geographical coordinates.
- Analyzed the initial house price distribution.

---

### ✅ Day 2 – Data Cleaning and Preprocessing

- Cleaned the housing dataset.
- Removed duplicate records.
- Normalized extreme property prices.
- Engineered temporal and housing age features.
- Prepared the dataset for spatial analysis.

---

### ✅ Day 3 – Spatial Feature Engineering

- Implemented BallTree neighbor search.
- Computed Haversine distances.
- Engineered neighborhood-based spatial features.
- Generated neighborhood pricing statistics.
- Created spatial analysis visualizations.
- Prepared the dataset for geospatial visualization and machine learning.

---

## 🔄 Upcoming Work

### 🚀 Week 1

#### Day 4

- Interactive Geospatial Visualization using Folium.
- Property Price Distribution Map.
- Neighborhood Price Heatmaps.
- Spatial Trend Analysis.

---

#### Day 5

- Finalize Week 1.
- Complete project documentation.
- Review geospatial preprocessing pipeline.
- Push finalized Week 1 implementation to GitHub.

---

### 🚀 Week 2

- Feature Engineering.
- Baseline Machine Learning Model.
- XGBoost Regression.
- Model Evaluation using RMSE and MAPE.

---

### 🚀 Week 3

- Graph Construction.
- K-Nearest Neighbor Graph.
- Spatial Embeddings.
- Graph Dataset Preparation.

---

### 🚀 Week 4

- Graph Neural Network (GNN).
- Attention-based Spatial Modeling.
- Model Comparison.
- Interactive Streamlit Dashboard.
- Final Project Deployment.

---

# Current Status

**Week 1 is currently in progress.**

The project has successfully completed:

- Dataset acquisition
- Data preprocessing
- Spatial feature engineering

The next phase focuses on interactive geospatial visualization before moving into machine learning and graph-based valuation models.

---

# Future Goal

Build an end-to-end Geospatial Real Estate Valuation System capable of leveraging neighborhood relationships through Graph Neural Networks to outperform traditional machine learning valuation models.