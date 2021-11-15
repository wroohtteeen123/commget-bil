# -*- coding = utf-8 -*-
# @Time : 2021-11-15    ⏰
# @Author : P.B.A.S     🍥
# @File : main.py       🫀
# @Software : PyCharm   💾


# import 列表。
import pymysql


#   这下面是变量。主要是一些空的。
database_host = "localhost"  # 数据库的位置，现在是本地。
database_user = "root"  # 数据库的用户名。
database_password = "root"  # 数据库，用户的密码。
database_database = "PyTest"  # 数据库名，你看着办吧。
table_name = "lidanglaoshi"  # 表单名称，建议修改。

temp_data = []


database = pymysql.connect(

    host=database_host,
    user=database_user,
    password=database_password,
    database=database_database

)  # 连接数据库。注意密码和数据库名。

database_cursor = database.cursor()
database_do = "SELECT * FROM %s" % table_name
# database_do = "SELECT * FROM %s WHERE ULike > %s" % (table_name, 1000)

try:    # 尝试运行。

    database_cursor.execute(database_do)
    database_results = database_cursor.fetchall()

    for database_row in database_results:

        temp_data = str(temp_data) + str(database_row[5])
        # print(type(temp_data))
        # print(database_row)

except:     # 异常子句过于宽泛？好吧，我觉得还行吧。

    print("ERR-我感觉出了些问题！")

database.close()

temp_data.replace('\n', '')
temp_data.replace('\r', '')

temp_data_list = list(temp_data)

list_del = ["\n", " ", "。", ".", "，", ",", "[", "]", "{", "}",
            "【", "】", "「", "」", "！", "!", "?", "？", "(", ")", "（", "）"]

temp_data_str = ""

for i in temp_data_list:

    for k in list_del:

        if str(i) == str(k):

            y = 1

    if y == 1:

        y = 0
        continue

    temp_data_str += str(i)









file_save = open("test2.txt", "w")

file_save.write(temp_data_str)

file_save.close()

print(list(temp_data_str))





#
#
# print(temp_data_str)
# print(type(temp_data))
