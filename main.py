# -*- coding = utf-8 -*-
# @Time : 2021-11-8     ⏰
# @Author : P.B.A.S     🍥
# @File : main.py       🫀
# @Software : PyCharm   💾


# import 列表。
import random
import urllib.request
import urllib.parse
import gzip
import os
import ssl
import time
import math
import json
import secrets
import pymysql

from tkinter import *
from pyfiglet import Figlet

ssl._create_default_https_context = ssl._create_unverified_context  # 全局取消验证。（其实我也不知道这句话是干嘛的（反正删掉了就不能用了（报错怎么办呢


#   这下面是全局变量。主要是一些空的。
database_host = ""          # 数据库的地址。
database_user = ""          # 数据库的用户。
database_password = ""      # 数据库的密码。
database_database = ""      # 哪个数据库？
table_name = ""             # 数据库里的表名。


# 各种函数。
def get_single_page(page_url):  # 用于获得单个网络页面的函数。

    block_page = {"code": 0, "message": "0", "ttl": 1, "data": {"replies": []}}
    header_bunker = {
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (Macintosh; Apple silicon Mac OS X 12_1_0) Gecko/20100101 Firefox/94.0"
    }  # 伪装成浏览器，也可以加一些别的。

    page_request = urllib.request.Request(url=page_url, headers=header_bunker)  # 把url地址和头部打包。
    page_data_raw = urllib.request.urlopen(page_request)                    # 开个网页，把返回的内容传给page_data_raw。
    page_data_mar = page_data_raw.read()                                    # 把网页返回的所有数据读出到page_data_mar。

    try:

        page_data_deco = gzip.decompress(page_data_mar).decode("utf-8")     # 将mar的数据解码成utf-8，存到deco。
        return page_data_deco  # 将网页解码得到的数据返回给函数。

    except:

        print("ERR-有点问题，可能是评论区被关闭了。")
        return str(block_page)


def get_full_pages(av_pin):    # 函数，是用来把这个视频里的所有评论提取分析出来其实并不是吧，嗯，也算是吧。

    page_tag = 1    # 这个是一开始的页数，并不是零21。（这个语音识别好怪哟，懒得改。

    while True:     # 这个循环式这个函数的主体，是这样说的吗？

        url = "https://api.bilibili.com/x/v2/reply?pn=%d&type=1&oid=%d&sort=2" % (page_tag, av_pin)
        data_download = get_single_page(url)                                    # 使用函数获得页的内容，再给到data_download。
        name_local_doc = "o-saveData_Av-%d_Page-%d.json" % (av_pin, page_tag)   # 这是保存在本地的网页文件的名字或者是位置。
        save_page_content(data_download, name_local_doc)                        # 使用函数，保存页的内容。
        print("PageTag: ", page_tag)                        # 打印页面号码。
        time.sleep(0.5 + (secrets.randbelow(40000) / 80000))    # 生成随机0.50-1.00秒以内的数字。。

        if not data_usability_test(name_local_doc, "c"):     # 调用检测每一页是否有评论的函数，决定是跳过或是中断。

            print("END-这个视频结束了！")
            break

        else:

            try:

                data_process_and_save(name_local_doc)

            except:     # 异常子句过于宽泛？好吧，我觉得还行吧。

                time.sleep(2)
                print("ERR-你的数据库应该是卡了。好吧，其实我也不知道到底是怎么回事，反正如果没有下一条提示的话，那应该是没什么大问题问题。")

                try:

                    data_process_and_save(name_local_doc)

                except:     # 异常子句过于宽泛？好吧，我觉得还行吧。

                    print("ERR-你的数据库多半是炸了，建议检查一下或是重启一下，如果还是不行的话，重启一下电脑。")
                    pass    # 我确实不知道你的数据库到底出什么问题，但我觉得好像是有些问题，但我确实又不知道什么问题。

            pass

        page_tag += 1  # 下一个页面。


