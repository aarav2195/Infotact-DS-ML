# Week 3 – Day 5 Report
## DQN Performance Evaluation and Final Comparison

### Objective

Evaluate the trained Deep Q-Network (DQN) model, compare its performance against previously implemented pricing strategies, and summarize the Deep Reinforcement Learning phase.

---

## Work Completed

- Loaded the trained DQN model.
- Evaluated the model over multiple hotel booking simulations.
- Measured business metrics including:
  - Average Revenue
  - Average Rooms Sold
  - Average Occupancy
  - Average Price
- Visualized the revenue distribution across evaluation episodes.
- Analyzed DQN training using:
  - Episode Reward Curve
  - Moving Average Reward
  - Epsilon Decay Curve
- Compared Deep Q-Network with:
  - Fixed Pricing
  - Random Pricing
  - Discount Pricing
  - Q-Learning
- Generated comparison charts for:
  - Average Revenue
  - Average Price
  - Average Rooms Sold

---

## Outcome

The Deep Q-Network successfully learned an adaptive pricing strategy capable of optimizing long-term revenue while maintaining competitive occupancy levels. Compared with heuristic pricing strategies, the DQN demonstrated improved decision-making through experience replay and neural network function approximation.

---

## Files Updated

- notebooks/15_dqn_evaluation.ipynb
- reports/day5_dqn_evaluation.md
- README.md

---

## Status

✅ Week 3 Completed Successfully