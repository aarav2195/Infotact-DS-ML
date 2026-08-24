# Week 4 – Day 1: GNN Environment and Graph Data Preparation

## Objective

Prepare the finalized Week 3 spatial graph for Graph Neural Network modeling using PyTorch Geometric.

## Work Completed

- Set up and verified the PyTorch and PyTorch Geometric environment.
- Loaded the finalized Week 3 graph datasets.
- Validated node, edge, and target alignment.
- Converted graph edges into PyTorch Geometric edge indices.
- Selected 24 valid node features after excluding `node_id` and the raw property `id`.
- Kept `price` separate as the prediction target.
- Created training, validation, and test masks using a 70/15/15 split.
- Applied feature scaling using training data only.
- Converted node features, graph edges, targets, and masks into a PyTorch Geometric `Data` object.
- Validated edge indices and self-loops.
- Saved the GNN-ready graph dataset.
- Reloaded the saved graph successfully.

## Final Results

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

## Generated Output

`data/processed/week-3/gnn/housing_graph_data.pt`

## Notebook

`notebooks/14_gnn_data_preparation.ipynb`

## Outcome

The finalized Week 3 graph has been successfully converted into a PyTorch Geometric dataset.

The GNN-ready graph now contains the spatial graph structure, 24 node features, property-price targets, and train/validation/test masks required for model training.

## Next Step

Build and train the baseline Graph Neural Network for property-price prediction.