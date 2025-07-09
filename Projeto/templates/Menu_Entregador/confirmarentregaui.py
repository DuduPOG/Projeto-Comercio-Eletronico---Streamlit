import streamlit as st
import pandas as pd
from view import View
from models.venda import Venda, Vendas
import time

class Confirmar_EntregaUI:

    @staticmethod
    def main():
        st.header("Confirmar Entrega")
        Confirmar_EntregaUI.confirmacao()

    def confirmacao():
        entregas = Vendas.listar()
        if len(entregas) == 0: 
            st.write("Nenhum pedido finalizado")
        else:
            try:
                op = st.selectbox("Escolha uma entrega para ser confirmada", entregas)
                if st.button("Confirmar"):
                    op.set_entrega(True)
                    st.success("Entrega confirmada com sucesso!")
                    time.sleep(2)
                    st.rerun()
            except ValueError as erro:
                st.error(erro)