import streamlit as st
st.title("EMC2 / Cloud Module")
st.header("AI is Great")
#st.video("https://www.youtube.com/watch?v=NPEsD6n9A_I&list=PLGjZwEtPN7j-Q59JYso3L4_yoCjj2syrM&ab_channel=AdamMarczak-AzureforEveryone")


st.sidebar.image("ehtp.png")
st.sidebar.header("Master Cloud Computing")
choice = st.sidebar.selectbox('Select app type', ['----- Choose application -----', 'OCR', 'Image Analysis', 'Face Analysis', 'Thumbnail Image']) 


if choice == 'Image Analysis':
  image_file = st.file_uploader('Upload an image', type = ['png', 'jpg'])
