import streamlit as st
import cv2
import numpy as np
from PIL import Image
from Test import run_yolo,my_function
from equality import base64_webp_to_png


def main():
    img_str = st.query_params.get('img_str')
    st.title(":rainbow[Traffic cam vehicle detector]")
    st.sidebar.title("Settings")
    st.sidebar.subheader("Parameters")
    st.sidebar.markdown("Here you can alter the parameters according to your needs")
    st.markdown(
        """
        
        <style>
        [data-testid="stSidebar][aria-expanded="true"] > div:first-child {
            width: 300px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 300px;
            margin-left: -300px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    app_mode= st.sidebar.selectbox("Choose the webpage",["About the page","Run on Image","Run on Video"])

    if app_mode == "About the page":
        st.markdown(":orange[**What is Object Detection?**]")
        st.markdown(
        """
        
        <style>
        [data-testid="stSidebar][aria-expanded="true"] > div:first-child {
            width: 300px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 300px;
            margin-left: -300px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
        st.markdown("Object detection is a computer vision technique that identifies and locates specific objects within an image or video. It involves recognizing the presence of objects and determining their exact positions within the image."
                    "For example, an object detection system could identify and locate cars, pedestrians, and traffic signs in a street scene image."
                    "This technology is widely used in various applications such as self-driving cars, image search, video surveillance, and more.")
        
        st.markdown(":orange[**Vehicle Detection**]")
        st.markdown(
        """
        
        <style>
        [data-testid="stSidebar][aria-expanded="true"] > div:first-child {
            width: 300px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 300px;
            margin-left: -300px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
        st.markdown("This is currently an experiment to see whether my code works or not. With better resources and more time, I plan to expand it to something truly useful.")
        st.markdown(":orange[**How does it work?**]")
        st.markdown(
        """
        
        <style>
        [data-testid="stSidebar][aria-expanded="true"] > div:first-child {
            width: 300px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 300px;
            margin-left: -300px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
        st.markdown("Currently only the **'Run on Image'** mode works.Just upload an image (keeping in mind the space and extension restrictions) "
                    "and it'll detect on it's own after a few seconds.")

    elif app_mode == "Run on Image":
        st.sidebar.markdown('---')
        confidence = st.sidebar.slider('Confidence score',min_value=0.2,max_value=1.0)
        st.sidebar.markdown('---')
        st.markdown(
        """
        
        <style>
        [data-testid="stSidebar][aria-expanded="true"] > div:first-child {
            width: 300px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            width: 300px;
            margin-left: -300px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
        img_file_buff = st.sidebar.file_uploader("Upload an Image",type=["jpg","jpeg","png"])
        #image_param = st.query_params["image_param"]
        DEMO_Image = "27260-362770008_tiny.jpg"

        if img_file_buff is not None :#and image_param is None:
            img = cv2.imdecode(np.fromstring(img_file_buff.read(),np.uint8),1)
            image = np.array(Image.open(img_file_buff))
        else:
            img = cv2.imread(DEMO_Image)
            image = np.array(Image.open(DEMO_Image))
        st.sidebar.text('Original Image')
        st.sidebar.image(image)
        run_yolo(image_url=img,confidence=confidence)
        my_function(image_url=img)


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass    
