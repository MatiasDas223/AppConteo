import streamlit as st
import pandas as pd
import os

def page1():
    st.title("Selección de Sucursal y Línea")
    
    # Leer las opciones de línea del archivo CONTEO.xlsx
    conteo_file_path = "H:/STOCK/CONTEOS/CODIGOS.xlsx"
    df_conteo = pd.read_excel(conteo_file_path)
    
    # Obtener las líneas únicas del archivo
    lineas = df_conteo["Linea"].unique()
    
    # Opciones de sucursal (puedes ajustar según sea necesario)
    sucursales = ["Alem", "Alberti", "Cordoba", "Carilo"]
    
    # Verificar si ya se ha realizado una selección y redirigir a la página 2 si es necesario
    if "sucursal" in st.session_state and "linea" in st.session_state:
        st.experimental_rerun()

    sucursal = st.selectbox("Selecciona una Sucursal", sucursales, key="sucursal_selectbox")
    linea = st.selectbox("Selecciona una Línea", lineas, key="linea_selectbox")

    if st.button("Siguiente"):
        file_path = f"H:/STOCK/CONTEOS/conteo_{sucursal}_{linea}.xlsx"
        if not os.path.exists(file_path):
            df = pd.DataFrame(columns=["Código", "Cantidad", "Descripción"])
            df.to_excel(file_path, index=False)
        
        # Actualizar session state y redirigir
        st.session_state["file_path"] = file_path
        st.session_state["sucursal"] = sucursal
        st.session_state["linea"] = linea
        st.session_state["current_page"] = "Página 2"
        st.experimental_rerun()
