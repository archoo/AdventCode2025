import sys,os,re,itertools,functools
from utils import *

world = {row[0]: row[1].strip().split() for row in [r.strip().split(':') for r in open('inputs/day_11.txt','rt').readlines()]}
visited = set()
tally = 0

@functools.cache
def dfc(node, fft, dac):
  if node == 'out':
      return 1 if fft and dac else 0
  if (outputs := world.get(node)) is None:
      return 0
  if node == 'fft': fft = True
  if node == 'dac': dac = True
  return sum(dfc(out, fft, dac) for out in outputs)

@functools.cache
def dfs(path,node,tgt):
  global tally
  path += node
  if node == tgt:
    tally += 1
    return
  links = world.get(node,[])
  for l in links:
    dfs(path,l,tgt)

dfs('','you','out')
print(tally)

tally = dfc('you',True,True)
print(tally)

tot = dfc('svr', False, False)
print(tot)