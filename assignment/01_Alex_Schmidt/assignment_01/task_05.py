print("Type length x")
x = int(input())
print("Type length y")
y = int(input())
print("Type length z")
z = int(input())

if z >= x + y: # Checks for triangle inequality
  print("Invalid input, please check for triangle inequality")

elif x == y == z: # Checks for equilateral triangles
  print("The triangle is equilateral")

elif x == y or x == z or y == z: # Checks for isoscale triangles
  print("The triangle is isoscele")

elif x != y != z: # Checks for scalene triangles
  print("The triangle is scalene")
