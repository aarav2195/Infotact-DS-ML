import numpy as np

def simulate_demand(price, days_remaining):
    """
    Simulate customer demand based on room price
    and remaining booking days.
    """

    # Lower expected demand (more realistic)
    if price <= 80:
        base_demand = 2.5

    elif price <= 100:
        base_demand = 2.0

    elif price <= 120:
        base_demand = 1.7

    elif price <= 140:
        base_demand = 1.3

    else:
        base_demand = 1.0

    # Booking demand increases slightly near departure
    if days_remaining <= 5:
        base_demand += 0.8

    elif days_remaining <= 10:
        base_demand += 0.4

    demand = np.random.poisson(base_demand)

    return max(demand, 0)