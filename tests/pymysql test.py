import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="c0ding_gw4n9",
    db="login_users",
    charset="utf8",
)
cur = conn.cursor()

cur.execute("SELECT * FROM users;")
myList1 = cur.fetchall()

print(myList1)  # 이중 튜플 형태!
print()

for i in myList1:
    print(i)  # 튜플로 나옴
print()

id1 = "'sjxp05'"
cur.execute(f"SELECT name FROM users WHERE id = {id1};")
name1 = cur.fetchall()
print(name1)  # 이중튜플로 나옴
print(name1[0][0])  # 원소로만 뽑기

conn.commit()
conn.close()