def data_process_and_save(data_file_tag):   # 这个函数是分析数据把数据再存到表里好吧，其实我也不知道应该怎么说，而且这个函数有点太长了,可能是吧。

    file_open = open(data_file_tag, "r")  # 打开本地保存的文件。
    file_content_str = file_open.read()  # 把内容写到file_content_str。
    file_open.close()  # 关闭文件。
    file_content_dict = json.loads(file_content_str)  # 把Json文件转换为字典。

    for user_temp_id in range(len(file_content_dict["data"]["replies"])):  # 检测有N个回复，循环N次。

        data_username = file_content_dict["data"]["replies"][user_temp_id]["member"]["uname"]
        data_gender = file_content_dict["data"]["replies"][user_temp_id]["member"]["sex"]
        data_bio = file_content_dict["data"]["replies"][user_temp_id]["member"]["sign"]
        data_uid = file_content_dict["data"]["replies"][user_temp_id]["member"]["mid"]
        data_level = file_content_dict["data"]["replies"][user_temp_id]["member"]["level_info"]["current_level"]
        data_say_what = file_content_dict["data"]["replies"][user_temp_id]["content"]["message"]
        data_u_like = file_content_dict["data"]["replies"][user_temp_id]["like"]
        data_c_time = file_content_dict["data"]["replies"][user_temp_id]["ctime"]
        # 把各种参数填到各种变量里。

        data_say_time_array = time.localtime(data_c_time)
        data_say_time = time.strftime("%Y-%m-%d %H:%M:%S", data_say_time_array)
        # 把时间码转换成标准的时间。

        # 这里的话，如果你想要打印这些内容，我觉得你可以打印，但是我觉得没有必要，所以我就不打印了。

        # print("用户名：", data_username)
        # print("性别：", data_Gender)
        # print("Bio：", data_Bio)
        # print("UID：", data_UID)
        # print("等级：", data_Level)
        # print("评论内容：", data_SayWhat)
        # print("点赞数：", data_ULike)
        # print("精准时间：", data_SayTime)
        # print("来自文件：", data_file_tag)
        # 这个用不了，变量名改了。

        # print("-" * 50)

        database = pymysql.connect(

            host=database_host,
            user=database_user,
            password=database_password,
            database=database_database

        )  # 连接数据库。注意密码和数据库名。

        database_cursor = database.cursor()  # 添加指针。

        database_do = "INSERT INTO %s(Username, \
            Gender, Bio, UID, Level, SayWhat, ULike, SayTime, FileTag) \
                VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                    (table_name, data_username, data_gender, data_bio, data_uid, data_level, data_say_what,
                    data_u_like, data_say_time, data_file_tag)

        try:        # 尝试运行。

            database_cursor.execute(database_do)    # 执行sql。
            database.commit()

        except:     # 异常子句过于宽泛？好吧，我觉得还行吧。

            print("ERR-没法把数据存到表里,多半是里面有单引号。也可能有其他的问题了，这也说不准。")
            database.rollback()             # 发生错误时回滚.

        database.close()    # 关闭数据库。


def save_page_content(page_data_download, file_name):    # 把每一页的文件保存。

    file_save = open(file_name, "w")                     # 打开saveDataTxt文件，如果没有就创建一个。
    file_save.write(page_data_download)                  # 把page_data_download内容写入。
    file_save.close()                                    # 关闭文件。


def data_usability_test(name_local_doc, mode):                                # 用于检测这一页文件没有视频。如果有评论返回真，如果没有评论返回假。

    file_open_for_end = open(name_local_doc, "r")                       # 打开上一个文件用于检验。
    file_content_str_for_end = file_open_for_end.read()                 # 把内容写到file_content_str_for_end。
    file_open_for_end.close()   # 关闭打开的文件。

    try:

        file_content_dict_for_end = json.loads(file_content_str_for_end)    # 把Json文件转换为字典。

    except:

        return False

    if mode == "c":     # 评论检测

        if len(file_content_dict_for_end["data"]["replies"]) == 0:          # 获取到的评论数量检测。

            os.remove(name_local_doc)  # 删除文件。
            return False    # 没有评论返回假。

        else:

            return True     # 有评论返回真。

    if mode == "v":     # 视频检测

        if len(file_content_dict_for_end["data"]["list"]["vlist"]) == 0:  # 获取到的评论数量检测。

            os.remove(name_local_doc)  # 删除文件。
            return False  # 没有评论返回假。

        else:

            return True  # 有评论返回真。

    if mode == "f":     # 视频检测

        if len(file_content_dict_for_end["data"]["list"]) == 0:  # 获取到的评论数量检测。

            os.remove(name_local_doc)  # 删除文件。
            return False  # 没有评论返回假。

        else:

            return True  # 有评论返回真。


