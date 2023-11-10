
import tensorflow as tf
import streamlit as st
import numpy as np
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification

# Cargar el modelo y el tokenizer
#model = TFAutoModelForSequenceClassification.from_pretrained('/saved_model_BERT_multilingual.pb')
#tokenizer = AutoTokenizer.from_pretrained('bert-base-multilingual-cased')

# Función para predecir la veracidad de la noticia
#def predict_veracity(statement):
 #   inputs = tokenizer(statement, return_tensors="tf", padding=True)
  #  outputs = model(inputs)[0]
  #  probabilities = tf.nn.softmax(outputs, axis=1)
  #  prediction = np.argmax(probabilities, axis=1)
  #  return prediction

# Crear la interfaz de usuario con Streamlit
st.title('Clasificador de Noticias con BERT')
statement = st.text_area("Introduce la afirmación para verificar:")

#if st.button('Verificar'):
 #   prediction = predict_veracity(statement)
  #  st.write(f'La noticia es: {"Verdadera" if prediction else "Falsa"}')
