from 学生管理.file_manager.file_manager_1 import read_json


def alter_student(name):
    key = value = ''
    first_student_information = read_json(name + '.json', {})
    second_student_information = first_student_information.get('all_student', [])
    if not second_student_information:
        print('请添加学生!!!')
        return
    while True:
        num = input('1.按学生的姓名修改\n2.按学生的学号修改\n3.返回\n请选择:')
        if num == '1':

            key = 'student_name'
            value = input('请输入要修改的学生姓名')
            print('正在按名字查找……')
            break
        elif num == '2':
            key = 'student_sno'
            value = input("请输入要修改学生的学号:")
            print('正在按学号查找……')
            break
        elif num == '3':
            return
        else:
            print('请输入正确的选择:')
    # thired_student_information = list(filter(lambda s: s.get(key, '') == value, second_student_information))
    # if not thired_student_information:
    #     print('没有找到对应的学生')
    #     return
    # for i, s in enumerate(second_student_information):
    #     print('标号：{}学号:{student_sno},姓名:{student_name},年龄:{student_age}'
    #           .format(i, **s))
    # n = input('请输入你要修改的学生的标号（0~{}）.q~返回:'.format(len(second_student_information)))
    # if not n.isdigit() and not 0 <= int(n) <= len(second_student_information):
    #     print('输入的内容{}不合法'.format(n))
    #     return
    # second_student_information.remove(second_student_information[int(n)])
    # student_name = input('请输入修改后学生的名字:')
    # student_sno = input('请输入修改后学生的学号：')
    # student_age = input('请输入修改后学生的年龄：')
    # from 学生管理.file_manager import model
    # s = model.Student(student_sno, student_name, student_age)
    # second_student_information.append(s.__dict__)
    # first_student_information['all_student'] = second_student_information
    # first_student_information['num'] = first_student_information['num']
    # from 学生管理.file_manager.file_manager_1 import wirter_json
    # wirter_json(name + '.json', first_student_information)
    thired_student_information = list(filter(lambda s: s.get(key, '') == value, second_student_information))
    if not thired_student_information:
        print('没有找到对应的学生')
        return
    for i, s in enumerate(second_student_information):
        print('标号：{}学号:{student_sno},姓名:{student_name},年龄:{student_age}'
              .format(i, **s))
    n = input('请输入你要修改的学生的标号（0~{}）.q~返回:'.format(len(second_student_information)))
    if not n.isdigit() and not 0 <= int(n) <= len(second_student_information):
        print('输入的内容{}不合法'.format(n))
        return
    if value == thired_student_information:
        second_student_information.remove(second_student_information[int(n)])
        student_name = input('请输入修改后学生的名字:')
        student_sno = input('请输入修改后学生的学号：')
        student_age = input('请输入修改后学生的年龄：')
        from 学生管理.file_manager import model
        s = model.Student(student_sno, student_name, student_age)
        second_student_information.append(s.__dict__)
        first_student_information['all_student'] = second_student_information
        first_student_information['num'] = first_student_information['num']
        from 学生管理.file_manager.file_manager_1 import wirter_json
        wirter_json(name + '.json', first_student_information)
    else:
        print('不允许操作该数据,你与输入的数据不符合')
