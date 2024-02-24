#!/usr/bin/python3

""" a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time, write
one that is safe from MySQL injections!
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    my_connect = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            database=argv[3],
            port=3306
    )
    state_name = argv[4]

    my_cursor = my_connect.cursor()
    query = "SELECT * FROM states WHERE BINARY name LIKE %s ORDER BY states.id"
    my_cursor.execute(query, (state_name,))

    results = my_cursor.fetchall()
    for row in results:
        print(row)

    my_cursor.close()
    my_connect.close()
