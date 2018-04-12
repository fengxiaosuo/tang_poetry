#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "broadcom", "tang_poetry", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM tang_poetry.poetries where content like '%床前明月光%' limit 1;"

try:
	# 执行SQL语句
	cursor.execute(sql)
	# 获取所有记录列表
	results = cursor.fetchall()

	for row in results:
		myid = row[0]
		poet = row[1]
		content = row[2]
		title = row[3]
		print "id=%d,poet=%d,content=%s,title=%s" % (myid, poet, content, title)
except:
   print "Error: unable to fecth data1111"

# 关闭数据库连接
db.close()