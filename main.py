# -*- coding = utf-8 -*-
# @Time : 2021-11-8     ⏰
# @Author : P.B.A.S     🍥
# @File : main.py       🫀
# @Software : PyCharm   💾


# import 列表。
import os
import ssl
import time
import math
import json
import secrets
import random
import sys


import urllib.request
import urllib.parse
import gzip

import pymysql
import jieba


from pyfiglet import Figlet
from tkinter import *

lang_set = "cn"




class Lang:

    if lang_set == "en":

        # Powered by Google Translate. (LOL
        # 这翻译出来的都是什么鬼。。。

        lc_err_01 = "ERR-Error."
        lc_err_02 = "ERR-Unknown error."
        lc_err_03 = "ERR-There is a problem, it may be that the comment area is closed ."
        lc_err_04 = "ERR-Your database is stuck ."
        lc_err_05 = "ERR-Your database has exploded, it is recommended to check it. "
        lc_err_06 = "ERR-Can't save the data in the table, it contains single quotes. "
        lc_err_07 = "ERR-Please check the input (y/n). "
        lc_err_08 = "ERR-Please check the input (p/v/f/s/r/e)."
        # lc_err_09 =

        lc_opt_01 = "Use the default settings. "
        lc_opt_02 = "All pages are processed! "
        lc_opt_03 = "It should be completely over now, I suggest you check it, goodbye. "
        lc_opt_04 = "This step is over, that's it. "
        lc_opt_05 = "Connection succeeded. "
        # lc_opt_06 =
        # lc_opt_07 =
        # lc_opt_08 =
        # lc_opt_09 =

        lc_bre_01 = "Video page number: "
        lc_bre_02 = "Follow page number: "
        lc_bre_03 = "Page being processed: "
        lc_bre_04 = "Input mode (p/v/f/s/r/o): "
        lc_bre_05 = "Enter a table name to be processed (str): "
        lc_bre_06 = "Do you need to customize the database connection (y/n): "
        lc_bre_07 = "Enter the BV number (str): "
        lc_bre_08 = "Enter user number (int): "
        lc_bre_09 = "Please enter the location you want to save to (str): "
        lc_bre_10 = "Please enter the form you want to compare (str): "
        # lc_bre_11 =
        # lc_bre_12 =




        lc_uit_01 = "Welcome! Please select a mode! "
        lc_uit_02 = "|Comments of a single video:p|Videos of a single user:v|Users followed by the user:f| "
        lc_uit_03 = "|Save the comment of the form: s|Analyze the content of the form: r|Quit and del cache: o| "
        # lc_uit_04 =
        # lc_uit_05 =
        # lc_uit_06 =
        # lc_uit_07 =
        # lc_uit_08 =
        # lc_uit_09 =

    if lang_set == "cn":

        lc_err_01 = "ERR-错误。"
        lc_err_02 = "ERR-未知错误。"
        lc_err_03 = "ERR-有点问题，可能是评论区被关闭了。"
        lc_err_04 = "ERR-你的数据库卡了。"
        lc_err_05 = "ERR-你的数据库炸了，建议检查一下。"
        lc_err_06 = "ERR-没法把数据存到表里,内含单引号。"
        lc_err_07 = "ERR-请确认输入(y/n)。"
        lc_err_08 = "ERR-请确认输入(p/v/f/s/r/e)。"
        # lc_err_09 =

        lc_opt_01 = "使用默认设置。"
        lc_opt_02 = "所有页面处理完毕！"
        lc_opt_03 = "现在应该是完全结束了，我建议你检查一下，再见。"
        lc_opt_04 = "这一步完成了。"
        lc_opt_05 = "连接成功。"
        # lc_opt_06 =
        # lc_opt_07 =
        # lc_opt_08 =
        # lc_opt_09 =

        lc_bre_01 = "视频页号: "
        lc_bre_02 = "关注页号: "
        lc_bre_03 = "正在处理的页面:"
        lc_bre_04 = "输入模式(p/v/f/s/r/o)："
        lc_bre_05 = "输入一个需要处理的表名(str)："
        lc_bre_06 = "需要自定义数据库连接吗(y/n)："
        lc_bre_07 = "输入BV号(str)："
        lc_bre_08 = "输入用户号码(int)："
        lc_bre_09 = "请输入你要保存到的位置(str):"
        lc_bre_10 = "请输入你要对比的表单(str):"
        # lc_bre_11 =
        # lc_bre_12 =

        lc_uit_01 = "欢迎使用这个程序!请根据提示选择模式!"
        lc_uit_02 = "|单个视频的评论:p|单个用户的视频:v|用户关注的用户:f|"
        lc_uit_03 = "|保存表单的评论:s|分析表单的内容:r|清空缓存后退出:o|分析表单的内容:w|"
        # lc_uit_04 =
        # lc_uit_05 =
        # lc_uit_06 =
        # lc_uit_07 =
        # lc_uit_08 =
        # lc_uit_09 =

        # Lang.lc_


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

    try:

        page_request = urllib.request.Request(url=page_url, headers=header_bunker)  # 把url地址和头部打包。

    except:

        try:

            time.sleep(10)
            page_request = urllib.request.Request(url=page_url, headers=header_bunker)
            print(Lang.lc_err_01)

        except:

            print(Lang.lc_err_02)

    page_data_raw = urllib.request.urlopen(page_request)                    # 开个网页，把返回的内容传给page_data_raw。
    page_data_mar = page_data_raw.read()                                    # 把网页返回的所有数据读出到page_data_mar。

    try:

        page_data_deco = gzip.decompress(page_data_mar).decode("utf-8")     # 将mar的数据解码成utf-8，存到deco。
        return page_data_deco  # 将网页解码得到的数据返回给函数。

    except:

        print(Lang.lc_err_03)
        return str(block_page)


