class User:
    __id_counter = 0

    def __init__(self, name):
        User.__id_counter += 1

        self.__id = User.__id_counter
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def __str__(self):
        return self.__name + "{" + str(self.__id) + "}"

    def serialize(self):
        return {"id": self.__id,
                "name": self.__name}
