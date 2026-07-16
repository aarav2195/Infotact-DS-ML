import numpy as np

def simulate_demand(price, days_remaining):
    """
    Simulate hotel room demand.

    Demand decreases as price increases and
    increases as the arrival date gets closer.
    """

    # Base demand according to price
    demand_map = {
        80: 1.8,
        100: 1.5,
        120: 1.2,
        140: 0.9,
        160: 0.6
    }

    base = demand_map.get(price, 1.0)

    # Booking window effect
    if days_remaining > 20:
        booking_factor = 0.80
    elif days_remaining > 10:
        booking_factor = 1.00
    elif days_remaining > 5:
        booking_factor = 1.20
    else:
        booking_factor = 1.45

    expected_demand = base * booking_factor

    demand = np.random.poisson(expected_demand)

    return max(0, demand)