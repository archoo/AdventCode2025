import sys,os,re,itertools,functools
from utils import *

# rawdata = [[f.strip() for f in r.strip().split(' ') if f.strip() != ''] for r in open('day_06_test.txt','rt').readlines()]
rawdata = [r.strip('\n') for r in open('inputs/day_06.txt','rt').readlines()]

newdata = []
ops = rawdata.pop()
for i in range(len(ops)):
  col = [ops[i]]
  for j in range(len(rawdata)):
    col.append(rawdata[j][i])
  newdata.append(col)
print(newdata)

problist = []
for col in newdata:
  if col[0] in ['+','*']:
    prob = [col.pop(0)]
  n = functools.reduce(lambda a,b: a+b,col)
  if n == ' '*len(col):
    problist.append(prob)
  else:
    prob.append(int(n))
problist.append(prob)
print(problist) 
  
t = 0
for row in problist:
  f = row.pop(0)
  if f == '+':
    t+=sum(row)
  if f == '*':
    t+=functools.reduce(lambda a,b: a*b,row)
    
print(t)
