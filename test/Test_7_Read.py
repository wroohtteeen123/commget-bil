import jieba
import pymysql
import json


# print(temp_data_list)

list_del = ["\n", " ", "。", ".", "，", ",", "[", "]", "{", "}",
            "【", "】", "「", "」", "！", "!", "?", "？", "(", ")", "（", "）", "/", ":", "”", ";",
            "-", "=", "_", "…", "~", "～", "+", "▿", "&", "#", "@", "："]  # 这个是删除的列表。

y = 0  # 这个是用来判断的。

file_dic = open("file_dic.cb", "r")  # 这句用来读取文件。
next_str = file_dic.read()
tab_data = {}
tab_data = json.loads(next_str)
# print(next_dic)
file_dic.close()

# print(tab_data)
# print(type(tab_data))

# {"你好": {"a": 213, "o": 324}, "心医": {"a": 643, "o": 12}}
# 这里是一个词典，前面是词后面跟着的词典A代表你的目标，O代表着你和他目标有多不相关.


# Test_list = ["这个up有个特点，他总是以最大的恶意去揣测西方，但是每次西方都会打他的脸，西方做起来比他揣测的还要恶毒。",
#              "以前的中国人承诺不清算日本跟我现在的中国人有什么关系？[doge]",
#              "小约翰可汗是嬉笑怒骂有时候要接点广告，毕竟人家视频干货是真的足，一个二十多岁刚毕业在上海的年轻人要生活能理解，"
#              "而且价值观很正，我不说他恰烂钱 心医三十多岁事业小成，生活富足，自己可以专心当心理医生，"
#              "却敢于站出来用自己的声音去喊醒很多人，自己不接单，不投原创，甚至不要求投币，这类人都被污蔑为恰烂钱，可见那些人以为钱是万能的",
#              "我以前还不信心医说的新型公知，但气象武器那次对线以及这次东京奥运会使劲舔这个阴间开幕式让我发现二鬼子是真的多，我更相信心医的话了，他们并不愿意我们有戒备心理，这是很危险的，还请大家小心[辣眼睛][辣眼睛]"
#              ]    # 测试list，太离谱了。


def db_get_comm(db_host="localhost", db_user="root", db_password="root", db_database="PyTest", table_name="bilcome"):   # 这个函数是用来获取数据库的评论全部。
    # database_host = "localhost"  # 数据库的位置，现在是本地。
    # database_user = "root"  # 数据库的用户名。
    # database_password = "root"  # 数据库，用户的密码。
    # database_database = "PyTest"  # 数据库名，你看着办吧。
    # table_name = "simanan"  # 表单名称，建议修改。

    # database_ ==> db_

    temp_data_list = []  # 把获得到的所有数据存在这个列表里。

    database = pymysql.connect(

        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database

    )  # 连接数据库。注意密码和数据库名。

    database_cursor = database.cursor()  # 这个是数据库的指针。

    database_do = "SELECT * FROM %s" % table_name  # 需要执行的数据库命令。%s是用来输入表明的。

    # database_do = "SELECT * FROM %s WHERE ULike > %s" % (table_name, 1000) # 这一条是用来搜索具体的料。

    try:  # 尝试运行。

        database_cursor.execute(database_do)
        database_results = database_cursor.fetchall()

        for database_row in database_results:
            temp_data_list.append(str(database_row[5]))

    except:  # 异常子句过于宽泛？好吧，我觉得还行吧。

        print("ERR-我感觉出了些问题！")

    database.close()

    return temp_data_list


for list_str in db_get_comm(table_name="simanan"):  # 列表里的每一个人字符串。

    # print(tab_data)

    temp_data_str = ""  # 清空零食数据字符串。

    print(list_str)

    for i in list(list_str):  # 把字符串打成列表。

        for del_str in list_del:  # 选取删除列表中的每个需要删除的字，然后判断这一个只是不是要删除。

            if str(i) == str(del_str):  # 如果这个只需要删除的话，y就等于1。

                y = 1

        if y == 1:  # 如果需要删除就不保存，到临时大数据字符串。

            y = 0
            continue

        temp_data_str += str(i)  # 如果不需要删除就把这一个文字保存到临时的数据字符串。

    # print(temp_data_str)
    # print(type(temp_data_str))

    if not temp_data_str:
        continue

    seg_list = jieba.cut(temp_data_str)  # 结果是个生成器，还不能直接使用

    break_list = [x for x in seg_list]  # 将分词的结果保存到列表中，可以看到元素是分好的词，列表长度即为分好的词的数量

    # print(temp_data_str)

    con_tab = False
    temp_data_int = 0

    for i in break_list:
        try:

            temp_data_int += int(tab_data[i])
            # --------------------------------------------

        except:

            con_tab = True

            break

    if not con_tab:

        if temp_data_int >= 0.8:

            for break_str in break_list:
                tab_data[break_str] = float(tab_data[break_str]) + 0.1
                # print("HELLO")

            print(temp_data_int)
            print("Con_Tab Running+")

        elif temp_data_int <= -0.8:

            for break_str in break_list:
                tab_data[break_str] = float(tab_data[break_str]) + -0.1

            print(temp_data_int)
            print("Con_Tab Running-")

        else:

            print("Con_Tab")

        file_dic = open("file_dic.cb", "w+")

        file_dic.write(json.dumps(tab_data))

        file_dic.close()

        file_dic = open("file_dic.cb", "r")

        next_str = file_dic.read()
        tab_data = json.loads(next_str)
        # print(next_dic)

        file_dic.close()

        continue

    if con_tab:
        pass

    # print("这是正常的评论(y/n/p):", end="")
    # c_input = input()

    c_input = "n"

    # print("分词输出", break_list)
    # print("="*300)

    for break_str in break_list:

        if c_input == "y":

            try:  # 把现有的字典里的东西增加。

                tab_data["_commin_"]["a"] = tab_data["_commin_"]["a"] + 1

            except:  # 现有字典没有的话，就新建一个字典的条目。

                tab_data["_commin_"] = {"a": 1, "o": 0}

            # ------------------------------

            try:  # 把现有的字典里的东西增加。

                tab_data[break_str]["a"] = tab_data[break_str]["a"] + 1

            except:  # 现有字典没有的话，就新建一个字典的条目。

                tab_data[break_str] = {"a": 1, "o": 0}

        if c_input == "n":

            try:  # 把现有的字典里的东西增加。

                tab_data["_commin_"]["o"] = tab_data["_commin_"]["o"] + 1

            except:  # 现有字典没有的话，就新建一个字典的条目。

                tab_data["_commin_"] = {"a": 0, "o": 1}

            # ------------------------------

            try:  # 把现有的字典里的东西增加。

                tab_data[break_str]["o"] = tab_data[break_str]["o"] + 1

            except:  # 现有字典没有的话，就新建一个字典的条目。

                tab_data[break_str] = {"a": 0, "o": 1}

        if c_input == "p":
            pass

    # print(tab_data)
print(tab_data)
