
"""
Step 5: Calculate range of student averages
"""

def calculate_range_score(students):
    """
    Compute range (max - min) of student averages.

    Args:
        students (List[dict]): List with 'average' field.

    Returns:
        float: Range value
    """
    averages = [s["average"] for s in students]
    return max(averages) - min(averages)
