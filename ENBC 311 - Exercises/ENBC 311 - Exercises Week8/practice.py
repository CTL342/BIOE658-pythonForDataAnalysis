class py_course:
    chapter6 = "OOP"
    chapter7 = "Numpy Module"

    def __init__(self, year, num_students):
        self.year = year
        self.num_students = num_students

course2020 = py_course(2020, 30)
course2025 = py_course(2025, 35)

print(course2020.year)
print(course2025.year)