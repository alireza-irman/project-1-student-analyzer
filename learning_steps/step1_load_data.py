
"""
Step 1: Load student data from CSV
"""

import csv
from pathlib import Path

def load_student_data(file_path):
    """
    Load student data from a CSV file.

    Args:
        file_path (str or Path): Path to CSV file with student records.

    Returns:
        List[dict]: List of students with name and score list.
    """
    students = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            scores = [int(row["Math"]), int(row["Science"]), int(row["History"])]
            students.append({"name": row["Name"], "scores": scores})
    return students

# Demo
if __name__ == "__main__":
    data = load_student_data(Path("data/students.csv"))
    print(f"Loaded {len(data)} students.")
    print(data[0])
