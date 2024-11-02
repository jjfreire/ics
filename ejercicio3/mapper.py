#!/usr/bin/env python

import sys
import os
import random
import re

wine_type = os.environ['mapreduce_map_input_file'].split('/')[-1]

for line in sys.stdin:
    line = line.strip()
    if re.search(r'[a-zA-Z]', line):
        continue
    fields = line.split(';')

    random_key = random.randint(0, 1)
    if wine_type.endswith('white.csv'):
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (random_key, 'white', fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8], fields[9], fields[10], fields[11])
    else:
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (random_key, 'red', fields[0], fields[1], fields[2], fields[3], fields[4], fields[5], fields[6], fields[7], fields[8], fields[9], fields[10], fields[11])