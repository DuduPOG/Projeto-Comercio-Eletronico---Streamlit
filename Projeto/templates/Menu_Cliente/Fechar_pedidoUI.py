import streamlit as st
import pandas as pd
from view import View
from models.venda import Vendas

class Fechar_pedido:

    @staticmethod
    def main(carrinho,id_cliente):
        st.write("Resumo do seu pedido antes de finalizar:")

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

        if st.button("Confirmar e Fechar Pedido?"):
            #atualizar os atributos do carrinho
            carrinho.set_carrinho(False)
            #carrinho.set_id_cliente(id_cliente)
            # atualizar o carrinho atual
            View.carrinho_atualizar(carrinho, id_cliente)
            # atualizar a venda no arquivo JSON     
            Vendas.atualizar(carrinho)

            if "carrinho_atual" in st.session_state:
                del st.session_state.carrinho_atual
                
            st.rerun()  
