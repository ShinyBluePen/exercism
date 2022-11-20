"""Space Age

https://exercism.org/tracks/python/exercises/space-age
"""

class SpaceAge:
    """Use seconds to determine one's age on each of the Solar system's planets.

    Arguments:
    :seconds: int - Used to determine the age of an individual in a specified planets' years.
    
    Attributes:
    :ORBITAL_PERIODS: dict{str, float} - Orbital periods of each planet in the solar system in seconds.
    
    Methods:
    :on_{planet}: - Return the age in years (to the second decimal) of an individual on the given planet.
    """
    def __init__(self, seconds: int):
        esois = 31557600 # earth standard orbit in seconds
        _planets = "mercury venus earth mars jupiter saturn uranus neptune".split()
        _ratios = [0.2408467, 0.61519726, 1, 1.8808158, 11.862615, 29.447498, 84.016846, 164.79132]
        self.ORBITAL_PERIODS = {planet: esois * ratio for planet, ratio in zip(_planets, _ratios)}
        
        for planet, year in self.ORBITAL_PERIODS.items():
            age = round((seconds / year), 2)
            setattr(self, f"on_{planet}", lambda x=age: x)
