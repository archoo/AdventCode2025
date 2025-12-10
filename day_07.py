import sys,os,re,itertools,time,functools
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
        case '.': col = 31
        case '|': col = 34
        case '^': col = 37
      put(newdata[y][x],x,y,col)

t = 0
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
      if beams[x] == '|': t+=1
      beams[x-1] = '|'
      beams[x] = '.'
      beams[x+1] = '|'
      ch = '^'
      col = 37
      line = line[:-1]+'|^'
  newdata.append(list(line))

refresh()
print(len([x for x in beams if x=='|']), t)

finalpaths,stable = set(),True
t = 0
x,y = start

def search(node,path):
  global t
  step = '.'
  if node is None:
    return
  path.append(node)
  x,y = node
  # put(newdata[y][x],x,y,39)
  try:
    step = newdata[y+2][x]
  except IndexError:
    t+=1
    if t%100000==0:
      mv(0,h+2)
      print(t)
    path.pop()
    # put(newdata[y][x],x,y,39)
    return
  if step == '|':
    search((x,y+2),path)
  if step == '^':
    search((x-1,y+2),path)
    search((x+1,y+2),path)
  path.pop()
  # put(newdata[y][x],x,y,39)
  return

search(start,[])

# for pth in finalpaths:
#   refresh()
#   for i,j in pth:
#     put(newdata[j][i],i,j,39)
#   time.sleep(0.1)
# mv(0,h+2)
# print(len(finalpaths))
