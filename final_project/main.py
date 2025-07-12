
"""
main.py - Final version of Student Analyzer
Author: Alireza Ahmadi Dehnavi
Description: Load student scores, compute statistics, and export processed results.
"""

import csv
import os
from statistics import mean, median, mode, StatisticsError, variance, stdev
from pathlib import Path

# === Paths ===
DATA_PATH = Path("data/students.csv")
OUTPUT_PATH = Path("results/processed.csv")

def load_student_data(file_path):
    """
    Load student data from a CSV file.

    Args:
        file_path (str or Path): Path to the input CSV file.

    Returns:
        List[dict]: List of students with name and scores.
    """
    students = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            scores = [
                int(row["Math"]),
                int(row["Science"]),
                int(row["History"])
            ]
            students.append({
                "name": row["Name"],
                "scores": scores
            })
    return students

def calculate_averages(students):
    """
    Calculate average score for each student.

    Args:
        students (List[dict]): Students with scores

    Returns:
        List[dict]: Updated list with 'average' field
    """
    for student in students:
        student["average"] = mean(student["scores"])
    return students

def calculate_stats(students):
    """
    Compute overall statistics from student averages.

    Args:
        students (List[dict]): Students with 'average' scores

    Returns:
        dict: Dictionary with median, mode, range, variance, std deviation
    """
    averages = [s["average"] for s in students]
    try:
        mod = mode(averages)
    except StatisticsError:
        mod = "No unique mode"
    return {
        "median": median(averages),
        "mode": mod,
        "range": max(averages) - min(averages),
        "variance": variance(averages),
        "std_dev": stdev(averages)
    }

def export_results(students, file_path=OUTPUT_PATH):
    """
    Export student data with averages to CSV file.

    Args:
        students (List[dict]): List of students with 'average'
        file_path (Path): Path to save the output CSV
    """
    os.makedirs(file_path.parent, exist_ok=True)
    with open(file_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "math", "science", "history", "average"])
        for s in students:
            writer.writerow([
                s["name"],
                s["scores"][0],
                s["scores"][1],
                s["scores"][2],
                f"{s['average']:.2f}"
            ])

def main():
    students = load_student_data(DATA_PATH)
    students = calculate_averages(students)
    stats = calculate_stats(students)
    export_results(students)

    print("✅ Final Statistics:")
    for key, value in stats.items():
        print(f"{key.title()}: {value}")

if __name__ == "__main__":
    main()
قبل 
