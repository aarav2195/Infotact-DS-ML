"""
Replay Buffer
-------------
Stores experiences collected by the DQN agent and allows
random sampling during training.
"""

import random
from collections import deque


class ReplayBuffer:
    """
    Experience Replay Buffer

    Stores experiences in the form:

    (state, action, reward, next_state, done)
    """

    def __init__(self, capacity=10000):
        """
        Parameters
        ----------
        capacity : int
            Maximum number of experiences stored.
        """
        self.memory = deque(maxlen=capacity)

    def push(self, state, action, reward, next_state, done):
        """
        Store one experience.
        """

        experience = (state,action,reward,next_state,done)
        self.memory.append(experience)

    def sample(self, batch_size):
        """
        Randomly sample a mini-batch.
        """
        return random.sample(self.memory, batch_size)

    def __len__(self):
        """
        Current replay buffer size.
        """
        return len(self.memory)

    def clear(self):
        """
        Remove all stored experiences.
        """
        self.memory.clear()


if __name__ == "__main__":

    buffer = ReplayBuffer(capacity=100)
    buffer.push([50, 30],2,120,[49, 29],False)

    print("Replay Buffer Size:", len(buffer))
    print(buffer.sample(1))