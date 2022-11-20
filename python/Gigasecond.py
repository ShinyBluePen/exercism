"""Gigasecond

https://exercism.org/tracks/python/exercises/gigasecond
"""

import datetime as dt

def add(moment: dt.datetime) -> dt.datetime:
    "Given a `moment`, determine the moment that would be after a gigasecond has passed."
    return moment + dt.timedelta(seconds=10**9)
