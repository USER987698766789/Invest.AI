import streamlit as st
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="IA de Investimentos", layout="centered")
st.title("IA para Análise de Cripto e Ações")
st.write("Este mini app analisa dados de criptomoedas e entrega insights com IA.")

if st.button("Analisar agora"):
    criptos = pegar_dados_crypto()
    resultado = analisar_oportunidades(criptos)
    st.subheader("Análise da IA:")
    st.write(resultado)
