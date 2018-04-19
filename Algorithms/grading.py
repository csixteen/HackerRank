for _ in range(int(input())):
    grade = int(input())
    if grade < 38:
        print(grade)
    else:
        diff = 5 - (grade % 5)
        if diff < 3:
            grade += diff

        print(grade)
