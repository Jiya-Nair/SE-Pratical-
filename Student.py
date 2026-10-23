students = []

def add_student(name, roll_no):
    students.append({
        "name": name,
        "roll_no": roll_no
    })

def display_students():
    for student in students:
        print(student)

add_student("Rahul", 101)
add_student("Priya", 102)

display_students()
