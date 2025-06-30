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
            for obj in produtos: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome: ")
        desc = st.text_input("Informe a descrição: ")
        preco = st.number_input("Informe seu preço: ")
        estoque = st.number_input("Informe o estoque: ")
        id_categoria = st.selectbox("Selecione a categoria", View.categoria_listar())
        if st.button("Cadastrar"):
            View.produto_inserir(nome, desc, preco, estoque, id_categoria)
            st.success("Produto inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        produto = View.produto_listar()
        if len(produto) == 0: 
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de cliente")
            nome = st.text_input("Informe o novo nome")
            preco = st.number_input("Informe o novo preço")
            estoque = st.number_input("Informe o novo estoque")
            id_categoria = st.selectbox("Selecione a categoria", View.categoria_listar(), index=op.id_categoria)
            if st.button("Atualizar"):
                View.produto_atualizar(op.id, nome, preco, estoque, id_categoria)
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
                View.produto_excluir(op.id)
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()