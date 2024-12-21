import streamlit as st
st.title("EMC2 / Cloud Module")
st.header("AI is Great")
#st.video("https://www.youtube.com/watch?v=NPEsD6n9A_I&list=PLGjZwEtPN7j-Q59JYso3L4_yoCjj2syrM&ab_channel=AdamMarczak-AzureforEveryone")


st.sidebar.image("ehtp.png")
st.sidebar.header("Master Cloud Computing")
choice = st.sidebar.selectbox('Select app type', ['----- Choose application -----', 'OCR', 'Image Analysis', 'Face Analysis', 'Thumbnail Image']) 


if choice == 'Image Analysis':
  image_file = st.file_uploader('Upload an image', type = ['png', 'jpg'])


# Use Read API to read text in image
with open(image_file, mode="rb") as image_data:
    read_op = cv_client.read_in_stream(image_data, raw=True)

    # Get the async operation ID so we can check for the results
    operation_location = read_op.headers["Operation-Location"]
    operation_id = operation_location.split("/")[-1]

    # Wait for the asynchronous operation to complete
    while True:
        read_results = cv_client.get_read_result(operation_id)
        if read_results.status not in [OperationStatusCodes.running, OperationStatusCodes.not_started]:
            break
        time.sleep(1)

    # If the operation was successfully, process the text line by line
    if read_results.status == OperationStatusCodes.succeeded:
        for page in read_results.analyze_result.read_results:
            for line in page.lines:
                print(line.text)
                # Uncomment the following line if you'd like to see the bounding box 
                #print(line.bounding_box)
