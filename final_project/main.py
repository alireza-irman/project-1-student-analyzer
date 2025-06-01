import csv
from statistics import mean, median, mode, StatisticsError, variance, stdev

def load_student_data(file_path):
    students = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            scores = [int(row["math"]), int(row["science"]), int(row["history"])]
            students.append({"name": row["name"], "scores": scores})
    return students

def calculate_averages(students):
    for student in students:
        student["average"] = mean(student["scores"])
    return students

def calculate_stats(students):
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
    students = load_student_data("data/students.csv")
    students = calculate_averages(students)
    stats = calculate_stats(students)
    export_results(students)

    print("Final Statistics:")
    for key, value in stats.items():
        print(f"{key.title()}: {value}")
