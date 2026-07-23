# Week 3 – Day 4 Report
## DQN Training Improvements

### Objective
Improve the Deep Q-Network training process by introducing stabilization techniques commonly used in Deep Reinforcement Learning.

### Work Completed
- Added a Target Network for stable Q-value estimation.
- Replaced Mean Squared Error loss with Smooth L1 (Huber) Loss.
- Applied reward scaling before training.
- Implemented gradient clipping to prevent unstable updates.
- Increased training iterations to 500 updates.
- Updated the target network periodically during training.
- Evaluated the trained DQN agent on multiple episodes.
- Visualized the DQN training loss.

### Outcome
The updated DQN training process became significantly more stable. The training loss initially decreased rapidly before converging to a relatively stable range, indicating improved learning behavior compared to the previous implementation.

### File Modified
- src/dqn_agent.py

### File Created
- notebooks/14_dqn_training.ipynb

### Status
✅ Completed