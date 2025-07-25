import streamlit as st

st.set_page_config(page_title="Análise de Perfis Instagram", layout

st.title("Análise de Perfil do Instagram com IA")

username = st.text_input("Digite o @ do Instagram")
if username and st.button("Analisar"):
    st.info(f"Analisando perfil @{username}...")
    st.success("✅ Análise simulada concluída!")
    st.write("Bio analisada: Exemplo da bio do perfil.")
    st.write("Sugestões de melhoria:")
    st.markdown("- Postar com mais frequência\n- Melhorar identidade visual\n- Incluir número de contato na bio")
