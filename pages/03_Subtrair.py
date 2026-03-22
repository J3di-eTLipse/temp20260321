import streamlit as st

### Page Configuration ###
st.set_page_config(
    page_title = 'Calculador - Subtrair',
    page_icon = '➖',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.zigurat.com',
    }
)

st.markdown('### Subtrait')

numeroA = st.number_input('Numero A')
numeroB = st.number_input('Numero B')

subtracao = numeroA - numeroB

st.markdown('Resultado:')
st.markdown(subtracao)