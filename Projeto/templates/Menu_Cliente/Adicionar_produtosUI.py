import streamlit as st
import pandas as pd
from view import View
import time

class Adicionar_produtos:

    @staticmethod
    def main(carrinho):
        st.header("Adicionar Produtos ao Carrinho")

        produtos = View.produto_listar()

        
        op = st.selectbox("Selecione o Produto:", produtos)
        quantidade = st.number_input("Digite a quantidade dos produtos:")

        if st.button("Adicionar"):
            View.inserir_no_carrinho(carrinho, op.get_id(), quantidade)
                    
            st.success("produto adicionado com sucesso!")
            time.sleep(2)
            st.rerun()

   