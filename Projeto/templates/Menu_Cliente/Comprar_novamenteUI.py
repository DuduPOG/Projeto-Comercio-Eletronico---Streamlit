import streamlit as st
from view import View
from models.venda import Vendas
import time

class Comprar_novamente:
    
    @staticmethod
    def main(id_cliente):
        st.header("Comprar Novamente")
        
        if st.button("iniciar novo carrinho"):
 
            st.success("Carrinho iniciado com sucesso!")
            time.sleep(2)

            if "carrinho_atual" in st.session_state:
                del st.session_state.carrinho_atual

            st.rerun()


        