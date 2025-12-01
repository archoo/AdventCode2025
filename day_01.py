import sys,os,re,itertools
from utils import *

p,t,tz = 50,0,0
rawdata = [(r[0],int(r[1:])) for r in open('day_01.txt','rt').readlines()]

def sign(i):
  if i<0: return -1
  if i>0: return 1
  return 0

for (d,m) in rawdata:
  z=0
  print(f'{p:03d}',d,f'{m:03d}',end=' ')
  c=m%100
  z=(m-c)//100
  if d == 'R':
    if p!=0 and p+c > 100: z+=1
    p=(p+c)%100
  if d == 'L': 
    if p!=0 and p-c < 0: z+=1
    p=(p-c)%100
  tz += 1 if p==0 else 0
  z += 1 if p==0 else 0
  t+=z
  print(f'{z:03d}',f'{p:03d}')

print(len(rawdata))
print(t,tz)
