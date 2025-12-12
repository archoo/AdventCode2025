import sys,os,re,itertools,pprint
from utils import *

rawdata = [[int(c) for c in r.strip().split(',')] for r in open('inputs/day_09.txt','rt').readlines()]
w = max([x[0] for x in rawdata])+1
h = max([y[1] for y in rawdata])+1

newdata = rawdata[::]
newdata.append(rawdata[0])

possible = list(itertools.combinations(rawdata,2))
rects = [((abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1),a,b) for a,b in possible]
rects.sort(reverse=True)

turtle()
for i in range(len(rawdata)):
  a,b = newdata[i],newdata[i+1]
  if a[0] == b[0]:
    for y in range(a[1],b[1],1 if a[1]<=b[1] else -1):
      put('#',a[0],y,colours['green'])
  if a[1] == b[1]:
    for x in range(a[0],b[0],1 if a[0]<=b[0] else -1):
      put('#',x,a[1],colours['green'])
for x,y in rawdata:
  put('#',x,y,colours['red'])


mv(0,h+1)