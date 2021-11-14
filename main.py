# -*- coding = utf-8 -*-
# @Time : 2021-11-8     ⏰
# @Author : P.B.A.S     🍥
# @File : main.py       🫀
# @Software : PyCharm   💾

# 不要抖机灵！不要耍个性！不要觉得找不到你！🙂

# 已知问题  2021-11-12：
# 连接数据库的时候可能有些问题，有的时候连接不上。(好像又没有这个问题了，啊这🤔
# 如果简介或是发的评论里有英文的半角，单引号就可能会没法储存。
# 我也不知道现在最快的速度应该是几秒，我确实不知道。
# 已知问题  2021-11-13：
# END-还有就是现在数据库的位置，密码还有表格都表名都没办法DIY。
# 保存的表名不能自定义，要怎么写才能用啊！🤔

# 我在想什么 2021-11-12：
# 感觉是不是要加一个直接建表的一个功能。
# 之后的话，其实可以就是把用户的ID复制的时候把用户所有的视频底下的评论都下载下来。
# 感觉差不多能用了，但其实也就不到两百多行。把空格删掉之后还是挺紧凑的。好吧，好像并不是这样。
# 怎么新建数据库啊！
# 我觉得可以直接输入UID获得UPer的所有视频。
# 服了，爆拼写错误，这变量名也不是我写的啊。

# 我在想什么 2021-11-13：
# VSCode真的是什么都能干。
# 🍋🍋🍋🍋🍋🍋🍋🍋🍋
# 好想贴贴（（（（（（
# 测试中！Washouts it call mom

# 我在想什么 2021-11-14：
# 好吧，挂了梯子的话，localhost会变呢。


# import 列表。
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


# 全局取消验证。（其实我也不知道这句话是干嘛的）（反正删掉了就不能用了）（报错怎么办呢）
ssl._create_default_https_context = ssl._create_unverified_context


#   这下面是全局变量。主要是一些空的。
database_host = ""
database_user = ""
database_password = ""
database_database = ""

table_name = ""


# 各种函数。
def get_single_page(page_url):  # 用于获得单个网络页面的函数。

    header_bunker = {
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (Macintosh; Apple silicon Mac OS X 12_1_0) Gecko/20100101 Firefox/94.0"
    }  # 伪装成浏览器，也可以加一些别的。
    page_request = urllib.request.Request(url=page_url, headers=header_bunker)  # 把url地址和头部打包。
    page_data_raw = urllib.request.urlopen(page_request)              # 开个网页，把返回的内容传给page_data_raw。
    page_data_mar = page_data_raw.read()                              # 把网页返回的所有数据读出到page_data_mar。
    page_data_deco = gzip.decompress(page_data_mar).decode("utf-8")   # 将mar的数据解码成utf-8，存到deco。
    return page_data_deco                                             # 将网页解码得到的数据返回给函数。


def get_full_pages(av_pin):

    page_tag = 1

    while True:

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
                    pass

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

        database_do = "INSERT INTO siMaNan(Username, \
            Gender, Bio, UID, Level, SayWhat, ULike, SayTime, FileTag) \
                VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                    (data_username, data_gender, data_bio, data_uid, data_level, data_say_what,
                    data_u_like, data_say_time, data_file_tag)

        try:

            database_cursor.execute(database_do)    # 执行sql语句.
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
    file_content_dict_for_end = json.loads(file_content_str_for_end)    # 把Json文件转换为字典。

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
    database_cursor.execute(database_do)  # 执行命令。

    database_do = "CREATE TABLE %s (Username  VARCHAR(100) NOT NULL, Gender  VARCHAR(100), Bio VARCHAR(500), UID INT UNSIGNED NOT NULL, Level INT UNSIGNED NOT NULL, SayWhat VARCHAR(3000) NOT NULL, ULike INT, SayTime DATETIME NOT NULL, FileTag VARCHAR(500) NOT NULL )" % table_name
    # 命令，长？我也没什么办法。

    database_cursor.execute(database_do)  # 执行命令。
    database.close()  # 关闭数据库。


def get_full_video(uid_upper):
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

                print("-" * 30)

            if break_tag == 1:

                print("BRE-现在应该是完全结束了，我猜是这样，也可能不是这样，我建议你检查一下，好吧，拜拜。")
                break

        page_tag += 1  # 下一个页面。
        time.sleep(0.5 + (secrets.randbelow(40000) / 80000))    # 生成随机0.50-1.00秒以内的数字。。


# main.
if __name__ == '__main__':

    database_host = "localhost"     # 数据库的位置，现在是本地。
    database_user = "root"          # 数据库的用户名。
    database_password = "root"      # 数据库，用户的密码。
    database_database = "PyTest"    # 数据库名，你看着办吧。
    table_name = "simanan"            # 表单名称，建议修改。

    creation_new_tab(database_host, database_user, database_password, database_database)  # 创建一个新表，参数在上面。

    # get_full_video(612492134)  # 把这个UP主的所有视频下的评论一起下载。

    # get_full_pages(bv_to_av("BV1Cg411K7wJ"))  # 下载这个视频的全部评论。

    pass
