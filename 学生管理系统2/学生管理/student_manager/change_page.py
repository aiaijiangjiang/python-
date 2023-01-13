from 学生管理.student_manager import student_function_district
from 学生管理.student_manager.student_function_district.add_student import add_student


def change_page(a):
    while True:
        from 学生管理.student_manager import welcome_file
        welcome_file.show_manager(username=a)
        num = input('请选择1~5里面的数字,进入相应的功能:')
        if num == '1':
            print('进入添加学生页面')
            from 学生管理.student_manager import student_function_district
            add_student(a)
        elif num == '2':
            print('进入查找学生页面')
            from 学生管理.student_manager.student_function_district.show_student import show_student
            show_student(a)
        elif num == '3':
            print('进入修改学生信息页面')
            from 学生管理.student_manager.student_function_district.alter_student import alter_student
            alter_student(a)
        elif num == '4':
            print('进入删除学生页面')
            from 学生管理.student_manager.student_function_district import delete_student
            delete_student.delete_student(a)
        elif num == '5':
            print('返回主页面')
            return
        else:
            print('请重新输入')
            continue


if __name__ == '__main__':
    change_page('3')
