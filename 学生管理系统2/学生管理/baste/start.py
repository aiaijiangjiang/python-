# 创建开始文件,用于首页
from 学生管理.baste.login import login
from 学生管理.baste.register import register


def start():
    try:
        with open('../file/start.txt', mode='r', encoding='utf8') as stream:
            content = stream.read()

    except FileNotFoundError:
        print('文件未找到')

    Tage = True
    while Tage:
        a = input(content + '\n请选择（1~3）:')
        if a == '1':
            print('登陆中，请等待')
            login()
        elif a == '2':
            print('请开始你的注册')
            register()
        elif a == '3':
            print('退出')
            Tage = False
        else:
            print('请输入正确的数字')


start()

