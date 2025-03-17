def KE(mass, speed):
  Kinetic = 0.5 * mass * speed * speed
  return Kinetic

def GPE(mass,height):
  Gravitational = mass * 10 * height
  return Gravitational


m = float(input())
s = float(input())
h = float(input())

mech = KE(m,s) + GPE(m,h)
print(mech)