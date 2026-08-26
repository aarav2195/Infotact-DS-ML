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
│       ├── week-3
│       │   ├── gnn
│       │   │   ├── baseline_gnn_predictions.csv
│       │   │   ├── baseline_gnn_training_curve.png
│       │   │   ├── baseline_gnn_training_history.csv
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
│   ├── baseline_gnn.pt
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
│   ├── 07_model_evaluation.ipynb
│   ├── 08_week2_validation.ipynb
│   ├── 09_knn_graph_construction.ipynb
│   ├── 10_graph_validation_analysis.ipynb
│   ├── 11_spatial_embedding_generation.ipynb
│   ├── 12_graph_dataset_preparation.ipynb
│   ├── 13_week3_final_validation.ipynb
│   ├── 14_gnn_data_preparation.ipynb
│   └── 15_gnn_model_training.ipynb
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
│       ├── day1_gnn_data_preparation.md
│       └── day2_gn_model_training.md
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

## 🔄 Week 4 – GNN / Attention Modeling and Geospatial Dashboard

### ✅ Day 1 – GNN Environment and Graph Data Preparation

- Set up and verified PyTorch and PyTorch Geometric.
- Loaded the finalized Week 3 spatial graph.
- Validated node, edge and target alignment.
- Converted graph edges into PyTorch Geometric edge indices.
- Selected 24 valid node features.
- Excluded `node_id` and raw property `id` from model inputs.
- Kept `price` separate as the prediction target.
- Created a 70/15/15 train, validation and test split.
- Applied training-only feature scaling.
- Created and validated the PyTorch Geometric graph dataset.
- Saved and reloaded the GNN-ready graph artifact.

### 📊 Day 1 Results

| Parameter | Result |
|---|---:|
| Graph Nodes | 21,613 |
| Graph Edges | 108,065 |
| Node Features | 24 |
| Training Nodes | 15,129 |
| Validation Nodes | 3,242 |
| Test Nodes | 3,242 |
| Target | `price` |
| Self-Loops | 0 |
| Validation | Passed ✅ |

### Output

`data/processed/week-3/gnn/housing_graph_data.pt`

---

### ✅ Day 2 – Baseline GNN Model Training

- Implemented a GraphSAGE-based baseline GNN using `SAGEConv`.
- Used the 24 validated node features.
- Standardized the target using training data only.
- Trained the model using the training-node mask.
- Implemented validation monitoring and early stopping.
- Restored the best validation checkpoint.
- Generated training, validation and test predictions.
- Evaluated RMSE, MAPE and R².
- Saved the trained GNN model and training artifacts.

### 📊 Day 2 Results

| Split | RMSE | MAPE | R² |
|---|---:|---:|---:|
| Training | $77,712.08 | 12.39% | 0.9043 |
| Validation | $79,574.98 | 13.01% | 0.9001 |
| **Test** | **$80,285.81** | **12.32%** | **0.8905** |

### 📈 GNN vs XGBoost Benchmark

| Model | Test RMSE | Test MAPE | Test R² |
|---|---:|---:|---:|
| XGBoost | $103,398.17 | 17.31% | 0.8274 |
| **Baseline GNN** | **$80,285.81** | **12.32%** | **0.8905** |

The baseline GNN achieved approximately **22.36% lower RMSE** and **28.83% lower MAPE** than the Week 2 XGBoost benchmark.

### 📁 Day 2 Outputs

- `models/baseline_gnn.pt`
- `data/processed/week-3/gnn/baseline_gnn_training_history.csv`
- `data/processed/week-3/gnn/baseline_gnn_training_curve.png`
- `data/processed/week-3/gnn/baseline_gnn_predictions.csv`

### 📌 Week 4 Progress

The baseline GNN has now been successfully trained and evaluated.

The test MAPE improved from the traditional XGBoost benchmark of **17.31%** to **12.32%** using the spatial graph, providing evidence that incorporating neighborhood relationships improves property-price prediction.

The next stage will introduce an attention-based spatial model to determine whether learned neighbor importance can further improve the baseline GNN.

---

## 🚀 Upcoming Work

### 🔄 Week 4 – GNN / Attention Modeling and Geospatial Dashboard

### ⏳ Day 3 – Attention-Based Spatial Modeling

- Implement an attention-based Graph Neural Network.
- Learn the relative importance of neighboring properties.
- Generate attention-based property-price predictions.
- Compare the attention model against the baseline GNN.

### ⏳ Day 4 – Model Comparison and Prediction Analysis

- Compare XGBoost, baseline GNN and attention-based GNN.
- Calculate RMSE, MAPE, MAE and R².
- Analyze spatial prediction improvements.
- Analyze prediction disparities and model errors.
- Prepare the final model for deployment.

### ⏳ Day 5 – Advanced Geospatial Dashboard and Final Validation

- Build the modular Streamlit valuation dashboard.
- Add property-price prediction.
- Add interactive geospatial maps.
- Add neighborhood intelligence.
- Add spatial price-disparity analysis.
- Add model comparison.
- Add prediction explanations.
- Add what-if valuation.
- Validate the complete application.
- Finalize deployment and documentation.

---

# Current Status

**Week 1 – Completed ✅**

**Week 2 – Completed ✅**

**Week 3 – Completed ✅**

**Week 4 – In Progress 🔄**

### Completed Work

#### Week 1

- Dataset acquisition and exploration
- Data cleaning and preprocessing
- Spatial feature engineering
- BallTree-based neighbor analysis
- Haversine distance calculation
- Neighborhood pricing features
- Interactive geospatial visualization
- Week 1 validation and documentation

#### Week 2

- Standard tabular feature engineering
- House-age and renovation features
- Distance-to-city-center feature
- Property-level ratio features
- Train/test split
- Linear Regression baseline
- XGBoost Regression baseline
- RMSE, MAPE, MAE and R² evaluation
- Prediction-error analysis
- Price-range error analysis
- XGBoost benchmark selection
- Week 2 validation and documentation

#### Week 3

- KNN spatial graph construction
- Graph validation and neighborhood analysis
- Spatial embedding generation
- Graph dataset preparation
- Node, edge and target dataset generation
- Final graph validation
- GNN-ready spatial dataset preparation

#### Week 4 – Day 1

- GNN environment setup
- PyTorch Geometric graph preparation
- 24-node-feature validation
- Target separation
- 70/15/15 train/validation/test masks
- Training-only feature scaling
- PyTorch Geometric `Data` object creation
- GNN graph artifact generation

#### Week 4 – Day 2

- GraphSAGE baseline GNN
- Training with spatial graph message passing
- Target standardization
- Early stopping
- Validation checkpoint selection
- Test-set evaluation
- Property-price prediction
- Baseline GNN model artifact generation

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

### Next Phase

The next stage focuses on **attention-based spatial modeling**.

The baseline GNN achieved a test MAPE of **12.32%**, improving substantially over the Week 2 XGBoost benchmark of **17.31%**.

The next objective is to implement an attention-based GNN that can learn the relative importance of neighboring properties and determine whether attention-based spatial modeling can further improve property-price prediction.

---

# Future Goal

Build an end-to-end **Geospatial Real Estate Valuation System** that combines conventional property attributes with neighborhood relationships and spatial dependencies.

The final system will aim to demonstrate that spatially aware models can outperform traditional tabular machine-learning approaches for property valuation.