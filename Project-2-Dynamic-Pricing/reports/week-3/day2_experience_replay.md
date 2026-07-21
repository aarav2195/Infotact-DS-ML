# Week 3 - Day 2 Report

## Objective

Implement the Experience Replay mechanism required for Deep Q-Network (DQN) training.

## Tasks Completed

- Implemented the Replay Buffer class.
- Stored state transition experiences.
- Verified replay memory size.
- Randomly sampled mini-batches from memory.
- Demonstrated automatic removal of old experiences when buffer capacity is exceeded.
- Explained the importance of Experience Replay in stabilizing DQN training.

## Files Created

- src/replay_buffer.py
- notebooks/12_replay_buffer.ipynb

## Outcome

The Replay Buffer is fully functional and ready to be integrated with the DQN Agent. Random experience sampling has been successfully verified, providing the foundation for stable neural network training in the next phase.