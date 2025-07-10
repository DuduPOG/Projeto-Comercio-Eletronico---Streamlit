import streamlit as st
import pandas as pd
from view import View
from models.venda import Venda, Vendas
import time

class Listar_EntregasUI:

    @staticmethod
    def main():
        st.header("Listagem de Entregas")
        Listar_EntregasUI.listar()

    def listar():
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
                dic = []
                for obj in entregas_lista: dic.append(obj.to_json())
                df = pd.DataFrame(dic)
                st.dataframe(df)
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)