def bv_to_av(bv):   # 不知道从哪儿偷来的代码,忘了。。。

    bvno1 = bv[2:]

    keys = {
        '1': '13', '2': '12', '3': '46', '4': '31', '5': '43', '6': '18', '7': '40', '8': '28', '9': '5',
        'A': '54', 'B': '20', 'C': '15', 'D': '8', 'E': '39', 'F': '57', 'G': '45', 'H': '36', 'J': '38', 'K': '51',
        'L': '42', 'M': '49', 'N': '52', 'P': '53', 'Q': '7', 'R': '4', 'S': '9', 'T': '50', 'U': '10', 'V': '44',
        'W': '34', 'X': '6', 'Y': '25', 'Z': '1',
        'a': '26', 'b': '29', 'c': '56', 'd': '3', 'e': '24', 'f': '0', 'g': '47', 'h': '27', 'i': '22', 'j': '41',
        'k': '16', 'm': '11', 'n': '37', 'o': '2',
        'p': '35', 'q': '21', 'r': '17', 's': '33', 't': '30', 'u': '48', 'v': '23', 'w': '55', 'x': '32', 'y': '14',
        'z': '19'
    }

    bvno2 = []

    for index, ch in enumerate(bvno1):

        bvno2.append(int(str(keys[ch])))

    bvno2[0] = int(bvno2[0] * math.pow(58, 6))
    bvno2[1] = int(bvno2[1] * math.pow(58, 2))
    bvno2[2] = int(bvno2[2] * math.pow(58, 4))
    bvno2[3] = int(bvno2[3] * math.pow(58, 8))
    bvno2[4] = int(bvno2[4] * math.pow(58, 5))
    bvno2[5] = int(bvno2[5] * math.pow(58, 9))
    bvno2[6] = int(bvno2[6] * math.pow(58, 3))
    bvno2[7] = int(bvno2[7] * math.pow(58, 7))
    bvno2[8] = int(bvno2[8] * math.pow(58, 1))
    bvno2[9] = int(bvno2[9] * math.pow(58, 0))

    bv_to_av_sum = 0

    for i in bvno2:

        bv_to_av_sum += i

    bv_to_av_sum -= 100618342136696320
    temp = 177451812
    return bv_to_av_sum ^ temp


def creation_new_tab(host_i, user_i, password_i, database_i):   # 这个函数是用来创建一个新表。

    database = pymysql.connect(
        host=host_i,
        port=3306,
        user=user_i,
        password=password_i,
        database=database_i,
        charset='utf8'
    )  # 连接数据库。输入各种参数。

    database_cursor = database.cursor()  # 添加指针。
    database_do = "DROP TABLE IF EXISTS %s" % table_name  # 命令新建表格。
    # print(database_do)
    database_cursor.execute(database_do)  # 执行命令。

    database_do = "CREATE TABLE %s (Username  VARCHAR(100) NOT NULL, Gender  VARCHAR(100), Bio VARCHAR(500), UID INT UNSIGNED NOT NULL, Level INT UNSIGNED NOT NULL, SayWhat VARCHAR(3000) NOT NULL, ULike INT, SayTime DATETIME NOT NULL, FileTag VARCHAR(500) NOT NULL )" % table_name
    # 命令，长？我也没什么办法。

    database_cursor.execute(database_do)  # 执行命令。
    database.close()  # 关闭数据库。


