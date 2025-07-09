import streamlit as st
import pandas as pd
from view import View
import time

class ManterCategoriaUI:
    
    @staticmethod
    def main():
        st.header("Cadastro de Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCategoriaUI.listar()
        with tab2: ManterCategoriaUI.inserir()
        with tab3: ManterCategoriaUI.atualizar()
        with tab4: ManterCategoriaUI.excluir()
        
    def listar():
        categorias = View.categoria_listar()
        if len(categorias) == 0: 
            st.write("Nenhuma categoria cadastrada")
        else:    
            dic = []
            for obj in categorias: dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df)
    
    def inserir():
        desc = st.text_input("Informe uma descrição: ")
        if st.button("Cadastrar"):
            View.categoria_inserir(desc)
            st.success("Categoria inserida com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        categorias = View.categoria_listar()
        if len(categorias) == 0: 
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Atualização de cliente", categorias)
            desc = st.text_input("Informe a nova descrição", op.get_desc())
            if st.button("Atualizar"):
                View.categoria_atualizar(op.get_id(), desc)
                st.success("Categoria atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        categorias = View.categoria_listar()
        if len(categorias) == 0: 
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Exclusão de categoria", categorias)
            if st.button("Excluir"):
                View.categoria_excluir(op.get_id())
                st.success("Categoria excluída com sucesso")
                time.sleep(2)
                st.rerun()