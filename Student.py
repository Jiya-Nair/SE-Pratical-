students = [
    {"name": "Rahul", "roll_no": 101},
    {"name": "Priya", "roll_no": 102}
]

def search_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return "Student not found"

print(search_student(102))


