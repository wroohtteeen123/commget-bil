# -*- coding = utf-8 -*-
# @Time : 2021-11-14    â°
# @Author : P.B.A.S     ð¥
# @File : Test_0.py     ð«
# @Software : PyCharm   ð¾


# import åè¡¨ã
import pymysql


def count_sig_str(str_input, mode_one):         # è¿ä¸ªå½æ°æ¯ç¨æ¥æ£æµå­ç¬¦ä¸²ééå¤å­çæ°éï¼å¹¶ä¸è½¬æ¢æå­å¸ã

    new_dict = {}           # è¿æ¯è¾å¥çæºå­å¸ã
    all_new_dict = {}       # è¿ä¸ªæ¯æç»çå­å¸ã

    list_input = list(str_input)                # é¦åæè¾å¥çå­ç¬¦ä¸²è½¬æ¢æåè¡¨ãç±äºå¨ä¸ä¸æ­¥å·²ç»å»é¤äºåç§æ ç¹ç¬¦å·ã

    for unu_a in range(0, len(list_input)):     # è¿éçè¯ï¼æ£æµåè¡¨çé¿åº¦éå¤åè¡¨é¿åº¦æ¬¡ã

        srt_one = list_input.pop()              # è¿éä½¿ç¨popæä»¤æ¥ï¼æ¯è¾å¿«éã

        try:        # æç°æçå­å¸éçä¸è¥¿å¢å ã

            new_dict[srt_one] = 1 + int(new_dict[srt_one])

        except:     # ç°æå­å¸æ²¡æçè¯ï¼å°±æ°å»ºä¸ä¸ªå­å¸çæ¡ç®ã

            new_dict[srt_one] = 1

    temp_list = sorted(new_dict.items(), key=lambda x: x[1], reverse=mode_one)  # è¿éæ¯æè¿ä¸ä¸ªä¸è¥¿æåä¸ä¸ã

    for unu_b in temp_list:     # ç±äºä¸ä¸æ­¥æååºæ¥çä¸æ¯å­å¸ï¼è¿è¦æè¿ä¸ªä¸è¥¿è½¬æ¢æå­å¸ã

        all_new_dict[unu_b[0]] = unu_b[1]

    return all_new_dict         # æåæå­å¸è¿ååå»ã

    # for i in k_list:          # è¿ä¸ªä¹è½ç¨ï¼ä¸è¿countçæçå¤ªä½äºï¼ï¼
    #         a = k_list.count(i)
    #         print(a)
    #         temp_srr[i] = k_list.count(i)
    #         for k in range(0, a):
    #               try:
    #             k_list.remove(i)
    #               except:
    #                   print("ERR")
    #                   pass
    #         print(temp_srr)


database_host = "localhost"     # æ°æ®åºçä½ç½®ï¼ç°å¨æ¯æ¬å°ã
database_user = "root"          # æ°æ®åºçç¨æ·åã
database_password = "root"      # æ°æ®åºï¼ç¨æ·çå¯ç ã
database_database = "PyTest"    # æ°æ®åºåï¼ä½ ççåå§ã
table_name = "XY"     # è¡¨ååç§°ï¼å»ºè®®ä¿®æ¹ã

temp_data = []

database = pymysql.connect(

    host=database_host,
    user=database_user,
    password=database_password,
    database=database_database

)  # è¿æ¥æ°æ®åºãæ³¨æå¯ç åæ°æ®åºåã

database_cursor = database.cursor()

database_do = "SELECT * FROM %s" % table_name

# database_do = "SELECT * FROM %s WHERE ULike > %s" % (table_name, 1000)

try:    # å°è¯è¿è¡ã

    database_cursor.execute(database_do)
    database_results = database_cursor.fetchall()

    for database_row in database_results:

        temp_data = str(temp_data) + str(database_row[5])

except:     # å¼å¸¸å­å¥è¿äºå®½æ³ï¼å¥½å§ï¼æè§å¾è¿è¡å§ã

    print("ERR-ææè§åºäºäºé®é¢ï¼")

database.close()

# print(temp_data)

temp_data.replace('\n', '')
temp_data.replace('\r', '')
temp_data_list = list(temp_data)

list_del = ["\n", " ", "ã", ".", "ï¼", ",", "[", "]", "{", "}",
            "ã", "ã", "ã", "ã", "ï¼", "!", "?", "ï¼", "(", ")", "ï¼", "ï¼"]

temp_data_str = ""
y = 0

for i in temp_data_list:

    for k in list_del:

        if str(i) == str(k):

            y = 1

    if y == 1:

        y = 0
        continue

    temp_data_str += str(i)

temp_srr = {}

k_list = list(temp_data_str)

print(count_sig_str(k_list, True))

