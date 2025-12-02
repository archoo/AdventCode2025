import sys,os,re,itertools
from utils import *

t=0
rawdata = [r.strip().split(',') for r in open('inputs/day_02.txt','rt').readlines()]
for row in rawdata[0]:
  fr,to = row.split('-')
  for i in range(int(fr),int(to)+1):
    n = str(i)
    if re.fullmatch(r'(.+)\1+',n):
    # if n[:len(n)//2] == n[len(n)//2:]: 
      t+=i

print(t)