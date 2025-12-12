import sys,os,re,itertools,time,functools,random
from utils import *

rawdata = [list(r.strip()) for r in open('inputs/day_07.txt','rt').readlines()]
w,h = len(rawdata[0]),len(rawdata)

beams = []
for c in rawdata[0]:
  beams.append('.') if c=='.' else beams.append('|')

newdata = []
def refresh():
  turtle()
  for y in range(len(newdata)):
    for x in range(len(newdata[0])):
      match newdata[y][x]:
        case '.': col = 30
        case '|': col = colours['RED']
        case '^': col = colours['green']
      put(newdata[y][x],x,y,col)

t = 0
paths = [0 if c == '.' else 1 for c in rawdata[0]]
for y in range(h):
  line = ''
  for x in range(w):
    if rawdata[y][x] == 'S':
      start = (x,y)
      beams[x] = '|'
      ch = 'S'
      col = 31
      line += ch
    if rawdata[y][x] == '.':
      ch = beams[x]
      col = 34
      line += ch
    if rawdata[y][x] == '^':
      if beams[x] == '|': 
        t+=1
        paths[x-1]+=paths[x]
        paths[x+1]+=paths[x]
        paths[x] = 0
      beams[x-1] = '|'
      beams[x] = '.'
      beams[x+1] = '|'
      ch = '^'
      col = 37
      line = line[:-1]+'|^'
  newdata.append(list(line))

refresh()
print(len([x for x in beams if x=='|']), t, sum(paths))

x,y = start
while True:
  put(newdata[y][x],x,y,col)
  y+=1
  if y>=h:
    x,y = start
    continue
  if newdata[y][x] == '|':
    col = random.choice(list(colours.values()))
    continue
  if newdata[y][x] == '^':
    col = colours['WHITE']
    x += random.choice([-1,1])
  