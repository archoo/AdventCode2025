import sys,os,re,itertools,random,functools
from utils import *

def pb(n,l):
  f = '{0:0'+str(l)+'b}'
  return f.format(n)

tot = 0
rawdata = [r.strip() for r in open('inputs/day_10.txt','rt').readlines()]
for row in rawdata:
  print(row)
  l = re.search(r'\[(.*)\]',row).group(1)
  ll = len(l)
  lights = int(''.join(['0' if c == '.' else '1' for c in l]),2)
  
  power =  re.search(r'\{(.*)\}',row).group(1)
  # p = ''.join(['0' if p == '.' else '1' for c in lights])
  
  btns = []
  b = row[row.find(']')+1:row.find('{')].strip('( )').split(') (')
  for btn in b:
    t = ['0' for c in l]
    for i in btn.split(','): t[int(i)] = '1'
    btns.append(int(''.join(t),2))
  
  for i in range(len(btns)):
    poss = itertools.combinations(btns,i)
    if lights in [functools.reduce(lambda a,b: a^b,p,0) for p in poss]:
      tot += i
      break
    
print(tot)