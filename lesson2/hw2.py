class Employee:

    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary

    def work(self):
        return "I come to the office."

    def check_salary(self, days):
        return "Salary for {} days is {}$".format(days,  self.salary * days)


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

recruiter = Recruiter(name = 'Ivan Ivanov', email = 'ivanov@gmail.com', salary = 20)
programmer = Programmer(name = 'Petr Petrov', email = 'petrov@mail.ru', salary = 50)

print(recruiter)
print(recruiter.check_salary(20))

print(programmer)
print(programmer.check_salary(50))