class Teacher():
    def __init__(self, name, password):
        from 学生管理.file_manager import tools
        self.name = name
        self.password = tools.Password(password)


class Student():
    def __init__(self, student_sno, student_nam, student_age,a=None):
        self.student_sno = student_sno
        self.student_name = student_nam
        self.student_age = student_age
        self.a=a