def get_full_pages(av_pin):    # 函数，是用来把这个视频里的所有评论提取分析出来其实并不是吧，嗯，也算是吧。

    page_tag = 1    # 这个是一开始的页数，并不是零21。（这个语音识别好怪哟，懒得改。

    # print("页面号: ", end=" ")

    while True:     # 这个循环式这个函数的主体，是这样说的吗？

        url = "https://api.bilibili.com/x/v2/reply?pn=%d&type=1&oid=%d&sort=2" % (page_tag, av_pin)
        data_download = get_single_page(url)                                    # 使用函数获得页的内容，再给到data_download。
        name_local_doc = "./cache/av/o-saveData_Av-%d_Page-%d.json" % (av_pin, page_tag)   # 这是保存在本地的网页文件的名字或者是位置。
        save_page_content(data_download, name_local_doc)                        # 使用函数，保存页的内容。

        # print(page_tag, end=" ")                        # 打印页面号码。

        print("\r", end="")
        print(Lang.lc_bre_03, page_tag, end="")

        sys.stdout.flush()

        time.sleep(0.4 + (secrets.randbelow(3000) / 10000))    # 生成随机0.50-1.00秒以内的数字。。

        if not data_usability_test(name_local_doc, "c"):     # 调用检测每一页是否有评论的函数，决定是跳过或是中断。

            print("\r", end="")
            print(Lang.lc_opt_02)
            break

        else:

            try:

                data_process_and_save(name_local_doc)

            except:     # 异常子句过于宽泛？好吧，我觉得还行吧。

                time.sleep(2)
                print("")
                print(Lang.lc_err_04)
                # print("ERR-你的数据库应该是卡了。好吧，其实我也不知道到底是怎么回事，反正如果没有下一条提示的话，那应该是没什么大问题问题。")

                try:

                    data_process_and_save(name_local_doc)

                except:     # 异常子句过于宽泛？好吧，我觉得还行吧。

                    print(Lang.lc_err_05)
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

        # print("━" * 50)

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
                    (table_name, data_username, data_gender, data_bio, data_uid, data_level,
                    data_say_what, data_u_like, data_say_time, data_file_tag)

        try:        # 尝试运行。

            database_cursor.execute(database_do)    # 执行sql。
            database.commit()

        except:     # 异常子句过于宽泛？好吧，我觉得还行吧。

            print("")
            print(Lang.lc_err_06)
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
        name_local_doc = "./cache/upperuid/o-saveData_upperUid-%d_Page-%d.json" % (uid_upper, page_tag)
        # 这是保存在本地的网页文件的名字或者是位置。
        save_page_content(data_download, name_local_doc)  # 使用函数，保存页的内容。
        print(Lang.lc_bre_01, page_tag)  # 打印页面号码。

        if not data_usability_test(name_local_doc, "v"):  # 调用检测每一页是否有评论的函数，决定是跳过或是中断。

            print(Lang.lc_opt_03)
            print("━" * 65)
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

                print("━" * 65)
                need_help()
                print("━" * 65)

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

                print(Lang.lc_opt_04)
                print("━" * 65)
                break

        page_tag += 1  # 下一个页面。
        time.sleep(0.4 + (secrets.randbelow(3000) / 10000))    # 生成随机0.50-1.00秒以内的数字。。


def get_full_follow(uid_upper):  # 这个函数， 检测这个用户关注的所有用户。

    page_tag = 1
    break_tag = 0

    while True:

        url = "https://api.bilibili.com/x/relation/followings?vmid=%d&pn=%d" % (uid_upper, page_tag)
        data_download = get_single_page(url)  # 使用函数获得页的内容，再给到data_download。
        name_local_doc = "./cache/followuid/o-saveData_followUid-%d_Page-%d.json" % (uid_upper, page_tag)
        # 这是保存在本地的网页文件的名字或者是位置。
        save_page_content(data_download, name_local_doc)  # 使用函数，保存页的内容。

        print(Lang.lc_bre_02, page_tag)  # 打印页面号码。

        if not data_usability_test(name_local_doc, "f"):  # 调用检测每一页是否有评论的函数，决定是跳过或是中断。

            print(Lang.lc_opt_03)
            print("━" * 65)
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

                print("━" * 65)
                need_help()
                print("━" * 65)

                get_full_video(data_mid)

            if break_tag == 1:

                print(Lang.lc_opt_03)
                print("━" * 65)
                break

        page_tag += 1  # 下一个页面。
        time.sleep(0.4 + (secrets.randbelow(3000) / 10000))    # 生成随机0.50-1.00秒以内的数字。。


