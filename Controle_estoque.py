import streamlit as st
import json
import os

# Nome do arquivo JSON
ARQUIVO = "estoque.json"

# Carrega estoque
def carregar_estoque():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return {}

# Salva estoque
def salvar_estoque(estoque):
    with open(ARQUIVO, "w") as f:
        json.dump(estoque, f, indent=4)

# Carrega estoque ao iniciar
estoque = carregar_estoque()


# -------------------------------------------
# CSS MODERNO
# -------------------------------------------
st.markdown("""
    <style>
        .main-title {
            font-size: 32px;
            font-weight: bold;
            color: #4f8bf9;
            text-align: center;
            margin-bottom: 20px;
        }

        .card {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.10);
            margin-bottom: 20px;
        }

        .btn-add {
            background-color: #4CAF50 !important;
            color: white !important;
        }

        .btn-remove {
            background-color: #E53935 !important;
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)


# -------------------------------------------
# Título bonito
# -------------------------------------------
st.markdown("<h1 class='main-title'>📦 Controle de Estoque</h1>", unsafe_allow_html=True)


# -------------------------------------------
# MENU LATERAL
# -------------------------------------------
menu = st.sidebar.radio(
    "Menu",
    ["Adicionar item", "Remover item", "Listar estoque"],
    index=0
)


# -------------------------------------------
# PÁGINAS
# -------------------------------------------

# ADICIONAR ITEM
if menu == "Adicionar item":
    st.subheader("➕ Adicionar item ao estoque")

    nome = st.text_input("Nome do item").lower()
    quantidade = st.number_input("Quantidade", min_value=1)

    if st.button("Adicionar", type="primary"):
        if nome:
            estoque[nome] = estoque.get(nome, 0) + int(quantidade)
            salvar_estoque(estoque)
            st.success(f"Item **{nome}** adicionado com sucesso!")
        else:
            st.error("Digite um nome válido.")


# REMOVER ITEM
elif menu == "Remover item":
    st.subheader("🗑 Remover item do estoque")

    nome = st.text_input("Nome do item a remover").lower()

    if st.button("Remover", type="secondary"):
        if nome in estoque:
            del estoque[nome]
            salvar_estoque(estoque)
            st.success(f"Item **{nome}** removido!")
        else:
            st.error("Item não encontrado.")


# LISTAR ESTOQUE
elif menu == "Listar estoque":
    st.subheader("📋 Itens no estoque")

    if estoque:
        st.table(estoque)
    else:
        st.warning("Nenhum item no estoque.")
