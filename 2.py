students = {}

# Заполнение словаря
n = int(input("Введите количество студентов: "))
for i in range(n):
    surname = input("Введите фамилию студента: ")
    name = input("Введите имя студента: ")
    birthdate = input("Введите дату рождения студента (дд-мм-гггг): ")
    record_book = input("Введите номер зачетной книжки студента: ")
    subjects = []
    m = int(input("Введите количество предметов: "))
    for j in range(m):
        subject = input("Введите название предмета: ")
        exam_date = input("Введите дату экзамена (дд-мм-гггг): ")
        teacher = input("Введите ФИО преподавателя: ")
        grade = input("Введите оценку: ")
        subjects.append([subject, exam_date, teacher, grade])
    students[record_book] = [surname, name, birthdate, subjects]

# Вывод студентов с двойками
bad_students = []
for record_book, info in students.items():
    for subjects in info[3]:
        if "2" in subjects[3]:
            bad_students.append([info[0], info[1]])
            break

# Вывод таблицы студентов с двойками
print("Список студентов с двойками:")
print("{:<15} {:<15}".format("Фамилия", "Имя"))
for student in bad_students:
    print("{:<15} {:<15}".format(student[0], student[1]))
