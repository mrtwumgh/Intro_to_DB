import mysql.connector
try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mypass'
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error:
    print("An error occurred when establishing a connection")
finally:
    mycursor.close()
    mydb.close()