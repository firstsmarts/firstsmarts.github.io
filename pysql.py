import pymysql

conn = pymysql.connect(host="localhost",port=3306,user="root",password="12",db="test")
mycursor = conn.cursor()
name = input('>>姓名')
age = input('>>年龄')
degree = input('>>学历')
id = input('>>id')
# executemany [("姓名","年龄","学历","id"),("姓名","年龄","学历","id")]
# mycursor.execute('insert into mytable(name,age,degree,id) values(%s,%s,%s,%s)',(name,int(age),degree,int(id)))
mycursor.execute('update mytable set name = %s where id = 1','haha')
conn.commit()
mycursor.close()
conn.close()
# print(data)