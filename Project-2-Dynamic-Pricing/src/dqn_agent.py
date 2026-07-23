"""
DQN Agent
---------
Implements the Deep Q-Network (DQN) Agent responsible for
action selection and experience storage.
"""

import random
import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim

from src.dqn_model import DQN
from src.replay_buffer import ReplayBuffer

class DQNAgent:
    """
    Deep Q-Network Agent
    """

    def __init__(self,state_size,action_size,learning_rate=0.001,gamma=0.99,epsilon=1.0,epsilon_min=0.05,epsilon_decay=0.998,memory_size=20000,batch_size=128):
        self.state_size = state_size
        self.action_size = action_size

        self.gamma = gamma

        self.learning_rate = learning_rate

        self.batch_size = batch_size

        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay

        self.device = torch.device("cpu")

        # Deep Q-Network
        self.model = DQN(state_size,action_size).to(self.device)

        self.target_model = DQN(state_size, action_size).to(self.device)

        self.target_model.load_state_dict(self.model.state_dict())

        self.target_model.eval()

        self.optimizer = optim.Adam(self.model.parameters(),lr=learning_rate)

        self.criterion = nn.SmoothL1Loss()

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

    def train(self):
        if len(self.memory) < self.batch_size:
            return None
        batch = self.memory.sample(self.batch_size)
        states = np.array([exp[0] for exp in batch],dtype=np.float32)
        actions = np.array([exp[1] for exp in batch])
        rewards = np.array([exp[2] for exp in batch],dtype=np.float32)
        next_states = np.array([exp[3] for exp in batch],dtype=np.float32)
        dones = np.array([exp[4] for exp in batch],dtype=np.float32)

        states = torch.FloatTensor(states)
        next_states = torch.FloatTensor(next_states)
        rewards = torch.FloatTensor(rewards) / 100.0
        actions = torch.LongTensor(actions)
        dones = torch.FloatTensor(dones)

        current_q = self.model(states)
        current_q = current_q.gather(1,actions.unsqueeze(1)).squeeze()

        with torch.no_grad():
            next_q = self.model(next_states)
            next_q = torch.max(next_q,dim=1)[0]

        target_q = rewards + (self.gamma * next_q * (1-dones))

        loss = self.criterion(current_q,target_q.detach())

        self.optimizer.zero_grad()

        loss.backward()

        torch.nn.utils.clip_grad_norm_(self.model.parameters(),max_norm=1.0)

        self.optimizer.step()

        return loss.item()

    def update_target_network(self):

        self.target_model.load_state_dict(self.model.state_dict())

if __name__ == "__main__":

    from src.config import PRICE_LEVELS

    agent = DQNAgent(state_size=2,action_size=len(PRICE_LEVELS))

    print("=" * 50)
    print("DQN Agent Initialized Successfully")
    print("=" * 50)

    print(f"State Size     : {agent.state_size}")
    print(f"Action Size    : {agent.action_size}")
    print(f"Gamma          : {agent.gamma}")
    print(f"Learning Rate  : {agent.learning_rate}")
    print(f"Epsilon        : {agent.epsilon}")
    print(f"Batch Size     : {agent.batch_size}")
    print(f"Replay Buffer  : {len(agent.memory)}")

    sample_state = [50, 30]

    action = agent.select_action(sample_state)

    print(f"\nSample State   : {sample_state}")
    print(f"Selected Action: {action}")
    print(f"Selected Price : {PRICE_LEVELS[action]}")