print("Upper bound")
num = int(input()) # Converts input to int

a = 0
b = 1

print(0, end = " ")
while num > 1:
    print (b, end = " ")
    a, b = b, a + b

    num -= 1
