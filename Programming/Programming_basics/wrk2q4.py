attendance = int(input("enter student's attendence: "))
examscore = int(input("ente student's exam score: "))
if attendance < 90:
    grade = "fail"
elif examscore > 90:
    grade = "A"
elif examscore > 80 and examscore <= 90:
    grade = "B"
elif examscore > 70 and examscore  <=80:
    grade = "c"
else:
    grade = "Fail"

print(grade)