def boot_func():

    what_day()

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
# 输入模式(p / v / f)：

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#    ____                                     _        ____  _ _
#  / ___|___  _ __ ___  _ __ ___   __ _  ___| |_     | __ )(_) |
# | |   / _ \| '_ ` _ \| '_ ` _ \ / _` |/ _ \ __|____|  _ \| | |
# | |__| (_) | | | | | | | | | | | (_| |  __/ ||_____| |_) | | |
#  \____\___/|_| |_| |_|_| |_| |_|\__, |\___|\__|    |____/|_|_|
#                                 |___/
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#       欢迎使用这个程序!请根据提示选择模式!帮助不丹的可怜儿童！
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#    | 单个视频的评论: p | 单个用户的视频:v | 用户关注的用户: f |
#    | 处理表单的评论: p | 单个用户的视频:v | 用户关注的用户: f |
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 输入模式(p / v / f)：

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#    ____                                     _        ____  _ _
#  / ___|___  _ __ ___  _ __ ___   __ _  ___| |_     | __ )(_) |
# | |   / _ \| '_ ` _ \| '_ ` _ \ / _` |/ _ \ __|____|  _ \| | |
# | |__| (_) | | | | | | | | | | | (_| |  __/ ||_____| |_) | | |
#  \____\___/|_| |_| |_|_| |_| |_|\__, |\___|\__|    |____/|_|_|
#                                 |___/
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#       欢迎使用这个程序!请根据提示选择模式!帮助海地的游击队员！
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#    | 单个视频的评论: p | 单个用户的视频: v | 用户关注的用户: f |
#    | 保存表单的评论: s | 分析表单的内容: r | 退出程序的选项: o |
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 输入模式(p / v / f / s / r / o)：

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#    ____                                     _        ____  _ _
#  / ___|___  _ __ ___  _ __ ___   __ _  ___| |_     | __ )(_) |
# | |   / _ \| '_ ` _ \| '_ ` _ \ / _` |/ _ \ __|____|  _ \| | |
# | |__| (_) | | | | | | | | | | | (_| |  __/ ||_____| |_) | | |
#  \____\___/|_| |_| |_|_| |_| |_|\__, |\___|\__|    |____/|_|_|
#                                 |___/
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#       欢迎使用这个程序!请根据提示选择模式!帮助阿联酋的异性恋者！
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#      | 单个视频的评论:p | 单个用户的视频:v | 用户关注的用户:f |
#      | 保存表单的评论:s | 分析表单的内容:r | 清空缓存后退出:o |
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 输入模式(p / v / f / s / r / o)：

    print("━" * 65)

    t_text_1 = Lang.lc_uit_01 + str(need_help(True))
    print("{: ^38s}".format(str(t_text_1)))

    print("━" * 65)

    t_text_2 = Lang.lc_uit_02
    print("{: ^38s}".format(str(t_text_2)))

    t_text_3 = Lang.lc_uit_03
    print("{: ^38s}".format(str(t_text_3)))

    print("━" * 65)

    print(Lang.lc_bre_04, end="")
    ot_input = input()

    if ot_input == "o":

        cache_del()
        time.sleep(1)
        exit()

    print(Lang.lc_bre_06, end="")
    is_custom_database_input = input()

    if is_custom_database_input == "y":

        print("━" * 65)
        print("Host(localhost):", end="")
        database_host = input()
        print("User(root):", end="")
        database_user = input()
        print("Password(root):", end="")
        database_password = input()
        print("Database(PyTest):", end="")
        database_database = input()
        print("━" * 65)

    elif is_custom_database_input == "n":

        print(Lang.lc_opt_01)
        database_host = "localhost"  # 数据库的位置，现在是本地。
        database_user = "root"  # 数据库的用户名。
        database_password = "root"  # 数据库，用户的密码。
        database_database = "PyTest"  # 数据库名，你看着办吧。

    else:

        print(Lang.lc_err_07)

        print("3s_exit()")
        time.sleep(1)
        print("2s_exit()")
        time.sleep(1)
        print("1s_exit()")
        time.sleep(1)

        exit()

    print(Lang.lc_bre_05, end="")
    table_name = input()

    if ot_input == "w":

        print("-" * 30)

        print("下面是表", table_name, "的统计:")

        db_get_what_leve(db_host=database_host, db_user=database_user, db_password=database_password,
                        db_database=database_database, table_name=table_name)
        db_get_what_gend(db_host=database_host, db_user=database_user, db_password=database_password,
                        db_database=database_database, table_name=table_name)

        print("-" * 30)

        exit()

    if ot_input == "p":

        creation_new_tab(database_host, database_user, database_password, database_database)  # 创建一个新表，参数在上面。
        print(Lang.lc_opt_05)

        print(Lang.lc_bre_07, end="")
        temp_p = input()

        print("━" * 65)
        get_full_pages(bv_to_av(temp_p))  # 下载这个视频的全部评论。

    elif ot_input == "v":

        creation_new_tab(database_host, database_user, database_password, database_database)  # 创建一个新表，参数在上面。
        print(Lang.lc_opt_05)

        print(Lang.lc_bre_08, end="")
        temp_v = int(input())

        print("━" * 65)
        get_full_video(temp_v)  # 把这个UP主的所有视频下的评论一起下载。

    elif ot_input == "f":

        creation_new_tab(database_host, database_user, database_password, database_database)  # 创建一个新表，参数在上面。
        print(Lang.lc_opt_05)

        print(Lang.lc_bre_08, end="")
        temp_f = int(input())

        print("━" * 65)
        get_full_follow(temp_f)  # 下载这个用户关注的最后250位用户的全部视频的全部评论。

    elif ot_input == "s":

        save_data_cb(db_host=database_host, db_user=database_user, db_password=database_password, db_database=database_database, table_name=table_name)

    elif ot_input == "r":

        proc_data_cb(db_host=database_host, db_user=database_user, db_password=database_password, db_database=database_database, table_name=table_name)

    else:

        print(Lang.lc_err_08)

        print("3s_exit()")
        time.sleep(1)
        print("2s_exit()")
        time.sleep(1)
        print("1s_exit()")
        time.sleep(1)

        exit()

    print("━" * 65)
    time.sleep(2)


