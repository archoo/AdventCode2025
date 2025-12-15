import sys,os,re,itertools,functools
from utils import *

world = {row[0]: row[1].strip().split(' ') for row in [r.strip().split(':') for r in open('inputs/day_11.txt','rt').readlines()]}
tally = 0

@functools.cache
def dfs(path,node,tgt):
  global tally
  path += node
  if node == tgt:    
    tally+=1
    return
  links = world.get(node,[])
  for l in links:
    dfs(path,l,tgt)
    path = path[:-1]

dfs('','you','out')
print(tally)

dfs('','svr','ffs')
print(tally)

dfs('','ffs','dac')
print(tally)

dfs('','dac','out')
print(tally)
