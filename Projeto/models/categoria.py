import json
from models.Modelo import CRUD

class Categoria:

    def __init__(self, id, desc):
        self.set_id(id)
        self.set_desc(desc)

    def to_json(self):
        return {
            "id": self.get_id(),
            "desc": self.get_desc()
        }

    def set_id(self, id):
        if id < 0 or id == "":
            raise ValueError("ID não pode ser negativo nem vazio")
        else:
            self.__id = id

    def get_id(self):
        return int(self.__id)

    def set_desc(self, desc):
        if desc == "":
            raise ValueError("Descrição não pode ser vazia")
        else:
            self.__desc = desc

    def get_desc(self):
        return self.__desc

    def __str__(self):
        return f"{self.__id} - {self.__desc}"

class Categorias(CRUD):

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("categorias.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    c = Categoria(dic["id"], dic["desc"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump([obj.to_json() for obj in cls.objetos], arquivo)