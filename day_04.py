import sys,os,re,itertools
from utils import *

x,y=0,0
rawdata = [list(r.strip()) for r in open('inputs/day_04.txt','rt').readlines()]
h = len(rawdata)
w = len(rawdata[0])
  
def ring(data,x,y):
  ring = []
  for d in dir.values():
    if y+d[1]<0 or y+d[1]>=h or x+d[0]<0 or x+d[0]>=w:
      ring.append(None)
    else:
      ring.append(data[y+d[1]][x+d[0]])
  return ring

t=0
stuck = False
turtle()
while not stuck:
  stuck = True
  for y in range(h):
    for x in range(w):
      ch = rawdata[y][x]
      if ch=='@' and len([c for c in ring(rawdata,x,y) if c=='@']) < 4:
        stuck = False
        t+=1
        rawdata[y][x]='.'
        col = 31
      else:
        col = 34
      put(ch,x,y,col)
mv(0,h+1)

print(t)