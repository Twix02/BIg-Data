#!/usr/bin/python
import sys

nbTotal = 0
oldWord = None
listNodes = []

for line is sys.stdin:
    dataMapped = line.strip().split("\t")

    thisWord = str(dataMapped[0])
    thisNode = str(dataMapped[1])
    thisCount = str(dataMapped[2])
    print(thisCount)
    if oldWord and oldWord.lower() != thisWord.lower():
        listNodes.sort(key = lambda listNodes:len(listNodes)-1)
        print (oldWord, "\t", nbTotal, "\t", listNodes, "\n")  
        oldWord = thisWord
        nbTotal = 0
        listNodes = []
        
        oldWord = thisWord.lower()

        nbTotal = nbTotal + 1



if oldWord != None:
    listNodes.sort(key = lambda listNodes:len(listNodes)-1)

