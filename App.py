import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO

import tempfile
from Test import run_yolo,my_function
from video_predict_2 import video_process
import base64
from io import BytesIO
from equality import base64_webp_to_png
import re


def main():
    img_str = st.query_params.get('img_str')
    st.title(":rainbow[Object Detection for Fruits]")
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
        
        st.markdown(":orange[**Fruit Detection**]")
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
        DEMO_Image = "run\Images\image2.jpeg"

        if img_str is not None:
            st.text(img_str)
            # Replace special characters into their usual characters
            img_str = img_str.replace('-', '+')
            img_str = img_str.replace('_', '/')
            img_str = img_str.replace('.', '=')
            image_from_query = base64_webp_to_png(img_str)
            st.sidebar.text('Original Image')
            st.sidebar.image(image_from_query)
            run_yolo(image_url=image_from_query)
            my_function(image_from_query)

        else:
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
    
    elif app_mode == "Run on Video":
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
        st.markdown('---')
        use_webcam = st.sidebar.checkbox('Use Webcam')
        st.markdown('---')
        video_file_buffer = st.sidebar.file_uploader("Upload a Video",type=["mp4","avi","mov","asf"])

        DEMO_Video = r'C:\Users\prady\Downloads\Streamlit\videos\istockphoto-1922431095-640_adpp_is (1).mp4_out.mp4'

        tffile = tempfile.NamedTemporaryFile(suffix= '.mp4',delete=False)

        if not video_file_buffer:
            if use_webcam:
                tffile.name = 0
            else:
                vid = cv2.VideoCapture(DEMO_Video)
                tffile.name = DEMO_Video
                demo_vid = open(tffile.name ,'rb')
                demo_bytes = demo_vid.read()
                st.sidebar.text("Input Video")
                st.sidebar.video(demo_bytes)

        else:
            tffile.write(video_file_buffer.read())
            demo_vid = open(tffile.name ,'rb')
            demo_bytes = demo_vid.read()
            st.sidebar.text("Input Video")
            st.sidebar.video(demo_bytes)
        stframe = st.empty()
        st.markdown("<hr/>",unsafe_allow_html=True)
        kpi1 , kpi2 , kpi3 = st.columns(3)
        with kpi1:
            st.markdown("**Frame Rate**")
            kpi1_text = st.markdown(0)
        with kpi2:
            st.markdown("**Width**")
            kpi2_text = st.markdown(0)
        with kpi3:
            st.markdown("**Height**")
            kpi3_text = st.markdown(0)
        st.markdown("<hr/>",unsafe_allow_html=True)
        video_process(tffile.name)




















if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass    