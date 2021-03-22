def pentagonal_number(num):
  total = 1
  i = 1
  while i <= num:
    total = total + (5 * (i-1))
    i += 1
  return total

#1
num = 1
print(pentagonal_number(num))

#6
num = 2
print(pentagonal_number(num))

#16
num = 3
print(pentagonal_number(num))

