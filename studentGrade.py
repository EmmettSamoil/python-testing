import random
from re import I
randGrades = []
def randomize():
    for i in range (0, 50):
        randGrades.append(random.randint(1, 100))
randomize()
print(f'''
Menu
1. Display All Grades
2. Randomize Grades
3. Stats
4. Count Honors
5. Exit
''')
selection = int(input("Selection: "))
if selection == 1:
    print(*randGrades, sep = "\n")
if selection == 2:
    randGrades = []
    randomize()
    print(*randGrades, sep = "\n")
if selection == 3:
    highGrade = max(randGrades)
    lowGrade = min(randGrades)
    avgGrade = sum(randGrades) / len(randGrades)
    print(f"Highest Grade: {highGrade}")
    print(f"Lowest Grade: {lowGrade}")
    print(f"Average Grade: {avgGrade}")
if selection == 4: 
    n = 0
    for i in randGrades:
        if i >= 80:
            n += 1
    print(n)
if selection == 5:
    print("")
