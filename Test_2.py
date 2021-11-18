import NeedHelp
import time

print("━"*65)
print("""  ____                                     _        ____  _ _ 
 / ___|___  _ __ ___  _ __ ___   __ _  ___| |_     | __ )(_) |
| |   / _ \| '_ ` _ \| '_ ` _ \ / _` |/ _ \ __|____|  _ \| | |
| |__| (_) | | | | | | | | | | | (_| |  __/ ||_____| |_) | | |
 \____\___/|_| |_| |_|_| |_| |_|\__, |\___|\__|    |____/|_|_|
                                |___/                         """)
print("━"*65)

print("   欢迎使用这个程序！", end="  ")
print("请根据提示选择模式！", end=" ")
NeedHelp.need_help()

print("━"*65)

print("｜单个视频的评论： p ", end="｜")
print("单个用户的视频： v ", end="｜")
print("用户关注的用户： f ", end="｜\n")

print("━"*65)

print("输入模式(p/v/f)：", end="")
ot_input = input()
print("输入一个表名(str)：", end="")
tab_name_input = input()
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
    database_host = "localhost"     # 数据库的位置，现在是本地。
    database_user = "root"          # 数据库的用户名。
    database_password = "root"      # 数据库，用户的密码。
    database_database = "PyTest"    # 数据库名，你看着办吧。

else:

    print("ERR-请确认输入(y/n)。")
    print("3s_exit()")
    time.sleep(1)
    print("2s_exit()")
    time.sleep(1)
    print("1s_exit()")
    time.sleep(1)
    exit()

if ot_input == "p":

    print("输入BV号(str)：")
    temp_p = input()
    get_full_pages(bv_to_av("BVKenenNe"))  # 下载这个视频的全部评论。

elif ot_input == "v":

    print("输入用户号码(int)：")
    temp_v = input()
    get_full_video(temp_v)  # 把这个UP主的所有视频下的评论一起下载。

elif ot_input == "f":

    print("输入用户号码(int)：")
    temp_f = input()
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

print("━"*65)
time.sleep(2)


