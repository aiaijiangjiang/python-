from 学生管理.file_manager import file_manager_1
from 学生管理.file_manager import model


def add_student(name):
    content = file_manager_1.read_json(name + '.json', {})
    if not content:
        student = []
        num = 0
    else:
        student = content['all_student']
        num = int(content['num'])
    while True:
        student_name = input('请输入学生的名字:')
        student_sno = input('请输入学生的学号：')
        student_age = input('请输入学生的年龄：')
        num += 1
        s = model.Student(student_sno, student_name, student_age)
        student.append(s.__dict__)

        data = {'all_student': student, 'num': len(student)}
        print('添加成功')
        file_manager_1.wirter_json(name + '.json', data)
        return
