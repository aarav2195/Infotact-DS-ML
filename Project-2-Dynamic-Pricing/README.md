# 🏨 Dynamic Hotel Pricing using Reinforcement Learning

> **Project 2 - Infotact Solutions Data Science & Machine Learning Internship**

An intelligent **Dynamic Hotel Pricing System** built using **Reinforcement Learning (Q-Learning)** to optimize hotel room pricing based on inventory levels, booking window, and customer demand.

The project simulates a real-world hotel booking environment where an AI agent learns pricing strategies that maximize long-term revenue while maintaining realistic occupancy levels.

---

# 📌 Project Overview

Dynamic pricing is widely used in industries such as:

- 🏨 Hotels
- ✈ Airlines
- 🚕 Ride Sharing
- 🎟 Event Ticketing
- 🛍 E-commerce

Instead of keeping room prices fixed, this project trains an intelligent pricing agent that automatically decides the best room price according to the current booking situation.

The objective is to maximize cumulative revenue through Reinforcement Learning.

---

# 🎯 Objectives

- Build a realistic hotel booking simulator.
- Implement heuristic pricing strategies.
- Train a Q-Learning pricing agent.
- Compare Reinforcement Learning against traditional pricing methods.
- Evaluate pricing decisions using business metrics.

---

# 🛠 Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python 3 |
| Numerical Computing | NumPy |
| Data Analysis | Pandas |
| Visualization | Matplotlib |
| Reinforcement Learning | Q-Learning |
| Environment | Custom Gym-style Environment |
| Version Control | Git & GitHub |
| Notebook | Jupyter Notebook |

---

# 📂 Project Structure

```text
Project-2-Dynamic-Pricing/

│
├── data/
│   ├── raw/
│   └── processed/
│       ├── baseline_results.csv
│       ├── dqn_training_history.csv
│       ├── qlearning_results.csv
│       ├── simulation_results.csv
│       ├── state_space.csv
│       └── week2_final_comparison.csv
│
├── models/
│   ├── dqn_model.pth
│   └── q_table.npy
│
├── notebooks/
│   ├── 01_problem_formulation.ipynb
│   ├── 02_environment_design.ipynb
│   ├── 03_demand_simulation.ipynb
│   ├── 04_environment_validation.ipynb
│   ├── 05_environment_testing.ipynb
│   ├── 06_baseline_strategies.ipynb
│   ├── 07_qlearning_preparation.ipynb
│   ├── 08_qlearning_implementation.ipynb
│   ├── 09_qlearning_training.ipynb
│   ├── 10_performance_analysis.ipynb
│   ├── 11_dqn_setup.ipynb
│   ├── 12_replay_buffer.ipynb
│   ├── 13_dqn_agent.ipynb
│   ├── 14_dqn_training.ipynb
│   └── 15_dqn_evaluation.ipynb
│
├── reports/
│   ├── week-1/
│   │   ├── day1_problem_formulation.md
│   │   ├── day2_environment_design.md
│   │   ├── day3_demand_simulation.md
│   │   ├── day4_environment_validation.md
│   │   ├── day5_environment_testing.md
│   │   └── week1_summary.md
│   ├── week-2/
│   │   ├── day1_baseline_strategies.md
│   │   ├── day2_qlearning_preparation.md
│   │   ├── day3_qlearning_implementation.md
│   │   ├── day4_qlearning_training.md
│   │   ├── day5_performance_analysis.md
│   │   └── week2_summary.md
│   └── week-3/
│       ├── day1_dqn_setup.md
│       ├── day2_experience_replay.md
│       ├── day3_dqn_agent.md
│       ├── day4_dqn_training.md
│       ├── day5_dqn_evaluation.md
│       └── week3_summary.md
│
├── src/
│   ├── baseline_agents.py
│   ├── config.py
│   ├── demand.py
│   ├── dqn_agent.py
│   ├── dqn_model.py
│   ├── environment.py
│   ├── q_learning.py
│   ├── q_learning_utils.py
│   └── replay_buffer.py
│
├── README.md
└── requirements.txt
```

---

# ⚙ Problem Statement

Hotels often use fixed pricing, which can lead to:

- Unsold inventory
- Revenue loss
- Poor occupancy management

This project develops an AI pricing agent capable of learning better pricing decisions through continuous interaction with a simulated booking environment.

---

# 🧠 Reinforcement Learning Workflow

```
Current State
      │
      ▼
Q-Learning Agent
      │
Choose Price
      │
      ▼
Hotel Environment
      │
Receive Reward
      │
      ▼
Update Q-Table
      │
      ▼
Repeat
```

---

# 📊 State Representation

The environment represents each state using:

- Remaining hotel rooms
- Remaining booking days

Example:

```
State = (Rooms Remaining, Days Remaining)

(50,30)
(42,18)
(15,5)
```

---

# 🎯 Action Space

The agent selects one of five pricing actions.

| Action | Room Price |
|---------|-----------:|
| 0 | ₹80 |
| 1 | ₹100 |
| 2 | ₹120 |
| 3 | ₹140 |
| 4 | ₹160 |

---

# 💰 Reward Function

The learning objective is to maximize profit.

```
Reward = Rooms Sold × (Room Price − Operating Cost)
```

This encourages the agent to balance pricing decisions with customer demand.

---

# 📈 Baseline Pricing Strategies

Before applying Reinforcement Learning, three heuristic pricing strategies were implemented:

- 📌 Fixed Pricing
- 🎲 Random Pricing
- 📉 Discount Pricing

These serve as benchmark strategies for comparison.

---

# 🤖 Q-Learning Agent

The agent learns pricing policies using:

- Epsilon-Greedy Exploration
- Bellman Equation
- Q-Table Updates
- Episodic Learning

The learned policy is stored as:

```
models/q_table.npy
```

---

# 📊 Performance Metrics

The project evaluates pricing strategies using business-focused metrics:

- 💵 Average Revenue
- 🏨 Average Rooms Sold
- 📈 Average Occupancy (%)
- 💲 Average Room Price
- 🔁 Number of Evaluation Episodes

---

# 📉 Visualizations

The project generates:

- Revenue Comparison
- Occupancy Comparison
- Rooms Sold Comparison
- Average Price Comparison
- Training Reward Curve
- Moving Average Reward Curve

---

# 🚀 Project Progress

## ✅ Week 1

- Built hotel pricing environment.
- Implemented booking simulation.
- Designed the state and action space.
- Developed baseline pricing strategies.

---

## ✅ Week 2

- Implemented the Q-Learning algorithm.
- Built and trained the Q-Table.
- Tuned demand simulation and reward function.
- Evaluated learned pricing policies.
- Compared heuristic pricing strategies with Reinforcement Learning.
- Generated business performance reports and evaluation metrics.

---

## ✅ Week 3

### ✅ Day 1 – Deep Q-Network Setup

- Configured the PyTorch environment.
- Designed the Deep Q-Network architecture.
- Verified neural network forward propagation.
- Prepared the project for Deep Reinforcement Learning.

---

### ✅ Day 2 – Experience Replay

- Implemented the Experience Replay Buffer.
- Stored agent experiences for replay learning.
- Added random mini-batch sampling.
- Managed replay memory efficiently.

---

### ✅ Day 3 – DQN Agent Implementation

- Developed the Deep Q-Network Agent.
- Integrated replay memory with the neural network.
- Implemented epsilon-greedy exploration.
- Connected experience collection with DQN learning.

---

### ✅ Day 4 – Stable DQN Training

- Trained the Deep Q-Network.
- Added Target Network synchronization.
- Implemented Smooth L1 (Huber) Loss.
- Applied reward scaling.
- Added gradient clipping.
- Generated stable DQN training loss curves.
- Improved training convergence and learning stability.

---

### ✅ Day 5 – Performance Evaluation

- Evaluated the trained Deep Q-Network.
- Generated reinforcement learning performance visualizations.
- Compared DQN with Fixed Pricing, Random Pricing, Discount Pricing, and Q-Learning.
- Evaluated business metrics including revenue, occupancy, rooms sold, and pricing.
- Completed the Deep Reinforcement Learning implementation.

---

## 🔄 Upcoming Work

### 🚀 Week 4

- Hyperparameter Tuning
- Policy Optimization
- Performance Benchmarking
- Final Evaluation
- Project Documentation and Optimization

---

# 📁 Outputs

Generated project outputs include:

- Trained Q-Table
- Evaluation Reports
- Performance Comparison Dataset
- Business Performance Charts
- Weekly Progress Reports

---

# 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Reinforcement Learning
- Q-Learning
- Markov Decision Process (MDP)
- State-Action Value Functions
- Dynamic Pricing
- Business Analytics
- Simulation Design
- Python Development
- Git & GitHub Workflow

---

# 🔮 Future Improvements

- Deep Q-Network (DQN)
- Double DQN
- Prioritized Experience Replay
- Multi-Hotel Pricing
- Seasonal Demand Modeling
- Customer Segmentation
- Real-world Hotel Dataset Integration

---

# 👨‍💻 Author

**Aarav Shah**

Data Science & Machine Learning Intern

Infotact Solutions

---

# ⭐ Acknowledgements

Developed as part of the **Infotact Solutions Data Science & Machine Learning Internship Program**, focusing on Reinforcement Learning for Dynamic Pricing and Revenue Optimization.