def get_full_video(uid_upper):  # 这个函数，是用来把用户上传所有视频的AV，BV，还有别的信息提取出来，算是吧。

    page_tag = 1
    break_tag = 0

    while True:

        url = "https://api.bilibili.com/x/space/arc/search?mid=%d&ps=30&tid=0&pn=%d" % (uid_upper, page_tag)
        data_download = get_single_page(url)  # 使用函数获得页的内容，再给到data_download。
        name_local_doc = "o-saveData_upperUid-%d_Page-%d.json" % (uid_upper, page_tag)  # 这是保存在本地的网页文件的名字或者是位置。
        save_page_content(data_download, name_local_doc)  # 使用函数，保存页的内容。
        print("Video: ", page_tag)  # 打印页面号码。

        if not data_usability_test(name_local_doc, "v"):  # 调用检测每一页是否有评论的函数，决定是跳过或是中断。

            print("BRE-现在应该是完全结束了，我猜是这样，也可能不是这样，我建议你检查一下，好吧，再见。")
            print("-" * 40)
            break

        else:

            file_open = open(name_local_doc, "r")  # 打开本地保存的文件。
            file_content_str = file_open.read()  # 把内容写到file_content_str。
            file_open.close()  # 关闭文件。
            file_content_dict = json.loads(file_content_str)  # 把Json文件转换为字典。

            if len(file_content_dict["data"]["list"]["vlist"]) < 30:

                break_tag = 1

            for user_temp_id in range(len(file_content_dict["data"]["list"]["vlist"])):  # 检测有N个回复，循环N次。

                data_av = file_content_dict["data"]["list"]["vlist"][user_temp_id]["aid"]
                data_bv = file_content_dict["data"]["list"]["vlist"][user_temp_id]["bvid"]
                data_title = file_content_dict["data"]["list"]["vlist"][user_temp_id]["title"]

                print(data_av)
                print(data_bv)
                print(data_title)

                get_full_pages(data_av)

                print("-" * 40)
                need_help()
                print("-" * 40)

                # 这个是预览：

                # 460915509
                # BV1E5411M7gw
                # 【1.17更新】盔甲架挂头不闪，卡服下船正常【1.17发布预览1】
                # PageTag: 1
                # PageTag: 2
                # END - 这个视频结束了！
                # ----------------------------------------
                # 帮助海地的游击队员！
                # ----------------------------------------
                # 100264950
                # BV1W7411D7Ff
                # 【厉害】“N号房”背后：揭密26万韩国人与全球色情视频产业【全球视野05】
                # PageTag: 1
                # PageTag: 2
                # ERR - 没法把数据存到表里, 多半是里面有单引号。也可能有其他的问题了，这也说不准。
                # PageTag: 3
                # END - 这个视频结束了！
                # ----------------------------------------
                # 帮助立陶宛的跨性别者！
                # ----------------------------------------

            if break_tag == 1:

                print("BRE-这一步结束了，我猜是这样。")
                print("-" * 40)
                break

        page_tag += 1  # 下一个页面。
        time.sleep(0.5 + (secrets.randbelow(40000) / 80000))    # 生成随机0.50-1.00秒以内的数字。。


def get_full_follow(uid_upper):  # 这个函数， 检测这个用户关注的所有用户。

    page_tag = 1
    break_tag = 0

    while True:

        url = "https://api.bilibili.com/x/relation/followings?vmid=%d&pn=%d" % (uid_upper, page_tag)
        data_download = get_single_page(url)  # 使用函数获得页的内容，再给到data_download。
        name_local_doc = "o-saveData_followUid-%d_Page-%d.json" % (uid_upper, page_tag)  # 这是保存在本地的网页文件的名字或者是位置。
        save_page_content(data_download, name_local_doc)  # 使用函数，保存页的内容。

        print("Following: ", page_tag)  # 打印页面号码。

        if not data_usability_test(name_local_doc, "f"):  # 调用检测每一页是否有评论的函数，决定是跳过或是中断。

            print("BRE-现在应该是完全结束了，只能访问前250个关注，也可能不是这样，我建议你检查一下，好吧，再见。")
            print("-" * 40)
            break

        else:

            # print("Nice")
            # break

            file_open = open(name_local_doc, "r")  # 打开本地保存的文件。
            file_content_str = file_open.read()  # 把内容写到file_content_str。
            file_open.close()  # 关闭文件。
            file_content_dict = json.loads(file_content_str)  # 把Json文件转换为字典。

            if len(file_content_dict["data"]["list"]) < 50:

                break_tag = 1

            for user_temp_id in range(len(file_content_dict["data"]["list"])):  # 检测有N个回复，循环N次。

                data_mid = file_content_dict["data"]["list"][user_temp_id]["mid"]
                data_uname = file_content_dict["data"]["list"][user_temp_id]["uname"]
                data_sign = file_content_dict["data"]["list"][user_temp_id]["sign"]

                print(data_mid)
                print(data_uname)
                print(data_sign)

                print("-"*40)
                need_help()
                print("-" * 40)

                get_full_video(data_mid)

            if break_tag == 1:

                print("BRE-现在应该是完全结束了，我猜是这样，也可能不是这样，我建议你检查一下，好吧，拜拜。")
                print("-" * 40)
                break

        page_tag += 1  # 下一个页面。
        time.sleep(0.5 + (secrets.randbelow(40000) / 80000))    # 生成随机0.50-1.00秒以内的数字。。


