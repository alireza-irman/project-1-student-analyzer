import csv
import os
from statistics import mean, median, mode, StatisticsError, variance, stdev

def load_student_data(file_path):
    """
    Load student data from a CSV file.
    Expects columns: Name, Math, Science, History.
    Returns a list of dictionaries with name and scores.
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
    Calculate the average score for each student.
    Adds 'average' field to each student dictionary.
    """
    for student in students:
        student["average"] = mean(student["scores"])
    return students

def calculate_stats(students):
    """
    Compute overall statistics for the average scores.
    Returns a dictionary with median, mode, range, variance, and standard deviation.
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
def export_results(students, file_path="results/processed.csv"):
    """
    Export student data with calculated averages to a CSV file.
    Creates the output folder if it doesn't exist.
    """
    import os
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
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
if __name__ == "__main__":
    # Load data from the CSV file
    students = load_student_data(r"D:\AI\student_analyzer_complete\data\students.csv")

    # Calculate each student's average
    students = calculate_averages(students)

    # Compute overall statistics
    stats = calculate_stats(students)

    # Export the processed results
    export_results(students)

    # Print final statistics
    print("✅ Final Statistics:")
    for key, value in stats.items():
        print(f"{key.title()}: {value}")
