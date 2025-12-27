import streamlit as st
import time
from datetime import datetime
import pytz

# 1. Configuração da Página
st.set_page_config(
    page_title="Mega da Virada 2025 - Contagem Regressiva",
    page_icon="🎰",
    layout="centered"
)

# 2. Injeção de CSS para Esconder Elementos do Streamlit e Estilizar Casino
st.markdown("""
    <style>
    /* REMOVER CABEÇALHO E RODAPÉ DO STREAMLIT */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* Ajustar o espaçamento do topo */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
    }

    /* ESTILO CASINO VIP */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
        text-align: center;
    }
    .titulo {
        color: #FFD700;
        font-weight: bold;
        font-size: 2.8rem;
        text-shadow: 0 0 15px rgba(255, 215, 0, 0.6);
        margin-bottom: 10px;
    }
    .contador-box {
        background: linear-gradient(135deg, #bf953f, #fcf6ba, #b38728, #fbf5b7, #aa771c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 900;
        padding: 30px 10px;
        border: 2px solid #333;
        border-radius: 20px;
        margin: 25px 0;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.1);
    }
    .subtexto {
        color: #FFD700;
        font-size: 1.2rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Lógica do Tempo (Brasília)
fuso_br = pytz.timezone('America/Sao_Paulo')
data_alvo = fuso_br.localize(datetime(2025, 12, 31, 22, 0, 0))

st.markdown('<p class="titulo">🎰 MEGA DA VIRADA</p>', unsafe_allow_html=True)
st.markdown('<p class="subtexto">Contagem Regressiva Oficial</p>', unsafe_allow_html=True)

placeholder = st.empty()

# 4. Loop Infinito de Atualização
while True:
    agora = datetime.now(fuso_br)
    restante = data_alvo - agora
    
    if restante.total_seconds() <= 0:
        placeholder.markdown("<h1 style='color:gold;'>🎉 O SORTEIO COMEÇOU! BOA SORTE!</h1>", unsafe_allow_html=True)
        break
    
    dias = restante.days
    horas, rem = divmod(restante.seconds, 3600)
    minutos, segundos = divmod(rem, 60)
    
    # Frase exata conforme solicitado
    frase_final = f"Faltam {dias} dias, {horas}h, {minutos}min e {segundos}s"
    
    with placeholder.container():
        st.markdown(f'<div class="contador-box">{frase_final}</div>', unsafe_allow_html=True)
        st.markdown('<p style="color:#555;">para o sorteio da Mega da Virada 2025</p>', unsafe_allow_html=True)
    
    time.sleep(1)