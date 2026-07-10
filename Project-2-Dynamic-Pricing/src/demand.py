import numpy as np

def simulate_demand(price,days_remaining):
    """
    Simulate customer demand based on room price.
    Higher prices reduce expected bookings.
    """

    if price <= 80:
        base_demand = 8
    elif price <= 100:
        base_demand = 6
    elif price <= 120:
        base_demand = 5
    elif price <= 140:
        base_demand = 3
    else:
        base_demand = 2

    #Customer tends to book more as the departure approaches
    if days_remaining <= 5:
        base_demand += 2
    elif days_remaining <= 10:
        base_demand += 1
        
    demand = np.random.poisson(base_demand)

    return max(demand, 0)