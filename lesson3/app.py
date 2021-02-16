from models import Recruiter, Programmer, Candidate, Vacancy


def main():
    recruiter1 = Recruiter('Natali', nata@gmail.com, 20)
    programmer1 = Programmer('Alex', alex@mail.ru, 50)
    programmer2 = Programmer('Roman', roman@gmail.com, 60)
    candidate1 = Candidate('Vasil', vasyok@gmail.com, 'Python')
    candidate2 = Candidate('Grisha', grigor@rambler.ru, 'Python')
    candidate3 = Candidate('Katya', kate@gmail.com, 'FrontEnd')
    vacancy1 = Vacancy('Python')
    vacancy2 = Vacancy('FrontEnd')


if __name__ == '__main__':
    main()
