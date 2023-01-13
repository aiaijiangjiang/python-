from 学生管理.file_manager import file_manager_1


def login():
    a = input('请输入你的username:')

    content = file_manager_1.read_json('teacher.json', {})
    if a not in content:
        print('登录失败，账户username不正确')
        return

    b = input('请输入你的密码：')
    from 学生管理.file_manager import tools
    if content[a] == tools.Password(b):
        print('登录成功')
        from 学生管理.student_manager import change_page
        change_page.change_page(a)

    else:
        print('登录失败')


if __name__ == '__main__':
    login()
