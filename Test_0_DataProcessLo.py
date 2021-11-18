# -*- coding = utf-8 -*-
# @Time : 2021-11-15    ⏰
# @Author : P.B.A.S     🍥
# @File : main.py       🫀
# @Software : PyCharm   💾


# import 列表。
import pymysql


def count_sig_str(str_input, mode_one):         # 这个函数是用来检测字符串里重复字的数量，并且转换成字典。

    new_dict = {}           # 这是输入的源字典。
    all_new_dict = {}       # 这个是最终的字典。

    list_input = list(str_input)                # 首先把输入的字符串转换成列表。由于在上一步已经去除了各种标点符号。

    for unu_a in range(0, len(list_input)):     # 这里的话，检测列表的长度重复列表长度次。

        srt_one = list_input.pop()              # 这里使用pop指令来，比较快速。

        try:        # 把现有的字典里的东西增加。

            new_dict[srt_one] = 1 + int(new_dict[srt_one])

        except:     # 现有字典没有的话，就新建一个字典的条目。

            new_dict[srt_one] = 1

    temp_list = sorted(new_dict.items(), key=lambda x: x[1], reverse=mode_one)  # 这里是把这一个东西排列一下。

    for unu_b in temp_list:     # 由于上一步排列出来的不是字典，还要把这个东西转换成字典。

        all_new_dict[unu_b[0]] = unu_b[1]

    return all_new_dict         # 最后把字典返回回去。

    # for i in k_list:          # 这个也能用，不过count的效率太低了！！
    #         a = k_list.count(i)
    #         print(a)
    #         temp_srr[i] = k_list.count(i)
    #         for k in range(0, a):
    #               try:
    #             k_list.remove(i)
    #               except:
    #                   print("ERR")
    #                   pass
    #         print(temp_srr)


database_host = "localhost"     # 数据库的位置，现在是本地。
database_user = "root"          # 数据库的用户名。
database_password = "root"      # 数据库，用户的密码。
database_database = "PyTest"    # 数据库名，你看着办吧。
table_name = "lidanglaoshi"     # 表单名称，建议修改。

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

except:     # 异常子句过于宽泛？好吧，我觉得还行吧。

    print("ERR-我感觉出了些问题！")

database.close()
temp_data.replace('\n', '')
temp_data.replace('\r', '')
temp_data_list = list(temp_data)

list_del = ["\n", " ", "。", ".", "，", ",", "[", "]", "{", "}",
            "【", "】", "「", "」", "！", "!", "?", "？", "(", ")", "（", "）"]

temp_data_str = ""
y = 0

for i in temp_data_list:

    for k in list_del:

        if str(i) == str(k):

            y = 1

    if y == 1:

        y = 0
        continue

    temp_data_str += str(i)

temp_srr = {}

k_list = list(temp_data_str)

print(count_sig_str(k_list, True))

