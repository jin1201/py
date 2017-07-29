import sqlite3


con, cur = None, None
sid,sname,pid = "","",""
profid,pname,room = "","",""
data1,data2,data3 = "","",""


sqlRow = None

con = sqlite3.connect("jin-DB")
cur=con.cursor()

cur.execute("CREATE TABLE   stud (sid char(4),sname char(15),pid char(4))")
cur.execute("INSERT INTO stud VALUES('1234','홍길동','101')")
cur.execute("INSERT INTO stud VALUES('1235','최판서','102')")
cur.execute("INSERT INTO stud VALUES('1236','김우주','102')")
cur.execute("INSERT INTO stud VALUES('1237','이태양','101')")


cur.execute("CREATE TABLE  profe(profid char(4),pname char(15),room char(4))")
cur.execute("INSERT INTO profe VALUES('101','이동훈','312')")
cur.execute("INSERT INTO profe VALUES('102','윤진하','313')")
cur.execute("INSERT INTO profe VALUES('103','박종철','314')")





cur.execute("SELECT stud.sname, profe.pname, profe.room FROM stud INNER JOIN profe ON stud.pid = profe.profid ;") 
print("---------------------------------------------------")
print(" 학생명(sname)  교수명(pname)    연구실(room)")
print("---------------------------------------------------")

while(True) :
    sqlRow= cur.fetchone()
    if sqlRow == None :
        break;
    data1= sqlRow[0]
    data2 = sqlRow[1]
    data3 = sqlRow[2]
    print("%3s %15s  %10s" % (data1,data2,data3))
  

con.commit()
con.close()

