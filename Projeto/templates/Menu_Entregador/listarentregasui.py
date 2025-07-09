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
        vendas = Vendas.listar()
        if len(vendas) == 0: 
            st.write("Nenhum pedido finalizado")
        else:
            try:
                dic = []
                for obj in vendas: dic.append(obj.to_json())
                df = pd.DataFrame(dic)
                st.dataframe(df)
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)