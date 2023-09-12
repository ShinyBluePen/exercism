"""Currency Exchange

https://exercism.org/tracks/python/exercises/currency-exchange
"""

def exchange_money(budget: float, exchange_rate: float) -> float:
    """Spending power of the `budget` in a foreign currency based on the `exchange_rate`.

    :param budget: - Amount of money you are planning to exchange.
    :param exchange_rate: - Unit value of the foreign currency.
    :return: - Exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: int) -> float:
    """Leftover money after a currency exchange.

    :param budget: - Amount of money you own.
    :param exchanging_value: - Amount of your money you want to exchange now.
    :return: - Amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Total value of all `bills` based on their `denomination`.

    :param denomination: - The value of a bill.
    :param number_of_bills: - Amount of bills you received.
    :return: - Total value of bills you now have.
    """
    return denomination * number_of_bills


def get_number_of_bills(budget: float, denomination: int) -> int:
    """Total amount of bills that will be received from an exchange.

    :param budget: - The amount of money you are planning to exchange.
    :param denomination: - The value of a single bill.
    :return: - Number of bills after exchanging all your money.
    """
    return budget // denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """The maximum value you can get from a currency exchange.

    :param budget: - The amount of your money you are planning to exchange.
    :param exchange_rate: - The unit value of the foreign currency.
    :param spread: - Percentage that is taken as an exchange fee.
    :param denomination: - The value of a single bill.
    :return: - Maximum value you can get.
    """
    exchange_rate += exchange_rate * (spread / 100)
    exchanged_value = exchange_money(budget, exchange_rate)
    number_of_exchanged_bills = get_number_of_bills(exchanged_value, denomination)

    return get_value_of_bills(number_of_exchanged_bills, denomination)


def get_leftover_of_bills(budget: float, denomination: int) -> float:
    """Number of bills which can not be exchaned.

    :param budget: - The amount of your money you are planning to exchange.
    :param denomination: - The value of a single bill.
    :return: - Non-exchangeable value.
    """
    return budget % denomination
