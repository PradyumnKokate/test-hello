from ultralytics import YOLO
from PIL import Image
import streamlit as st
import cv2 as cv2

#yolo = YOLO('yolov8n.pt')
def run_yolo(image_url, confidence=0.15, iou=0.7):
    
    yolo = YOLO(r'C:\Users\prady\Downloads\Streamlit\runs\detect\train\weights\best.pt')
    results = yolo.predict(image_url,conf=confidence, iou=iou)
    res = results[0].plot()[:, :, [2,1,0]]
    #image = run_yolo(image_url)
    #st.image(image)
    return Image.fromarray(res)
    #image = run_yolo(image_url)
    #st.image(image)


def my_function(image_url):
    #cv2.imread(image_url)
    #image_url = r'C:\Users\prady\Downloads\Streamlit\run\Images\image2.jpeg'
    image = run_yolo(image_url)
    #resize_frame = cv2.resize(image, (0,0), fx=0.5 , fy=0.5 , interpolation=cv2.INTER_AREA)
    #cv2.imshow("Frame",resize_frame)
    st.image(image,use_column_width=True)


# def video_loader(video_name,kpi1_text,kpi2_text,kpi3_text,stframe):
#     cap = cv2.VideoCapture(video_name)
#     threshold = 0.2

#     yolo = YOLO(r'C:\Users\prady\Downloads\Streamlit\run\best.pt')

#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     frame_width = int(cap.get(3))
#     frame_height = int(cap.get(4))

#     out = cv2.VideoWriter('output.avi' , cv2.VideoWriter_fourcc('M','J','P','G'), 10 ,(frame_width,frame_height))

#     while True:
#         ret , frame = cap.read()

#         if ret:
#             #result = list(yolo.predict(frame,conf=0.2))
#             results = yolo(frame)[0]

#             for result in results.boxes.data.tolist():
#                 x1, y1, x2, y2, score, class_id = result

#                 if score > threshold:
#                     cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
#                     cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
