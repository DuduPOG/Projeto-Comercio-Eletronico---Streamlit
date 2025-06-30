from datetime import datetime
import json

class Venda:

    def __init__(self, id):
        self.set_id(id)
        self.set_data(datetime.now())
        self.set_carrinho(True)
        self.set_total(0)
        self.set_id_cliente(id_cliente=0)

    def to_json(self):
        return {
            "id": self.get_id(),
            "data": self.get_data().strftime("%d/%m/%Y %H:%M"),
            "carrinho": self.get_carrinho(),
            "total": self.get_total(),
            "id_cliente": self.get_id_cliente()
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
        if not isinstance(carrinho, bool):
            raise ValueError("Carrinho deve ser um valor booleano")
        else:
            self.__carrinho = carrinho

    def get_carrinho(self):
        return self.__carrinho

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


    def __str__(self):
        return f"{self.get_id()} - {self.get_data().strftime('%d/%m/%Y %H:%M')} - {self.get_carrinho()} - {self.get_total()} - {self.get_id_cliente()}"

class Vendas:

    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        if cls.objetos:
            maior = max(item.get_id() for item in cls.objetos)
            obj.set_id(maior + 1)
        else:
            obj.set_id(0)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendas.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    c = Venda(dic["id"])
                    c.set_data(datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
                    c.set_carrinho(dic["carrinho"])
                    c.set_total(dic["total"])
                    c.set_id_cliente(dic["id_cliente"])
                    cls.objetos.append(c)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump([obj.to_json() for obj in cls.objetos], arquivo)