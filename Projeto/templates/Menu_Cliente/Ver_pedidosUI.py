import streamlit as st
import pandas as pd
from view import View # Certifique-se de que sua classe View está em view.py
import time

class Ver_pedidos:

    @staticmethod
    def main(carrinho):
        #st.write(carrinho)
        st.header("Meus Pedidos")
        carrinho = st.session_state.get('carrinho_atual')

        meus_carrinhos = View.visualizar_meu_carrinho(carrinho)

        if len(meus_carrinhos) == 0: 
            st.write("Seu carrinho está vazio.")
        else: 
            df = pd.DataFrame(meus_carrinhos)

            colunas_remover = ['id_item_venda', 'id'] 
            colunas_existentes_para_remover = [col for col in colunas_remover if col in df.columns]

            if colunas_existentes_para_remover:
                df = df.drop(columns=colunas_existentes_para_remover)
            
            st.dataframe(df)

        
         

        
