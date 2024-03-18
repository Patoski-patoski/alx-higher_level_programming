#!/usr/bin/env python3
# a script that lists all states from the database hbtn_0e_0_usa

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    my_db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306,
        )

    my_cursor = my_db.cursor()
    query = """SELECT * from states ORDER by id"""
    my_cursor.execute(query)

    results = my_cursor.fetchall()
    for row in results:
        print(row)

    my_cursor.close()
    my_db.close()
