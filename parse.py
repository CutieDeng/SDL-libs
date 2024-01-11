import os 
import sys 

args = sys.argv[1:] 

with open(args[0], 'r') as f: 
    # read all lines 
    lines = f.readlines()

for i in range(len(lines)):
    j = lines[i]
    j = j.strip() 
    j = f"    \"{j}\","
    lines[i] = j 
# print (lines)
# print (type(lines))
for i in lines: 
    print (i)