import pymysql
import threading


#  ('残梦希望12', '保密', 'BIO', 329415145, 4, '全都有了', 0, datetime.datetime(2021, 4, 12, 18, 16, 59), 'o-saveData_Av-757572522_Page-67.json')

class Lang:

    lc_err_02 = "err"

def db_get_full(db_host="localhost", db_user="root", db_password="root", db_database="PyTest",table_name="bilcome"):  # 这个函数是用来获取数据库的全部。

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


def db_get_comm(db_host="localhost", db_user="root", db_password="root", db_database="PyTest",table_name="bilcome"):

    temp_data_list = []  # 把获得到的所有数据存在这个列表里。

    database_results = db_get_full(db_host=db_host, db_user=db_user, db_password=db_password, db_database=db_database, table_name=table_name)

    for database_row in database_results:

        temp_data_list.append(str(database_row[5]))

    return temp_data_list


def db_get_gend(db_host="localhost", db_user="root", db_password="root", db_database="PyTest",table_name="bilcome"):

    temp_data_list = []  # 把获得到的所有数据存在这个列表里。

    database_results = db_get_full(db_host=db_host, db_user=db_user, db_password=db_password, db_database=db_database, table_name=table_name)

    for database_row in database_results:

        temp_data_list.append(str(database_row[1]))

    return temp_data_list


def db_get_leve(db_host="localhost", db_user="root", db_password="root", db_database="PyTest",table_name="bilcome"):

    temp_data_list = []  # 把获得到的所有数据存在这个列表里。

    database_results = db_get_full(db_host=db_host, db_user=db_user, db_password=db_password, db_database=db_database, table_name=table_name)

    for database_row in database_results:

        temp_data_list.append(str(database_row[4]))

    return temp_data_list


def db_get_what_leve(db_host="localhost", db_user="root", db_password="root", db_database="PyTest",table_name="bilcome"):

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

    print(what_lever)

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

    print("-" * 30)


def db_get_what_gend(db_host="localhost", db_user="root", db_password="root", db_database="PyTest",table_name="bilcome"):

    what_lever = {"All": 0, "男": 0, "女": 0, "保密": 0}

    k = db_get_gend(db_host=db_host, db_user=db_user, db_password=db_password, db_database=db_database,table_name=table_name)

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

    print(what_lever)

    print("-" * 30)

    print("共计评论数:", what_lever["All"])
    print("男 评论数:", what_lever["男"])
    print("女 评论数:", what_lever["女"])
    print("保密 评论数:", what_lever["保密"])

    print("-" * 30)

    print("男 评论比例:", (what_lever["男"] / what_lever["All"]))
    print("女 评论比例:", (what_lever["女"] / what_lever["All"]))
    print("保密 评论比例:", (what_lever["保密"] / what_lever["All"]))

    print("-" * 30)


if __name__ == '__main__':

    db_get_what_leve(db_host="127.0.0.1", db_user="root", db_password="root", db_database="PyTest",table_name="MDG")

    db_get_what_gend(db_host="127.0.0.1", db_user="root", db_password="root", db_database="PyTest",table_name="MDG")




    # print(db_get_full(db_host="localhost", db_user="root", db_password="root", db_database="PyTest",table_name="bilcome"))
    # # 获得数据库，全部内容。
    #
    # print(db_get_comm(db_host="localhost", db_user="root", db_password="root", db_database="PyTest", table_name="bilcome"))
    # # 获得数据库里的全部评论。
    #
    # print(db_get_gend(db_host="localhost", db_user="root", db_password="root", db_database="PyTest",table_name="bilcome"))
    # # 获得数据库里的全部性别。
    #
    # print(db_get_leve(db_host="localhost", db_user="root", db_password="root", db_database="PyTest",table_name="bilcome"))
    # # 获得数据库里的全部等级。





