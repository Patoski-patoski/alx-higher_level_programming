#!/usr/bin/python3

# a script that lists all states from the database hbtn_0e_0_usa


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(
        user='root',
        password='root',
        database='hbtn_0e_0_usa',
        port=3306
        )
        
    my_cursor = connection.cursor()
    my_cursor.execute("SELECT * FROM states")

    results = my_cursor.fetchall()
    for rows in results:
        print(rows)

    my_cursor.close()
    connection.close()

