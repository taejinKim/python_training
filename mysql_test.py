import pymysql

#db서버에 대한 정보 , 각자의 환경에 맞춰 입력 바랍니다.  demo_shop이라는 데이타베이스를 사용합니다.
server = "localhost"
user = "root"
password = "q12w3e4rye"
dbname="demo_shop"

conn = pymysql.connect(server, user, password, dbname, charset="utf8")

cursor = conn.cursor()

cursor.execute("select * from TB_PRODUCT;")

row = cursor.fetchone()

while row:
    print(str(row[1]) + "\t" + str(row[2]) + "\t" + str(row[3]) + "\t" + str(row[4]) )
    row = cursor.fetchone()

conn.close()