import streamlit as st
import pandas as pd
from view import View

class Listar_produtos():
    
    @staticmethod
    def main():
        st.header("Esses são todos os produtos:")

        try:
            produtos = View.produto_listar()
        except Exception as e:
            st.error(f"Erro ao carregar produtos: {e}. Por favor, tente novamente mais tarde.")
            return           

        if len(produtos) == 0: 
            st.write("Nenhum produto disponível")
        else:    
            list_dic = []
            for obj in produtos:
                dic_produtos = obj.to_json()
                list_dic.append(dic_produtos)
            df = pd.DataFrame(list_dic)
            colunas_remover = ['id', 'estoque', 'id_categoria']
            df = df.drop(columns = colunas_remover)
            st.dataframe(df)