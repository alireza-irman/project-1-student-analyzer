
"""
Step 2: Calculate average score for each student
"""

from statistics import mean

def calculate_averages(students):
    """
    Add average score to each student dictionary.

    Args:
        students (List[dict]): List with 'scores' field.

    Returns:
        List[dict]: Updated list with 'average' field.
    """
    for student in students:
        student["average"] = mean(student["scores"])
    return students
