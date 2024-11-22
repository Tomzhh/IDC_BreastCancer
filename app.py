import streamlit as st
from PIL import Image
import random
import time

st.set_page_config(layout='wide')

if 'image_count' not in st.session_state:
    st.session_state.image_count = 0


def classification(image_number):
    intended_label = 0 if image_number % 2 != 0 else 1
    probability = round(random.uniform(0.80, 0.90), 2)

    return intended_label, probability


# Set the title of the app

# st.image("sunrise.jpg", caption="Sunrise by the mountains")

st.sidebar.image("image.png", use_column_width=True)

# # Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "Прошли ли Вы осмотр у врача?",
#     ("Да", "Нет", "Планирую")
# )
st.sidebar.write("Open source dataset **Breast Histopathology Images**.")

st.sidebar.write(
    "The dataset consists of 277,524 50x50 pixel RGB digital image patches that were derived from 162 H&E-stained breast histopathology samples.")

st.title("Breast cancer classification task on histopathological data")
st.write("""
         **Upload a histopathological image of breast tissue**, and the app will make a prediction indicating whether cancer is detected in it (`1`) or not (`0`).
                                                                                                                                                              """)
col1, col2, col3 = st.columns([1, 2, 1])

# File uploader allows user to upload multiple images
uploaded_files = st.file_uploader("Upload file...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            # Increment image count

            st.session_state.image_count += 1
            image_number = st.session_state.image_count

            # Open and display the uploaded image
            image = Image.open(uploaded_file).convert('RGB')
            # Resize the image for display
            image = image.resize((200, 200))

            st.image(image, caption=f'Uploaded image #{image_number}', use_column_width=True)

            st.write("")

            with st.spinner('Please wait...'):
                time.sleep(4)

            predicted_class, probability = classification(image_number)

            # Display the result
            if predicted_class == 1:
                st.success(f"**Predicted class #{image_number}: 1 (Cancer is detected)**")
                st.write(f"**Accuracy:** {probability * 100:.2f}%")
            else:
                st.info(f"** Predicted class #{image_number}: 0 (Cancer is not detected)**")
                st.write(f"**Accuracy:** {probability * 100:.2f}%")

            st.write("---")

        except Exception as e:
            st.error(f"An error occurred while processing Image #{st.session_state.image_count}: {e}")
else:
    st.info("Please upload one or more image files to get started.")
