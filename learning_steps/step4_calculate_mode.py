from step2_calculate_average import calculate_averages
from step1_load_data import load_student_data
from statistics import mode, StatisticsError

def calculate_mode_score(students):
    averages = [s["average"] for s in students]
    try:
        return mode(averages)
    except StatisticsError:
        return "No unique mode found"

# Demo
if __name__ == "__main__":
    students = load_student_data("data/students.csv")
    students = calculate_averages(students)
    result = calculate_mode_score(students)
    print(f"Mode Score: {result}")
