from 学生管理.file_manager import file_manager_1


def show_student(name):
    content = file_manager_1.read_json(name + '.json', {})
    if not content:
        print('你还没有学生哦，请添加学生')
        return
    while True:
        c = input('1.查找所有学生\n2.根据学号查找学生\n3.根据姓名查找学生\n4.退出当前系统\n请输入你的选择:')
        all_student = content.get('all_student', {})  # 获取关键字用get的避免出错
        if c == '1':
            for student in all_student:
                print('学号:{student_sno} 姓名:{student_name} 年龄:{student_age} a:{a}'.format(**student))  # 解压缩字典
            num = content.get('num', {})
            print('一共有NUM个数据:{}'.format(num))
        elif c == '2':
            sno = input('请输入学生的学号:')
            for student in all_student:
                if student['student_sno'] == sno:
                    print('学号:{student_sno} 姓名:{student_name} 年龄:{student_age} a:{a}'.format(**student))
                    break
                else:
                    print('该学号:{}不存在'.format(sno))
                    break

        elif c == '3':
            name = input('请输入学生的姓名:')
            student_name_filter = filter(lambda a: a['student_name'] == name, all_student)
            # filter(function,iterable):根据函数对可迭代对象进行过来，返回filter可迭代对象

            if not list(student_name_filter):  # 注意这是一个可迭代对象，我们要把它转化为静态变量
                print('学生不存在')
            else:
                for i in student_name_filter:
                    print('学号:{student_sno} 姓名:{student_name} 年龄:{student_age} a:{a}'.format(**i))
        elif c == '4':
            return
        else:
            print('请输入正确的选择')
            continue
