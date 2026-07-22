"""
DQN Agent
---------
Implements the Deep Q-Network (DQN) Agent responsible for
action selection and experience storage.
"""

import random
import torch

from src.dqn_model import DQN
from src.replay_buffer import ReplayBuffer

class DQNAgent:
    """
    Deep Q-Network Agent
    """

    def __init__(self,state_size,action_size,learning_rate=0.001,gamma=0.99,epsilon=1.0,epsilon_min=0.05,epsilon_decay=0.995,memory_size=10000):
        self.state_size = state_size
        self.action_size = action_size

        self.gamma = gamma

        self.learning_rate = learning_rate

        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay

        self.device = torch.device("cpu")

        # Deep Q-Network
        self.model = DQN(state_size,action_size).to(self.device)

        # Replay Memory
        self.memory = ReplayBuffer(capacity=memory_size)

    def select_action(self, state):
        """
        Select an action using epsilon-greedy policy.
        """

        # Exploration
        if random.random() < self.epsilon:
            return random.randint(0,self.action_size - 1)

        # Exploitation
        state = torch.FloatTensor(state).unsqueeze(0)

        state = state.to(self.device)

        with torch.no_grad():
            q_values = self.model(state)

        action = torch.argmax(q_values).item()

        return action

    def remember(self,state,action,reward,next_state,done):
        """
        Store experience in Replay Buffer.
        """

        self.memory.push(state,action,reward,next_state,done)

    def decay_epsilon(self):
        """
        Reduce exploration rate.
        """

        if self.epsilon > self.epsilon_min:

            self.epsilon *= self.epsilon_decay

            self.epsilon = max(self.epsilon,self.epsilon_min)


if __name__ == "__main__":

    agent = DQNAgent(state_size=2,action_size=5)

    state = [50, 30]

    action = agent.select_action(state)

    print("Selected Action:", action)

    print("Current Epsilon:", agent.epsilon)