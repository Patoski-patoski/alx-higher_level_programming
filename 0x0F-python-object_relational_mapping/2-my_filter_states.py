#!/usr/bin/python3

"""a script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa """

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
    state = argv[4]

    my_cursor = my_connect.cursor()
    q = "SELECT * FROM states WHERE BINARY name LIKE '{}' ORDER BY states.id"
    my_cursor.execute(q.format(state))

    rows = my_cursor.fetchall()
    for row in rows:
        print(row)

    my_cursor.close()
    my_connect.close()