def boot_func():

    global database_host
    global database_user
    global database_password
    global database_database
    global table_name

    print("━" * 65)

    print(Figlet().renderText("Commget-Bil!"), end="")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#    ____                                     _        ____  _ _
#  / ___|___  _ __ ___  _ __ ___   __ _  ___| |_     | __ )(_) |
# | |   / _ \| '_ ` _ \| '_ ` _ \ / _` |/ _ \ __|____|  _ \| | |
# | |__| (_) | | | | | | | | | | | (_| |  __/ ||_____| |_) | | |
#  \____\___/|_| |_| |_|_| |_| |_|\__, |\___|\__|    |____/|_|_|
#                                 |___/
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 欢迎使用这个程序！  请根据提示选择模式！ 帮助津巴布韦的亚洲移民！
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ｜单个视频的评论： p ｜单个用户的视频： v ｜用户关注的用户： f ｜
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    print("━" * 65)

    print("   欢迎使用这个程序！", end="  ")
    print("请根据提示选择模式！", end=" ")
    need_help()

    print("━" * 65)

    print("｜单个视频的评论： p ", end="｜")
    print("单个用户的视频： v ", end="｜")
    print("用户关注的用户： f ", end="｜\n")

    print("━" * 65)

    print("输入模式(p/v/f)：", end="")
    ot_input = input()
    print("输入一个表名(str)：", end="")
    table_name = input()
    print("需要自定义数据库连接吗(y/n)：", end="")
    is_custom_database_input = input()

    if is_custom_database_input == "y":

        print("-" * 40)
        print("Host(localhost):")
        database_host = input()
        print("User(root):")
        database_user = input()
        print("Password(root):")
        database_password = input()
        print("Database(PyTest):")
        database_database = input()
        print("-" * 40)

    elif is_custom_database_input == "n":

        print("使用默认设置。")
        database_host = "localhost"  # 数据库的位置，现在是本地。
        database_user = "root"  # 数据库的用户名。
        database_password = "root"  # 数据库，用户的密码。
        database_database = "PyTest"  # 数据库名，你看着办吧。

    else:

        print("ERR-请确认输入(y/n)。")

        print("3s_exit()")
        time.sleep(1)
        print("2s_exit()")
        time.sleep(1)
        print("1s_exit()")
        time.sleep(1)

        exit()

    creation_new_tab(database_host, database_user, database_password, database_database)  # 创建一个新表，参数在上面。
    print("连接成功。")

    if ot_input == "p":

        print("输入BV号(str)：")
        temp_p = int(input())
        get_full_pages(bv_to_av(temp_p))  # 下载这个视频的全部评论。

    elif ot_input == "v":

        print("输入用户号码(int)：")
        temp_v = int(input())
        get_full_video(temp_v)  # 把这个UP主的所有视频下的评论一起下载。

    elif ot_input == "f":

        print("输入用户号码(int)：")
        temp_f = int(input())
        get_full_follow(temp_f)  # 下载这个用户关注的最后250位用户的全部视频的全部评论。

    else:

        print("ERR-请确认输入(p/v/f)。")

        print("3s_exit()")
        time.sleep(1)
        print("2s_exit()")
        time.sleep(1)
        print("1s_exit()")
        time.sleep(1)

        exit()

    print("━" * 65)
    time.sleep(2)


