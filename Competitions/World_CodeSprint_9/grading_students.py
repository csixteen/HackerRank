for _ in range(int(input())):
    grade = int(input())
    if grade % 5 >= 3 and grade >= 38:
        print(grade + 5 - grade % 5)
    else:
        print(grade)
