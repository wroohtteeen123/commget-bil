import jieba
import pymysql

# Test_list = ["这个up有个特点，他总是以最大的恶意去揣测西方，但是每次西方都会打他的脸，西方做起来比他揣测的还要恶毒。",
#              "以前的中国人承诺不清算日本跟我现在的中国人有什么关系？[doge]",
#              "小约翰可汗是嬉笑怒骂有时候要接点广告，毕竟人家视频干货是真的足，一个二十多岁刚毕业在上海的年轻人要生活能理解，"
#              "而且价值观很正，我不说他恰烂钱 心医三十多岁事业小成，生活富足，自己可以专心当心理医生，"
#              "却敢于站出来用自己的声音去喊醒很多人，自己不接单，不投原创，甚至不要求投币，这类人都被污蔑为恰烂钱，可见那些人以为钱是万能的",
#              "我以前还不信心医说的新型公知，但气象武器那次对线以及这次东京奥运会使劲舔这个阴间开幕式让我发现二鬼子是真的多，我更相信心医的话了，他们并不愿意我们有戒备心理，这是很危险的，还请大家小心[辣眼睛][辣眼睛]"
#              ]    # 太离谱了。

database_host = "localhost"  # 数据库的位置，现在是本地。
database_user = "root"  # 数据库的用户名。
database_password = "root"  # 数据库，用户的密码。
database_database = "PyTest"  # 数据库名，你看着办吧。
table_name = "XY492808243"  # 表单名称，建议修改。

temp_data_list = []  # 把获得到的所有数据存在这个列表里。

database = pymysql.connect(

    host=database_host,
    user=database_user,
    password=database_password,
    database=database_database

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

# print(temp_data_list)

list_del = ["\n", " ", "。", ".", "，", ",", "[", "]", "{", "}",
            "【", "】", "「", "」", "！", "!", "?", "？", "(", ")", "（", "）", "/", ":", "”", ";",
            "-", "=", "_", "…", "~", "～", "+", "▿", "&", "#", "@", "："]  # 这个是删除的列表。

y = 0  # 这个是用来判断的。

tab_data = {}
# {"欧美":[1,2],心理医生:[32,34]}

for list_str in temp_data_list:  # 列表里的每一个人字符串。

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

        except:

            con_tab = True

            break

    if not con_tab:

        if temp_data_int >= 0.8:

            tab_data[break_str] = 0.1 + int(tab_data[break_str])
            print("Con_Tab Running+")

        elif temp_data_int <= -0.8:

            tab_data[break_str] = -0.1 + int(tab_data[break_str])
            print("Con_Tab Running-")

        else:

            print("Con_Tab")

        continue

    if con_tab:

        pass

    print("这个评论有关极右吗(y/n/p):", end="")
    c_input = input()

    # print("分词输出", break_list)
    # print("="*300)

    for break_str in break_list:

        if c_input == "y":

            try:  # 把现有的字典里的东西增加。

                tab_data[break_str] = 1 + int(tab_data[break_str])

            except:  # 现有字典没有的话，就新建一个字典的条目。

                tab_data[break_str] = 1

        if c_input == "n":

            try:  # 把现有的字典里的东西增加。

                tab_data[break_str] = -1 + int(tab_data[break_str])

            except:  # 现有字典没有的话，就新建一个字典的条目。

                tab_data[break_str] = -1

        if c_input == "p":

            pass

    print(tab_data)
