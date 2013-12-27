#!/usr/bin/python
#Given a line of text which possibly contains the latitude and longitude of a point, can you use regular expressions to identify the latitude and longitude referred to (if any)?
import re;
n=int(raw_input().strip())
for i in range(n):
    line=str(raw_input().strip())
    m=re.search('(?<=\()[+-]?[1-9]+[0-9]*(.[0-9]+)?(?=, )',line)
    if m is None:
        print 'Invalid'
    else:
        try:
            a=float(m.group(0))
            #print a;
            if a<=90 and -90<=a:
                m=re.search('(?<=, )[+-]?[1-9]+[0-9]*(.[0-9]+)?(?=\))',line)
                b=float(m.group(0))
                #print b
                if b<=180 and -180<=b:
                    print 'Valid'
                else:
                    print 'Invalid'
            else:
                print 'Invalid'
        except:
            print 'Invalid'
