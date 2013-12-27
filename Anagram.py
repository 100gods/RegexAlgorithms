#!/usr/bin/python

#Sid is obsessed about reading short stories. Being a CS student, he is doing some interesting frequency analysis with the books. From two short story books, he choses strings having length a from the first and strings having length b from the second one. The strings are such that the difference of length is <= 1

#i.e.

#|a-b|<=1, where |x| represents the absolute value function.

#He believes that both the strings should be anagrams based on his experiment. Your challenge is to help him find the minimum number of characters of the first string he needs to change to make it an anagram of the second string. Neither can he add a character nor delete a character from the first string. Only replacement of the characters with new ones is allowed.

import collections;
n=int(raw_input().strip())
for i in range(n):
    count=0;
    line=str(raw_input().strip())
    length=len(line)
    if length%2 == 0:
        a=collections.Counter(line[0:length/2])
        b=collections.Counter(line[length/2:])
        for elm in a:
            count+= 0 if (a[elm]-b[elm]) < 0 else (a[elm]-b[elm])
        print count        
    else:
        print -1
