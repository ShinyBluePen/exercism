"""Guido's Gorgeous Lasagna

https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna
"""

EXPECTED_BAKE_TIME = 40

# equal to the time it takes to prepare a single layer


def bake_time_remaining(minutes):
    """Calculate the bake time remaining.
    
    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    
    return EXPECTED_BAKE_TIME - minutes
  
def preparation_time_in_minutes(layers):
    """ """
    return layers * PREPARATION_TIME
  
def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """ """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
