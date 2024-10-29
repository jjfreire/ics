#!/usr/bin/env python

import sys

city_id_max = None
city_id_min = None
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

    if max_temp is None or current_max_temp > max_temp:
        max_temp = current_max_temp
        city_id_max = current_city_id

    if min_temp is None or current_min_temp < min_temp:
        min_temp = current_min_temp
        city_id_min = current_city_id


print '%s\t%s' % (city_id_max, max_temp)
print '%s\t%s' % (city_id_min, min_temp)