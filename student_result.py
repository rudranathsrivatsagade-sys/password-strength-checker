def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"


students = {
    "Rudra": [85, 90, 88],
    "Alex": [70, 65, 72],
    "Sam": [55, 60, 58]
}

for name, marks in students.items():
    avg = calculate_average(marks)
    grade = calculate_grade(avg)
    print(f"{name} -> Average: {avg:.2f}, Grade: {grade}")
