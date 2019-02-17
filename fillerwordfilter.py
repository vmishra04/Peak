#!/usr/bin/env python3
# -*- coding: utf-8 -*-
m

"""
Created on Sat Feb 16 16:39:42 2019

@author: Megha
"""
string1= "Um so i have expeirence well working in uh Software Development"
string2="i ah want this job becuase uh i think i can ah just hmmm"
splitstring= string1.split()
splitstring= string2.split()
list1=[] #empty list to store repeated words 
list2=["um","so","well","like","uh", "ah", "just","hmmm", "hmm","er","mhm",
       "uh huh","okay", "i think that", "you know", "i mean", "i guess","something",
       "kind of","basically","actually","literally","seriously"] 
#liat of repeated words 
for word in splitstring:
    if word in list2:
        list1.append(word)
lengthstring= len(list1)
# count the number of times an element is repeated
from collections import Counter
words_repeated = dict(Counter(list1))
#for word in list1:
if lengthstring > 2:
    print("You have the tendancy to repeat certain words in your interview performance.")
    print("You have a total of",lengthstring,"filler words.")
    print("You have used the filler word:",words_repeated, "many times.") 
else: 
    print("Good job!"/n)
    print("Filler words are not an issue in your interview performance.")