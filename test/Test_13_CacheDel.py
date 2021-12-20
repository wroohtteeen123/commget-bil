import os

class Lang:

    lc_opt_04 = "这一步完成了。"


def cache_del():

    av_full_file = os.listdir(path="../cache/av")
    fo_full_file = os.listdir(path="../cache/followuid")
    up_full_file = os.listdir(path="../cache/upperuid")

    for i in range(len(av_full_file)):

        av_pop = av_full_file.pop()

        if not av_pop == "这里存放着文件":

            os.remove("../cache/av/%s" % av_pop)

    for i in range(len(fo_full_file)):

        fo_pop = fo_full_file.pop()

        if not fo_pop == "这里存放着文件":

            os.remove("../cache/followuid/%s" % fo_pop)

    for i in range(len(up_full_file)):

        up_pop = up_full_file.pop()

        if not up_pop == "这里存放着文件":

            os.remove("../cache/upperuid/%s" % up_pop)

    print(Lang.lc_opt_04)

