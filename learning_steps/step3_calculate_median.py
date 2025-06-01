from step2_calculate_average import calculate_averages
from step1_load_data import load_student_data
from statistics import median

def calculate_median_score(students):
    averages = [s["average"] for s in students]
    return median(averages)

# Demo
if __name__ == "__main__":
    students = load_student_data("data/students.csv")
    students = calculate_averages(students)
    med = calculate_median_score(students)
    print(f"Median Score: {med:.2f}")
