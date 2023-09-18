"""Ledger

https://exercism.org/tracks/python/exercises/ledger
"""

# -*- coding: utf-8 -*-
from datetime import datetime

LOCALES = {
    "en_US": {
        "title": ["Date", "Description", "Change"],
        "date": "%m/%d/%Y",
        "change": lambda n, symbol: (lambda s: f"({s})" if n < 0 else f"{s} ") (f"{symbol}{abs(n)/100:,.2f}"),
    },
    "nl_NL": {
        "title": ["Datum", "Omschrijving", "Verandering"],
        "date": "%d-%m-%Y",
        "change": lambda n, symbol: f"{symbol} {n/100:_.2f} ".replace(".", ",").replace("_", "."),
    },
}
CURRENCIES = {"USD": "$", "EUR": "€"}


class LedgerEntry:
    """Contains information regarding a transaction.
    
    Parameters:
    ----------
    date: 
        The date of the transaction.
    description: 
        A brief description of the transaction.
    change: 
        The amount of the transaction in the smallest whole units.

    Attributes:
    ----------
    date: 
        Same as parameter `date`.
    description: 
        Same as parameter `description`.
    change: 
        Same as parameter `change`.

    Functions:
    ---------
    None

    Raises:
    ------
    None
    """
    def __init__(self, date: str, description: str, change: int):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.description = description
        self.change = change

    def __lt__(self, other):
        return self.change < other.change


def create_entry(date: str, description: str, change: int) -> LedgerEntry:
    """Create a `LedgerEntry` object."""
    return LedgerEntry(date, description, change)


def format_entries(currency: str, locale: str, entries: list[LedgerEntry]) -> str:
    """Format a list of `LedgerEntry` objects into a nice view.
    
    :param currency: - "USD" for dollars and "EUR" for euros.
    :param locale: - The string designation of the locale.  "en_US" is fallback.
    :param entries: - A list of `LedgerEntry` objects.
    :return: - A string representing a view of the formatted `LedgerEntry` objects.
    """
    format = LOCALES[locale]
    
    date, description, change = format["title"]
    table = [f"{date:<10} | {description:<25} | {change:<13}"]

    for entry in sorted(entries):
        description = entry.description if len(entry.description) < 26 else f"{entry.description[:22]}..."
        date = entry.date.strftime(format["date"])
        change = format['change'](entry.change, CURRENCIES[currency])

        table.append(f"{date:<10} | {description:<25} | {change:>13}")

    return "\n".join(table)
