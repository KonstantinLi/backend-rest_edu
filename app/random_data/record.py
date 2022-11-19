from .user import User
from .category import Category


class Record:
    __id_counter = 0

    def __init__(self, user_id, category_id, date, pay):
        Record.__id_counter += 1

        self.__id = Record.__id_counter
        self.__user = user_id
        self.__category = category_id
        self.__date = date.strftime("%b %d, %Y %X")
        self.__pay = pay

    def get_id(self):
        return self.__id

    def get_user(self):
        return self.__user

    def get_category(self):
        return self.__category

    def get_date(self):
        return self.__date

    def get_pay(self):
        return self.__pay

    def __str__(self):
        return self.__user + "-" \
               + self.__category \
               + "{id=" + str(self.__id) \
               + ", date=" + str(self.__date) \
               + ", pay=" + str(self.__pay) + "}"

    def serialize(self):
        return {"id": self.__id,
                "user_id": self.__user,
                "category_id": self.__category,
                "date": self.__date,
                "pay": self.__pay}
