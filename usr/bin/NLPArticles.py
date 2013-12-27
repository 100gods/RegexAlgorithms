#!/usr/bin/python

#This problem will help you warm up and practice basic text and string processing techniques. This will be a first step towards more complex Text and Natural Language Processing and Analysis tasks.

#You will be given a fragment of text.
#    In this fragment, you need to identify the articles used (i.e., ‘a’, ‘an’, ‘the’).
#    And you also need to identify dates (which might be expressed in a variety of ways such as ‘15/11/2012’,’15/11/12’, ‘15th March 1999’,’15th March 99’ or ‘20th of March, 1999’).

#You can make the following assumptions 1) In the date, year and day will always be in numeric form. Which means, you don’t have to worry about “fifteenth” or “twentieth” etc. Month, could be either numeric form (1-12) or with its name (January-December, Jan-Dec).

#2) This is a bit open ended, and somewhat intentionally so. The aim is for you to try to write something which figures out as many common patterns as possible, in which dates are present in text.

#3) Most of the test cases are Wikipedia articles. Having a look at the common formats in which dates occur in those, will help.

#4) Dates could either be in the form: Month followed by Day followed by Year, or Day followed by Month followed by Year.

#5) The day could be in the form of either (1,2,3,…31) or (1st, 2nd, 3rd…31st).

#A fragment is a valid date if it contains day, month and year information (all three of them should be present). To extract date information, you will need to try detecting different kinds of representations of dates, some of which have been shown above. The more patterns you match and identify correctly, the greater your score will be.


import re;
n=int(raw_input().strip())
for i in range(n):
    line=str(raw_input().strip())
    #print line
    print len(re.split('(?<![a-zA-Z0-9])[aA](?= )',line))-1
    print len(re.split('(?<![a-zA-Z0-9])[aA]n(?= )',line))-1
    print len(re.split('(?<![a-zA-Z0-9])[tT]he(?= )',line))-1
    count=0;
    m=re.search('([0-9]{2}).+(?=[0-9]{4})',line)
    count+= 0 if m is None else len(m.groups())
    m=re.search('\d+/\d+/\d+',line)
    count+=0 if m is None else len(m.groups())
    print count
    line =raw_input() if i !=n-1 else '';
