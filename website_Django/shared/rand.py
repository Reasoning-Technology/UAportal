#--------------------------------------------------------------------------------
# generate a random string length n of form
#    "" | [A-Za-z^IloO] | [A-Za-z^IloO][0-9A-Za-z_-^IloO01]*[A-Za-z^IloO]
#

import random

# note missing IloO01.
# period and comman might be difficult, light period might be missed
# capital I in san-serif font looks like number 1.
legal_chars_end = "ABCDEFGHJKLMNPQRSTUVWXaZbcdefghijkmnpqrstuvwxz"
legal_chars = "23456789ABCDEFGHJKLMNPQRSTUVWXZabcdefghijkmnpqrstuvwxz_-"

def index():
  return random.randrange(0 ,len(legal_chars))

def index_end():
  return random.randrange(0 ,len(legal_chars_end))

def char():
  return legal_chars[index()]
  
def char_end():
  return legal_chars_end[index_end()]

def string(n=6):
  if n < 0 : raise Exception("string called with negative length")
  if n == 0 : return ""

  result = char_end()
  if  n == 1: return result

  for _ in range(n-2): result += char()
  result += char_end()

  return result

def  test_0():
  limit = 1e7 # surely by then
  i = 0
  c = char()
  while c != '~' and i < limit:
    i += 1
    c = char()
  print(i)
  return i < limit

def  test_1():
  limit = 1e7 # surely by then
  i = 0
  c = char()
  while c != '0' and i < limit:
    i += 1
    c = char()
  print(i)
  return i < limit

def  test_2():
  limit = 1e7 # surely by then
  i = 0
  c = char_end()
  while c != 'z' and i < limit:
    i += 1
    c = char_end()
  print(i)
  return i < limit

def  test_3 ():
  limit = 1e7 # surely by then
  i = 0
  c = char_end()
  while c != 'A' and i < limit:
    i += 1
    c = char_end()
  print(i)
  return i < limit

def  test_4():
  s0 = string()
  s1 = string(10)
  s2 = string(100)

  print(s0)
  print(s1)
  print(s2)

  return len(s0)==6 and len(s1)==10 and len(s2)==100

