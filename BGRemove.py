from io import BytesIO
import streamlit as st
from PIL import Image
from rembg import remove

# App title
st.title("TechAbhee BGRemover")
st.write("Upload an image to remove its background quickly and easily!")

# Image uploader
image_upload = st.file_uploader("Upload an image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

# Convert the image to BytesIO for download
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

# Process the uploaded image
if image_upload:
    try:
        st.write("Original Image:")
        st.image(image_upload, caption="Uploaded Image", use_column_width=True)

        # Load and process the image
        image = Image.open(image_upload)
        with st.spinner("Processing..."):
            fixed = remove(image)

        st.write("Processed Image:")
        st.image(fixed, caption="Background Removed", use_column_width=True)

        # Prepare for download
        downloadable_image = convert_image(fixed)
        st.download_button(
            label="Download Image with Background Removed",
            data=downloadable_image,
            file_name="bg_removed.png",
            mime="image/png"
        )
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload an image to start.")
