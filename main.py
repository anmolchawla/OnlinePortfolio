import utils.display as udisp
import streamlit as st
import src.pages.home
import src.pages.stockscreener
import src.pages.mnist
import src.pages.about
import streamlit.components.v1 as stc


MENU = {
    "Home" : src.pages.home,
    "Stock Screener" : src.pages.stockscreener,
    "Handwriting Recognition" : src.pages.mnist,
    "Contact" : src.pages.about
}

def main():
    """Main Navigation Code"""
    st.sidebar.title("Navigation")
    menu_selection = st.sidebar.selectbox("Go To",list(MENU.keys()))
    menu = MENU[menu_selection]
    st.sidebar.title("User Controls")
    with st.spinner(f"Loading {menu_selection} ..."):
        udisp.render_page(menu)



if __name__=='__main__':
    main()
