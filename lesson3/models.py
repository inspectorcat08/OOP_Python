class Employee:

    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    def work(self):
        return "I come to the office."

    def check_salary(self, days):
        return "Salary for {} days is {}$".format(days, self.salary * days)


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

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.full_name)


class Vacancy(object):

    def __init__(self):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level

    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.title)
