import streamlit as st
from view import View
from models.venda import Vendas
import time
from templates.Menu_Cliente.Adicionar_produtosUI import Adicionar_produtos

class Comprar_novamente:
    
    @staticmethod
    def main(carrinho):
        st.header("Comprar Novamente")
        
        if st.button("iniciar novo carrinho"):
            id_cliente = st.session_state.get('cliente_id')
            del carrinho
            st.session_state.carrinho_atual = View.iniciar_carrinho(id_cliente)
 
            st.success("Carrinho iniciado com sucesso!")
            Adicionar_produtos.main(st.session_state.carrinho_atual)
            time.sleep(2)
            st.rerun()
            


        