import mysql.connector
from mysql.connector import errorcode

try:
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        # default there is no password
        database = 'test'
    )
    print "it's works"
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print "Someting is wrong in username or password"
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print "No db exist"     
    else:
        print e
