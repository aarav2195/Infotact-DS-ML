"""
Deep Q-Network (DQN) Model
--------------------------
This modeule defines the neural network architecture used by the DQN agent.
"""

import torch
import torch.nn as nn

class DQN(nn.Module):
    """
    Deep Q-Network

    Input:
        State = [Rooms Remaining, Days Remaining]

    Output:
        Q-values for each pricing action.
    """

    def __init__(self, state_size, action_size):
        super(DQN,self).__init__()

        self.network = nn.Sequential(nn.Linear(state_size,64),nn.ReLU(),nn.Linear(64,64),nn.ReLU(),nn.Linear(64,32),nn.ReLU(),nn.Linear(32,action_size))

    def forward(self,state):
        return self.network(state)
    
if __name__ == "__main__":
    model = DQN(2,5)
    sample = torch.FloatTensor([50,30])
    print(model)
    print("\nPredicted Q-Values:")
    print(model(sample))