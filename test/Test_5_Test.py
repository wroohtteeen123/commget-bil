import json

file_dic = open("file_dic.cb", "r")  # 这句用来读取文件。
next_str = file_dic.read()
tab_data = {}
tab_data = json.loads(next_str)
# print(next_dic)
file_dic.close()

print(tab_data)