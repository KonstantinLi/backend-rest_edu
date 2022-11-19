class Category:
    __id_counter = 0

    def __init__(self, type):
        Category.__id_counter += 1

        self.__id = Category.__id_counter
        self.__type = type

    def get_id(self):
        return self.__id

    def get_type(self):
        return self.__type

    def __str__(self):
        return self.__type + "{" + str(self.__id) + "}"

    def serialize(self):
        return {"id": self.__id,
                "type": self.__type}
