# Week 3 – Day 1: KNN Graph Construction

## Objective

Convert the spatially enriched housing dataset into a KNN-based graph where each property is represented as a node and connected to its nearest geographic neighbors.

## Work Completed

- Loaded and validated the spatial housing dataset.
- Created unique `node_id` values for all properties.
- Implemented KNN graph construction with `K = 5`.
- Used BallTree with Haversine distance.
- Calculated geographic distances in kilometers.
- Created directed graph edges between neighboring properties.
- Handled duplicate coordinates and prevented self-loops.
- Separated property price from node features to prevent target leakage.
- Validated the final graph structure.

## Graph Configuration

| Parameter | Value |
|---|---|
| Number of properties/nodes | 21,613 |
| K nearest neighbors | 5 |
| Distance metric | Haversine |
| Neighbor search algorithm | BallTree |
| Graph type | Directed KNN graph |
| Number of directed edges | 108,065 |
| Self-loops | 0 |

## Results

- **Nodes:** 21,613
- **K:** 5
- **Edges:** 108,065
- **Self-Loops:** 0
- **Distance Metric:** Haversine
- **Validation:** Passed ✅

## Generated Files

- `data/processed/week-3/graph_node_features.csv`
- `data/processed/week-3/graph_targets.csv`
- `data/processed/week-3/knn_graph_edges.csv`

## Outcome

Week 3 Day 1 successfully established the KNN-based spatial graph for the real estate valuation project.

The graph nodes, geographic edges, node features, and property-price targets are now prepared for neighborhood analysis and spatial embedding generation.

## Next Step

Day 2 will focus on graph validation, neighborhood connectivity analysis, and graph-level statistics.