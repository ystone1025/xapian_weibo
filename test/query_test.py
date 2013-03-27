# -*- coding:utf-8 -*-

import sys
import  calendar
import datetime

sys.path.append('../xapian_weibo')
from xapian_backend import XapianSearch
from utils import top_keywords, not_low_freq_keywords

s = XapianSearch(path='../data/', name='hehe')

count, get_results = s.search(query={'text': [u'中国'], 'user': 1217743083, 'timestamp': {'$gt': 0, '$lt': 1334450340}}, sort_by=['-timestamp'], fields=['text', 'timestamp', 'user', 'terms'])

print 'query1:'

for r in get_results():
    print r['user'], r['text'], r['terms'], r['timestamp']

print 'hits: %s' % count


# 下面的用法由于接口的修改暂时没有维护, 但具有参考价值
"""
print 'query2:'
query_dict = {'$and': [{'text': [u'中国'], 'uid': 1217743083},
                       {'uid': 1217743083},
                       {'$or': [{'ts': {'gt': 0,
                                        'lt': 1334450340}},
                                {'uid': 0000000000}]}],
              '$not': {'text': u'宝马', 'name': u'白之兔'},
              'name': u'袁岳'
              }

results = s.search(query=query_dict, sort_by=['-ts'], fields=['text', 'ts', 'name'])

for r in results['results']:
    print r['text']
    print r['name']

print 'hits: %s' % results['hits']
print s.parse_query(query_dict)
"""
"""
begin_ts1 = calendar.timegm(datetime.datetime(2011, 10, 1).timetuple())
end_ts1 = calendar.timegm(datetime.datetime(2011, 12, 31).timetuple())
begin_ts2 = calendar.timegm(datetime.datetime(2010, 10, 1).timetuple())
end_ts2 = calendar.timegm(datetime.datetime(2010, 12, 31).timetuple())

query_dict = {'$or':
              [{'ts': {
                '$gt': begin_ts1,
                '$lt': end_ts1,
                }},
               {'ts': {
                '$gt': begin_ts2,
                '$lt': end_ts2,
                }}]}

results = s.search(query=query_dict, fields=['uid', 'text', 'ts', 'name', 'emotions'])
for r in results['results']:
    print r['emotions']
print results['hits']
"""

"""
begin_ts1 = calendar.timegm(datetime.datetime(2011, 10, 1).timetuple())
end_ts1 = calendar.timegm(datetime.datetime(2011, 12, 31).timetuple())
begin_ts2 = calendar.timegm(datetime.datetime(2010, 10, 1).timetuple())
end_ts2 = calendar.timegm(datetime.datetime(2010, 12, 31).timetuple())

query_dict = {'$or':
              [{'ts': {
                '$gt': begin_ts1,
                '$lt': end_ts1,
                }},
               {'ts': {
                '$gt': begin_ts2,
                '$lt': end_ts2,
                }}]}


for word, count in top_keywords(s, query_dict, emotions_only=True, top=1000):
    print word, count
"""
"""
begin_ts1 = calendar.timegm(datetime.datetime(2011, 1, 1).timetuple())
end_ts1 = calendar.timegm(datetime.datetime(2011, 12, 31).timetuple())
query_dict = {
    'ts': {
        '$gt': begin_ts1,
        '$lt': end_ts1,
    },
    'text': u'抓狂',
}

for word, count in top_keywords(s, query_dict, emotions_only=True, top=1000):
    print word, count

for word, count in not_low_freq_keywords(s, query_dict, emotions_only=True):
    print word, count
"""
