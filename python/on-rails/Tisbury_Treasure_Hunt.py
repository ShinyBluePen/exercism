"""Tisbury Treasure Hunt

https://exercism.org/tracks/python/exercises/tisbury-treasure-hunt
"""

def get_coordinate(record: tuple[str]) -> str:
    """Extract a map coordinate from a record.

    :param record: tuple[str] - A (treasure, coordinate) pair.
    :return: str - The extracted map coordinate.
    """
    return record[1]

def convert_coordinate(coordinate: str) -> tuple[str]:
    """Coordinates converted from string form to tuple form.

    :param coordinate: str - A string map coordinate.
    :return: tuple - The string coordinate seperated into its individual components.
    """
    return tuple(coordinate)

def compare_records(azara_record, rui_record) -> bool:
    """Return True if coordinates match from both records.

    :param azara_record: tuple - A (treasure, coordinate) pair.
    :param rui_record: tuple - A (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """
    acoord = convert_coordinate(get_coordinate(azara_record))

    return acoord in rui_record
    

def create_record(azara_record: tuple[str], rui_record: tuple[str]):
    """Combine two records, or output, "not a match".

    :param azara_record: tuple - A (treasure, coordinate) pair.
    :param rui_record: tuple - A (location, coordinate, quadrant) trio.
    :return: tuple - Combined record, or "not a match" if the records are incompatible.
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record

    return "not a match"

def clean_up(combined_record_group: tuple[tuple[str]]) -> str:
    """Return the formatted information from a `combined_record_group`.

    :param combined_record_group: tuple of tuples - Everything from both participants.
    :return: string of tuples separated by newlines - Everything "cleaned". Excess 
    coordinates and information removed.
    """
    report = ""
    
    for group in combined_record_group:
        treasure, _, location, coordinate, quadrant = group
        report += str((treasure, location, coordinate, quadrant)) + "\n"
        
    return report
