"""Electric Bill

https://exercism.org/tracks/python/exercises/electric-bill
"""

def get_extra_hours(hours: int) -> int:
    """Return the amount of hours.

    :param: hours: - Amount of hours.
    :return: - Amount of "extra" hours.
    """
    return (hours + 3) % 24

def get_kW_amount(watts: int) -> float:
    """Return the kW amount of a given watt amount.

    :param: watts: - Watt amount.
    :return: - kW amount.
    """
    return round((watts / 1000), 1)

def get_kwh_amount(watts: int) -> int:
    """Return the kWh amount of a given watt amount and hours.

    :param: watts: - Watt amount.
    :return: - Kilowatt hour amount.
    """
    return (watts / 1000) // 3600

def get_efficiency(power_factor: float) -> float:
    """Return the efficiency calculated from the power factor.

    :param: power_factor: - Amount of power.
    :return: - Efficiency.
    """
    return power_factor / 100

def get_cost(watts: int, power_factor: float, price: float) -> float:
    """Calculate the cost of a given kWh value, efficiency and price.

    :param: watts: - Watt value.
    :param: power_factor: - Efficiency.
    :param: price: - Price of kWh.
    :return: - Cost of kWh.
    """
    return get_kwh_amount(watts) * price / get_efficiency(power_factor)
