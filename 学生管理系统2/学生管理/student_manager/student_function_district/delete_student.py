from 学生管理.file_manager.file_manager_1 import read_json, wirter_json


def delete_student(name):
    key = value = ''
    first_student_informationn = read_json(name + '.json', {})  # 读取第一轮文件信息
    seconde_student_information = first_student_informationn.get('all_student', [])  # 第二轮数据信息
    if not seconde_student_information:
        print('该老师还没有学生，请添加')
        return
    num = input('1.按照姓名删除\n2.按学号删\n其他:返回\n请选择:')
    if num == '1':
        key = 'student_name'
        value = input('请输入要删除的学生姓名')
    elif num == '2':
        key = 'student_sno'
        value = input('请输入要删除的学生的学号:')
    else:
        return

    third_student_information = list(filter(lambda s: s.get(key, '') == value, seconde_student_information))
    # 第三轮获取信息

    if not third_student_information:
        print("没有找到对应的学生")
        return

    for i, s in enumerate(seconde_student_information):
        print('标号：{}学号:{student_sno},姓名:{student_name},年龄:{student_age}'
              .format(i, **s))
    n = input('请输入需要删除学生的标号（0~{}）,q-返回:'.format(len(seconde_student_information) - 1))
    if not n.isdigit() and not 0 < int(n) <= len(seconde_student_information) - 1:
        print('输入的内容不合法')
        return

    # if n.isdigit():
    #     n = int(n)
    #     if 0 <= n <= len(seconde_student_information):
    #         print('删除')
    #     else:
    #         return

    seconde_student_information.remove(seconde_student_information[(int(n))])
    first_student_informationn['all_student'] = seconde_student_information
    first_student_informationn['num'] = first_student_informationn['num'] - 1
    # print(first_student_informationn)
    wirter_json(name + '.json', first_student_informationn)
