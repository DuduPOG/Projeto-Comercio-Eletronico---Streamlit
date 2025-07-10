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
        pedidos = Vendas.listar()
        entregas = 0
        entregas_lista = []
        for pedido in pedidos:
            if pedido.get_carrinho() == False:
                entregas += 1
                entregas_lista.append(pedido)
        if entregas == 0: 
            st.write("Nenhum pedido finalizado")
        else:
            try:
                op = st.selectbox("Escolha uma entrega para ser confirmada", entregas_lista)
                if st.button("Confirmar"):
                    op.set_entrega(True)
                    Vendas.atualizar(op)
                    st.success("Entrega confirmada com sucesso!")
                    time.sleep(2)
                    st.rerun()
            except ValueError as erro:
                st.error(erro)