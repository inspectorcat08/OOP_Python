class Employee(object):
    clear = open('emails.txt', 'w')
    clear.close()

    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary
        self.emails_check()

    def work(self):
        return "I come to the office."

    def check_salary(self, days):
        return f"{self.name}'s salary for {days} months will be {self.salary * days}$"

    def save_email(self):
        file = open('emails.txt', 'a+')
        file.write(f"{self.__class__.__name__} {self.name}: {self.email}\n")
        file.close()

    def emails_check(self):
        file = open('emails.txt', 'r+').read()
        if self.email in file:
            raise ValueError(f'This email "{self.email}" is already in use')
        elif self.email not in file:
            self.save_email()


class Recruiter(Employee):

    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.name)


class Programmer(Employee):

    def work(self):
        return "I come to the office and start to coding."

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.name)


class Candidate(object):

    def __init__(self, full_name, email, technologies,
                 main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def work(self):
        raise UnableToWorkException("I’m not hired yet, lol.")

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.full_name)


class Vacancy(object):

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.title)

class UnableToWorkException(Exception):
    pass

