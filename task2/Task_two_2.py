if __name__ == '__main__':
    n = int(input())
    students = []
    for _ in range(n):
        name = input()
        score = float(input())
        students.append((name, score))
    students.sort(key=lambda x: x[1])
    second_lowest_grade = None
    for i in range(1, n):
        if students[i][1] > students[i - 1][1]:
            second_lowest_grade = students[i][1]
            break
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
    second_lowest_students.sort()
    for student in second_lowest_students:
        print(student)
