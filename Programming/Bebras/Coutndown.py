flag = False
while flag == False:
  num = int(input("enter number"))
  if num < 101 and num > 1:
    flag = True
for i in range(0,num):
    print(num - i)

print("lift off")