from models.cliente import Cliente, Clientes
from models.produto import Produto, Produtos
from models.venda import Venda, Vendas
from models.venda_item import VendaItem, VendaItens
from models.cliente import Cliente, Clientes
from models.categoria import Categoria, Categorias
from models.entregador import Entregador, Entregadores

class View:

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.get_id(), "nome" : c.get_nome()}
        return None

    @staticmethod
    def cadastrar_admin():
        for cliente in Clientes.listar():
            if cliente.get_email() == "admin":
                return
        View.cliente_inserir("admin", "admin", "84911223344","1234")

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        x = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(x)

    @staticmethod
    def cliente_listar():
        return Clientes.listar()

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        cliente = Clientes.listar_id(id)
        if cliente is not None:
            Clientes.excluir(cliente)
        else:
            print("Cliente não encontrado!")
            return
    
    @staticmethod
    def categoria_inserir(desc):
        c = Categoria(0, desc)
        Categorias.inserir(c)

    @staticmethod
    def categoria_excluir(id):
        categoria = Categorias.listar_id(id)
        if categoria is not None:
            Categorias.excluir(categoria)
        else:
            print("Categoria não encontrada!")
            return

    @staticmethod
    def categoria_atualizar(id, desc):
        c = Categoria(id, desc)
        Categorias.atualizar(c)

    @staticmethod
    def categoria_listar():
        return Categorias.listar()
    
    @staticmethod
    def produto_inserir(nome, preco, desc, id_categoria):
        p = Produto(0, nome, preco, desc, id_categoria)
        Produtos.inserir(p)

    @staticmethod
    def produto_excluir(id):
        produto = Produtos.listar_id(id)
        if produto is not None:
            Produtos.excluir(produto)
        else:
            return

    @staticmethod
    def produto_atualizar(id, nome, preco, desc, id_categoria):
        p = Produto(id, nome, preco, desc, id_categoria)
        Produtos.atualizar(p)

    @staticmethod
    def produto_listar():
        return Produtos.listar()
    
    @staticmethod
    def entregador_inserir(id, nome, email, fone, senha):
        e = Entregador(id, nome, email, fone, senha)
        Entregadores.inserir(e)

    @staticmethod
    def entregador_excluir(id):
        entregador = Entregadores.listar_id(id)
        if entregador is not None:
            Entregadores.excluir(entregador)
        else:
            return
        
    @staticmethod
    def entregador_atualizar(id, nome, email, fone, senha):
        e = Entregador(id, nome, email, fone, senha)
        Entregadores.atualizar(e)

    @staticmethod
    def entregador_listar():
        return Entregadores.listar()

    @staticmethod
    def iniciar_carrinho():
        carrinho = Venda(0)
        Vendas.inserir(carrinho)
        return carrinho
    
    @staticmethod
    def listar_carrinho(id):
        for c in Vendas.listar():
            print(c)
    
    @staticmethod
    def visualizar_carrinho(carrinho):
        if carrinho is not None:
            print("O produto vai ser inserido nesse carrinho: ", carrinho)
            for item in VendaItens.listar():
                if item.get_id_venda() == carrinho.get_id():
                    id_produto = item.get_id_produto()
                    produto = Produtos.listar_id(id_produto)
                    if produto is not None:
                        descricao = produto.get_desc()
                        print(f"   {descricao} - Quantidade: {item.get_qtd()} - Preço: R$ {item.get_preco():.2f}")
                    else:
                        descricao = "(Produto não encontrado)"
        else:
            print("Você precisar criar um carrinho primeiro!")
            return
        
    @staticmethod
    def visualizar_meu_carrinho(carrinho):
        itens_no_carrinho = [] 
        if carrinho is not None:
            for item_venda in VendaItens.listar():
                if item_venda.get_id_venda() == carrinho.get_id():
                    id_produto = item_venda.get_id_produto()
                    produto = Produtos.listar_id(id_produto)
                    if produto is not None:
                         itens_no_carrinho.append({
                            "id_item_venda": item_venda.get_id(), 
                            "nome_produto": produto.get_desc(),
                            "preco_unitario": produto.get_preco(),
                            "quantidade": item_venda.get_qtd(),
                            "subtotal_item": item_venda.get_qtd() * float(produto.get_preco())
                        })
        return itens_no_carrinho 
    @staticmethod
    def inserir_no_carrinho(carrinho, id_produto, qtd):
        produto = Produtos.listar_id(id_produto)
        if produto is None:
            return
        preco = float(produto.get_preco())
        vi = VendaItem(0, qtd, preco)
        vi.set_id_venda(carrinho.get_id())
        vi.set_id_produto(id_produto)
        VendaItens.inserir(vi)
        # atualizar o total da venda (carrinho)
        subtotal = qtd * preco
        carrinho.set_total(carrinho.get_total() + subtotal)
        Vendas.atualizar(carrinho)

    @staticmethod
    def listar_minhas_compras(cliente):
        for venda in Vendas.listar():
            if venda.get_id_cliente() == cliente.get_id():
                print(f"Carrinho ID: {venda.get_id()}, Total: R$ {venda.get_total():.2f}, Status: {'Finalizada' if not venda.get_carrinho() else 'Em aberto'}")

    @staticmethod
    def confirmar_compra(carrinho):
        if carrinho is None:
            print("Nenhum carrinho iniciado!")
            return
        carrinho.set_carrinho(False)
        Vendas.atualizar(carrinho)
        for item in VendaItens.listar():
            if item.get_id_venda() == carrinho.get_id():
                produto = Produtos.listar_id(item.get_id_produto())
                if produto is not None:
                    produto.set_estoque(produto.get_estoque() - item.get_qtd())
                    Produtos.atualizar(produto)

    @staticmethod
    def produto_reajustar_preco(produto, novo_preco):
        produto = Produtos.listar_id(produto)
        if produto is not None:
            produto.set_preco(novo_preco)
            Produtos.atualizar(produto)
        else:
            return

    pass
"""
    @staticmethod
    def desconfirmar_compra(carrinho):
        if carrinho.get_carrinho() is True:
            print("Esta compra ainda não foi acabada!")
            return
        carrinho.set_carrinho(True)
        Vendas.atualizar(carrinho)
        for item in VendaItens.listar():
            if item.get_id_venda() == carrinho.get_id():
                produto = Produtos.listar_id(item.get_id_produto())
                if produto is not None:
                    produto.set_estoque(produto.get_estoque() + item.get_qtd())
                    Produtos.atualizar(produto)

    def login_inserir(email, senha):
        l = Login(0, email, senha)
        Logins.inserir(l)


    def login_excluir(id):
        l = Login(id, "", "")
        Logins.excluir(l)


    def login_atualizar(id, email, senha):
        l = Login(id, email, senha)
        Logins.atualizar(l)

    
    def login_listar():
        return Logins.listar()
"""