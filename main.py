from collections import deque


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

def encode(s):
  i = 0
  enc = ""
  while i < len(s):
    current = s[i]
    previous = s[i]
    run = 0
    while current == previous:
      run += 1
      previous = current
      i += 1
      if(i == len(s)):
        break
      current = s[i]
    enc += str(run)
    enc += previous
  return enc

#3A4B2C
s = "AAABBBBCC"
print(encode(s))

#1L2B1W1E15Q1C
s = "LBBWEQQQQQQQQQQQQQQQC"
print(encode(s))

def decode(s):
  dec = ""
  i = 0
  while i<len(s):
    num = s[i]
    i += 1
    let = s[i]
    i += 1
    dec += let * int(num)
  return dec

#AAABBBBCC
s = "3A4B2C"
print(decode(s))

#LBBWEQQQC
s = "1L2B1W1E3Q1C"
print(decode(s))

def is_balanced(s):
  stack = deque()
  for letter in s:
    if letter == '(' or letter == "{" or letter == "[":
      stack.append(letter)
    if letter == ")":
      if stack[-1] == "(":
        stack.pop()
    if letter == "}":
      if stack[-1] == "{":
        stack.pop()
    if letter == "]":
      if stack[-1] == "[":
        stack.pop()
  return len(stack) == 0

#true
s = "([])[]({})"
print(is_balanced(s))

#false
s = "([])[({})"
print(is_balanced(s))

