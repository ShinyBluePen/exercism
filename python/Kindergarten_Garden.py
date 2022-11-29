"""Kindergarten Garden

https://exercism.org/tracks/python/exercises/kindergarten-garden

@Okram24 has a nice solution, too:
https://exercism.org/tracks/python/exercises/kindergarten-garden/solutions/okram24
"""

class Garden:
    """Generates a garden with two rows of plants.

    Parameters:
    :param diagram: str - The planned arrangement of plants.
    :param students: list[str]=ROSTER - List of students in the class.

    Attributes:
    :ROSTER: list[str] - Default roster of students in a class.
    :PLANTS: dict[str, str] - Plant dictionary map.
    :diagram: str - Modified parameter diagram for easier manipulation.
    :students: list[str] - All students possessing plants in the garden.
    :student_plants: dict[str, list[str] - Map each students own plants.

    Methods:
    :plants(self, student: str) -> list: - Return the plants belonging to a student.

    Raises:
    None
    """
    ROSTER = [
        "Alice",  "Bob",    "Charlie", "David",
        "Eve",    "Fred",   "Ginny",   "Harriet",
        "Ileana", "Joseph", "Kincaid", "Larry",
    ]
    PLANTS = {
        "C": "Clover",
        "G": "Grass",
        "R": "Radishes",
        "V": "Violets",
    }
 
    def __init__(self, diagram: str, students: list[str]=None):
        self.diagram = diagram.split()
        self.students = sorted(students) if students else self.ROSTER
        self.student_plants = {}

        rows = self.diagram
        for student in self.students:
            x = []
            i = 0
            for row in rows:
                for ch in row[:2]:
                    if ch in self.PLANTS:
                        x.append(self.PLANTS[ch])
                    rows[i] = row[2:]
                i += 1
            self.student_plants[student] = x

    def plants(self, student: str) -> list:
        return self.student_plants[student]
