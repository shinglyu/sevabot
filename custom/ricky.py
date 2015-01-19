#!/usr/bin/env python
import json
import urllib2

try:
    data = json.load(urllib2.urlopen("https://github.com/mozilla-b2g/gaia/graphs/contributors-data"))
except (ValueError, NameError) as e:
    print 'Request timeout. Please try again.'

ordinal = ['th', 'st', 'nd', 'rd'] + ['th'] * 6
commits = 0
for i in xrange(100):
    if data[i]['author']['login'] == 'RickyChien':
        commits = data[i]['total']
        m = 100
        M = 0
        for j in xrange(100):
            if data[j]['total'] == commits:
                m = min(m, j)
                M = max(M, j)
        rank = 100 - (m + M - i)
        print 'RickyChien is currently ranked %d%s among all the Gaia contributors in the world.' % (rank, ordinal[rank % 10])
        break
else:
    print 'RickyChien is not one of the top 100 Gaia contributors.'