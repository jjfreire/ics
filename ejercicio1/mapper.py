#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split()
    print '%s\t%s\t%s' % (fields[0], fields[5], fields[6])
