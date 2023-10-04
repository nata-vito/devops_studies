class Student:
    def __init__(self) -> None:
        self.student_id = ''
        self.student_plan = ''
        self.student_coins = ''
        self.student_couse = ''
        self.student_courses_qtd = ''
        self.forum = 0


class CoursePlatform:
    def __init__(self) -> None:
        self.coins_to_cripto_rule = 0
        self.users = []
        self.qtd_users = 0
        self.qtd_premium_users = 0
        self.premium_users = []

    def RegisterUser(self, plan='Normal'):
        student = Student()
        student.student_id = self.qtd_users
        self.qtd_users += 1
        student.student_plan = plan
        student.student_coins = 0
        student.student_couse = 0
        student.student_courses_qtd = 1
        self.users.append(student)

        if student.student_plan == 'Premium':
            self.qtd_premium_users += 1
            self.premium_users.append(student)

    def FindPremiumUsers(self):
        premium_users_id = []

        if not self.premium_users:
            return False

        for i in range(len(self.premium_users)):
            premium_users_id.append(self.premium_users[i].student_id)

        return premium_users_id

    def Bonus(self):
        aux = 0
        bonus_usr_id = None

        for i in range(len(self.users)):
            if self.users[i].forum > aux:
                bonus_usr_id = self.users[i].student_id

        if not bonus_usr_id:
            return False

        return bonus_usr_id

    def ScoreToCourse(self, ruler_number):
        if (self.users[0].student_courses_qtd > 0) and (
                self.users[0].student_courses_qtd < ruler_number):
            score = self.users[0].student_courses_qtd - ruler_number
            return score

        return False

    def ScoreToCripto(self, std_coins, cripto_cois_rule):
        student = Student()
        course_platform = CoursePlatform()

        student.student_coins = std_coins
        course_platform.coins_to_cripto_rule = cripto_cois_rule

        if student.student_coins < course_platform.coins_to_cripto_rule:
            return course_platform.coins_to_cripto_rule - student.student_coins

        return False

class Contratar:
    def __init__(self, idade) -> None:
        self.idade = idade
        self.tipo_contrato = None
    
    def ContratarPessoa(self):
        if self.idade < 16:
            return False
        elif self.idade >= 16 and self.idade < 18:
            self.tipo_contrato = 'Meio Periodo'
            return True
        elif self.idade >= 18 and self.idade <= 55:
            self.tipo_contrato = 'integral'
            return True
        elif self.idade > 55:
            return False
        
