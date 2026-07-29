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
│       ├── final_startegy_comparison.csv
│       ├── policy_evaluation.csv
│       ├── price_trajectory.csv
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
│   ├── 15_dqn_evaluation.ipynb
│   ├── 16_policy_evaluation.ipynb
│   ├── 17_strategy_comparison.ipynb
│   └── 18_price_trajectory_analysis.ipynb
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
│   ├── week-3/
│   │   ├── day1_dqn_setup.md
│   │   ├── day2_experience_replay.md
│   │   ├── day3_dqn_agent.md
│   │   ├── day4_dqn_training.md
│   │   ├── day5_dqn_evaluation.md
│   │   └── week3_summary.md
│   └── week-4/
│       ├── day1_policy_evaluation.md
│       ├── day2_strategy_comparison.md
│       └── day3_price_trajectory.md
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

- Built the hotel pricing simulation environment.
- Implemented realistic booking demand generation.
- Designed the state and action space for reinforcement learning.
- Developed baseline pricing strategies for comparison.

---

## ✅ Week 2

- Implemented the Q-Learning algorithm.
- Built and trained the Q-Table.
- Improved the reward function and demand simulation.
- Evaluated the learned pricing policy.
- Benchmarked Q-Learning against heuristic pricing strategies.
- Generated business performance metrics and evaluation reports.

---

## ✅ Week 3

- Designed and implemented the Deep Q-Network (DQN) architecture.
- Developed the Experience Replay Buffer for efficient experience sampling.
- Implemented the DQN Agent with epsilon-greedy exploration.
- Integrated replay memory with neural network training.
- Added Target Network synchronization for stable learning.
- Applied Smooth L1 (Huber) Loss, reward scaling, and gradient clipping.
- Trained and evaluated the Deep Q-Network model.
- Compared DQN against Fixed Pricing, Random Pricing, Discount Pricing, and Q-Learning.
- Generated reinforcement learning training curves and business performance visualizations.
- Successfully completed the Deep Reinforcement Learning implementation.

---

## 🚀 Week 4 (In Progress)

### ✅ Day 1 – Large-Scale Policy Evaluation

- Loaded the trained Deep Q-Network model.
- Evaluated the pricing policy across 1,000 simulated booking seasons.
- Collected revenue, rooms sold, occupancy, and average price metrics.
- Generated descriptive statistics and performance distributions.
- Exported the policy evaluation dataset for further business analysis.

---

### ✅ Day 2 – Strategy Benchmarking

- Loaded the Week 2 baseline evaluation results.
- Integrated the Deep Q-Network policy evaluation results.
- Benchmarked DQN against Fixed Pricing, Random Pricing, Discount Pricing, and Q-Learning.
- Compared business metrics including revenue, rooms sold, occupancy, and average price.
- Generated comparative business performance visualizations.
- Exported the final strategy comparison dataset for dashboard development.

### ✅ Day 3 – Pricing Trajectory Analysis

- Simulated a complete hotel booking season using the trained DQN agent.
- Recorded daily pricing decisions throughout the booking horizon.
- Tracked room inventory, occupancy progression, and cumulative revenue.
- Generated pricing trajectory and business performance visualizations.
- Exported trajectory data for dashboard development.

---

## 🔄 Upcoming Work

### Week 4

- Develop the business performance dashboard.
- Integrate evaluation, benchmarking, and trajectory analytics.
- Perform final business analysis and policy evaluation.
- Complete project documentation and repository finalization.

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