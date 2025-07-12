
"""
Step 7: Export student data to CSV
"""

import csv
import os
from pathlib import Path

def export_results(students, output_file):
    """
    Export student scores and averages to CSV.

    Args:
        students (List[dict]): List of student data.
        output_file (str or Path): Path to output CSV.
    """
    os.makedirs(Path(output_file).parent, exist_ok=True)
    with open(output_file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "math", "science", "history", "average"])
        for s in students:
            writer.writerow([
                s["name"],
                *s["scores"],
                f"{s['average']:.2f}"
            ])
