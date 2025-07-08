import streamlit as st
import pandas as pd
from view import View
import time

class Ver_pedidos:

    @staticmethod
    def main(carrinho):
        st.header("Este é o seu carrinho:")
        op = View.listar_minhas_compras
        op = st.selectbox("Selecione o Pedido", produtos)
        quantidade = st.number_input("Digite a quantidade dos produtos:")

        if st.button("Ver pedidos"):
            st.success("produto adicionado com sucesso!")
            time.sleep(2)
            st.rerun() 