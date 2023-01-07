#!/usr/bin/python

import sys

for line in sys.stdin:
    if len(data) == 6 :
        data = line.strip().split("\t")
        print ("{0}\t{1}".format(item,cost))
        
