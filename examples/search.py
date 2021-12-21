#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from bluebird import BlueBird

query = {
    'fields': [
        # {'items': ['PGC2021'], 'target': 'hashtag'}
        # {'items': ['PGLMAJOR'], 'target': 'hashtag'}
        # {'items': ['Worlds2021'], 'target': 'hashtag'}
        # {'items': ['FINAAbuDhabi2021'], 'target': 'hashtag'}
        # {'items': ['WorldSeries'], 'target': 'hashtag'}
        # {'items': ['AbuDhabiGP'], 'target': 'hashtag'}

    ],
    'since': '2021-09-01',
    'until': '2021-12-18'
}
a = []
f = open("../data/ABUDABIGP.txt", "a+")
index = 0
for tweet in BlueBird().stream(query):
    print(tweet)
    if tweet['id'] in a:
        print('loop')
    else:
        f.write(json.dumps(tweet))
        a.append(tweet['id'])