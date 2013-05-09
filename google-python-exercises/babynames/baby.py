#!/bin/python
import sys,re
f_name = sys.argv[1]
fo = open(f_name, "r+")
year = re.search(r'\d\d\d\d', fo.name)
print year.group()
data = fo.read()
names = re.findall(r'<td>\d+</td><td>\w+</td><td>\w+</td>', data)

huge_list=[]
grp = ''
for i in range(0,10):
	grp = re.search(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', names[i])
	huge_list.append((grp.group(2)+" "+grp.group(1))) 
	huge_list.append((grp.group(3)+" "+grp.group(1))) 
fo.close()
huge_list.sort()
print '\n'.join(huge_list)
