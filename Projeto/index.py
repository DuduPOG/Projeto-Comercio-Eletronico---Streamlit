import streamlit as st
from view import View
from templates.mantercategoriaui import ManterCategoriaUI
from templates.manterclienteui import ManterClienteUI
from templates.manterprodutoui import ManterProdutoUI
from templates.manterentregadorui import ManterEntregadorUI
from templates.loginUI import LoginUI

class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        #if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Listar Produtos", "Adicionar Produto no Carrinho", "Ver Carrinho", 
                                           "Fechar Pedido", "Ver Meus Pedidos"])

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