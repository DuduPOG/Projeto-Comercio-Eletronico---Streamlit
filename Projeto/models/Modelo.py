import json
from abc import ABC, abstractmethod

class CRUD(ABC):
    
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
    @abstractmethod
    def abrir(cls):
        pass

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass