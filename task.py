class Task:
    def __init__(self, id, name, status):
        self.__id = id
        self.__name = name
        self.__status = status
    
    def get_name(self):
        return self.__name
    
    def get_status(self):
        return self.__status
    
    def get_id(self):
        return self.__id
    
    def to_dict(self):
        return {"id": self.__id, "name": self.__name, "status": self.__status}