import streamlit as st
import pandas as pd
import os

# Dirección de guardado de los archivos
DIRECTORIO_GUARDADO = "H:/STOCK/CONTEOS"

def cargar_conteos():
    archivos = [f for f in os.listdir(DIRECTORIO_GUARDADO) if f.endswith('.xlsx')]
    conteos = {}
    for archivo in archivos:
        ruta = os.path.join(DIRECTORIO_GUARDADO, archivo)
        df = pd.read_excel(ruta)
        conteos[archivo] = df
    return conteos

def mostrar_resultados():
    st.title("Resultados de Inventario")

    conteos = cargar_conteos()
    
    if not conteos:
        st.warning("No se encontraron archivos de conteo.")
        return
    
    archivo_seleccionado = st.selectbox("Seleccione un archivo de conteo", list(conteos.keys()))

    if archivo_seleccionado:
        df = conteos[archivo_seleccionado]
        st.write(f"Resultados para {archivo_seleccionado}")
        st.dataframe(df)

    # Botón para regresar al menú principal
    if st.button("Menu Principal"):
        st.session_state.page = "main"

if __name__ == "__main__":
    mostrar_resultados()
