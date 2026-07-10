# Week 1 Day 3 Report

## Objective

Integrate customer demand simulation into the custom Gym environment.

## Tasks Performed

- Implemented a stochastic demand simulation module.
- Modeled customer demand using a Poisson distribution.
- Connected demand simulation with the Gym environment.
- Updated inventory after room bookings.
- Calculated revenue as the reward function.
- Verified environment behaviour using multiple simulation steps.

## Files Created

- src/demand.py
- notebooks/03_demand_simulation.ipynb

## Files Updated

- src/environment.py

## Result

The environment now simulates realistic customer bookings based on pricing decisions and updates inventory and revenue dynamically.