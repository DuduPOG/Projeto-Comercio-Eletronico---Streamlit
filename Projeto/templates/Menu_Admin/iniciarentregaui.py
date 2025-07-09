import streamlit as st
import pandas as pd
from view import View
from models.venda import Venda, Vendas
from models.entregador import Entregadores
import time

class Iniciar_EntregaUI:

    @staticmethod
    def main():
        st.header("Iniciar Entrega")
        Iniciar_EntregaUI.listar()

    def listar():
        vendas = Vendas.listar()
        if len(vendas) == 0: 
            st.write("Nenhum pedido criado")
        else:
            try:
                op = st.selectbox("Escolha um pedido para ser iniciado", vendas)
                op1 = st.selectbox("Escolha um Entregador", Entregadores.listar())
                if st.button("Iniciar"):
                    op.set_id_entregador(op1.get_id())
                    st.success("Entrega iniciada com sucesso!")
                    time.sleep(2)
                    st.rerun()
            except ValueError as erro:
                st.error(erro)