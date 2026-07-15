import numpy as np

from src.config import (ALPHA,GAMMA,EPSILON)

def choose_action(q_table,state):
    if np.random.random() < EPSILON:
        return np.random.randint(q_table.shape[1])
    return np.argmax(q_table[state])

def update_q_table(q_table,state,action,reward,next_state):
    current_q = q_table[state,action]
    max_future = np.max(q_table[next_state])
    new_q = current_q + ALPHA * (reward + GAMMA * max_future - current_q)
    q_table[state,action] = new_q