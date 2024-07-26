import cv2 as cv
import numpy as np 
import math
from ultralytics import YOLO


def video_process(video_name,conf=0.2):
    cap = cv.VideoCapture(video_name)
    ret, frame = cap.read()
    H, W, _ = frame.shape
    out = cv.VideoWriter(video_name, cv.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv.CAP_PROP_FPS)), (W, H))

    #model_path = os.path.join('.', 'runs', 'detect', 'train', 'weights', 'last.pt')

    # Load a model
    model = YOLO(best.pt)  # load a custom model

    threshold = conf

    while ret:

        results = model(frame)[0]

        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result

            if score > threshold:
                cv.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                            cv.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv.LINE_AA)

        out.write(frame)
        ret, frame = cap.read()
        #cv.imshow("Frame",results)

    cap.release()
    out.release()
    cv.destroyAllWindows()