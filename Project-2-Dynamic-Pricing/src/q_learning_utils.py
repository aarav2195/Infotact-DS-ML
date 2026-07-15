import numpy as np

from src.config import(NUM_ROOMS,NUM_DAYS,NUM_ACTIONS)

def state_to_index(rooms_remaining, days_remaining):
    """
    Convert (rooms,days) into a unique state index.
    """
    return rooms_remaining * NUM_DAYS + days_remaining

def initialize_q_table():
    """
    Initialize Q-table with zeroes.
    """
    total_states = NUM_ROOMS * NUM_DAYS
    return np.zeros((total_states,NUM_ACTIONS))