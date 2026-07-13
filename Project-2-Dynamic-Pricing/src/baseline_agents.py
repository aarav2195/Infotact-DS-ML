import numpy as np

def fixed_price_agent():
    """
    Always chooses the middle price level.
    """
    return 2

def random_price_agent():
    """
    Selects a random price action.
    """
    return np.random.randint(0,5)

def discount_agent(day_remaining):
    """
    Applies larger discount as departure approaches.
    """

    if day_remaining > 20:
        return 4
    elif day_remaining > 10:
        return 3
    elif day_remaining > 5:
        return 2
    else:
        return 10