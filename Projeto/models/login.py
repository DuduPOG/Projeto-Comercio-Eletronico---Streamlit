import json
from models.Modelo import CRUD

class Login:
    def __init__(self, id, user, password):
        self.set_id(id)
        self.set_user(user)
        self.set_password(password)

    def to_json(self):
        return {
            "id": self.get_id(),
            "user": self.get_user(),
            "password": self.get_password()
        }

    def set_id(self, id):
        if id < 0 or id == "":
            raise ValueError("ID não pode ser negativo nem vazio")
        else:
            self.__id = id

    def get_id(self):
        return int(self.__id)

    def set_user(self, user):
        if user == "":
            raise ValueError("Usuário não pode ser vazio")
        else:
            self.__user = user

    def get_user(self):
        return self.__user

    def set_password(self, password):
        if password == "":
            raise ValueError("Senha não pode ser vazia")
        else:
            self.__password = password

    def get_password(self):
        return self.__password

    def __str__(self):
        return f"{self.__id} - {self.__user} - {self.__password}"

class Logins(CRUD):

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:    
            with open("logins.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    c = Login(dic["id"], dic["user"], dic["password"])
                    cls.objetos.append(c)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("logins.json", mode="w") as arquivo:
            json.dump([obj.to_json() for obj in cls.objetos], arquivo)