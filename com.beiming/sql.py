import pymysql.cursors

# 链接数据库
connect = pymysql.Connect(
    host='localhost',
    user='root',
    passwd='0000',
    db='test'
)

cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
effect_row = cursor.execute("select * from user_info")
# 获取所有数据
result = cursor.fetchall()
# 获取下一个数据
next = cursor.fetchone()
print(next)
# 获取下一个数据 在上一个的基础之上
print(result)
print(effect_row)



# # 获取游标
# cursor = connect.cursor()
#
# sql = "insert into user_info(username,password) VALUES ('jgm','1000')"
# # data = ('jgm', '1000')
# # cursor.execute(sql % data)
# connect.commit()



