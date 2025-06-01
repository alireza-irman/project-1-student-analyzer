import csv

def load_student_data(file_path):
    students = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            scores = [int(row["math"]), int(row["science"]), int(row["history"])]
            students.append({"name": row["name"], "scores": scores})
    return students

# Demo run (optional)
if __name__ == "__main__":
    data = load_student_data("data/students.csv")
    print(data)
