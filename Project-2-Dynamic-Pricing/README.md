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
│       ├── qlearning_results.csv
│       ├── simulation_results.csv
│       └── state_space.csv
│
├── models/
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
│   └── 10_performance_analysis.ipynb
│
├── reports/
│   ├── week-1/
│   │   ├── day1_problem_formulation.md
│   │   ├── day2_environment_design.md
│   │   ├── day3_demand_simulation.md
│   │   ├── day4_environment_validation.md
│   │   ├── day5_environment_testing.md
│   │   └── week1_summary.md
│   └── week-2/
│       ├── day1_baseline_strategies.md
│       ├── day2_qlearning_preparation.md
│       ├── day3_qlearning_implementation.md
│       ├── day4_qlearning_training.md
│       ├── day5_performance_analysis.md
│       └── week2_summary.md
│
├── src/
│   ├── baseline_agents.py
│   ├── config.py
│   ├── demand.py
│   ├── environment.py
│   ├── q_learning.py
│   └── q_learning_utils.py
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

- Built hotel pricing environment
- Implemented booking simulation
- Designed state and action space
- Created baseline pricing agents

---

## ✅ Week 2

- Implemented Q-Learning algorithm
- Created Q-Table
- Trained pricing agent
- Tuned demand simulation
- Improved reward function
- Evaluated learned pricing policy
- Compared RL with heuristic strategies
- Generated business performance reports

## 🚀 Week 3 (In Progress)

### Day 1
- Installed PyTorch for Deep Reinforcement Learning.
- Designed the Deep Q-Network architecture.
- Verified forward propagation using sample hotel booking states.
- Prepared the project for DQN agent implementation.

---

## 🔄 Upcoming Work

### Week 3

- Deep Q-Network (DQN)
- Neural Network Function Approximation
- Experience Replay
- Target Network

### Week 4

- Hyperparameter Tuning
- Policy Optimization
- Performance Benchmarking
- Final Evaluation

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