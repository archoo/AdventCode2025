import sys,os,re,itertools,math,pprint
from utils import *

rawdata = {tuple([int(c) for c in r.strip().split(',')]):set() for r in open('inputs/day_08_test.txt','rt').readlines()}
possible = list(itertools.combinations(rawdata,2))
connections = []
for i in range(10):
  m = math.inf
  for a,b in possible:
    d = math.sqrt(pow(abs(a[0]-b[0]),2) + pow(abs(a[1]-b[1]),2) + pow(abs(a[2]-b[2]),2))
    if d<m:
      x,y = a,b
      m = d
  possible.remove((x,y))
  rawdata[x].add(y)
  rawdata[y].add(x)
  connections.append(tuple(sorted([x,y])))
  print(x,y,m)

pprint.pprint(rawdata)