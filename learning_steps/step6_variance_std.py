from step2_calculate_average import calculate_averages
from step1_load_data import load_student_data
from statistics import variance, stdev

def calculate_variance_std(students):
    averages = [s["average"] for s in students]
    return variance(averages), stdev(averages)

# Demo
if __name__ == "__main__":
    students = load_student_data("data/students.csv")
    students = calculate_averages(students)
    var, std = calculate_variance_std(students)
    print(f"Variance: {var:.2f}")
    print(f"Standard Deviation: {std:.2f}")
