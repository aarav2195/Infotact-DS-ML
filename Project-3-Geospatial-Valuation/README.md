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
│   ├── 02_spatial_feature_engineering.ipynb
│   └── 03_geospatial_visualization.ipynb
│
├── reports
│   └──week-1
│      ├── visualizations
│      │   ├── property_locations.html
│      │   ├── property_price_distribution.html
│      │   └── property_price_heatmap.html
│      ├── day1_data_acquisition.md
│      ├── day2_geospatial_preprocessing.md
│      ├── day3_spatial_feature_engineering.md
│      └── day4_geospatial_visualizations.md
│
├── requirements.txt
└── README.md
```

---

# 🚀 Project Progress

## ✅ Week 1

### ✅ Day 1 – Data Acquisition and Exploration
- Downloaded and organized the King County Housing Dataset.
- Performed Exploratory Data Analysis (EDA).
- Verified latitude and longitude coordinates.
- Analyzed house price distribution and geographical coverage.
- Prepared the raw dataset for preprocessing.

---

### ✅ Day 2 – Data Cleaning and Preprocessing
- Removed duplicate property records.
- Handled missing values.
- Normalized extreme house price outliers.
- Created additional temporal and housing age features.
- Saved cleaned dataset for spatial analysis.

---

### ✅ Day 3 – Spatial Feature Engineering
- Implemented BallTree for efficient K-Nearest Neighbor search.
- Calculated Haversine distances between neighboring houses.
- Generated neighborhood-based spatial features.
- Computed neighborhood price statistics.
- Created GeoJSON dataset for map visualization.
- Saved spatial feature dataset for visualization.

---

### ✅ Day 4 – Interactive Geospatial Visualization
- Built interactive Folium maps.
- Visualized property locations on an interactive map.
- Generated property price distribution map.
- Created neighborhood price heatmap.
- Exported interactive HTML maps.
- Verified geographical pricing trends visually.

---

# 🚀 Upcoming Work

### ⏳ Day 5
- Finalize Week 1 implementation.
- Review complete geospatial preprocessing pipeline.
- Validate generated spatial datasets.
- Update documentation.
- Push finalized Week 1 implementation to GitHub.

---

## ⏳ Week 2 – Baseline Machine Learning
- Engineer additional valuation features.
- Calculate distance to city center.
- Train Linear Regression baseline.
- Train XGBoost Regressor.
- Evaluate using RMSE and MAPE.
- Compare baseline models.

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

**Week 1 is currently in progress.**

The project has successfully completed:

- Dataset acquisition
- Data preprocessing
- Spatial feature engineering
- Interactive Geospatial Visualization

The next phase focuses on interactive geospatial visualization before moving into machine learning and graph-based valuation models.

---

# Future Goal

Build an end-to-end Geospatial Real Estate Valuation System capable of leveraging neighborhood relationships through Graph Neural Networks to outperform traditional machine learning valuation models.