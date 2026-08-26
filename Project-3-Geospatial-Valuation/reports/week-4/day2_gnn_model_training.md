# Week 4 – Day 2: Baseline GNN Model Training

## Objective

Train a baseline Graph Neural Network for property-price prediction using the validated spatial graph prepared during Day 1.

## Work Completed

- Loaded the PyTorch Geometric graph dataset.
- Implemented a GraphSAGE-based baseline GNN using `SAGEConv`.
- Used the 24 validated node features.
- Kept property price separate as the prediction target.
- Standardized the target using training data only.
- Trained the GNN using the training node mask.
- Monitored validation RMSE during training.
- Implemented early stopping.
- Restored the best validation checkpoint.
- Evaluated the final model on the training, validation and test sets.
- Generated property-price predictions.
- Saved training history and the training curve.
- Saved the trained baseline GNN model.

## Model Configuration

- Architecture: GraphSAGE
- Graph Convolution Layers: 3
- Hidden Channels: 64
- Dropout: 0.20
- Optimizer: Adam
- Learning Rate: 0.001
- Weight Decay: 1e-5
- Loss Function: MSE
- Maximum Epochs: 300
- Early Stopping Patience: 30

## Final Results

| Split | RMSE | MAPE | R² |
|---|---:|---:|---:|
| Training | $77,712.08 | 12.39% | 0.9043 |
| Validation | $79,574.98 | 13.01% | 0.9001 |
| **Test** | **$80,285.81** | **12.32%** | **0.8905** |

## Comparison with XGBoost Benchmark

The Week 2 XGBoost benchmark achieved:

- RMSE: $103,398.17
- MAPE: 17.31%
- R²: 0.8274

The baseline GNN achieved:

- **RMSE: $80,285.81**
- **MAPE: 12.32%**
- **R²: 0.8905**

This represents approximately:

- **22.36% lower RMSE**
- **28.83% lower MAPE**

compared with the XGBoost benchmark.

## Generated Outputs

- `models/baseline_gnn.pt`
- `data/processed/week-3/gnn/baseline_gnn_training_history.csv`
- `data/processed/week-3/gnn/baseline_gnn_training_curve.png`
- `data/processed/week-3/gnn/baseline_gnn_predictions.csv`

## Notebook

`notebooks/15_gnn_model_training.ipynb`

## Outcome

The baseline GraphSAGE model successfully learned from the spatial graph and produced substantially better test performance than the traditional XGBoost benchmark.

The baseline GNN achieved a test MAPE of **12.32%**, establishing a strong benchmark for the attention-based spatial model.

## Next Step

Develop and train an attention-based Graph Neural Network to determine whether learned neighbor importance can further improve property-price prediction.