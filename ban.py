import MySQLdb
def fun(cursor):
    a="select * from EMPLOYEE"
    try:
      print"s"
      cursor.execute(a)
      print"sd"
      result=cursor.fetchall()
      print("a")
      for row in result:
         print(row)
    except:
        print("dc")
