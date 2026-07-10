import numpy as np

def simulate_demand(price):
    """
    Simulate customer demand based on room price.
    Higher prices reduce expected bookings.
    """

    if price <= 80:
        mean_demand = 8
    elif price <= 100:
        mean_demand = 6
    elif price <= 120:
        mean_demand = 5
    elif price <= 140:
        mean_demand = 3
    else:
        mean_demand = 2

    demand = np.random.poisson(mean_demand)

    return max(demand, 0)