# -*- coding = utf-8 -*-
# @Time : 2021-11-16    ⏰
# @Author : P.B.A.S     🍥
# @File : Test_3_NeedHelp.py   🫀
# @Software : PyCharm   💾


import random
import time


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


need_help()
