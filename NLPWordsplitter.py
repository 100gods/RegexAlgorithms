#!/usr/bin/python

#Deterministic Url and HashTag Segmentation
#This problem will introduce you to the segmentation of Domain Names and Social Media HashTags, into English Language words. To give you a quick idea of what segmentation means, here are a few examples of Domain names and Hash Tags which have been segmented.

#Domain Name Examples:-
#www.checkdomain.com => [check domain]
#www.bigrock.com => [big rock]
#www.namecheap.com => [name cheap]
#www.appledomains.in => [apple domains]
#Twitter Hash Tag Examples:
# #honestyhour => [honesty hour]

# #beinghuman => [being human]

# #followback => [follow back]

# #socialmedia => [social media]

# #30secondstoearth => [30 seconds to earth]

#The segmentation should be based on the list of 5000 most common words from here Apart from the words in this list, you should also pick up numbers (both integer and decimal) like 100, 200.10 etc.

#At this stage, we are going to use a very simple algorithm for the process. In case the input is a domain name, ignore the www. and/or the extensions (.com,.edu,.org,.in, etc.) In case the input is a hashtag, ignore the first # symbol. Split the input string, into a sequence of tokens. A token can either be:

#    A word in from the provided lexicon/dictionary.
#    An integer or decimal number.

#There might be cases where it might be possible to parse (or split) an input string into tokens in multiple possible ways.

#currentratesoughttogodown 

#This can be split into:
#   current rate sought to go down

# current rates ought to go down.

#  thisisinsane

#This can be split into:

#    this is in sane
#    this is insane

#Write your splitter in such a way, that as you tokenise a string from left to right; in case there are multiple possible ways to split the string,

#select the longest possible string from the left side, such that the remaining string can be split into valid tokens. So, for the two cases above, the appropriate ways to split the strings are:

#    current rates ought to go down
#    this is insane

#In case there is no valid way to split the string into a valid sequence of tokens, output the original string itself, after scrubbing out the # for hashtags, the ‘www’ and extensions for domain names.

res=str()
tmp=[]
def match(line):
        #print '------------------------------------------------------------------'
        #print '------------------------------------------------------------------'
        if len(line)==0:
            return True 
        #print 'line='+line
        global res;
        global tmp
        #print 'first ='+res
        j=0
        while j<=(len(line)):
            #print '------------------------------------------------------------------'
            #print 'j='+str(j)
            max=0
            matchIndex=-1;
            matchs=[]
            flag=False;
            for i in range((j+1),len(line)+1):
                #print '.....................................................'#
                #print 'i='+str(i)
                #print 'traing to match='+line[j:i]
                if line[j:i] in words:
                    #print 'match='+line[j:i]
                    matchIndex=i
                    matchs.append(i)                    
            for m in sorted(matchs,reverse=True):
                flag=match(line[m:])
                max=max if not flag else (m-j)
                if flag:
                   tmp.append(line[j:j+max].strip())
                   res+=line[j:j+max]+' '
                   #print 'res original2='+res
                   #print 'tmp res='+str(tmp)
                   break;                    
                #print '.....................................................'
            global res
            #print 'res='+line[j:+max]
            #print 'max='+str(max)        
            #print 'res original='+res
            if max > 0:
                j+=max            
            else:
                j+=1
            #print 'retuning '+str(True if flag else False)
            #print '------------------------------------------------------------------'
            #print '------------------------------------------------------------------'
            return True if flag else False
import re;
#words=['art','i','steer','stock','daily']
words=[]
f = open("words.txt")
try:
    for line in f:
        words.append(str(line).strip().lower())
finally:
    f.close()
#print words;
#words.append(str(''));
#words.append(str('internet'));
#words.append(str('daily'));
#words.append(str('sale'));
#words.remove('ad')
n=int(raw_input())
for i in range(n):
    global res
    global tmp
    tmp=[]
    res=str()
    line=str(raw_input().strip().lower())
    line=line.replace('^#','')
    m=re.match('.+(?=\..*)',line)
    line= line if m is None else m.group(0)
    m=re.match('.+(?=\..*)',line)
    line= line if m is None else m.group(0)
    #print line
    m=re.match('[0-9]+',line)
    digit='' if m is None else m.group(0)
    #print digit
    line=line.replace(digit,'')
    #print line
    if digit != '':
        tmp.append(digit)
    j=0
    res=''
    #print 'len of line='+str(len(line))
    match(line)
    #print res.strip();
    res=' '.join(reversed(tmp))
    print res.strip()
