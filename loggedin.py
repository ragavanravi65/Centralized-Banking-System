import MySQLdb


def check(cursor,name,amm):
    sql=("select * from customer where name=%s"%(name))
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        mini=row[5]
        original=row[4]
    print(mini)
    print(original)
    print(amm)
    if mini<(original-amm):
        return True
    print"print correct ammount you have "+original+" in your account"
    return False


def adminlogin(cursor,db):
    f=0
    print("1.display\n2.deleted list\n3.delete\n4.logout\n")
    choice=input("choice")
    if choice==1:
        sql="select * from customer"
        cursor.execute(sql)
        result=cursor.fetchall()
        for p in result:
            print(type(p))
        print"acno|    name   |  age |gender| money\n"
        for row in result:
            dis=" "
            if(row[4]==-1):
                pass
            else:
                n=0
                for i in row:
                    if((i==5000 or i==0) and n>4):
                        pass
                    else:
                        dis=dis+str(i)+"   "
                        n=n+1
                print(dis+"\n")
    elif choice==2:
        sq="select *from customer"
        cursor.execute(sq)
        res=cursor.fetchall()
        print"acno|    name   |  age |gender| money\n"
        for row in res:
            dis=" "
            if(row[4] !=-1):
                pass
            else:
                n=0
                for i in row:
                    if((i==5000 or i==0)and n>4):
                         pass
                    else:
                        dis=dis+str(i)+"      "
                        n=n+1
            
                print(dis+"\n")
    elif choice==3:
        print"enter the account number to be deleted"
        num=input()
        n=-1
        #print type(n)
        sql = "UPDATE customer SET money = -1 where accno = %d"%(num)
        cursor.execute(sql)
        db.commit()
        sql2="delete from login where accno = %d"%(num)
        cursor.execute(sql2)
        db.commit()
    else:
        f=1
        print"bye admin\n\n"
    if f==0:
        adminlogin(cursor,db)



def normal(cursor,name):
    print("welcome "+name)
    m=0
    sp=("select *from customer where name='%s'"%(name))
    cursor.execute(sp)
    result=cursor.fetchall()
    print("1.deposit\n2.withdraw\n3.transfer\n4.logout")
    sys=input("choice ")
    if sys==1:
        am=-1
        print"enter amount to be deposited"
        while(am<0):
            am=input("RS ")
        sql_0 = """UPDATE customer SET money =%s where name = %s"""
        sql_1=(am,name)
        cursor.execute(sql_0,sql_1)
        cursor.commit()
    elif sys==2:
        print"enter the ammount to withdraw"
        while True:
            amm=input("RS ")
            if(check(cursor,acc,amm)):
                break
        sq = "UPDATE customer SET money = money - %d where name = %s"%(amm,name)
        db.commit()
    elif sys==3:
        flag=0
        note=1
        print "enter the ammount to transfer"
        amo=input("RS ")
        if(amo<0):
            note=0
        print "enter the receiver account number"
        account=input("ACCNO ")
        sql="select * from customer"
        cursor.execute(sql)
        result=cursor.fetchall()
        f=0
        for row in result:
            if(row[0]==account):
                flag=1
                if(row[4]==-1):
                    f=1
        if(flag==1 and f==0 and note==1):
            dep = "UPDATE customer SET money = money - %d where name = %s"%(amo,name)
            cursor.execute(dep)
            db.commit()
            withdraw="UPDATE customer SET money = money + %d where name = %s"%(amo,name)
            cursor.execute(withdraw)
            db.commit()
        else:
            print"enter valid one"
    elif sys==4:
        m=1
        print "bye"+name
    if(m==0):
        normal(name)
