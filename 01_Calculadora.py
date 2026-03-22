import streamlit as st

### Page Configuration ###
st.set_page_config(
    page_title = 'Calculadora',
    page_icon = '🧮',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.zigurat.com',
        'About': 'Prática Zigurat.'
    }
)

st.markdown(
    '''<p>
    Descrição:
    
    Exemplo de usos de Streamlit com Python.
    '''
    , unsafe_allow_html = True)
