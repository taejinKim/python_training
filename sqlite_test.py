import sqlite3

# 데이타베이스를 사용하기 위해, 일단 연결을 해야함
# db파일명을 미리 만들필요는 없다. 없으면 새로 생성됨
conn = sqlite3.connect("sqlite_test.db", isolation_level=None)

# cursor는 SQL문을 저장하는 단위 라고 보면 됨
cursor = conn.cursor()

# 테이블이 없다면 테이블생성함, 데이타 구조를 정한다.
cursor.execute(
    "create table if not exists addressbook(serial_no INTEGER, category TEXT, firstname TEXT, lastname TEXT, cellphone_number TEXT)")

sql = "delete from addressbook"
cursor.execute(sql)

sql = "Insert into addressbook(serial_no, category, firstname, lastname, cellphone_number) values(?,?,?,?,?)"
cursor.execute(sql, (1, 'customer', 'John', 'Doe', '010-1111-2222'))

sql = "Insert into addressbook(serial_no, category, firstname, lastname, cellphone_number) values(?,?,?,?,?)"
cursor.execute(sql, (2, 'family', 'David', 'Kim', '010-1111-3333'))

sql = "select serial_no, category, firstname, lastname, cellphone_number from addressbook"
cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(str(row[0]) + " " + row[1] )
    print("\t" + row[2] + " " + row[3] )
    print("\t" + row[4] )

conn.close()
