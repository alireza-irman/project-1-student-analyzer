
"""
Step 3: Calculate median of student averages
"""

from statistics import median

def calculate_median_score(students):
    """
    Compute median of all student average scores.

    Args:
        students (List[dict]): List with 'average' field.

    Returns:
        float: Median value
    """
    averages = [s["average"] for s in students]
    return median(averages)
