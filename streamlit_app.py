import tensorflow as tf

# Asegúrate de que la ruta esté correcta y sea una cadena de caracteres.
saved_model_path = "/home/adminuser/models/my_saved_model"

# Ahora puedes intentar cargar el modelo
try:
    loaded_model = tf.saved_model.load(saved_model_path)
    st.write("Modelo cargado con éxito.")
except Exception as e:
    st.write("Error al cargar el modelo:", e)
# List out the available signatures for inference
signatures = list(loaded_model.signatures.keys())

# Assuming 'serving_default' is your signature key of interest
inference = loaded_model.signatures['serving_default']

# Now to integrate it with Streamlit, here's a starter code:
import streamlit as st

st.title("Noticias Veracidad Checker")

# Text input for the news statement
statement = st.text_area("Ingresa la afirmación para verificar su veracidad:")

# Button to trigger prediction
if st.button("Verificar"):
    if statement:
        # Preprocessing and tokenization steps would go here
        # For the sake of this example, let's assume the model takes tokenized text
        tokenized_text = tokenize(statement)  # replace 'tokenize' with your actual function

        # Run the model's inference
        result = inference(tf.constant([tokenized_text]))  # adjust according to the model's expected input

        # Postprocess the results and display
        # Here you would convert the model output to a human-readable form
        prediction = result['output_0'].numpy()[0]  # adjust 'output_0' to your actual output key
        st.write("La afirmación es:", "Verdadera" if prediction > 0.5 else "Falsa")
    else:
        st.write("Por favor, ingresa una afirmación para verificar.")
