print("Upper bound")
x = int(input()) # Converts input to int
i = 0

while i <= x:
  if i % 3 != 0 or i == 0: # Only prints if i is divisible by 3 (or is 0)
    print(i)
  i = i + 1
  continue
