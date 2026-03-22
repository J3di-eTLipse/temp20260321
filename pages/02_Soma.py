import streamlit as st

### Page Configuration ###
st.set_page_config(
    page_title = 'Calculador - Soma',
    page_icon = '➕',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.zigurat.com',
    }
)

st.markdown('### Soma')

numeroA = st.number_input('Numero A')
numeroB = st.number_input('Numero B')

soma = numeroA + numeroB

st.markdown('Resultado:')
st.markdown(soma)