import sys,argparse
from pathlib import Path

parser = argparse.ArgumentParser(prog='AoC DayFile Creator')
parser.add_argument('day_num',type=int,help='day of the advent to create files for')
parser.add_argument('--nocode',action='store_true',help='skip basic code to "read day_input.txt as array of lines')
arg = parser.parse_args()

d = str(arg.day_num).rjust(2,'0')
Path(f'inputs/day_{d}.txt').touch()
Path(f'inputs/day_{d}_test.txt').touch()

if arg.nocode:
  Path(f'day_{d}.py').touch()
else:
  with open(f'day_{d}.py','wt',newline='\n') as sf:
    sf.write('import sys,os,re,itertools\nfrom utils import *\n\n')
    sf.write(f"rawdata = [r.strip() for r in open('inputs/day_{d}_test.txt','rt').readlines()]\n")
    sf.write("for row in rawdata:\n  print(row)\n")
  
    
