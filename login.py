import MySQLdb
from loggedin import *
def sign():
    print"sybbf"
def signin(cursor):
    print"enter the username and password"
    stt="select * from login"
    cursor.execute(stt)
    result=cursor.fetchall()
    ok=1
    while(ok==1):
        uname=raw_input("username")
        paas=raw_input("Password")
        for row in result:
            if row[0]==uname and row[1]==paas:
                if row[0]=="admin":
                    adminlogin(cursor)
                else:
                    normal(cursor,row[0])
                ok=0
        if ok==1:
            print"username or password is/are wrong\n\n"
    
def signup(cursor,dp):
    print "welcome to sign up page"
    sql="select * from customer"
    cursor.execute(sql)
    result = cursor.fetchall()
    acc=0;
    for row in result:
        acc=row[0]
    name =raw_input("Enter your name")
    age = input("age")
    gender=raw_input("m-male\nf-female\no-others")
    money=input("Initial deposit ammount")
    print"do you want to open current account or saving account y-currnet n-savings"
    mode = raw_input()
    if mode=='y':
        mini=5000
    else:
        mini=0
    sq= "INSERT INTO customer(accno, \
       name,age,gender,money,mini) \
       VALUES ('%d','%s','%d','%c','%d','%d')" % \
       (acc+1,name,age,gender,money,mini)
    try:
        cursor.execute(sq)
        dp.commit()
    except:
        dp.rollback()
    print"\nchoose username and password\n\n"
    user=raw_input("usernmae")
    password=raw_input("password")
    sql1="insert into login(username,\
         pass)\
         values('%s','%s')"%\
         (user,password)
    try:
        cursor.execute(sql1)
        dp.commit()
    except:
        dp.rollback()
    
