#!/usr/bin/env python

import sys

urls = {}
users = {}

for line in sys.stdin:
    line = line.strip()
    url, user, is_ps = line.split('\t')
    is_ps = int(is_ps)

    url_count = urls.get(url)
    if url_count is None:
        urls[url] = 1
    else:
        urls[url] = url_count + 1

    if is_ps:
        ps_count = users.get(user)
        if ps_count is None:
            users[user] = 1
        else:
            users[user] = ps_count + 1


max_url = max(urls, key=urls.get)
max_user = max(users, key=users.get)

print '%s\t%d' % (max_user, users[max_user])
print '%s\t%d' % (max_url, urls[max_url])
