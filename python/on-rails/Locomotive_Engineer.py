"""Locomotive Engineer
 
https://exercism.org/tracks/python/exercises/locomotive-engineer
"""
def get_list_of_wagons(*args):
    """Return a list of wagons.
 
    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)
  
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.
 
    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first, second, new_head, *rest = each_wagons_id
    return [new_head, *missing_wagons, *rest, first, second]
  
def add_missing_stops(route: dict, **kwargs):
    """Add missing stops to route dict.
 
    :param route: - the dict of routing information.
    :param **kwargs: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return {**route, "stops": list(kwargs.values())}
  
def extend_route_information(route: dict, more_route_information: dict) -> dict:
    """Extend route information with more_route_information.
 
    :param route: - the route information.
    :param more_route_information: -  extra route information.
    :return: - extended route information.
    """
    return {**route, **more_route_information}
  
def fix_wagon_depot(wagons_rows: list[tuple]) -> list[tuple]:
    """Fix the list of rows of wagons.
 
    :param wagons_rows: - the list of rows of wagons.
    :return: - list of rows of wagons.
    """
    return [list(i) for i in zip(*wagons_rows)]
