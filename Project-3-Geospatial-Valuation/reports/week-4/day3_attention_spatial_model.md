# Week 4 – Day 3: Attention-Based Spatial Modeling

## Objective

Develop an attention-based Graph Neural Network that learns the relative importance of neighboring properties while incorporating geographic edge distance.

## Work Completed

* Loaded the validated Week 3 spatial graph.
* Used the same graph structure and train/validation/test split as the baseline GNN.
* Added Haversine-based `distance_km` as an edge feature.
* Standardized edge distance using logarithmic transformation and scaling.
* Implemented a Graph Attention Network using `GATConv`.
* Used multi-head attention to aggregate information from neighboring properties.
* Standardized the property-price target using training data only.
* Trained the attention-based model with early stopping.
* Selected the best checkpoint using validation RMSE.
* Evaluated the final model on the held-out test set.
* Generated attention-model predictions and training history.
* Compared the attention model against the baseline GNN.

## Model Configuration

* Architecture: Graph Attention Network (GAT)
* Hidden Channels: 32
* Attention Heads: 4
* Dropout: 0.20
* Optimizer: Adam
* Learning Rate: 0.001
* Weight Decay: 1e-5
* Loss Function: MSE
* Maximum Epochs: 300
* Early Stopping Patience: 30
* Edge Feature: Haversine distance

## Final Results

| Model            |      Test RMSE |  Test MAPE |    Test R² |
| ---------------- | -------------: | ---------: | ---------: |
| XGBoost          |    $103,398.17 |     17.31% |     0.8274 |
| **Baseline GNN** | **$80,285.81** | **12.32%** | **0.8905** |
| Attention GNN    |    $121,562.18 |     19.40% |     0.7490 |

## Attention Model Comparison

The Attention GNN produced a test MAPE of **19.40%**, compared with **12.32%** for the baseline GraphSAGE model.

Therefore, the Attention GNN showed approximately:

* **57.44% higher MAPE**
* **51.41% higher RMSE**

than the baseline GNN.

The attention model therefore did not improve upon the simpler GraphSAGE architecture in the current configuration.

## Key Finding

The baseline GNN remains the strongest model developed so far.

The current model ranking is:

**Baseline GNN → XGBoost → Attention GNN**

The results demonstrate that incorporating spatial graph relationships substantially improved valuation performance, while the specific attention architecture tested here did not provide an additional improvement.

## Generated Outputs

* `models/attention_gnn.pt`
* `data/processed/week-3/gnn/attention_gnn_training_history.csv`
* `data/processed/week-3/gnn/attention_gnn_training_curve.png`
* `data/processed/week-3/gnn/attention_gnn_predictions.csv`
* `data/processed/week-3/gnn/gnn_model_comparison.csv`

## Notebook

`notebooks/16_attention_spatial_model.ipynb`

## Outcome

The attention-based spatial modeling experiment was successfully completed and evaluated.

The baseline GraphSAGE model remains the preferred valuation model for the next stage because it achieved the lowest held-out MAPE of **12.32%**.

## Next Step

Day 4 will focus on formal model comparison, prediction-error analysis, and selection of the model that will power the final geospatial valuation dashboard.
