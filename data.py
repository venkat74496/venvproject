import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",  password="",  database = "Venkat")
def count(table):
    mycursor = mydb.cursor()
    e="SELECT count(*) from "+table
    mycursor.execute(e)
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult
def storestudent(x):
    mydb = mysql.connector.connect(host="localhost", user="root",  password="",  database = "Venkat")
    r=count("login")
    y=[r[0][0]]
    for e in x.keys():
        y.append(x[e])
    y.append("student")
    y=tuple(y)
    d="INSERT INTO login(id, name,regno,batch, email, PASSWORD, role) VALUES  (%s,%s,%s,%s,%s,%s,%s)"
    print(d)
    mycursor = mydb.cursor()
    mycursor.execute(d,y)
    mydb.commit()
    n=tuple(y[2].split())
    d="INSERT INTO "+y[3]+"(regno) VALUES  (%s)"
    print(d)
    mycursor = mydb.cursor()
    mycursor.execute(d,n)
    mydb.commit()
    mydb.close()
    mydb.close()
def login(user,pas):
    mydb = mysql.connector.connect(host="localhost", user="root",  password="",  database = "Venkat")
    mycursor = mydb.cursor()
    e="SELECT name,role,email FROM login where email='%s' and password='%s'"%(user,pas)
    mycursor.execute(e)
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult
def currentdat():
    import datetime 
    return str(datetime.datetime.now())[0:10] 
def stores(x,code,em):
    mydb = mysql.connector.connect(host="localhost", user="root",  password="",  database = "Venkat")
    mycursor = mydb.cursor()
    r=x["sub"]+'_'+currentdat()[-2:]+'_'+currentdat()[-5:-3]+'_'+x["time"]
    e="alter table "+x["batch"]+" add "+r+" varchar(50)"
    mycursor.execute(e)
    y=tuple([em,code,r])
    d="INSERT INTO fcode(facultymail, code, gentime) VALUES  (%s,%s,%s)"
    print(d)
    mycursor = mydb.cursor()
    mycursor.execute(d,y)
    mydb.commit()
    mydb.close()
def storeats(x,em):
    
    mydb = mysql.connector.connect(host="localhost", user="root",  password="",  database = "Venkat")
    mycursor = mydb.cursor()
    e="SELECT  batch,regno FROM login where email='%s' "%(em)
    mycursor.execute(e)
    myresult = mycursor.fetchall()
    table=(myresult[0][0])
    rid=(myresult[0][1])
    print(table,rid)
    mycursor = mydb.cursor()
    e="SELECT gentime  FROM fcode where code='%s' "%(x["sub"])
    mycursor.execute(e)
    myresult = mycursor.fetchall()
    col=(myresult[0][0])
    print(col)
    y=tuple([rid])
    mycursor = mydb.cursor()
    d="update "+table+" set "+col+"='present' where regno = %s" 
    print(d)
    mycursor.execute(d,y)
    mydb.commit()
    mydb.close()

    


    
