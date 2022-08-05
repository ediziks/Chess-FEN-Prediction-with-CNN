import streamlit as st
from utils import predicted_fen_plot
import tempfile
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Chess FEN Generator")

image = st.file_uploader("Upload an image", type=["jpeg", "jpg"])
if image is not None:
    # Save the image to a temporary file bc streamlit doesn't support getting the path!!!
    with tempfile.NamedTemporaryFile(mode="wb") as temp:
        bytes_data = image.getvalue()
        temp.write(bytes_data)
        image = temp.name
        st.pyplot(predicted_fen_plot(image))
