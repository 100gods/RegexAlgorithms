#!/usr/bin/python

#A search engine is badly in need of a feature where it can understand common acronyms, or abbreviations.
#To begin with, we’d like it to be able to figure out, the expansions of abbreviations which refer to popular organizations, which might include agencies, colleges, universities or companies. 

import re;
def search(key,line):
    #print 'here key='+key+' line='+line
    n=re.search('.+(?=\('+key+'\))',line)
    if n is None:
        #print 'advace search TODO'
        try:
            n=re.search(key[0]+'.*',line)
            tmp=str(n.group(0)).strip().split(" ")
        except:
            return -1;
        i=0;
        j=0;
        while i<len(key):
            k=0
            flag=True;
            while flag:
                #print 'compare '+tmp[j][k]+' === '+key[i]
                try:
                    if tmp[j][k].lower() == key[i].lower():
                        flag=True;
                        i+=1
                        k+=1
                    else:
                        flag=False;
                except:
                    flag=False;
            j+=1;
        print ' '.join(tmp[0:j])
        
            
            
    else:
        tmp=key[0]
        #print key[0]
        res=str(n.group(0))
        #print 'res='+res
        res=res.replace('The','');
        #print 'res after eplace='+res
        print res.strip()
        

n=int(raw_input().strip())
text=[]
for i in range(n):
    text.append(str(raw_input().strip()))
#print text;
for i in range(n):
    key=str(raw_input().strip())
    #print key
    for line in text:
        m=re.search(key,line)
        #print 'search key ='+key +' line='+text[j]
        if m is None:
            continue;
        else:
            #print 'call '
            search(key,line)
            text.remove(line)
