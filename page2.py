import streamlit as st
import pandas as pd

def page2():
    if "file_path" not in st.session_state or "linea" not in st.session_state:
        st.warning("Por favor, selecciona una sucursal y línea en la Página 1.")
        return
    
    file_path = st.session_state["file_path"]
    codigos_file_path = "H:/STOCK/CONTEOS/CODIGOS.xlsx"
    
    df_codigos = pd.read_excel(codigos_file_path)
    
    # Filtrar los códigos por la línea seleccionada
    linea_seleccionada = st.session_state["linea"]
    df_codigos_filtrado = df_codigos[df_codigos["Linea"] == linea_seleccionada]
    
    st.title(f"Ingreso de Datos para {st.session_state['sucursal']} - {st.session_state['linea']}")
    
    codigo_plu_desc = st.selectbox("Selecciona Código - PLU - Descripción", df_codigos_filtrado["Codigo - PLU - Desc"].unique(), key="codigo_plu_desc")
    cantidad = st.number_input("Cantidad", min_value=0.0, step=0.1, format="%.3f", key="cantidad")
    
    if st.button("Agregar"):
        df = pd.read_excel(file_path)
        registro_seleccionado = df_codigos_filtrado[df_codigos_filtrado["Codigo - PLU - Desc"] == codigo_plu_desc].iloc[0]
        codigo = registro_seleccionado["Codigo"]
        descripcion = registro_seleccionado["Descripcion"]
        
        nuevo_registro = pd.DataFrame([{"Código": codigo, "Cantidad": cantidad, "Descripción": descripcion}])
        df = pd.concat([df, nuevo_registro], ignore_index=True)
        df.to_excel(file_path, index=False)
        
        st.session_state["last_action"] = "agregado"
    
    if "last_action" in st.session_state and st.session_state["last_action"] == "agregado":
        st.success("Registro agregado exitosamente.")
    
    df_mostrar = pd.read_excel(file_path)
    st.write("Registros Ingresados:")
    
    for index, row in df_mostrar.iterrows():
        st.write(f"**Código:** {row['Código']} **Cantidad:** {row['Cantidad']} **Descripción:** {row['Descripción']}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Editar", key=f"edit_{index}"):
                st.session_state[f"editing_{index}"] = True
        with col2:
            if st.button("Eliminar", key=f"delete_{index}"):
                df_mostrar = df_mostrar.drop(index)
                df_mostrar.to_excel(file_path, index=False)
                st.success("Registro eliminado exitosamente.")
                st.experimental_rerun()
    
        if st.session_state.get(f"editing_{index}", False):
            nuevo_codigo_plu_desc = st.selectbox("Nuevo Código - PLU - Descripción", df_codigos_filtrado["Codigo - PLU - Desc"].unique(), key=f"new_codigo_plu_desc_{index}")
            nueva_cantidad = st.number_input("Nueva Cantidad", min_value=0.0, value=float(row['Cantidad']), step=0.1, format="%.2f", key=f"new_cantidad_{index}")
            if st.button("Guardar", key=f"save_{index}"):
                registro_editado = df_codigos_filtrado[df_codigos_filtrado["Codigo - PLU - Desc"] == nuevo_codigo_plu_desc].iloc[0]
                df_mostrar.at[index, 'Código'] = registro_editado["Codigo"]
                df_mostrar.at[index, 'Descripción'] = registro_editado["Descripcion"]
                df_mostrar.at[index, 'Cantidad'] = nueva_cantidad
                df_mostrar.to_excel(file_path, index=False)
                st.success("Registro editado exitosamente.")
                st.session_state[f"editing_{index}"] = False
                st.experimental_rerun()
        st.write("----")
    st.dataframe(df_mostrar, hide_index=True)
