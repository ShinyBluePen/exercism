"""ETL (Extract-Transform-Load)

https://exercism.org/tracks/python/exercises/etl
"""

# This function is just inverting a dict.
def transform(legacy_data: dict) -> dict:
    """ETL legacy scrabble scoring data to work with the new scoring system.
    
    :param legacy_data: dict - Data formatted to work with the old system.
    :return: dict - Data formatted to work with the new system.
    """
    # new_data = {}
    # for point, ch_list in legacy_data.items():
    #     for c in ch_list:
    #         new_data[c.lower()] = point
    # return new_data

    return {c.lower(): point 
            for point in legacy_data 
            for c in legacy_data[point]} 
    
