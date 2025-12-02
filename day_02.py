import sys,os,re,itertools
from utils import *

t=0
rawdata = [r.strip().split(',') for r in open('day_02.txt','rt').readlines()]
for row in rawdata[0]:
  print(row)
  fr,to = row.split('-')
  for i in range(int(fr),int(to)+1):
    n = str(i)
    if n[:len(n)//2] == n[len(n)//2:]: 
      print(i,'dup')
      t+=i
    else: print(i)

print(t)