#!/usr/bin/python3

""" a script that lists all cities from the database hbtn_0e_4_usa """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    my_connect = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )

    my_cursor = my_connect.cursor()
    query = """ SELECT cities.id, cities.name, states.name
FROM cities
    JOIN states ON states.id = cities.state_id
ORDER BY cities.id;"""
    my_cursor.execute(query)

    rows = my_cursor.fetchall()
    for row in rows:
        print(row)

    my_cursor.close()
    my_connect.close()
