
"""
Step 4: Calculate mode of student averages
"""

from statistics import mode, StatisticsError

def calculate_mode_score(students):
    """
    Compute mode of all student average scores.

    Args:
        students (List[dict]): List with 'average' field.

    Returns:
        float or str: Mode or explanation if no unique mode
    """
    averages = [s["average"] for s in students]
    try:
        return mode(averages)
    except StatisticsError:
        return "No unique mode"
