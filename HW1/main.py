from application.salary import calculate_salary
import db.people as db
from datetime import datetime


def main():
    print(datetime.now())
    print(f"Start main.py: {__name__}")
    calculate_salary()
    db.get_employees()


if __name__ == '__main__':
    main()
