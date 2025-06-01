from step1_load_data import load_student_data
from statistics import mean

def calculate_averages(students):
    for student in students:
        student["average"] = mean(student["scores"])
    return students

# Demo
if __name__ == "__main__":
    data = load_student_data("data/students.csv")
    data_with_avg = calculate_averages(data)
    for item in data_with_avg:
        print(f"{item['name']} → Average: {item['average']:.2f}")
