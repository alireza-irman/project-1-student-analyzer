
"""
Step 6: Calculate variance and standard deviation
"""

from statistics import variance, stdev

def calculate_dispersion(students):
    """
    Compute variance and standard deviation of averages.

    Args:
        students (List[dict]): List with 'average' field.

    Returns:
        dict: variance and std deviation
    """
    averages = [s["average"] for s in students]
    return {
        "variance": variance(averages),
        "std_dev": stdev(averages)
    }
