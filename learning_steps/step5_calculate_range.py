from step2_calculate_average import calculate_averages
from step1_load_data import load_student_data

def calculate_score_range(students):
    averages = [s["average"] for s in students]
    return max(averages) - min(averages)

# Demo
if __name__ == "__main__":
    students = load_student_data("data/students.csv")
    students = calculate_averages(students)
    score_range = calculate_score_range(students)
    print(f"Score Range: {score_range:.2f}")
