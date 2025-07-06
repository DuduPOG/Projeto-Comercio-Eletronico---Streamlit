import streamlit as st
import pandas as pd
from view import View
import time

class ManterEntregadorUI:
    
    @staticmethod
    def main():
        st.header("Cadastro de Entregadores")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterEntregadorUI.listar()
        with tab2: ManterEntregadorUI.inserir()
        with tab3: ManterEntregadorUI.atualizar()
        with tab4: ManterEntregadorUI.excluir()

    def listar():
        entregadores = View.entregador_listar()
        if len(entregadores) == 0: 
            st.write("Nenhum entregador cadastrado")
        else:    
            list_dic = []
            for obj in entregadores:
                dic_entregador = obj.to_json()
                del dic_entregador["senha"]
                list_dic.append(dic_entregador)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
            
    def inserir():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o e-mail: ")
        fone = st.text_input("Informe o fone: ")
        senha = st.text_input("Informe a senha: ")
        if st.button("Cadastrar"):
            try:
                View.entregador_inserir(nome, email, fone, senha)
                st.success("Entregador inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.erro(erro)

    def atualizar():
        entregadores = View.entregador_listar()
        if len(entregadores) == 0: 
            st.write("Nenhum entregador cadastrado")
        else:
            try:
                op = st.selectbox("Atualização de entregador", entregadores)
                nome = st.text_input("Informe o novo nome: ", op.get_nome())
                email = st.text_input("Informe o novo e-mail: ", op.get_email())
                fone = st.text_input("Informe o novo fone: ", op.get_fone())
                if st.button("Atualizar"):
                    View.entregador_atualizar(op.get_id(), nome, email, fone, op.get_senha())
                    st.success("Entregador atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
            except ValueError as erro:
                st.error(erro)

    def excluir():
        entregadores = View.entregador_listar()
        if len(entregadores) == 0: 
            st.write("Nenhum entregador cadastrado")
        else:
            op = st.selectbox("Exclusão de entregador", entregadores)
            if st.button("Excluir"):
                View.entragador_excluir(op.get_id())
                st.success("Entregador excluído com sucesso")
                time.sleep(2)
                st.rerun()