def need_help():  # 帮助！

    f_list = ["乌干达", "刚果", "坦桑尼亚", "赤道几内亚", "阿富汗", "阿塞拜疆", "缅甸", "挪威", "朝鲜",
              "不丹", "保加利亚", "中国", "乍得", "古巴", "加拿大", "海地", "伊朗", "印度",
              "丹麦", "埃塞俄比亚", "日本", "立陶宛", "墨西哥", "波兰", "卡塔尔", "俄罗斯", "罗马尼亚", "南非",
              "瑞士", "叙利亚", "泰国", "美国", "英国", "阿联酋", "越南", "梵蒂冈", "赞比亚", "津巴布韦", "香港",
              "台湾", "索科特拉岛", "南极", "法属圭亚那", "百慕大", "车臣"]

    day_time = int(time.strftime("%m%d", time.localtime()))

    if day_time == 1120:

        s_list = ["跨性别者", ]

    else:

        s_list = ["可怜儿童", "少数群体", "国家官员", "民间组织", "残疾警官", "跨性别者", "同性恋者", "异性恋者", "无性恋者", "双性恋者",
                  "知识分子", "社会精英", "政治领袖", "非洲移民", "亚洲移民", "美洲移民", "欧洲移民", "基督教徒", "天主教徒", "道教教徒",
                  "回教教徒", "无产阶级", "底层农民", "游击队员", "民主人士", "技术工人"]

    main_str = "帮助%s的%s！" % (f_list[random.randint(0, len(f_list) - 1)], s_list[random.randint(0, len(s_list) - 1)])

    print(main_str)


def what_day():

    day_time = int(time.strftime("%m%d", time.localtime()))

    if day_time == 1120:

        show_window_transgender()


def show_window_transgender():

    r_swt = Tk()

    r_swt.title("TDoR")

    Button(r_swt, text="跨性别死难者纪念日", bd=15).pack()

    Label(r_swt, text=" " * 60, bg="light blue").pack()
    Label(r_swt, text=" " * 60, bg="pink").pack()
    Label(r_swt, text=" " * 60, bg="white").pack()
    Label(r_swt, text=" " * 60, bg="pink").pack()
    Label(r_swt, text=" " * 60, bg="light blue").pack()

    Label(r_swt, text="").pack()

    Label(r_swt, text="悼念被谋杀的跨性别者🕯").pack()

    Label(r_swt, text=" " * 70).pack()

    r_swt.mainloop()


# main.
if __name__ == '__main__':      # 这个是程序开始运行的地方。

    # database_host = "localhost"     # 数据库的位置，现在是本地。
    # database_user = "root"          # 数据库的用户名。
    # database_password = "root"      # 数据库，用户的密码。
    # database_database = "PyTest"    # 数据库名，你看着办吧。

    # table_name = "KK-LL-MM-JJ"    # 表单名称，建议修改。

    # creation_new_tab(database_host, database_user, database_password, database_database)  # 创建一个新表，参数在上面。

    # get_full_follow(123456789)  # 下载这个用户关注的最后250位用户的全部视频的全部评论。
    # get_full_video(123456789)  # 把这个UP主的所有视频下的评论一起下载。
    # get_full_pages(bv_to_av("BVXNe"))  # 下载这个视频的全部评论。

    what_day()
    boot_func()

    pass

# 已过时==>
# 上面的第一条主色调的就是创建一个新表，然后参数的话就在上面。
# 然后第二条就是把这个用户的所有视频里的评论都存到数据库里，然后这个数据库就是顶上的参数的那个数据库。
# 然后第三个这个指令，就是把这一个视频里所有的评论添加到你顶上的那个数据库里。
# 上面的表名记得改：data_process_and_save(data_file_tag)这个里面的
# 好吧，我在说什么，好怪欧。。。
