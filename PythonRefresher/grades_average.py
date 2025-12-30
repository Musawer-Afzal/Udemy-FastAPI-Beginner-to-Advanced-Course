def calculate_homework(homework_grades):
    sum = 0
    for grade in homework_grades.values():
        sum += grade
    average = round(sum / len(homework_grades), 2)
    return average