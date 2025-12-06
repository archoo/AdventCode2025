import sys,os,re,itertools
from utils import *

rawdata = [r.strip() for r in open('inputs/day_05.txt','rt').readlines()]
rng = []
ing = []
for row in rawdata:
  if '' == row: 
    continue
  if '-' in row: rng.append(tuple((int(r) for r in row.split('-'))))
  else: ing.append(int(row))
gd = set()
rng.sort()

t=0
for g in ing:
  for l,h in rng:
    t+=h-l 
    if g>=l and g<=h: gd.add(g) 
print(len(gd),t)
# [print(r,r[1]-r[0]+1) for r in rng]

realrng = []
rl,rh=rng.pop(0)
for l,h in rng:
  if l>rh:
    realrng.append((rl,rh))
    rl,rh=l,h
  else:
    if h>rh:
      rh=h
realrng.append((rl,rh))
a=0
for l,h in realrng:
  a+=(h-l)+1
[print(r,r[1]-r[0]+1) for r in realrng]
print(a)
  