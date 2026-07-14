import numpy as np

NUM_ROOMS = 51
NUM_DAYS = 31
NUM_ACTIONS = 5

def state_to_index(rooms_remaining, days_remaining):
    """
    Convert (rooms,days) into a unique state index.
    """
    return rooms_remaining * NUM_DAYS + days_remaining

def initialize_q_table():
    """
    Initialize Q-table with zeroes.
    """
    num_states = NUM_ROOMS * NUM_DAYS
    return np.zeros((num_states,NUM_ACTIONS))