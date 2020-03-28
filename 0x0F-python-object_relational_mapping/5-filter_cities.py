#!/usr/bin/env python3
# Use MySQLdb with python3

if __name__ == '__main__':
	import MySQLdb
	from sys import argv

	db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
	cur = db.cursor()
	size = cur.execute("SELECT cities.name FROM cities, states WHERE cities.state_id = states.id AND states.name = %s ORDER BY cities.id;", (argv[4], ))
	rows = cur.fetchall()
	i = 0
	for row in rows:
		if i < size - 1:
			print(row[0], end=", ")
		else:
			print(row[0])
		i += 1
	cur.close()
	db.close()
