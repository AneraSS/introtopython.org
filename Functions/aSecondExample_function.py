def show_students(students, message):
    print(message)
    for student in students:
        print(f" -{student.title()}")

students = ['anna', 'brady', 'michael']

students.sort()
show_students(students, "Our students in alphabetical order:") # as in: function (var1,var2)

students.sort(reverse=True)
show_students(students, "\nOur students in reverse alpha order:")