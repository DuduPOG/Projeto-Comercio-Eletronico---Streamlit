import streamlit as st
from view import View
from templates.mantercategoriaui import ManterCategoriaUI
from templates.manterclienteui import ManterClienteUI
from templates.manterprodutoui import ManterProdutoUI
from templates.manterentregadorui import ManterEntregadorUI
from templates.loginUI import LoginUI
from templates.Listar_produtosUI import Listar_produtos
from templates.Adicionar_produtosUI import Adicionar_produtos
from templates.Ver_carrinhoUI import Ver_carrinho
from templates.Fechar_pedidoUI import Fechar_pedido
from templates.Ver_pedidosUI import Ver_pedidos

class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        #if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        if "carrinho_atual" not in st.session_state:
            st.session_state.carrinho_atual = View.iniciar_carrinho()
        carrinho = st.session_state.carrinho_atual

        op = st.sidebar.selectbox("Menu", ["Listar Produtos", "Adicionar Produto no Carrinho", "Ver Carrinho", 
                                           "Fechar Pedido", "Ver Meus Pedidos"])
        
        if op == "Listar Produtos": Listar_produtos.main()

        if op == "Adicionar Produto no Carrinho" : Adicionar_produtos.main(carrinho)

        if op == "Ver Carrinho" : Ver_carrinho.main(carrinho)

        if op == "Fechar Pedido" : Fechar_pedido.main(carrinho)

        if op == "Ver Meus Pedidos" : Ver_pedidos.main(carrinho)


     
  
        

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Categorias", "Cadastro de Clientes", 
                                "Cadastro de Produtos", "Cadastro de Entregadores", "Listagem de Vendas"])
        
        if op == "Cadastro de Categorias":
            ManterCategoriaUI.main()

        if op == "Cadastro de Clientes":
            ManterClienteUI.main()

        if op == "Cadastro de Produtos":
            ManterProdutoUI.main()
            
        if op == "Cadastro de Entregadores":
            ManterEntregadorUI.main()

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
            else:
                IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()
    
    def main():
        # verifica a existe o usuário admin
        View.cadastrar_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()