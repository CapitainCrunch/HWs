__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400


class Student():

    def __init__(self):
        self.name = ''
        self.surname = ''
        self.middle_name = ''
        self.course = 0
        self.email = []
        self.mobile = ''
        self.rating = 0

    def change_course(self, course):
        if course < self.course:
            raise MyException('У этого студента курс старше!')
        elif course == self.course:
            raise MyException('Этот студент уже обучается на ' + course + 'курсе')
        else:
            self.course = course
        return self.course


class MyException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self, message):
        return self.message

students = []



while True:
    s = Student()
    user_msg = input('Что ты хочешь сделать? Введи цифру\n1. Сменить курс студента\n2. Узнать email студента\n3. Удалить студента из реестра\n\n')
    if user_msg:
        if user_msg != '1':
            print('Я просил цифруууу :(')
            raise MyException('Не тот тип введенных данных')
        else:
            if user_msg == str(1):
                to_course_usr = input('На какой курс перевести студента? Введи цифрой ')
                if not int(to_course_usr):
                    print('Я просил цифруууу :(')
                    raise MyException('Не тот тип введенных данных')
                else:
                    print('Студент ' + s.name + ' переведен на ' + str(s.change_course(int(to_course_usr))) + '\n\n')