def need_help(is_return=False):  # 帮助！

    f_list = ["乌干达", "刚果", "坦桑尼亚", "赤道几内亚", "阿富汗", "阿塞拜疆", "缅甸", "挪威", "朝鲜",
            "不丹", "保加利亚", "中国", "乍得", "古巴", "加拿大", "海地", "伊朗", "印度",
            "丹麦", "埃塞俄比亚", "日本", "立陶宛", "墨西哥", "波兰", "卡塔尔", "俄罗斯", "罗马尼亚", "南非",
            "瑞士", "叙利亚", "泰国", "美国", "英国", "阿联酋", "越南", "梵蒂冈", "赞比亚", "津巴布韦", "香港",
            "台湾", "索科特拉岛", "南极", "法属圭亚那", "百慕大", "车臣"]

    day_time = int(time.strftime("%m%d", time.localtime()))

    if day_time == 1120:

        s_list = ["跨性别者", ]

    elif day_time == 501:

        s_list = ["民间组织", "政治领袖", "亚洲移民", "美洲移民", "欧洲移民", "无产阶级", "底层农民", "游击队员", "民主人士", "技术工人"]

    else:

        s_list = ["可怜儿童", "少数群体", "国家官员", "民间组织", "残疾警官", "跨性别者", "同性恋者", "异性恋者", "无性恋者", "双性恋者",
                "知识分子", "社会精英", "政治领袖", "非洲移民", "亚洲移民", "美洲移民", "欧洲移民", "基督教徒", "天主教徒", "道教教徒",
                "回教教徒", "无产阶级", "底层农民", "游击队员", "民主人士", "技术工人"]

    main_str = "帮助%s的%s！" % (f_list[random.randint(0, len(f_list) - 1)], s_list[random.randint(0, len(s_list) - 1)])

    if is_return:

        return main_str

    else:

        print(main_str)


def what_day():

    day_init = {
        11: "1912年，中华民国正式成立。",
        14: "1969年，联合国大会第1904号决议通过了《联合国消除一切形式种族歧视宣言》。",
        501: "1886年，芝加哥劳工争取八小时工作制而被警察武装镇压。",
        523: "1943年，共产国际执行委员会主席团公开宣布《解散共产国际的决议》",
        1120: "1998年，Rita Hester被谋杀。",
        1123: "2021年，全斗焕死了。",
        1125: "1936年，日德签订反共产国际协定。",
        1129: "1947年，联大通过了第181号决议。",
        1212: "1979年，全斗焕发动了一场军事政变。",
        1214: "1960年，联大通过了第1514号决议。",
        1225: "1991年，苏联灭亡。",
    }

    day_time = int(time.strftime("%m%d", time.localtime()))

    try:

        # print("━" * 65)
        print(day_init[day_time])
        print("━" * 65)

    except:

        pass

    day_time = int(time.strftime("%m%d", time.localtime()))

    if day_time == 1120:

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


