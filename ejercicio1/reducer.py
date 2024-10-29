#!/usr/bin/env python

import sys

city_id = None
max_temp = None
min_temp = None

for line in sys.stdin:
    line = line.strip()
    current_city_id, current_max_temp, current_min_temp = line.split('\t')
    try:
        if current_max_temp == "-9999.0" or current_min_temp == "-9999.0":
            raise Exception
        current_max_temp = float(current_max_temp)
        current_min_temp = float(current_min_temp)
    except (ValueError, Exception):
        continue

    if city_id == current_city_id:
        if max_temp is None or current_max_temp > max_temp:
            max_temp = current_max_temp
        if min_temp is None or current_min_temp < min_temp:
            min_temp = current_min_temp
    else:
        if city_id is not None:
            print '%s\t%s\t%s' % (city_id, max_temp, min_temp)
        city_id = current_city_id
        max_temp = current_max_temp
        min_temp = current_min_temp

if city_id == current_city_id:
    print '%s\t%s\t%s' % (current_city_id, max_temp, min_temp)
