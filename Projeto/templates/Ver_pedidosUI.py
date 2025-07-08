import streamlit as st
import pandas as pd
from view import View # Certifique-se de que sua classe View está em view.py
import time

class Ver_pedidos:

    @staticmethod
    def main(cliente):
        st.header("Meus Pedidos")

        # 1. Obter os carrinhos do cliente
        # ASSUMIMOS que View.listar_minhas_compras(cliente) retorna um DataFrame
        # onde cada linha é um carrinho/pedido e tem uma coluna 'id_carrinho' (ou similar)
        # e outras colunas relevantes como 'data_compra', 'total', etc.
        try:
            carrinhos_df = View.listar_minhas_compras(cliente)

            if carrinhos_df.empty:
                st.info("Você ainda não fez nenhuma compra.")
                return

            st.subheader("Seus Carrinhos/Pedidos:")
            # Exibe o DataFrame de carrinhos para o usuário
            st.dataframe(carrinhos_df)

            # ---
            st.markdown("---") # Separador visual

            # 2. Permitir que o usuário selecione um carrinho
            # Usaremos o 'id_carrinho' para identificar o carrinho selecionado
            # É FUNDAMENTAL que 'id_carrinho' seja uma coluna no seu DataFrame retornado pela View.
            if 'id_carrinho' in carrinhos_df.columns:
                # Criamos uma lista de strings para o selectbox, mostrando informações úteis do carrinho
                opcoes_selecao = carrinhos_df.apply(
                    lambda row: f"Pedido ID: {row['id_carrinho']} - Data: {row['data_compra'] if 'data_compra' in row else 'N/A'} - Total: R${row['total'] if 'total' in row else 'N/A'}",
                    axis=1
                ).tolist()

                carrinho_selecionado_str = st.selectbox(
                    "Selecione um Pedido para ver os detalhes dos produtos:",
                    options=opcoes_selecao,
                    index=0 # Inicia com o primeiro pedido selecionado
                )

                if carrinho_selecionado_str:
                    # Extrai o ID do carrinho da string selecionada no selectbox
                    # Ex: "Pedido ID: 123 - Data: ..." -> "123"
                    carrinho_id_str = carrinho_selecionado_str.split(" - ")[0].replace("Pedido ID: ", "")
                    
                    # Converte o ID para o tipo correto (provavelmente int, dependendo do seu banco/modelo)
                    try:
                        carrinho_id_selecionado = int(carrinho_id_str)
                    except ValueError:
                        st.error("Não foi possível identificar o ID do carrinho selecionado.")
                        return

                    # 3. Listar os produtos do carrinho selecionado
                    # ASSUMIMOS que View.listar_produtos_do_carrinho(carrinho_id_selecionado)
                    # retorna um DataFrame com os produtos desse carrinho
                    produtos_carrinho_df = View.listar_produtos_do_carrinho(carrinho_id_selecionado)

                    if not produtos_carrinho_df.empty:
                        st.subheader(f"Produtos do Pedido ID: {carrinho_id_selecionado}")
                        st.dataframe(produtos_carrinho_df)
                    else:
                        st.info("Nenhum produto encontrado para este pedido.")
            else:
                st.error("A coluna 'id_carrinho' não foi encontrada no DataFrame de seus pedidos. Por favor, verifique a implementação de 'View.listar_minhas_compras'.")

        except Exception as e:
            st.error(f"Ocorreu um erro ao carregar seus pedidos ou produtos: {e}")
            st.warning("Verifique se as funções `View.listar_minhas_compras` e `View.listar_produtos_do_carrinho` retornam DataFrames com as colunas esperadas.")
