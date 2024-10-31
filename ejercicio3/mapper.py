#!/usr/bin/env python

import sys
import os

wine_type = os.environ['mapreduce_map_input_file'].split('/')[-1]

first_line = True

for line in sys.stdin:
    
    if first_line:
        first_line= False
        continue

    line = line.strip()
    fields = line.split()
    if wine_type.endswith('red.csv'):
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % ('red', fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8], fields[9], fields[10], fields[11])
    else:
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % ('white', fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8], fields[9], fields[10], fields[11])