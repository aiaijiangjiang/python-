def show_manager(username):
    # with open('../file/student.txt', 'r', encoding='utf8') as stream:
    #     # d = stream.read() % username
    from 学生管理.file_manager import file_manager_1
    stream = file_manager_1.reder_file('student.txt')
    d = stream.format(username)
    print(d)


if __name__ == '__main__':
    a = input('输入用户:')
    show_manager(a)
