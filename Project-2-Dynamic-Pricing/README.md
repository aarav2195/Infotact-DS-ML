# Dynamic Pricing using Reinforcement Learning

## Overview

This project develops a Reinforcement Learning based dynamic pricing system for the travel and hospitality industry. The objective is to maximize hotel revenue by learning an optimal pricing policy over a finite booking horizon.

## Current Progress

### Week 1

Completed

- Project initialization
- Markov Decision Process formulation
- Custom Gym environment development
- Customer demand simulation
- Booking-horizon demand adjustment
- Revenue reward calculation
- Environment validation
- Multi-episode simulation testing

### Week 2

Completed

- Implemented Fixed, Random, and Discount pricing agents.
- Evaluated baseline strategy performance.
- Defined discrete state representation.
- Initialized the Q-table.
- Implemented epsilon-greedy action selection.
- Implemented the Q-Learning update rule.
- Verified successful Q-table learning through initial training.
- Trained the Q-Learning agent for 1000 episodes.
- Monitored cumulative reward during training.
- Evaluated the learned pricing policy.
- Compared Q-Learning with heuristic baseline strategies.
- Saved the trained Q-table for future evaluation.

## Technologies

- Python
- NumPy
- Pandas
- Gymnasium
- Stable-Baselines3
- PyTorch
- Streamlit