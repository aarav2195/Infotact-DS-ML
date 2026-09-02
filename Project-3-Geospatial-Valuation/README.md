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

### Data & Scientific Computing

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

### Geospatial Processing

- BallTree
- Haversine Distance
- Folium
- GeoJSON

### Machine Learning

- Linear Regression
- XGBoost
- RMSE
- MAPE
- MAE
- R²

### Graph Deep Learning

- PyTorch
- PyTorch Geometric
- GraphSAGE
- Graph Attention
- Spatial Edge Features

### Dashboard & Visualization

- Streamlit
- Plotly
- PyDeck
- Custom CSS

### Development & Version Control

- Jupyter Notebook
- Git
- GitHub

---

# Project Structure

```text
Project-3-Geospatial-Valuation
│
├── app
│   ├── assets
│   │   └── style.css
│   │
│   ├── modules
│   │   ├── __init__.py
│   │   ├── error_analysis.py
│   │   ├── model_comparison.py
│   │   ├── model_explanation.py
│   │   ├── neighborhood.py
│   │   ├── overview.py
│   │   ├── prediction.py
│   │   ├── property_map.py
│   │   ├── spatial_disparity.py
│   │   └── what_if.py
│   │
│   ├── utils
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── prediction.py
│   │   ├── spatial.py
│   │   └── ui.py
│   │
│   ├── app.py
│   └── config.py
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
│       ├── week-3
│       │   ├── gnn
│       │   │   ├── day4
│       │   │   │   └── final_model_split.csv
│       │   │   │   
│       │   │   ├── attention_gnn_predictions.csv
│       │   │   ├── attention_gnn_training_curve.png
│       │   │   ├── attention_gnn_training_history.csv
│       │   │   ├── baseline_gnn_predictions.csv
│       │   │   ├── baseline_gnn_training_curve.png
│       │   │   ├── baseline_gnn_training_history.csv
│       │   │   ├── dashboard_predictions.csv
│       │   │   ├── final_model_comparison.csv
│       │   │   ├── final_prediction_error_analysis.csv
│       │   │   ├── final_price_range_analysis.csv
│       │   │   ├── gnn_model_comparison.csv
│       │   │   └── housing_graph_data.pt
│       │   │
│       │   ├── final_graph_edges.csv
│       │   ├── final_graph_nodes.csv
│       │   ├── final_graph_targets.csv
│       │   ├── graph_distance_statistics.csv
│       │   ├── graph_node_features.csv
│       │   ├── graph_node_statistics.csv
│       │   ├── graph_targets.csv
│       │   ├── knn_graph_edges.csv
│       │   └── spatial_embeddings.csv
│       │
│       ├── clean_house_data.csv
│       ├── clean_houses.geojson
│       ├── spatial_features.csv
│       └── tabular_features.csv
│
├── models
│   ├── attention_gnn.pt
│   ├── baseline_gnn.pt
│   ├── linear_regression_baseline.pkl
│   ├── xgboost_baseline.pkl
│   └── xgboost_comparison.pkl
│
├── notebooks
│   ├── 01_data_acquisition.ipynb
│   ├── 02_spatial_feature_engineering.ipynb
│   ├── 03_geospatial_visualization.ipynb
│   ├── 04_tabular_feature_engineering.ipynb
│   ├── 05_linear_regression_baseline.ipynb
│   ├── 06_xgboost_baseline.ipynb
│   ├── 07_model_evaluation.ipynb
│   ├── 08_week2_validation.ipynb
│   ├── 09_knn_graph_construction.ipynb
│   ├── 10_graph_validation_analysis.ipynb
│   ├── 11_spatial_embedding_generation.ipynb
│   ├── 12_graph_dataset_preparation.ipynb
│   ├── 13_week3_final_validation.ipynb
│   ├── 14_gnn_data_preparation.ipynb
│   ├── 15_gnn_model_training.ipynb
│   ├── 16_attention_spatial_model.ipynb
│   ├── 17_model_comparison_analysis.ipynb
│   └── 18_dashboard_validation.ipynb
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
│   │   ├── day5_week1_validation.md
│   │   └── week1_summary.md
│   │
│   ├── week-2
│   │   ├── day1_tabular_feature_engineering.md
│   │   ├── day2_linear_regression_baseline.md
│   │   ├── day3_xgboost_baseline.md
│   │   ├── day4_model_evaluation.md
│   │   ├── day5_week2_validation.md
│   │   └── week2_summary.md
│   │
│   ├── week-3
│   │   ├── visualizations
│   │   │   ├── graph_node_sample.html
│   │   │   ├── knn_distance_distribution.png
│   │   │   └── node_degree_distribution.png
│   │   │
│   │   ├── day1_knn_graph_construction.md
│   │   ├── day2_graph_validation_analysis.md
│   │   ├── day3_spatial_embedding_generation.md
│   │   ├── day4_graph_dataset_preparation.md
│   │   ├── day5_week3_final_validation.md
│   │   └── week3_summary.md
│   │
│   └── week-4
│       ├── visualizations
│       │   ├── final_actual_vs_predicted.png
│       │   └── final_model_mape_comparison.png
│       │
│       ├── day1_gnn_data_preparation.md
│       ├── day2_gnn_model_training.md
│       ├── day3_attention_spatial_model.md
│       ├── day4_model_comparison_analysis.md
│       ├── day5_final_validation.md
│       └── week4_summary.md
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

## ✅ Week 2 – Baseline Machine Learning

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

---

### ✅ Day 5 – Final Validation and Week 2 Completion

- Validated all Week 2 datasets and model artifacts.
- Verified the 80/20 training and holdout split.
- Checked missing and infinite values.
- Reloaded and validated Linear Regression and XGBoost models.
- Regenerated and verified holdout predictions.
- Revalidated RMSE, MAPE, MAE and R² results.
- Verified prediction-error and price-range analysis outputs.
- Finalized Week 2 documentation.
- Confirmed XGBoost as the traditional ML benchmark.

### 📊 Week 2 Final Benchmark

| Model | RMSE | MAPE | MAE | R² |
|---|---:|---:|---:|---:|
| Linear Regression | $129,959.74 | 23.50% | $99,623.90 | 0.7274 |
| **XGBoost** | **$103,398.17** | **17.31%** | **$75,525.97** | **0.8274** |

XGBoost achieved a **20.44% improvement in RMSE** and a **26.34% improvement in MAPE** compared with Linear Regression.

### 📌 Week 2 Outcome

Week 2 has been successfully completed.

The traditional machine-learning benchmark has been established using XGBoost Regression with a final **MAPE of 17.31%**.

The XGBoost model will serve as the benchmark for evaluating the spatial and graph-based models developed during the later phases of the project.

---

## ✅ Week 3 – Spatial Embeddings and Graph Construction

### ✅ Day 1 – KNN Graph Construction

- Converted properties into graph nodes using geographic coordinates.
- Constructed K-nearest-neighbor relationships based on physical proximity.
- Generated graph edges connecting each property to its nearest spatial neighbors.
- Prepared node and edge datasets for graph analysis.

---

### ✅ Day 2 – Graph Validation and Neighborhood Analysis

- Validated graph node and edge relationships.
- Checked node IDs and edge references.
- Detected and handled self-loop issues.
- Analyzed KNN neighborhood distances.
- Generated neighborhood-level graph statistics.
- Validated graph connectivity and spatial relationships.

---

### ✅ Day 3 – Spatial Embedding Generation

- Standardized latitude and longitude features.
- Calculated KNN neighborhood distance statistics.
- Generated localized neighborhood features.
- Created numerical spatial embeddings representing geographic and neighborhood context.
- Validated embedding dimensions and node alignment.
- Saved the spatial embedding dataset.

### 📊 Day 3 Results

| Parameter | Result |
|---|---:|
| Nodes | 21,613 |
| Embedding Dimensions | 8 |
| Missing Values | 0 |
| Duplicate Node IDs | 0 |
| Validation | Passed ✅ |

---

### ✅ Day 4 – Graph Dataset Preparation

- Combined node features with spatial embeddings.
- Validated node, embedding and target alignment.
- Validated graph edge references and distances.
- Checked for self-loops and invalid node IDs.
- Prevented target leakage from the node feature matrix.
- Validated missing values and duplicate node IDs.
- Verified KNN edge count and outgoing degree.
- Created separate final node, edge and target datasets.

### 📊 Day 4 Results

| Parameter | Result |
|---|---:|
| Graph Nodes | 21,613 |
| K Neighbors | 5 |
| Graph Edges | 108,065 |
| Node Features | 25 |
| Self-Loops | 0 |
| Invalid Node References | 0 |
| Missing Values | 0 |
| Validation | Passed ✅ |

### 📁 Day 4 Outputs

- `data/processed/week-3/final_graph_nodes.csv`
- `data/processed/week-3/final_graph_edges.csv`
- `data/processed/week-3/final_graph_targets.csv`

---

### ✅ Day 5 – Final Validation and Week 3 Completion

- Validated the complete Week 3 graph pipeline.
- Verified node, embedding and target ID alignment.
- Validated KNN edge references and connectivity.
- Confirmed absence of self-loops.
- Validated edge distance values.
- Validated node features and spatial embeddings.
- Checked target alignment and target leakage.
- Verified all required Week 3 output files.
- Completed final graph dataset validation.
- Finalized Week 3 documentation.

### 📊 Week 3 Final Results

| Parameter | Result |
|---|---:|
| Graph Nodes | 21,613 |
| K Neighbors | 5 |
| Graph Edges | 108,065 |
| Node Features | 25 |
| Spatial Embedding Dimensions | 8 |
| Prediction Targets | 21,613 |
| Self-Loops | 0 |
| Invalid Edge References | 0 |
| Missing Values | 0 |
| Target Leakage | None |
| Validation | Passed ✅ |

### 📁 Week 3 Final Outputs

- `data/processed/week-3/final_graph_nodes.csv`
- `data/processed/week-3/final_graph_edges.csv`
- `data/processed/week-3/final_graph_targets.csv`
- `data/processed/week-3/spatial_embeddings.csv`

### 📌 Week 3 Outcome

Week 3 has been successfully completed.

The project now contains a validated spatial graph representation of the housing dataset, including KNN-based geographic connectivity, node features, localized spatial embeddings and separate prediction targets.

The finalized graph dataset is ready for the **GNN modeling stage in Week 4**.

---

## ✅ Week 4 – GNN / Attention Modeling and Geospatial Dashboard

### ✅ Day 1 – GNN Data Preparation

- Prepared the finalized spatial graph for PyTorch Geometric.
- Validated graph nodes, edges, targets, and feature alignment.
- Selected 24 valid model input features.
- Created the train-validation-test masks.
- Prepared the graph dataset for GNN training.
- Applied training-only feature scaling.
- Validated the final graph artifact and model input structure.

### 📊 Day 1 Results

| Parameter | Result |
|---|---:|
| Graph Nodes | 21,613 |
| Graph Edges | 108,065 |
| Model Features | 24 |
| Training Nodes | 15,129 |
| Validation Nodes | 3,242 |
| Test Nodes | 3,242 |

---

### ✅ Day 2 – Baseline GNN Model Training

- Implemented a GraphSAGE-based baseline GNN.
- Used the finalized spatial graph and 24 node features.
- Standardized the prediction target using training nodes only.
- Trained the GNN with validation monitoring.
- Implemented checkpoint selection and early stopping.
- Generated test-set property-price predictions.
- Evaluated RMSE, MAPE and R².

### 📊 Day 2 Results

| Metric | Test Result |
|---|---:|
| RMSE | $80,285.81 |
| MAPE | **12.32%** |
| R² | **0.8905** |

The Baseline GNN established the primary graph-based valuation benchmark with a **12.32% test MAPE**.

---

### ✅ Day 3 – Attention-Based Spatial Modeling

- Implemented an attention-based graph neural network.
- Added geographic edge-distance information.
- Applied preprocessing to spatial edge-distance features.
- Used the same graph structure and evaluation split.
- Trained the Attention GNN with validation monitoring.
- Generated attention-based property-price predictions.
- Compared the Attention GNN with the Baseline GNN.

### 📊 Day 3 Results

| Model | Test MAPE | Test R² |
|---|---:|---:|
| **Baseline GNN** | **12.32%** | **0.8905** |
| Attention GNN | 19.40% | 0.7490 |

The Attention GNN did not improve on the Baseline GNN and therefore the Baseline GNN remained the stronger graph-based model.

---

### ✅ Day 4 – Controlled Model Comparison and Error Analysis

- Created a controlled common model-evaluation workflow.
- Retrained XGBoost using the same feature set and common test properties used by the graph models.
- Evaluated XGBoost, Baseline GNN and Attention GNN on the same held-out test set.
- Calculated RMSE, MAPE, MAE and R².
- Performed prediction-error analysis.
- Performed price-range error analysis.
- Generated dashboard-ready prediction outputs.
- Generated final model-comparison visualizations.
- Selected the deployment candidate using the lowest test MAPE.

### 📊 Day 4 Final Comparison

| Model | Test RMSE | Test MAPE | Test R² |
|---|---:|---:|---:|
| **XGBoost** | **$75,232.36** | **11.39%** | **0.9038** |
| Baseline GNN | $80,285.81 | 12.32% | 0.8905 |
| Attention GNN | $121,562.18 | 19.40% | 0.7490 |

XGBoost became the best-performing model in the controlled comparison with a **11.39% test MAPE**.

The original Week 2 XGBoost benchmark achieved **17.31% MAPE**. The controlled Day 4 XGBoost evaluation improved this to **11.39% MAPE** on the common test set.

---

### ✅ Day 5 – Advanced Geospatial Dashboard and Final Validation

- Built the final modular Streamlit application.
- Implemented a professional GeoValuation AI interface.
- Added an Overview and model-performance monitoring module.
- Added property-level valuation analysis.
- Added an interactive property map.
- Added neighborhood intelligence and nearest-property analysis.
- Added spatial price-disparity analysis.
- Added model comparison across XGBoost, Baseline GNN and Attention GNN.
- Added detailed prediction-error analysis.
- Added What-If valuation simulation.
- Added local XGBoost prediction explanations.
- Added reusable dashboard UI utilities and styling.
- Validated the final model artifact.
- Validated the 24-feature prediction pipeline.
- Validated node and target alignment.
- Validated dashboard prediction outputs.
- Validated the modular application structure.
- Confirmed XGBoost as the deployment candidate.

### 📊 Final Deployment Model

| Model | Test MAPE | Status |
|---|---:|---|
| **XGBoost** | **11.39%** | **Primary Deployment Model ✅** |
| Baseline GNN | 12.32% | Spatial Benchmark |
| Attention GNN | 19.40% | Experimental Model |

### 🖥️ Final Dashboard Modules

The final dashboard contains:

- Overview
- Property Prediction
- Interactive Property Map
- Neighborhood Intelligence
- Spatial Price Disparity
- Model Comparison
- Error Analysis
- What-If Valuation
- Prediction Explanation

### 📌 Week 4 Outcome

Week 4 has been successfully completed.

The project now combines traditional machine learning, graph-based spatial modeling, attention-based modeling, explainable valuation and an interactive geospatial dashboard.

The final workflow is:

**Spatial Graph Preparation → Baseline GNN → Attention GNN → Controlled Model Comparison → Best Model Selection → Explainable Valuation → Geospatial Dashboard**

The current primary deployment model is **XGBoost with 11.39% test MAPE** on the controlled evaluation set.

---

# Current Status

## ✅ Week 1 – Geospatial Data Acquisition and Processing

- Dataset acquisition and exploratory analysis completed.
- Data cleaning and preprocessing completed.
- Spatial feature engineering completed.
- BallTree-based neighborhood analysis completed.
- Haversine distance calculations completed.
- Geospatial visualizations generated.
- Week 1 validation and documentation completed.

**Status: Completed ✅**

---

## ✅ Week 2 – Baseline Machine Learning

- Standard tabular feature engineering completed.
- Linear Regression baseline implemented.
- XGBoost regression baseline implemented.
- Train/test evaluation completed.
- RMSE, MAPE, MAE and R² analysis completed.
- Prediction-error and price-range analysis completed.
- XGBoost established as the traditional ML benchmark with **17.31% MAPE**.
- Week 2 validation and documentation completed.

**Status: Completed ✅**

---

## ✅ Week 3 – Spatial Graph Construction and Embeddings

- KNN spatial graph construction completed.
- Graph validation and neighborhood analysis completed.
- Spatial embedding generation completed.
- Graph dataset preparation completed.
- Node, edge and target datasets finalized.
- Target leakage and self-loop validation completed.
- Final graph validation completed.
- Week 3 documentation completed.

**Status: Completed ✅**

---

## ✅ Week 4 – GNN / Attention Modeling and Geospatial Dashboard

- GNN graph data preparation completed.
- PyTorch Geometric graph dataset validated.
- Baseline GraphSAGE model implemented and trained.
- Baseline GNN achieved **12.32% test MAPE**.
- Attention-based spatial GNN implemented and evaluated.
- Attention GNN achieved **19.40% test MAPE**.
- Controlled comparison of XGBoost, Baseline GNN and Attention GNN completed.
- XGBoost achieved the best controlled test performance with **11.39% MAPE**.
- Prediction-error and price-range analysis completed.
- Modular Streamlit geospatial valuation dashboard developed.
- Property Prediction module implemented.
- Interactive Property Map implemented.
- Neighborhood Intelligence module implemented.
- Spatial Price Disparity analysis implemented.
- Model Comparison module implemented.
- Prediction Error Analysis implemented.
- What-If Valuation module implemented.
- Prediction Explanation module implemented.
- Final dashboard model and prediction pipeline validated.
- Week 4 final validation and documentation completed.

**Status: Completed ✅**

---

## 📊 Final Model Performance

| Model | Test RMSE | Test MAPE | Test R² |
|---|---:|---:|---:|
| **XGBoost** | **$75,232.36** | **11.39%** | **0.9038** |
| Baseline GNN | $80,285.81 | 12.32% | 0.8905 |
| Attention GNN | $121,562.18 | 19.40% | 0.7490 |

**Final Deployment Model: XGBoost – 11.39% Test MAPE**

### Current Outputs

#### Week 2

- `data/processed/tabular_features.csv`
- `data/processed/week-2/X_train.csv`
- `data/processed/week-2/X_test.csv`
- `data/processed/week-2/y_train.csv`
- `data/processed/week-2/y_test.csv`
- `data/processed/week-2/baseline_model_comparison.csv`
- `data/processed/week-2/model_evaluation.csv`
- `data/processed/week-2/prediction_error_analysis.csv`
- `data/processed/week-2/price_range_error_analysis.csv`
- `data/processed/week-2/predictions/model_prediction_comparison.csv`
- `models/linear_regression_baseline.pkl`
- `models/xgboost_baseline.pkl`

#### Week 3

- `data/processed/week-3/graph_node_features.csv`
- `data/processed/week-3/graph_targets.csv`
- `data/processed/week-3/knn_graph_edges.csv`
- `data/processed/week-3/graph_node_statistics.csv`
- `data/processed/week-3/graph_distance_statistics.csv`
- `reports/week-3/visualizations/node_degree_distribution.png`
- `reports/week-3/visualizations/knn_distance_distribution.png`
- `reports/week-3/visualizations/graph_node_sample.html`
- `data/processed/week-3/spatial_embeddings.csv`
- `data/processed/week-3/final_graph_nodes.csv`
- `data/processed/week-3/final_graph_edges.csv`
- `data/processed/week-3/final_graph_targets.csv`

#### Week 4

- `data/processed/week-3/gnn/housing_graph_data.pt`
- `models/baseline_gnn.pt`
- `data/processed/week-3/gnn/baseline_gnn_training_history.csv`
- `data/processed/week-3/gnn/baseline_gnn_training_curve.png`
- `data/processed/week-3/gnn/baseline_gnn_predictions.csv`
- `models/attention_gnn.pt`
- `data/processed/week-3/gnn/attention_gnn_training_history.csv`
- `data/processed/week-3/gnn/attention_gnn_training_curve.png`
- `data/processed/week-3/gnn/attention_gnn_predictions.csv`
- `data/processed/week-3/gnn/gnn_model_comparison.csv`
- `data/processed/week-3/gnn/day4/final_model_split.csv`
- `data/processed/week-3/gnn/day4/final_model_comparison.csv`
- `data/processed/week-3/gnn/day4/final_prediction_error_analysis.csv`
- `data/processed/week-3/gnn/day4/final_price_range_analysis.csv`
- `data/processed/week-3/gnn/day4/dashboard_predictions.csv`
- `models/xgboost_comparison.pkl`
- `reports/week-4/visualizations/final_model_mape_comparison.png`
- `reports/week-4/visualizations/final_actual_vs_predicted.png`

---

## 🏆 Project Status

**All four weeks completed successfully.**

**Project Development: Completed ✅**

# Final Project Outcome

The completed system provides an end-to-end **Geospatial Real Estate Valuation System** combining traditional property attributes with geographic and neighborhood relationships.

The project demonstrates a complete progression from conventional machine learning to spatial graph modeling and finally to an interactive valuation dashboard.

The final system integrates:

- Property-level features
- Geographic coordinates
- Haversine distance
- KNN neighborhood relationships
- Spatial embeddings
- Graph Neural Networks
- Attention-based spatial modeling
- Controlled model comparison
- Explainable XGBoost valuation
- Interactive geospatial visualization
- Neighborhood intelligence
- What-If valuation analysis

The final application is designed to provide both **predictive valuation** and **spatial decision-support insights** for real-estate analysis.

```markdown
## Deployment

Run the dashboard from the project root with:

```bash
streamlit run app/app.py