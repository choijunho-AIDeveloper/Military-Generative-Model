import streamlit as st
from PIL import Image

st.set_page_config(page_title="작전정보통신단", page_icon="./icons/logo.png")

st.markdown(
    """
    ## 🧷작전정보통신단 GPT🧷입니다!🙃
    💬**아래 챗봇 중 하나를 이용해보세요**💬 
    - [🚗][**EXAONE-3.5-2.4B-BASELINE**](/EXAONE-3.5-2.4B-BASELINE)
    - [🚓][**EXAONE-3.5-2.4B-SFT**](/EXAONE-3.5-2.4B-SFT)
    - [🚕][**EXAONE-3.5-2.4B-RAG**](/EXAONE-3.5-2.4B-RAG)
    - [🚗][**EXAONE-3.5-7.8B-BASELINE**](/EXAONE-3.5-7.8B-BASELINE)
    """
)