def db_get_full(db_host="localhost", db_user="root", db_password="root", db_database="PyTest", table_name="bilcome"):  # 这个函数是用来获取数据库的全部。

    # database_host = "localhost"  # 数据库的位置，现在是本地。
    # database_user = "root"  # 数据库的用户名。
    # database_password = "root"  # 数据库，用户的密码。
    # database_database = "PyTest"  # 数据库名，你看着办吧。
    # table_name = "simanan"  # 表单名称，建议修改。

    # database_ ==> db_

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

        database.close()
        return database_results

    except:  # 异常子句过于宽泛？好吧，我觉得还行吧。

        print(Lang.lc_err_02)

        database.close()
        return 0


def db_get_comm(db_host="localhost", db_user="root", db_password="root", db_database="PyTest", table_name="bilcome"):

    temp_data_list = []  # 把获得到的所有数据存到这个列表里。

    database_results = db_get_full(db_host=db_host, db_user=db_user, db_password=db_password, db_database=db_database, table_name=table_name)

    for database_row in database_results:
        temp_data_list.append(str(database_row[5]))

    return temp_data_list


def db_get_gend(db_host="localhost", db_user="root", db_password="root", db_database="PyTest", table_name="bilcome"):

    temp_data_list = []  # 把获得到的所有数据存在这个列表里。

    database_results = db_get_full(db_host=db_host, db_user=db_user, db_password=db_password, db_database=db_database, table_name=table_name)

    for database_row in database_results:

        temp_data_list.append(str(database_row[1]))

    return temp_data_list


def db_get_leve(db_host="localhost", db_user="root", db_password="root", db_database="PyTest", table_name="bilcome"):

    temp_data_list = []  # 把获得到的所有数据存在这个列表里。

    database_results = db_get_full(db_host=db_host, db_user=db_user, db_password=db_password, db_database=db_database, table_name=table_name)

    for database_row in database_results:

        temp_data_list.append(str(database_row[4]))

    return temp_data_list


