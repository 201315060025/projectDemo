# encoding: utf-8
"""
python 链接redis 数据库
"""

import redis

# 连接redis服务器
# r = redis.Redis(host='120.27.230.147',port=6390,db=0)
r = redis.Redis(host='10.100.111.5',port=6380, db=0)
#key为database

r.set('webname','www.biancheng.net')
print(r.get('webname'))
