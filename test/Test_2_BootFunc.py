# -*- coding = utf-8 -*-
# @Time : 2021-11-18    â°
# @Author : P.B.A.S     ð¥
# @File : Test_2.py     ð«
# @Software : PyCharm   ð¾

import Test_3_NeedHelp
import time

print("â"*65)
print("""  ____                                     _        ____  _ _ 
 / ___|___  _ __ ___  _ __ ___   __ _  ___| |_     | __ )(_) |
| |   / _ \| '_ ` _ \| '_ ` _ \ / _` |/ _ \ __|____|  _ \| | |
| |__| (_) | | | | | | | | | | | (_| |  __/ ||_____| |_) | | |
 \____\___/|_| |_| |_|_| |_| |_|\__, |\___|\__|    |____/|_|_|
                                |___/                         """)
print("â"*65)

print("   æ¬¢è¿ä½¿ç¨è¿ä¸ªç¨åºï¼", end="  ")
print("è¯·æ ¹æ®æç¤ºéæ©æ¨¡å¼ï¼", end=" ")
NeedHelp.need_help()

print("â"*65)

print("ï½åä¸ªè§é¢çè¯è®ºï¼ p ", end="ï½")
print("åä¸ªç¨æ·çè§é¢ï¼ v ", end="ï½")
print("ç¨æ·å³æ³¨çç¨æ·ï¼ f ", end="ï½\n")

print("â"*65)

print("è¾å¥æ¨¡å¼(p/v/f)ï¼", end="")
ot_input = input()
print("è¾å¥ä¸ä¸ªè¡¨å(str)ï¼", end="")
tab_name_input = input()
print("éè¦èªå®ä¹æ°æ®åºè¿æ¥å(y/n)ï¼", end="")
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

    print("ä½¿ç¨é»è®¤è®¾ç½®ã")
    database_host = "localhost"     # æ°æ®åºçä½ç½®ï¼ç°å¨æ¯æ¬å°ã
    database_user = "root"          # æ°æ®åºçç¨æ·åã
    database_password = "root"      # æ°æ®åºï¼ç¨æ·çå¯ç ã
    database_database = "PyTest"    # æ°æ®åºåï¼ä½ ççåå§ã

else:

    print("ERR-è¯·ç¡®è®¤è¾å¥(y/n)ã")
    print("3s_exit()")
    time.sleep(1)
    print("2s_exit()")
    time.sleep(1)
    print("1s_exit()")
    time.sleep(1)
    exit()

if ot_input == "p":

    print("è¾å¥BVå·(str)ï¼")
    temp_p = input()
    get_full_pages(bv_to_av("BVKenenNe"))  # ä¸è½½è¿ä¸ªè§é¢çå¨é¨è¯è®ºã

elif ot_input == "v":

    print("è¾å¥ç¨æ·å·ç (int)ï¼")
    temp_v = input()
    get_full_video(temp_v)  # æè¿ä¸ªUPä¸»çææè§é¢ä¸çè¯è®ºä¸èµ·ä¸è½½ã

elif ot_input == "f":

    print("è¾å¥ç¨æ·å·ç (int)ï¼")
    temp_f = input()
    get_full_follow(temp_f)  # ä¸è½½è¿ä¸ªç¨æ·å³æ³¨çæå250ä½ç¨æ·çå¨é¨è§é¢çå¨é¨è¯è®ºã

else:

    print("ERR-è¯·ç¡®è®¤è¾å¥(p/v/f)ã")
    print("3s_exit()")
    time.sleep(1)
    print("2s_exit()")
    time.sleep(1)
    print("1s_exit()")
    time.sleep(1)
    exit()

print("â"*65)
time.sleep(2)


