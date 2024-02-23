#!/usr/bin/python3

""" a script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    my_connect = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            database=argv[3],
            port=3306
        )

    state = argv[4]

    my_cursor = my_connect.cursor()
    my_cursor.execute("SELECT * FROM states WHERE name = %s "
                      "ORDER BY id", (state,))

    results = my_cursor.fetchall()
    for row in results:
        print(row)

    my_cursor.close()
    my_connect.close()
