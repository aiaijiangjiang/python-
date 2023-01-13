import main
from 学生管理.file_manager import file_manager_1, model
from 学生管理.file_manager.file_manager_1 import read_json


# teacher = {}


# 这样写就有一个问题，每次单独启动的时候数据会被更新

def register():
    teacher = file_manager_1.read_json('teacher.json', {})  # 读取文件
    # default_data=={}
    while True:
        username = input('请输入你的用户名：（3-6）位:')
        if not 3 <= len(username) <= 6:
            print('账户不符合要求')
        else:
            # return  # finish functional
            break  # push out cycle

    while True:
        password = input('please writer your password(6~12)bit:')
        if not 6 <= len(password) <= 12:
            print('password is not clear')

        else:
            break

    print('---------------------')

    # teacher[username] = password  # 往里面加

    # 使用类的模式
    t = model.Teacher(username, password)
    teacher[t.name] = t.password  # 这里已经写入字典了
    print(teacher)
    file_manager_1.wirter_json('teacher.json', teacher)  # 重新写一篇


if __name__ == '__main__':
    register()
