import json

class VendaItem:

    def __init__(self, id, qtd, preco):
        self.set_id(id)
        self.set_qtd(qtd)
        self.set_preco(preco)
        self.set_id_venda(0)
        self.set_id_produto(0)

    def to_json(self):
        return {
            "id": self.get_id(),
            "qtd": self.get_qtd(),
            "preco": self.get_preco(),
            "id_venda": self.get_id_venda(),
            "id_produto": self.get_id_produto()
        }

    def set_id(self, id):
        if id < 0 or id == "":
            raise ValueError("ID não pode ser negativo nem vazio")
        else:
            self.__id = id

    def get_id(self):
        return int(self.__id)

    def set_qtd(self, qtd):
        if qtd < 0 or qtd == "":
            raise ValueError("Quantidade não pode ser negativa nem vazia")
        else:
            self.__qtd = qtd

    def get_qtd(self):
        return int(self.__qtd)

    def set_preco(self, preco):
        if preco < 0 or preco == "":
            raise ValueError("Preço não pode ser negativo nem vazio")
        else:
            self.__preco = preco

    def get_preco(self):
        return float(self.__preco)

    def set_id_venda(self, id_venda):
        if id_venda < 0 or id_venda == "":
            raise ValueError("ID da venda não pode ser negativo nem vazio")
        else:
            self.__id_venda = id_venda

    def get_id_venda(self):
        return int(self.__id_venda)

    def set_id_produto(self, id_produto):
        if id_produto < 0 or id_produto == "":
            raise ValueError("ID do produto não pode ser negativo nem vazio")
        else:
            self.__id_produto = id_produto

    def get_id_produto(self):
        return int(self.__id_produto)

    def __str__(self):
        return f"{self.get_id()} - {self.get_qtd()} - {self.get_preco()} - {self.get_id_venda()} - {self.get_id_produto()}"

class VendaItens:

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
            with open("vendaitens.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    c = VendaItem(dic["id"], dic["qtd"], dic["preco"])
                    c.set_id_venda(dic["id_venda"])
                    c.set_id_produto(dic["id_produto"])
                    cls.objetos.append(c)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("vendaitens.json", mode="w") as arquivo:
            json.dump([obj.to_json() for obj in cls.objetos], arquivo)