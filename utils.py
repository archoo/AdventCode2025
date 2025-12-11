def swap(l: list,i1,i2):
  l1 = l.pop(i1)
  l.insert(i1,0)
  l2 = l.pop(i2)
  l.insert(i2,l1)
  l.pop(i1)
  l.insert(i1,l2)

dir = {'N':(0,-1),
       'NE':(1,-1),
       'E':(1,0),
       'SE':(1,1),
       'S':(0,1),
       'SW':(-1,1),
       'W':(-1,0),
       'NW':(-1,-1)}

import os
def turtle():
  os.system('cls & color')
  print(f'\033[?25l')

def mv(x,y):
  print(f'\033[{y};{x}H',end='')

def put(ch,x,y,col=0):
  print(f'\033[{y+1};{x+1}H',end='')
  print(f'\033[{col}m'+ch+'\033[0m',end='')
  print(end='',flush=True)
  
def int2base(num, base, abc="0123456789abcdefghijklmnopqrstuvwxyz"):
  if num < 0:
    return '-' + int2base(-num, base, abc)
  output = abc[num % base] # rightmost digit
  while num >= base:
    num //= base # move to next digit to the left
    output = abc[num % base] + output # this digit
  return output

import math

def prime_sieve(n, output={}):
    nroot = int(math.sqrt(n))
    sieve = list(range(n+1))
    sieve[1] = 0
    for i in range(2, nroot+1):
        if sieve[i] != 0:
            m = n//i - i
            sieve[i*i:n+1:i] = [0] * (m+1)
    if type(output) == dict:
        pmap = {}
        for x in sieve:
            if x != 0:
                pmap[x] = True
        return pmap
    else:
      return [x for x in sieve if x != 0]

def get_prime_factors(n, primelist=None):
    if primelist is None:
        primelist = prime_sieve(n,output=[])
    fs = []
    for p in primelist:
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            fs.append((p, count))
    return fs


def plotLine(x0, y0, x1, y1):
  dx = abs(x1 - x0)
  sx = 1 if x0 < x1 else -1
  dy = -abs(y1 - y0)
  sy = 1 if y0 < y1 else -1
  error = dx + dy
    
  line = []
  while True:
    line.append((x0, y0))
    if x0 == x1 and y0 == y1: break
    e2 = 2 * error
    if e2 >= dy:
      error = error + dy
      x0 = x0 + sx
    if e2 <= dx:
      error = error + dx
      y0 = y0 + sy
  return line

def dfs(node,path):
  global t
  step = '.'
  if node is None:
    return
  path.append(node)
  x,y = node
  # put(newdata[y][x],x,y,39)
  try:
    step = newdata[y+2][x]
  except IndexError:
    t+=1
    if t%100000==0:
      mv(0,h+2)
      print(t)
    path.pop()
    # put(newdata[y][x],x,y,39)
    return
  if step == '|':
    search((x,y+2),path)
  if step == '^':
    search((x-1,y+2),path)
    search((x+1,y+2),path)
  path.pop()
  # put(newdata[y][x],x,y,39)
  return
