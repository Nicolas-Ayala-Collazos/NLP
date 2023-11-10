

import streamlit as st
import tensorflow as tf

st.title("Aplicación de Clasificación de Noticias")

# Define la ruta al directorio que contiene tu modelo
saved_model_path = '/saved_model_BERT_multilingual'

# Intenta cargar el modelo y define 'loaded_model' solo si la carga tiene éxito
try:
    loaded_model = tf.saved_model.load(saved_model_path)
    st.write("Modelo cargado con éxito.")
    # Asumiendo que quieres listar las firmas después de cargar el modelo
    signatures = list(loaded_model.signatures.keys())
    st.write("Firmas disponibles:", signatures)
except Exception as e:
    st.error(f"Error al cargar el modelo: {e}")
    # Si la carga del modelo falla, 'loaded_model' no debe ser usado más allá de este punto

        st.write("Por favor, ingresa una afirmación para verificar.")
