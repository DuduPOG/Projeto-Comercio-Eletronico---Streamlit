from datetime import datetime
import json
from models.Modelo import CRUD

class Venda:

    def __init__(self, id, carrinho, entrega, id_cliente, id_entregador):
        self.set_id(id)
        self.set_data(datetime.now())
        self.set_carrinho(carrinho)
        self.set_entrega(entrega)
        self.set_total(0)
        self.set_id_cliente(id_cliente)
        self.set_id_entregador(id_entregador)

    def to_json(self):
        return {
            "id": self.get_id(),
            "data": self.get_data().strftime("%d/%m/%Y %H:%M"),
            "carrinho": self.get_carrinho(),
            "entrega": self.get_entrega(),
            "total": self.get_total(),
            "id_cliente": self.get_id_cliente(),
            "id_entregador": self.get_id_entregador()
        }

    def set_id(self, id):
        if id < 0 or id == "":
            raise ValueError("ID não pode ser negativo nem vazio")
        else:
            self.__id = id

    def get_id(self):
        return int(self.__id)

    def set_data(self, data):
        if not isinstance(data, datetime):
            raise ValueError("Data deve ser um objeto datetime")
        else:
            self.__data = data

    def get_data(self):
        return self.__data

    def set_carrinho(self, carrinho):
        if carrinho == False:
            self.__carrinho = carrinho
        else:
            carrinho = True
            if not isinstance(carrinho, bool):
                raise ValueError("Carrinho deve ser um valor booleano")
            else:
                self.__carrinho = carrinho

    def get_carrinho(self):
        return self.__carrinho

    def set_entrega(self, entrega):
        if entrega == True:
            self.__entrega = entrega
        else:
            entrega = False
            if not isinstance(entrega, bool):
                raise ValueError("Entrega deve ser um valor booleano")
            else:
                self.__entrega = entrega

    def get_entrega(self):
        return self.__entrega

    def set_total(self, total):
        if total < 0 or total == "":
            raise ValueError("Total não pode ser negativo nem vazio")
        else:
            self.__total = total

    def get_total(self):
        return float(self.__total)

    def set_id_cliente(self, id_cliente):
        if id_cliente < 0 or id_cliente == "":
            raise ValueError("ID do cliente não pode ser negativo nem vazio")
        else:
            self.__id_cliente = id_cliente

    def get_id_cliente(self):
        return int(self.__id_cliente)
    
    def set_id_entregador(self, id_entregador):
        if id_entregador < 0 or id_entregador == "":
            raise ValueError("ID do cliente não pode ser negativo nem vazio")
        else:
            self.__id_entregador = id_entregador

    def get_id_entregador(self):
        return self.__id_entregador


    def __str__(self):
        return f"{self.get_id()} - {self.get_data().strftime('%d/%m/%Y %H:%M')} - {self.get_carrinho()} - {self.get_entrega()} - {self.get_total()} - {self.get_id_cliente()} - {self.get_id_entregador()}"

class Vendas(CRUD):

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendas.json", mode="r") as arquivo:
                c = json.load(arquivo)
                for dic in c: 
                    c = Venda(dic["id"], dic["carrinho"], dic["entrega"], dic["id_cliente"], dic["id_entregador"])
                    cls.objetos.append(c)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump([obj.to_json() for obj in cls.objetos], arquivo)