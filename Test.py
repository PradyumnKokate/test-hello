from ultralytics import YOLO
from PIL import Image
import streamlit as st
import cv2 as cv2


def run_yolo(image_url, confidence=0.15, iou=0.7):
    
    yolo = YOLO(r'C:\Users\prady\Downloads\Streamlit\runs\detect\train\weights\best.pt')
    results = yolo.predict(image_url,conf=confidence, iou=iou)
    res = results[0].plot()[:, :, [2,1,0]]
    return Image.fromarray(res)


def my_function(image_url):
    image = run_yolo(image_url)
    st.image(image,use_column_width=True)

