import sys,os,re,itertools,math,pprint,functools
from utils import *

rawdata = [tuple([int(c) for c in r.strip().split(',')]) for r in open('inputs/day_08.txt','rt').readlines()]
possible = list(itertools.combinations(rawdata,2))
connections = [(math.sqrt(pow(abs(a[0]-b[0]),2) + pow(abs(a[1]-b[1]),2) + pow(abs(a[2]-b[2]),2)),(a,b)) for a,b in possible]
connections.sort()
circuits = []

full = False
for d,cn in connections:
  if full: break
  x,y = cn
  found = False
  active = set()
  for c in circuits:
    if x in c or y in c: 
      found = True
      if active == set():
        active = c
        active.add(x)
        active.add(y)
      else:
        active |= c
        circuits.remove(c)
    if len(active) == len(rawdata): full = cn
  if not found:
    circuits.append(set([x,y]))
    
print(full,full[0][0]*full[1][0])
circuits.sort(key=len,reverse=True)
print(len(connections),len(circuits),functools.reduce(lambda a,b: a*b,[len(c) for c in circuits[:3]]))
# pprint.pprint(connections)