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
            return User(name).serialize()

        def create_category(category_type):
            return Category(category_type).serialize()

        def create_record(user_id, category_id, date, pay):
            return Record(user_id, category_id, date, pay).serialize()

        def write_users(users):
            f = open("users.txt", "w")
            for user in users:
                f.write(str(user) + "\n")
            f.close()

        users = [create_user(name) for name in names]
        categories = [create_category(category_type) for category_type in types]
        records = []

        for _ in range(10):
            random_user = random.choice(users)
            random_category = random.choice(categories)
            random_pay = random.randint(100, 2000)

            records.append(create_record(random_user["id"], random_category["id"], datetime.now(), random_pay))

        write_users(users)

        return {"users": users, "categories": categories, "records": records}
