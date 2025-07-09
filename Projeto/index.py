import streamlit as st
from view import View
from templates.Menu_Admin.mantercategoriaui import ManterCategoriaUI
from templates.Menu_Admin.manterclienteui import ManterClienteUI
from templates.Menu_Admin.manterprodutoui import ManterProdutoUI
from templates.Menu_Admin.reajustar_preco_produtos import Reajustar_PrecosUI
from templates.Menu_Admin.manterentregadorui import ManterEntregadorUI
from templates.loginUI import LoginUI
from templates.Menu_Cliente.Listar_produtosUI import Listar_produtos
from templates.Menu_Cliente.Adicionar_produtosUI import Adicionar_produtos
from templates.Menu_Cliente.Ver_carrinhoUI import Ver_carrinho
from templates.Menu_Cliente.Fechar_pedidoUI import Fechar_pedido
from templates.Menu_Cliente.Ver_pedidosUI import Ver_pedidos
from templates.Menu_Entregador.listarentregasui import Listar_EntregasUI
from templates.Menu_Entregador.confirmarentregaui import Confirmar_EntregaUI

class IndexUI:


    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        #if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        id_cliente = st.session_state.get('cliente_id')
        if "carrinho_atual" not in st.session_state:
            st.session_state.carrinho_atual = View.iniciar_carrinho(id_cliente)
        carrinho = st.session_state.carrinho_atual
        
        cliente = View.cliente_listar()

        op = st.sidebar.selectbox("Menu", ["Listar Produtos", "Adicionar Produto no Carrinho", "Ver Carrinho", 
                                           "Fechar Pedido", "Ver Meus Pedidos"])
        
        if op == "Listar Produtos": Listar_produtos.main()

        if op == "Adicionar Produto no Carrinho" : Adicionar_produtos.main(carrinho)

        if op == "Ver Carrinho" : Ver_carrinho.main(carrinho)

        if op == "Fechar Pedido" : Fechar_pedido.main(carrinho,id_cliente)

        if op == "Ver Meus Pedidos" : Ver_pedidos.main(cliente)

    def menu_entregador():
        op = st.sidebar.selectbox("Menu", ["Listar Minhas Entregas", "Confirmar Entrega"])
        if op == "Listar Minhas Entregas":
            Listar_EntregasUI.main()
        if op == "Confirmar Entrega":
            Confirmar_EntregaUI.main()

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Categorias", "Cadastro de Clientes", 
                                "Cadastro de Produtos", "Cadastro de Entregadores", "Reajustar Preços", "Listagem de Vendas"])
        
        if op == "Cadastro de Categorias":
            ManterCategoriaUI.main()

        if op == "Cadastro de Clientes":
            ManterClienteUI.main()

        if op == "Cadastro de Produtos":
            ManterProdutoUI.main()
            
        if op == "Cadastro de Entregadores":
            ManterEntregadorUI.main()
    
        if op == "Reajustar Preços":
            Reajustar_PrecosUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()

    def sidebar():
        st.write(st.session_state)
        if "cliente_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["cliente_nome"] == "admin"
            st.sidebar.write(f"Bem vindo(a), " + st.session_state["cliente_nome"])
            if admin:
                IndexUI.menu_admin()
            if st.session_state["cliente_nome"] == "eduardo":
                IndexUI.menu_entregador()
            else:
                IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()
    
    def main():
        # verifica a existe o usuário admin
        View.cadastrar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()