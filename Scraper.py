#!/usr/bin/python


#Stack Exchange is an information power-house, which contains libraries of crowdsourced problems (with answers) across a large number of topics which are as diverse as electronics, cooking , programming, etc.

#We are greatly interested in crawling and scraping as many questions, as we can, from stack-exchange. This is an example of a question library page from stack-exchange.

#Your task will be, to scrape the questions from each library page, in the order in which they are listed. You will be provided with the markup of question listing pages, from which you need to detect:
#(1) Identifier (2) Question text (which is on the Hyperlink to the question) (3) How long ago the question was asked.

#The Markup in the Test Cases will be similar to the sample fragment shown below. Please note, that since this markup is real markup from the website, it is likely to contain some stray control and escape characters, unexpected whitespaces and newlines.
import re;
line=str()
while 1:
    try:
        line+=str(raw_input()).strip()+'\n'
    except:
        break;
#pint line
m=re.split('<div class=\"question-summary\" id=\"question-summary-',line)
ans=str()
for i in range(1,len(m)):
    #print '---------------------------------------------------------------------'
    ans=''
    #tmp=re.split('">',m[i]);
    #ans=tmp[0]+';'
    mat=re.match('[0-9]+(?=">)',m[i])
    ans=mat.group(0)+';'
    mat=re.search('(?<=class="question-hyperlink">).+(?=</a>)',m[i])
    ans+=mat.group(0)+';'
    mat=re.search('(?<=class=\"relativetime\">).+(?=<)',m[i])
    ans+=mat.group(0)
    print ans
    #print '---------------------------------------------------------------------'
