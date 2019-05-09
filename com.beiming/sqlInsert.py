import pymysql

connect = pymysql.Connect(
    host='localhost',
    user='root',
    passwd='0000',
    db='test'
)

cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)

# effect_row = cursor.execute("insert into course(cou_name,time) values(%s,%s)", ("Engilsh", 100))
# print(effect_row)
cursor.execute("insert into user_info(username,password) VALUES (%s,%s)", ("金国民","0000"))

# cursor.execute("insert into user_info(username,password) VALUES ('jgm','1000')")
connect.commit()
cursor.close()
