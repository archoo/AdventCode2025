import sys,os,re,itertools
from utils import *
t=0
rawdata = [r.strip() for r in open('inputs/day_03.txt','rt').readlines()]
for row in rawdata:
  digits = list(row)
  print(digits)
  j = []
  n = 12
  i=0
  while n>0:
    search = digits[i:len(digits)-n+1]
    j.append(max(search))
    i = digits.index(j[-1],i)+1
    n-=1
  t+=int(''.join(j))
  print(j)
  
print(t)