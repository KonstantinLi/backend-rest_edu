from .user import User
from .category import Category
from .record import Record
from datetime import datetime
import random


class Creator:

    @staticmethod
    def create_data():
        names = ["Микола", "Костянтин", "Ольга", "Вадим", "Руслан"]
        types = ["Харчові продукти", "Комунальні послуги", "Дозвілля", "Іпотека"]

        def create_user(name):
            return User(name)

        def create_category(category_type):
            return Category(category_type)

        def create_record(user, category, date, pay):
            return Record(user, category, date, pay)

        def write_users(users):
            f = open("users.txt", "w")
            for user in users:
                f.write(user.get_name() + "\n")
            f.close()

        users = [create_user(name) for name in names]
        categories = [create_category(category_type) for category_type in types]
        records = []

        for _ in range(10):
            random_user = random.choice(users)
            random_category = random.choice(categories)
            random_pay = random.randint(100, 2000)

            records.append(create_record(random_user, random_category, datetime.now(), random_pay))

        write_users(users)

        return {"users": users, "categories": categories, "records": records}
