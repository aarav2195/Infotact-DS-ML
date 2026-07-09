import gymnasium as gym
from gymnasium import spaces
import numpy as np

from src.config import *

class HotelPricingEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.action_space = spaces.Discrete(len(PRICE_LEVELS))

        self.observation_space = spaces.Box(
            low=np.array([0,0]),
            high=np.array([TOTAL_ROOMS,BOOKING_DAYS]),
            dtype=np.int32
        )

        self.reset()
    
    def reset(self,seed=None,options=None):
        super().reset(seed=seed)
        self.rooms = TOTAL_ROOMS
        self.day = BOOKING_DAYS
        state = np.array([self.rooms,self.day])

        return state, {}
    
    def step(self, action):
        price = PRICE_LEVELS[action]
        reward = 0
        self.day -= 1
        done = self.day == 0
        state = np.array([self.rooms,self.day])
        return state,reward,done,False,{}