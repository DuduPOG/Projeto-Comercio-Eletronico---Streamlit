import json

class Cliente:

    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def to_json(self):
        return {
            "id": self.get_id(),
            "nome": self.get_nome(),
            "email": self.get_email(),
            "fone": self.get_fone(),
            "senha": self.get_senha()
        }

    def set_id(self, id):
        if id < 0 or id == "":
            raise ValueError("ID não pode ser negativo nem vazio")
        else:
            self.__id = id

    def get_id(self):
        return int(self.__id)

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome não pode ser vazio")
        else:
            self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_email(self, email):
        if email == 'admin':
            self.__email = email
        elif "@" not in email or email == "":
            raise ValueError("Email inválido")
        else:
            self.__email = email

    def get_email(self):
        return self.__email

    def set_fone(self, fone):
        if fone == "":
            raise ValueError("Telefone não pode ser vazio")
        else:
            self.__fone = fone

    def get_fone(self):
        return self.__fone
    
    def set_senha(self, senha):
        if senha == "":
            raise ValueError("Senha inválida!")
        else:
            self.__senha = senha

    def get_senha(self):
        return self.__senha

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class Clientes:

    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        if cls.objetos:
            maior = max(cliente.get_id() for cliente in cls.objetos)
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
            with open("clientes.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s:
                    c = Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])
                    cls.objetos.append(c)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump([c.to_json() for c in cls.objetos], arquivo)