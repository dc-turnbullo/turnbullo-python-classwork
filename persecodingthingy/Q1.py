p1 = int(input())
p2 = int(input())
p3 = int(input())

p1 *= 1.1
p1 = p1 - (p1 % 1)
p2 *= 1.1
p2 = p2 - (p2 % 1)
p3 *= 1.1
p3 = p3 - (p3 % 1)
p1 = int(p1)
p2 = int(p2)
p3 = int(p3)
print(p1 + p2 + p3)