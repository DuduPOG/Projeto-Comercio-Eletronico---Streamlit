import streamlit as st
import pandas as pd
from view import View
import time

class ManterProdutoUI:

    @staticmethod
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    def listar():
        produtos = View.produto_listar()
        if len(produtos) == 0: 
            st.write("Nenhum produto cadastrado")
        else:    
            dic = []
            for obj in produtos: dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome: ")
        preco = st.number_input("Informe seu preço: ")
        estoque = st.number_input("Informe o estoque: ")
        categoria = st.selectbox("Selecione a categoria", View.categoria_listar())
        if st.button("Cadastrar"):
            View.produto_inserir(nome, preco, estoque, categoria.get_id())
            st.success("Produto inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        produtos = View.produto_listar()
        if len(produtos) == 0: 
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de cliente", produtos)
            nome = st.text_input("Informe o novo nome", op.get_desc())
            preco = st.number_input("Informe o novo preço", op.get_preco())
            estoque = st.number_input("Informe o novo estoque", op.get_estoque())
            if st.button("Atualizar"):
                View.produto_atualizar(op.get_id(), nome, preco, estoque, op.get_id_categoria())
                st.success("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        produtos = View.produto_listar()
        if len(produtos) == 0: 
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de produto", produtos)
            if st.button("Excluir"):
                View.produto_excluir(op.get_id())
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()