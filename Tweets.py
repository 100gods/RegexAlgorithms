#!/usr/bin/python
#Increasing popularity of hackerrank can be seen in tweets like

#   I love #hackerrank
#  I just scored 27 points in the Picking Cards challenge on #HackerRank
# I just signed up for summer cup @hackerrank

#Given a set of most popular tweets, your task is to find out how many of those tweets has the string hackerrank in it.

import re;
n=int(raw_input());
count=0;
for i in range(n):
    line=str(raw_input())
    if (re.search('[hH][aA][cC][Kk][eE][rR][rR][aA][nN][kK]',line) is None):
        continue
    else:
        count=count+1;
print count
