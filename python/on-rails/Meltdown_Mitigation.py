"""Meltdown Mitigation

https://exercism.org/tracks/python/exercises/meltdown-mitigation
"""

def is_criticality_balanced(temperature: int, neutrons_emitted: int) -> bool:
    """Verify criticality is balanced.

    :param temperature: - Temperature value in kelvin.
    :param neutrons_emitted: - Number of neutrons emitted per second.
    :return: - True if conditions met.

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    t_n_product = temperature * neutrons_emitted
    
    return temperature < 800 and neutrons_emitted > 500 and t_n_product < 500000


def reactor_efficiency(voltage: int, current: int, theoretical_max_power: int) -> str:
    """Assess reactor efficiency zone.

    :param voltage: - Voltage value.
    :param current: = Current value.
    :param theoretical_max_power: - Power that corresponds to a 100% efficiency.
    :return: - .One of 'green', 'orange', 'red', or 'black'.

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    efficiency = (generated_power/ theoretical_max_power) * 100
    
    if efficiency >= 80:
        return "green"
    if 80 > efficiency >= 60:
        return "orange"
    if 60 > efficiency >= 30:
        return "red"
    return "black"


def fail_safe(temperature: int, neutrons_produced_per_second: int, threshold: int) -> str:
    """Assess and return status code for the reactor.

    :param temperature: - Value of the temperature in kelvin.
    :param neutrons_produced_per_second: - Neutron flux.
    :param threshold: - Threshold.
    :return: - One of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  'DANGER'
    """
    t_nps_product = temperature * neutrons_produced_per_second

    if t_nps_product > threshold * 1.1:
        return "DANGER"
    if t_nps_product < threshold * 0.9:
        return "LOW"
    return "NORMAL"
