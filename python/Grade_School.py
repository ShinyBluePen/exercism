"""Grade School

https://exercism.org/tracks/python/exercises/grade-school

@Rakeshksr had a good solution to this problem:
https://exercism.org/tracks/python/exercises/grade-school/solutions/Rakeshksr
"""

class School:
    """Generate a roster for a school.

    Parameters:
    None

    Attributes:
    :student_body: dict - All students in the school.
    :is_student_added_record: list[bool] - Boolean values which are True if a student is 
                                           added to the school.

    Methods:
    :add_student(self, name: str, grade: int): - Add a student to the school roster.
    :roster(self) -> list[str]: - The full roster of the school ordered by grade, then name.
    :grade(self, grade_number: int) -> list[str]: - Return the specified grade's roster.
    :added(self) -> list[bool]: - Return record of adding students to the roster.

    Raises:
    None
    """
    def __init__(self) -> None:
        self.student_body = {}
        self.is_student_added_record = []

    def add_student(self, name: str, grade: int) -> None:
        if grade not in self.student_body:
            self.student_body[grade] = []

        for grades, students in self.student_body.items():
            if name in students:
                return self.is_student_added_record.append(False)
        
        self.student_body[grade].append(name)
        
        return self.is_student_added_record.append(True)

    def roster(self) -> list[str]:
        roster = []
        for grade in sorted(self.student_body.items()):
            for student in sorted(grade[1]):
                roster.append(student)
        return roster

    def grade(self, grade_number: int) -> list[str]:
        return sorted(self.student_body.get(grade_number, []))

    def added(self) -> list[bool]:
        return self.is_student_added_record
