#!/usr/bin/env python

import sys
import os

user = os.environ['mapreduce_map_input_file'].split('/')[-1].split('.')[0][3:]

for line in sys.stdin:
    line = line.strip()
    fields = line.split()
    if fields[3].endswith('.ps'):
        print '%s\t%s\t%d' % (fields[3], user, 1)
    else:
        print '%s\t%s\t%d' % (fields[3], user, 0)