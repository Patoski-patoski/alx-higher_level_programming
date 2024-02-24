#!/usr/bin/python3

""" a script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa
"""

from ast import arg


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

    state_name = argv[4]

    my_cursor = my_connect.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON states.id = cities.state_id
    WHERE states.name = %s
    ORDER BY cities.id;
    """

    my_cursor.execute(query, (state_name,))
    array = []

    rows = my_cursor.fetchall()
    for row in rows:
        city = row[0]
        array.append(city)

    output = ', '.join(array)
    print(output)

    my_cursor.close()
    my_connect.close()
