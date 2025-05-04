
from ultralytics import YOLO
model = YOLO('besst.pt')
#model.predict(source='fire1.jpeg', imgsz=640,conf=0.6,show=True , save=True)



model.predict(source=0, imgsz=640, conf=0.6, show=True)