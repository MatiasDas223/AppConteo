import streamlit as st
from page1 import page1
from page2 import page2

def main():
    st.sidebar.title("Navegación")
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Página 1"
    
    if st.session_state["current_page"] == "Página 1":
        page1()
    elif st.session_state["current_page"] == "Página 2":
        page2()

if __name__ == "__main__":
    main()
