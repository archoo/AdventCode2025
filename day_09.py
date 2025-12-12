import sys,os,re,itertools,pprint
from utils import *

rawdata = [[int(c) for c in r.strip().split(',')] for r in open('inputs/day_09.txt','rt').readlines()]
w = max([x[0] for x in rawdata])
h = max([y[1] for y in rawdata])

print('unique x',len(set([x[0] for x in rawdata])))
print('unique y',len(set([y[1] for y in rawdata])))

possible = list(itertools.combinations(rawdata,2))
rects = [((abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1),a,b) for a,b in possible]
rects.sort(reverse=True)
print('part1',rects[0])

edges = set()
newdata = rawdata[::]
newdata.append(rawdata[0])
for i in range(len(rawdata)):
  a,b = newdata[i],newdata[i+1]
  if a[0] == b[0]:
    if a[1]<=b[1]:s,e=a[1],b[1]
    else: s,e=b[1],a[1]
    for y in range(s,e+1):
      edges.add((a[0],y))
      
  if a[1] == b[1]:
    if a[0]<=b[0]:s,e=a[0],b[0]
    else: s,e=b[0],a[0]
    for x in range(s,e+1):
      edges.add((x,a[1]))

print('rects',len(rects),' edges',len(edges))

print(len(possible))
restricted = []
for r in possible:
  c1,c2 = r
  minx = c1[0] if c1[0] < c2[0] else c2[0]
  miny = c1[1] if c1[1] < c2[1] else c2[1]
  maxx = c2[0] if c1[0] < c2[0] else c1[0]
  maxy = c2[1] if c1[1] < c2[1] else c1[1]
  for e in edges:
    if (minx < e[0] < maxx) and (miny < e[1] < maxy):
      break # rect is already bad
  else:
    restricted.append(r)
print(len(restricted))
  
rects = [((abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1),a,b) for a,b in restricted]
rects.sort(reverse=True)
print('part2',rects[0])  
