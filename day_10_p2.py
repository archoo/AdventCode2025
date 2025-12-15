import sys,os,re,itertools,random,functools
from utils import *

def pb(n,l):
  f = '{0:0'+str(l)+'b}'
  return f.format(n)

rawdata = [r.strip() for r in open('inputs/day_10.txt','rt').readlines()]

def sub(l1,l2):
  l3 = []
  for i in range(len(l1)):
    l3.append(l1[i]-l2[i])
  return l3

tot = 0
for row in rawdata:
  print(row)
  l = re.search(r'\[(.*)\]',row).group(1)
  ll = len(l)
  lights = [0 for c in l]
  
  p =  re.search(r'\{(.*)\}',row).group(1)
  power = [int(n) for n in p.split(',')]
  
  btns = []
  b = row[row.find(']')+1:row.find('{')].strip('( )').split(') (')
  for btn in b:
    t = [0 for c in l]
    for i in btn.split(','): t[int(i)] += 1
    btns.append(t)
  print(power,btns)

  while power != lights and sum(power) > 0 and len(btns) > 0:

    # find smarter way to pick next button
    mx = max(power)
    tg = [1 if n==mx else 0 for n in power]
    pf = lambda btn: sum([p for i,p in enumerate(power) if btn[i]==1])
    btns.sort(key=pf,reverse=True)
    nb = 0

    power = sub(power,btns[nb])
    tot+=1
    print(btns[nb],power,tot)

    if 0 in power:
      done = [1 if n==0 else 0 for n in power]
      for d in range(len(done)):
        if done[d] == 1:
          for btn in btns[::]:
            if btn[d] == 1:
              btns.remove(btn)

print(tot)