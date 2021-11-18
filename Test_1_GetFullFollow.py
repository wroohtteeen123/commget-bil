# -*- coding = utf-8 -*-
# @Time : 2021-11-16    ⏰
# @Author : P.B.A.S     🍥
# @File : Test_1.py     🫀
# @Software : PyCharm   💾


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
ssl._create_default_https_context = ssl._create_unverified_context  # 全局取消验证。（其实我也不知道这句话是干嘛的（反正删掉了就不能用了（报错怎么办呢
import Test_3_NeedHelp


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

        print("ERR-有点问题，可能是评论区被关闭了，或者是限制了5页的访问。")
        return str(block_page)


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

                # get_full_pages(data_av)
                # get_full_video(data_mid)

            if break_tag == 1:

                print("BRE-现在应该是完全结束了，我猜是这样，也可能不是这样，我建议你检查一下，好吧，拜拜。")
                break

        page_tag += 1  # 下一个页面。
        time.sleep(0.5 + (secrets.randbelow(40000) / 80000))    # 生成随机0.50-1.00秒以内的数字。。

# get_full_follow(289867)
Test_3_NeedHelp.need_help()