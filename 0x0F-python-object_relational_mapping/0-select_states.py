#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
Execute by (./0-select_states.py username password database_name)
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
    my_cursor = my_connect.cursor()
    my_cursor.execute('SELECT * FROM states ORDER BY states.id')
    rows = my_cursor.fetchall()
    for row in rows:
        print(row)
    my_cursor.close()
    my_connect.close()
