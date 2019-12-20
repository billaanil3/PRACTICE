import MySQLdb
conn = MySQLdb.connect("localhost", "lcmuser", "Lcmdbpass_123", "lcm")
cursor = conn.cursor()
sql = "SELECT * FROM auth_user WHERE id < '%d'" % (10)
cursor.execute(sql)
print cursor
for cur in cursor:
    print cur
cursor.close()
conn.close()
