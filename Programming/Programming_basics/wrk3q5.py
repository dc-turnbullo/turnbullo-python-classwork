t1ave = 0
t2ave = 0
t3ave = 0
t1 = 0
t2 = 0
t3 = 0
pupils = int(input("enter the number of pupils"))
for i in range(1,pupils+1):
    t1 = int(input("enter test 1 score for student",i))
    t2 = int(input("enter test 2 score for student",i))
    t3 = int(input("enter test 3 score for student",i))
    t1ave = t1ave + t1
    t2ave = t2ave + t2
    t3ave = t3ave + t3
#next i
overallave = (t1ave + t2ave + t3ave) / 90
t1ave = t1ave / 30
t2ave = t2ave / 30
t3ave = t3ave / 30
print(overallave)
print(t1ave)
print(t2ave)
print(t3ave)
