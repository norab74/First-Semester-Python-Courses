with open('Python Fundamentals/Comp10/GroupExercise/FoodInspectionsFY2010-en-us.csv') as csv:
    lines = csv.read()
    for line in lines.splitlines():
        print(line)