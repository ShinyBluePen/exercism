"""Making the Grade

https://exercism.org/tracks/python/exercises/making-the-grade
"""

def round_scores(student_scores: list) -> list[int]:
    """"Round all provided student scores.

    :param student_scores: list - List of student exam scores as float or int.
    :return: list[int] - List of student scores *rounded* to nearest integer value.
    """
    return [round(score) for score in student_scores]

def count_failed_students(student_scores: list[int]) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: list - List of integer student scores.
    :return: int - Integer count of student scores at or below 40.
    """
    failed_students = 0

    for score in student_scores:
        if score <= 40:
            failed_students +=1

    return failed_students

def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list[int] - List of integer scores.
    :param threshold : int - .
    :return: list[int] - List of integer scores that are at or above the "best" threshold.
    """

    best_student_scores = []
    
    for score in student_scores:
        if score >= threshold:
            best_student_scores.append(score)

    return best_student_scores
            
def letter_grades(highest: int) -> str:
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - Integer of highest exam score.
    :return: list[int] - List of integer lower threshold scores for each D-A letter grade interval.
        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:

        41 <= "D" <= 55
        56 <= "C" <= 70
        71 <= "B" <= 85
        86 <= "A" <= 100
    """
    letter_grade_ranges = []
    
    for s in range(40, highest-1, (highest-40)//4):
        letter_grade_ranges.append(s+1)
        
    return letter_grade_ranges

def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list[int] - List of scores in descending order.
    :param student_names: list[str] - List of names in descending order by exam score.
    :return: list[str] - List of strings in format ["<rank>. <student name>: <score>"].
    """
    ranked_students = []

    for rank, student in enumerate(zip(student_scores, student_names), start=1):
        ranked_students.append(f"{rank}. {student[1]}: {student[0]}")

    return ranked_students

def perfect_score(student_info: list[list[str]]):
    """Return list that contains the name and grade of the first student to make a perfect score.

    :param student_info: list[list[str]] - List of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for name, score in student_info:
        if score == 100:
            return [name, score]
            
    return []