def db_get_what_leve(db_host="localhost", db_user="root", db_password="root", db_database="PyTest", table_name="bilcome"):

    what_lever = {"All": 0, 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    k = db_get_leve(db_host=db_host, db_user=db_user, db_password=db_password, db_database=db_database, table_name=table_name)

    try:

        while True:

            leve_pop = k.pop()

            if leve_pop == "0":
                what_lever[0] += 1

            if leve_pop == "1":
                what_lever[1] += 1

            if leve_pop == "2":
                what_lever[2] += 1

            if leve_pop == "3":
                what_lever[3] += 1

            if leve_pop == "4":
                what_lever[4] += 1

            if leve_pop == "5":
                what_lever[5] += 1

            if leve_pop == "6":
                what_lever[6] += 1

            # print(leve_pop)

            what_lever["All"] += 1


    except:

        pass

    # print(what_lever)

    print("-" * 30)

    print("共计评论数:", what_lever["All"])
    print("0 级评论数:", what_lever[0])
    print("1 级评论数:", what_lever[1])
    print("2 级评论数:", what_lever[2])
    print("3 级评论数:", what_lever[3])
    print("4 级评论数:", what_lever[4])
    print("5 级评论数:", what_lever[5])
    print("6 级评论数:", what_lever[6])

    print("-" * 30)

    print("0 级评论比例:", (what_lever[0] / what_lever["All"]))
    print("1 级评论比例:", (what_lever[1] / what_lever["All"]))
    print("2 级评论比例:", (what_lever[2] / what_lever["All"]))
    print("3 级评论比例:", (what_lever[3] / what_lever["All"]))
    print("4 级评论比例:", (what_lever[4] / what_lever["All"]))
    print("5 级评论比例:", (what_lever[5] / what_lever["All"]))
    print("6 级评论比例:", (what_lever[6] / what_lever["All"]))

    # print("-" * 30)


def db_get_what_gend(db_host="localhost", db_user="root", db_password="root", db_database="PyTest", table_name="bilcome"):

    what_lever = {"All": 0, "男": 0, "女": 0, "保密": 0}

    k = db_get_gend(db_host=db_host, db_user=db_user, db_password=db_password, db_database=db_database, table_name=table_name)

    try:

        while True:

            leve_pop = k.pop()

            if leve_pop == "男":
                what_lever["男"] += 1

            if leve_pop == "女":
                what_lever["女"] += 1

            if leve_pop == "保密":
                what_lever["保密"] += 1

            # print(leve_pop)

            what_lever["All"] += 1


    except:

        pass

    # print(what_lever)

    print("-" * 30)

    print("共计评论数:", what_lever["All"])
    print("男 评论数:", what_lever["男"])
    print("女 评论数:", what_lever["女"])
    print("保密 评论数:", what_lever["保密"])

    print("-" * 30)

    print("男 评论比例:", (what_lever["男"] / what_lever["All"]))
    print("女 评论比例:", (what_lever["女"] / what_lever["All"]))
    print("保密 评论比例:", (what_lever["保密"] / what_lever["All"]))

    # print("-" * 30)


def save_data_cb(db_host="localhost", db_user="root", db_password="root", db_database="PyTest", table_name="bilcome"):

    print(Lang.lc_bre_09, end="")
    temp_p = str(input())

    file_name = temp_p + ".cb"

    list_del = ["\n", " ", "。", ".", "，", ",", "[", "]", "{", "}",
                "【", "】", "「", "」", "！", "!", "?", "？", "(", ")", "（", "）", "/", ":", "”", ";",
                "-", "=", "_", "…", "~", "～", "+", "▿", "&", "#", "@", "："]  # 这个是删除的列表。

    y = 0  # 这个是用来判断的。

    file_dic = open(file_name, "w+")  # 这句用来读取文件。
    next_str = file_dic.read()

    # print(next_str)
    #
    # time.sleep(4)

    # global tab_data

    # tab_data = json.loads(next_str)
    # # print(next_dic)
    # file_dic.close()

    try:

        tab_data = json.loads(next_str)
        # print(next_dic)
        file_dic.close()

    except:

        file_dic.close()

        file_dic = open(file_name, "w+")  # 这句用来读取文件。

        new_cb_file = "{}"
        file_dic.write(new_cb_file)

        file_dic.close()

        file_dic = open(file_name, "r")  # 这句用来读取文件。
        next_str = file_dic.read()

        tab_data = json.loads(next_str)
        # print(next_dic)
        file_dic.close()

        pass

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

    for list_str in db_get_comm(db_host, db_user, db_password, db_database, table_name):  # 列表里的每一个人字符串。

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

        # con_tab = False
        # temp_data_int = 0


        # for break_str in break_list:
        #     try:
        #
        #         temp_data_int += (float((int(tab_data[break_str]["a"]) + 0.000000001) / int(tab_data["_commin_"]["a"])) * 100) - (float((int(tab_data[break_str]["o"]) + 0.000000001) / int(tab_data["_commin_"]["o"])) * 100)
        #         # --------------------------------------------
        #
        #     except:
        #
        #         con_tab = True
        #
        #         break
        #
        # if not con_tab:
        #
        #     if temp_data_int >= 0.8:
        #
        #         for break_str in break_list:
        #
        #             tab_data["_commin_"]["a"] = tab_data["_commin_"]["a"] + 1
        #             tab_data[break_str]["a"] = tab_data[break_str]["a"] + 1
        #
        #             print("PA")
        #
        #             # tab_data[break_str] = float(tab_data[break_str]) + 0.1
        #             # print("HELLO")
        #
        #         print(temp_data_int)
        #         print("Con_Tab Running+")
        #
        #     elif temp_data_int <= -0.8:
        #
        #         for break_str in break_list:
        #
        #             tab_data["_commin_"]["o"] = tab_data["_commin_"]["o"] + 1
        #             tab_data[break_str]["o"] = tab_data[break_str]["o"] + 1
        #
        #             print("NE")
        #
        #             # tab_data[break_str] = float(tab_data[break_str]) + -0.1
        #
        #         print(temp_data_int)
        #         print("Con_Tab Running-")
        #
        #     else:
        #
        #         print("Con_Tab")
        #
        #     file_dic = open("file_dic.cb", "w+")
        #
        #     file_dic.write(json.dumps(tab_data))
        #
        #     file_dic.close()
        #
        #     file_dic = open("file_dic.cb", "r")
        #
        #     next_str = file_dic.read()
        #     tab_data = json.loads(next_str)
        #     # print(next_dic)
        #
        #     file_dic.close()
        #
        #     continue
        #
        # if con_tab:
        #     pass

        # print("这是正常的评论(y/n/p):", end="")
        # c_input = input()

        # ------------------------------------------------------------

        c_input = "n"

        # ------------------------------------------------------------

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

    file_dic = open(file_name, "w+")

    file_dic.write(json.dumps(tab_data))

    file_dic.close()

    # print(tab_data)


def proc_data_cb(db_host="localhost", db_user="root", db_password="root", db_database="PyTest", table_name="GCZW"):

    # print(temp_data_list)

    print(Lang.lc_bre_10, end="")
    temp_p = str(input())

    print("━" * 65)

    file_name = temp_p + ".cb"

    list_del = ["\n", " ", "。", ".", "，", ",", "[", "]", "{", "}",
                "【", "】", "「", "」", "！", "!", "?", "？", "(", ")", "（", "）", "/", ":", "”", ";",
                "-", "=", "_", "…", "~", "～", "+", "▿", "&", "#", "@", "："]  # 这个是删除的列表。

    y = 0  # 这个是用来判断的。

    all_data_int = 0
    all_data_cunt = 0

    file_dic = open(file_name, "r")  # 这句用来读取文件。
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

    for list_str in db_get_comm(db_host, db_user, db_password, db_database, table_name):  # 列表里的每一个人字符串。

        # print(tab_data)

        temp_data_str = ""  # 清空零食数据字符串。

        # print(list_str)

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

        for break_str in break_list:

            # print(tab_data[break_str]["a"])
            # print(tab_data["_commin_"]["a"])
            # print(tab_data[break_str]["o"])
            # print(tab_data["_commin_"]["o"])

            # print(
            # float((int(tab_data[break_str]["a"]) + 0.0001) / int(tab_data["_commin_"]["a"])) * 10
            # -
            # float((int(tab_data[break_str]["o"]) + 0.0001) / int(tab_data["_commin_"]["o"])) * 10
            # )

            # temp_data_int += (float((int(tab_data[break_str]["a"]) + 0.000000001) /
            # int(tab_data["_commin_"]["a"])) * 100)
            # - (float((int(tab_data[break_str]["o"]) + 0.000000001) / int(tab_data["_commin_"]["o"])) * 100)

            # print(tab_data)

            low = 0.0000000000000000000000000000000001

            try:

                temp_data_int += (float((int(tab_data[break_str]["a"]) + low) / int(tab_data["_commin_"]["a"])) * 100) - (float((int(tab_data[break_str]["o"]) + low) / int(tab_data["_commin_"]["o"])) * 100)
                # --------------------------------------------

            except:

                try:

                    if tab_data["_commin_"]["a"] == 0:

                        temp_data_int += 0 - (float((int(tab_data[break_str]["o"]) + low) / float(int(tab_data["_commin_"]["o"]) + low)) * 100)

                    if tab_data["_commin_"]["o"] == 0:

                        temp_data_int += (float((int(tab_data[break_str]["a"]) + low) / float(int(tab_data["_commin_"]["a"]) + low)) * 100) - 0

                    # temp_data_int += (float((int(tab_data[break_str]["a"]) + low) /
                    # float(int(tab_data["_commin_"]["a"]) + low)) * 100) -
                    # (float((int(tab_data[break_str]["o"]) + low) / float(int(tab_data["_commin_"]["o"]) + low)) * 100)

                    # --------------------------------------------

                    # print(float(int(tab_data[break_str]["a"]) + 0.000000001))
                    # print(float(tab_data["_commin_"]["a"])) * 100 + 0.000000001)
                    # print(tab_data[break_str]["o"])
                    # print(tab_data["_commin_"]["o"])
                    # print("-----------")

                except:

                    con_tab = True

                    print(Lang.lc_err_02)

                    break

            print("--"*10)
            print((float((int(tab_data[break_str]["a"]) + low) / float(int(tab_data["_commin_"]["a"]) + low)) * 100))
            print((float((int(tab_data[break_str]["o"]) + low) / float(int(tab_data["_commin_"]["o"]) + low)) * 100))
            print(temp_data_int)
            print("--" * 10)

        # print(temp_data_int)

        all_data_int += temp_data_int
        all_data_cunt += 1

        # if not con_tab:
        #
        #     if temp_data_int >= 0.8:
        #
        #         pass
        #
        #         # for break_str in break_list:
        #         #
        #         #     tab_data["_commin_"]["a"] = tab_data["_commin_"]["a"] + 1
        #         #     tab_data[break_str]["a"] = tab_data[break_str]["a"] + 1
        #         #
        #         #     print("PA")
        #         #
        #         #     tab_data[break_str] = float(tab_data[break_str]) + 0.1
        #         #     print("HELLO")
        #         #
        #         # print(temp_data_int)
        #         # print("Con_Tab Running+")
        #
        #     elif temp_data_int <= -0.8:
        #
        #         pass
        #
        #         # for break_str in break_list:
        #         #
        #         #     tab_data["_commin_"]["o"] = tab_data["_commin_"]["o"] + 1
        #         #     tab_data[break_str]["o"] = tab_data[break_str]["o"] + 1
        #         #
        #         #     print("NE")
        #         #
        #         #     tab_data[break_str] = float(tab_data[break_str]) + -0.1
        #
        #         # print(temp_data_int)
        #         # print("Con_Tab Running-")
        #
        #     else:
        #
        #         pass
        #
        #         # print("Con_Tab")
        #
        #     file_dic = open("file_dic.cb", "w+")
        #
        #     file_dic.write(json.dumps(tab_data))
        #
        #     file_dic.close()
        #
        #     file_dic = open("file_dic.cb", "r")
        #
        #     next_str = file_dic.read()
        #     tab_data = json.loads(next_str)
        #     # print(next_dic)
        #
        #     file_dic.close()
        #
        #     continue

        # if con_tab:
        #
        #     pass

        # print("这是正常的评论(y/n/p):", end="")
        # c_input = input()

        # # ------------------------------------------------------------
        #
        # c_input = "y"
        #
        # # ------------------------------------------------------------

        # print("分词输出", break_list)
        # print("="*300)

        # for break_str in break_list:
        #
        #     if c_input == "y":
        #
        #         try:  # 把现有的字典里的东西增加。
        #
        #             tab_data["_commin_"]["a"] = tab_data["_commin_"]["a"] + 1
        #
        #         except:  # 现有字典没有的话，就新建一个字典的条目。
        #
        #             tab_data["_commin_"] = {"a": 1, "o": 0}
        #
        #         # ------------------------------
        #
        #         try:  # 把现有的字典里的东西增加。
        #
        #             tab_data[break_str]["a"] = tab_data[break_str]["a"] + 1
        #
        #         except:  # 现有字典没有的话，就新建一个字典的条目。
        #
        #             tab_data[break_str] = {"a": 1, "o": 0}
        #
        #     if c_input == "n":
        #
        #         try:  # 把现有的字典里的东西增加。
        #
        #             tab_data["_commin_"]["o"] = tab_data["_commin_"]["o"] + 1
        #
        #         except:  # 现有字典没有的话，就新建一个字典的条目。
        #
        #             tab_data["_commin_"] = {"a": 0, "o": 1}
        #
        #         # ------------------------------
        #
        #         try:  # 把现有的字典里的东西增加。
        #
        #             tab_data[break_str]["o"] = tab_data[break_str]["o"] + 1
        #
        #         except:  # 现有字典没有的话，就新建一个字典的条目。
        #
        #             tab_data[break_str] = {"a": 0, "o": 1}
        #
        #     if c_input == "p":
        #         pass

    print("━" * 65)

    print(all_data_int)
    print(all_data_cunt)
    print(all_data_int / all_data_cunt)

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #   ____                                     _        ____  _ _ _
    #  / ___|___  _ __ ___  _ __ ___   __ _  ___| |_     | __ )(_) | |
    # | |   / _ \| '_ ` _ \| '_ ` _ \ / _` |/ _ \ __|____|  _ \| | | |
    # | |__| (_) | | | | | | | | | | | (_| |  __/ ||_____| |_) | | |_|
    #  \____\___/|_| |_| |_|_| |_| |_|\__, |\___|\__|    |____/|_|_(_)
    #                                 |___/
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #     欢迎使用这个程序!请根据提示选择模式!帮助香港的可怜儿童！
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #    |单个视频的评论:p|单个用户的视频:v|用户关注的用户:f|
    #    |保存表单的评论:s|分析表单的内容:r|退出程序的选项:o|
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 输入模式(p/v/f/s/r/o)：r
    # 输入一个需要处理的表名(str)：XY
    # 需要自定义数据库连接吗(y/n)：n
    # 使用默认设置。
    # 请输入你要对比的表单(str):XY
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # Building prefix dict from the default dictionary ...
    # Loading model from cache /XXX/XXXIX/XX/XXXIXeXXXIX_374895m342gn/T/jieba.cache
    # Loading model cost 0.319 seconds.
    # Prefix dict has been built successfully.
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 48475809.78273264
    # 31411
    # 1543.2749604512
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


def cache_del():
    av_full_file = os.listdir(path="cache/av")
    fo_full_file = os.listdir(path="cache/followuid")
    up_full_file = os.listdir(path="cache/upperuid")

    for i in range(len(av_full_file)):

        av_pop = av_full_file.pop()

        if not av_pop == "这里存放着文件":
            os.remove("cache/av/%s" % av_pop)

    for i in range(len(fo_full_file)):

        fo_pop = fo_full_file.pop()

        if not fo_pop == "这里存放着文件":
            os.remove("cache/followuid/%s" % fo_pop)

    for i in range(len(up_full_file)):

        up_pop = up_full_file.pop()

        if not up_pop == "这里存放着文件":
            os.remove("cache/upperuid/%s" % up_pop)

    print(Lang.lc_opt_04)


# main.
if __name__ == '__main__':      # 这个是程序开始运行的地方。

    boot_func()
    pass

    # what_day()
    # boot_func()
    #
    # pass

    # database_host = "localhost"     # 数据库的位置，现在是本地。
    # database_user = "root"          # 数据库的用户名。
    # database_password = "root"      # 数据库，用户的密码。
    # database_database = "PyTest"    # 数据库名，你看着办吧。

    # table_name = "KK-LL-MM-JJ"    # 表单名称，建议修改。

    # creation_new_tab(database_host, database_user, database_password, database_database)  # 创建一个新表，参数在上面。

    # get_full_follow(123456789)  # 下载这个用户关注的最后250位用户的全部视频的全部评论。
    # get_full_video(123456789)  # 把这个UP主的所有视频下的评论一起下载。
    # get_full_pages(bv_to_av("BVXNe"))  # 下载这个视频的全部评论。

# 已过时==>
# 上面的第一条主色调的就是创建一个新表，然后参数的话就在上面。
# 然后第二条就是把这个用户的所有视频里的评论都存到数据库里，然后这个数据库就是顶上的参数的那个数据库。
# 然后第三个这个指令，就是把这一个视频里所有的评论添加到你顶上的那个数据库里。
# 上面的表名记得改：data_process_and_save(data_file_tag)这个里面的
# 好吧，我在说什么，好怪欧。。。

