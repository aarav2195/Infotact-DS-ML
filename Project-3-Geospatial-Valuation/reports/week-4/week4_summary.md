# Week 4 Summary – GNN / Attention Modeling and Geospatial Dashboard

## Week Objective

The final sprint focused on advanced spatial machine learning, graph-based valuation, attention-based modeling, controlled model comparison, and deployment of an interactive geospatial property valuation dashboard.

## Day-by-Day Progress

### Day 1 – GNN Data Preparation

- Prepared the finalized spatial graph for PyTorch Geometric.
- Validated graph nodes, edges and targets.
- Selected 24 model features.
- Created the train-validation-test masks.
- Prepared the graph dataset for GNN training.
- Validated the graph artifact and model input structure.

### Day 2 – Baseline GNN

- Implemented a GraphSAGE-based baseline GNN.
- Used the prepared spatial graph and 24 node features.
- Applied training-only target scaling.
- Implemented model validation and early stopping.
- Generated property-price predictions.

### Baseline GNN Result

**Test MAPE: 12.32%**

This established the primary graph-based valuation benchmark.

### Day 3 – Attention Spatial Model

- Implemented an attention-based graph model.
- Integrated geographic distance as an edge feature.
- Applied edge-distance preprocessing.
- Used the same graph structure and data split.
- Trained and validated the Attention GNN.
- Generated attention-based property-price predictions.

### Attention GNN Result

**Test MAPE: 19.40%**

The Attention GNN did not outperform the Baseline GNN.

### Day 4 – Controlled Model Comparison

- Created the common model-evaluation workflow.
- Retrained XGBoost using the same feature set and common test properties.
- Evaluated XGBoost, Baseline GNN and Attention GNN.
- Calculated RMSE, MAPE, MAE and R².
- Performed prediction-error analysis.
- Performed price-range error analysis.
- Generated the dashboard-ready prediction dataset.
- Selected the best-performing model based on test MAPE.

### Day 4 Final Comparison

| Model | Test RMSE | Test MAPE | Test R² |
|---|---:|---:|---:|
| **XGBoost** | **$75,232.36** | **11.39%** | **0.9038** |
| Baseline GNN | $80,285.81 | 12.32% | 0.8905 |
| Attention GNN | $121,562.18 | 19.40% | 0.7490 |

### Final Model Ranking

**1. XGBoost – 11.39% MAPE**

**2. Baseline GNN – 12.32% MAPE**

**3. Attention GNN – 19.40% MAPE**

The original Week 2 XGBoost benchmark achieved 17.31% MAPE. The controlled Day-4 XGBoost evaluation improved this to **11.39% MAPE** on the common test set.

## Day 5 – Advanced Geospatial Dashboard and Final Validation

- Built the modular Streamlit application.
- Implemented the dashboard overview and KPI system.
- Implemented property-level valuation inspection.
- Implemented interactive property mapping.
- Implemented neighborhood intelligence.
- Implemented spatial price-disparity analysis.
- Implemented model-comparison analytics.
- Implemented prediction-error diagnostics.
- Implemented What-If valuation.
- Implemented local XGBoost prediction explanation.
- Added shared UI utilities and application styling.
- Validated the complete dashboard data and model pipeline.
- Validated the modular application structure.
- Confirmed XGBoost as the deployment candidate.

## Final Dashboard Architecture

The application is organized into separate modules for:

- Overview
- Property Prediction
- Interactive Property Map
- Neighborhood Intelligence
- Spatial Price Disparity
- Model Comparison
- Error Analysis
- What-If Valuation
- Prediction Explanation

Shared utilities provide:

- Data loading
- Model loading
- Prediction functions
- Spatial neighbor search
- Shared styling
- Common UI components

## Final Week 4 Outcome

Week 4 successfully connected advanced machine learning with an interactive geospatial valuation interface.

The final workflow is:

**Spatial Graph Preparation → GraphSAGE → Attention GNN → Controlled Model Comparison → Best Model Selection → Explainable Valuation → Geospatial Dashboard**

The final production candidate is:

**XGBoost – 11.39% Test MAPE**

The Baseline GNN remains a strong spatial benchmark, demonstrating the value of geographic relationships in property valuation, while the tested Attention GNN did not improve predictive performance in the final comparison.

## Final Project Status

| Week | Status |
|---|---|
| Week 1 | ✅ Completed |
| Week 2 | ✅ Completed |
| Week 3 | ✅ Completed |
| Week 4 | ✅ Completed |

## Overall Outcome

The project now provides a complete geospatial property-valuation workflow covering:

**Data Acquisition → Data Cleaning → Spatial Feature Engineering → KNN/Haversine Analysis → Geospatial Modeling → GNN Modeling → Attention Modeling → Model Comparison → Explainable Valuation → Interactive Geospatial Dashboard**

### Final Status

**PROJECT COMPLETED ✅**