from step2_calculate_average import calculate_averages
from step1_load_data import load_student_data
import csv

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

# Demo
if __name__ == "__main__":
    students = load_student_data("data/students.csv")
    students = calculate_averages(students)
    export_results(students)
    print("Results saved to results/processed.csv")
