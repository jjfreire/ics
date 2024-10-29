#!/usr/bin/env python

import sys

urls = []
url_counts = []
users = []
user_ps_counts = []

for line in sys.stdin:
    line = line.strip()
    url, user, is_ps = line.split('\t')
    is_ps = int(is_ps)

    if url in urls:
        url_index = urls.index(url)
        url_counts[url_index] += 1
    else:
        urls.append(url)
        url_counts.append(1)

    if is_ps == 1:
        if user in users:
            user_index = users.index(user)
            user_ps_counts[user_index] += 1
        else:
            users.append(user)
            user_ps_counts.append(1)

max_url_count = 0
max_url = None
for i in range(len(urls)):
    if url_counts[i] > max_url_count:
        max_url_count = url_counts[i]
        max_url = urls[i]

max_user_ps_count = 0
max_user = None
for i in range(len(users)):
    if user_ps_counts[i] > max_user_ps_count:
        max_user_ps_count = user_ps_counts[i]
        max_user = users[i]

print("Usuario con más accesos a archivos .ps: {}\tNúmero de accesos: {}".format(max_user, max_user_ps_count))
print("URL más visitada: {}\tNúmero de visitas: {}".format(max_url, max_url_count))