import streamlit as st
import pandas as pd
from view import View
import time

class Reajustar_PrecosUI:

    @staticmethod
    def main():
        st.header("Reajustar preço dos produtos")
        Reajustar_PrecosUI.listar()

    def listar():
        produtos = View.produto_listar()
        if len(produtos) == 0: 
            st.write("Nenhum produto cadastrado")
        else:
            try:
                dic = []
                for obj in produtos: dic.append(obj.to_json())
                df = pd.DataFrame(dic)
                st.dataframe(df)
                op = st.selectbox("Escolha um produto que queira mudar de preço", produtos)
                novo_preco = st.number_input("Informe o novo preço")
                if st.button("Alterar"):
                    View.produto_reajustar_preco(op.get_id(), novo_preco)
                    st.success("Preço reajustado com sucesso!")
                    time.sleep(2)
                    st.rerun()
            except ValueError as erro:
                st.error(erro)