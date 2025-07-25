import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Análise de Perfis Instagram",
    layout="centered"
)

st.title("🔍 Analisador de Perfil do Instagram")

username = st.text_input("Digite o @ do Instagram:")

if st.button("Analisar"):
    if username:
        # Simulação de resposta
        resposta_ia = {
            "bio": "Especialista em comida saudável e marmitas fitness.",
            "identidade_visual": "Boa presença visual com cores consistentes.",
            "posts": "Frequência ok, mas falta mostrar bastidores e promoções.",
            "melhorias": [
                "Adicione destaques com depoimentos de clientes.",
                "Use um padrão de fonte e cor para fortalecer a marca.",
                "Crie postagens com dicas de saúde para engajar mais."
            ]
        }

        st.subheader("🧠 Análise Inteligente")
        st.write(f"**Bio:** {resposta_ia['bio']}")
        st.write(f"**Identidade Visual:** {resposta_ia['identidade_visual']}")
        st.write(f"**Posts:** {resposta_ia['posts']}")
        st.write("**Sugestões de Melhorias:**")
        for item in resposta_ia["melhorias"]:
            st.markdown(f"- {item}")
    else:
        st.warning("Por favor, insira um @ para analisar.")
        
