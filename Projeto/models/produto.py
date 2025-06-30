import json

class Produto:

    def __init__(self, id, desc, preco, estoque, id_categoria):
        self.set_id(id)
        self.set_desc(desc)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_id_categoria(id_categoria)

    def to_json(self):
        return {
            "id": self.get_id(),
            "desc": self.get_desc(),
            "preco": self.get_preco(),
            "estoque": self.get_estoque(),
            "id_categoria": self.get_id_categoria(),
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

    def set_preco(self, preco):
        if preco < 0 or preco == "":
            raise ValueError("Preço não pode ser negativo nem vazio")
        else:
            self.__preco = preco

    def get_preco(self):
        return float(self.__preco)

    def set_estoque(self, estoque):
        if estoque < 0 or estoque == "":
            raise ValueError("Estoque não pode ser negativo nem vazio")
        else:
            self.__estoque = estoque

    def get_estoque(self):
        return int(self.__estoque)

    def set_id_categoria(self, id_categoria):
        if id_categoria < 0 or id_categoria == "":
            raise ValueError("ID da categoria não pode ser negativo nem vazio")
        else:
            self.__id_categoria = id_categoria

    def get_id_categoria(self):
        return int(self.__id_categoria)

    def __str__(self):
        return f"{self.__id} - {self.__desc} - {self.__preco} - {self.__estoque} - {self.__id_categoria}"

class Produtos:

    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        if cls.objetos:
            maior = max(produto.get_id() for produto in cls.objetos)
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
            with open("produtos.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    c = Produto(dic["id"], dic["desc"], dic["preco"], dic["estoque"], dic["id_categoria"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump([obj.to_json() for obj in cls.objetos], arquivo)