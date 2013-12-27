#!/usr/bin/python

#In this problem you will use regular expressions to help you detect the various Tags used in an HTML document.
import re;
n=int(raw_input())
array=[];
c=0;
for i in range(n):
    line=str(raw_input())
    m=re.split('<(?!/)',line)
    for j in range(1,len(m)):
        array.append(re.split('[\\s>]',m[j])[0]+';')
line=''
for i in sorted(set(array)):
    line+=i
print line[0:-1]
