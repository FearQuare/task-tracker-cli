class Task:
    def __init__(self, id, name, status, create_date, update_date):
        self.__id = id
        self.__name = name
        self.__status = status
        self.__create_date = create_date
        self.__update_date = update_date
    
    def to_dict(self):
        return {"id": self.__id, "name": self.__name, "status": self.__status, "create-date": self.__create_date, "update-date": self.__update_date}
