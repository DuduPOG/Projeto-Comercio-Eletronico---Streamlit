import streamlit as st
import pandas as pd
from view import View # Certifique-se de que sua classe View está em view.py
import time

class Ver_pedidos:

    @staticmethod
    def main():
        st.header("Meus Pedidos")
        id_cliente = st.session_state.get('cliente_id')

        meus_carrinhos = View.visualizar_meu_carrinho(id_cliente)

        if len(meu_carrinho) == 0: 
            st.write("Seu carrinho está vazio.")
        else: 
            df = pd.DataFrame(meu_carrinho)

            colunas_remover = ['id_item_venda'] 
            colunas_existentes_para_remover = [col for col in colunas_remover if col in df.columns]

            if colunas_existentes_para_remover:
                df = df.drop(columns=colunas_existentes_para_remover)
            
            st.dataframe(df)

        
         

        
