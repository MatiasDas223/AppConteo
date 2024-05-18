import streamlit as st
from page1 import page1
from page2 import page2

def main():
    if "sidebar_expanded" not in st.session_state:
        st.session_state["sidebar_expanded"] = False
    
    if st.session_state["sidebar_expanded"]:
        st.sidebar.title("Navegación")
        if st.button("Ocultar Barra"):
            st.session_state["sidebar_expanded"] = False
            st.experimental_rerun()
        if "current_page" not in st.session_state:
            st.session_state["current_page"] = "Página 1"
        
        if st.session_state["current_page"] == "Página 1":
            page1()
        elif st.session_state["current_page"] == "Página 2":
            page2()
    else:
        if st.button("Mostrar Barra"):
            st.session_state["sidebar_expanded"] = True
            st.experimental_rerun()
        if "current_page" not in st.session_state:
            st.session_state["current_page"] = "Página 1"
        
        if st.session_state["current_page"] == "Página 1":
            page1()
        elif st.session_state["current_page"] == "Página 2":
            page2()

if __name__ == "__main__":
    main()
