import streamlit as st
import pandas as pd
from view import View

class Ver_carrinho:
    @staticmethod
    def main(carrinho):
        st.header("Este é o seu carrinho:")
        
        meu_carrinho = View.visualizar_meu_carrinho(carrinho) 

        if len(meu_carrinho) == 0: 
            st.write("Seu carrinho está vazio.")
        else: 
            df = pd.DataFrame(meu_carrinho)

            colunas_remover = ['id_item_venda'] 
            colunas_existentes_para_remover = [col for col in colunas_remover if col in df.columns]

            if colunas_existentes_para_remover:
                df = df.drop(columns=colunas_existentes_para_remover)
            
            st.dataframe(df)