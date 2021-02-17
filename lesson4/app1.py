from models1 import *
from datetime import *
import traceback

def main():
    recruiter1 = Recruiter('Natali', 'nata@gmail.com', 20)

    programmer1 = Programmer('Alex', 'alex@mail.ru', 50)
    programmer2 = Programmer('Roman', 'roman@gmail.com', 60)

    candidate1 = Candidate('Vasil', 'vasyok@gmail.com', 'Python', 'has experience', 'Strong Junior')
    candidate2 = Candidate('Grisha', 'grigor@rambler.ru', 'Python', 'self-taught', 'Strong Junior')
    candidate3 = Candidate('Katya', 'kate@gmail.com', 'FrontEnd', 'not have', 'trainee')
    candidate1.work()
    candidate2.work()
    candidate3.work()


    vacancy1 = Vacancy("FrontEnd programmer", "FrontEnd", "Strong Junior")
    vacancy2 = Vacancy("Python QA tester", "Python", "Strong Junior")


try:
    main()

except ValueError as errEmail:
    logs = open('logs.py', 'a')
    error = traceback.format_exc().splitlines()
    logs.write('{} ValueError, {}, \n'.format(datetime.today(), errEmail))
    logs.close()
except UnableToWorkException as errWork:
    logs = open('logs.py', 'a')
    error = traceback.format_exc().splitlines()
    logs.write('{} UnableToWorkException, {}, \n'.format(datetime.today(), errWork))
    logs.close()

