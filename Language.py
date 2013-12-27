#!/usr/bin/python

#Every submission at hackerrank has a field called language which indicates the language in which a hacker has made his submission at hackerrank

#C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC

#Sometimes, error prone API requests has an invalid language field. Could you find out if a given submission has a valid language field or not.


import re;
lang=':C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC:'
n=int(raw_input());
for i in range(n):
    line=re.split(' ',str(raw_input()))[1]
    print 'INVALID' if re.search('[:]'+line.upper()+'([:])',lang) is None else 'VALID'
