import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import numpy as np
import pyttsx3
from cvlib.object_detection import detect_common_objects
from cvlib.object_detection import draw_bbox
import urllib.request
import concurrent.futures
url='http://192.168.43.215/cam-hi.jpg'
im=None
engine = pyttsx3.init()
def run1():
    print("run1")
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    
    while True:
        print("run1")
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
 
        cv2.imshow('live transmission',im)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break
            
    cv2.destroyAllWindows()
        
def run2():
    print("run2")
    cv2.namedWindow("detection", cv2.WINDOW_AUTOSIZE)
    
    while True:
        print("run2")
        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)
        

        bbox, label, conf = cv.detect_common_objects(im,confidence=0.5,nms_thresh=0.3,model="yolov3",enable_gpu=False)
        im = draw_bbox(im,bbox,label,conf,colors=None,write_conf=False)
        cv2.imshow('detection',im)
        engine.say(label)
        engine.runAndWait()
    
        key=cv2.waitKey(5)
        if key==ord('q'):
            break
            
    cv2.destroyAllWindows()
 
 
 
if _name_ == '_main_':
    print("started ")
    with concurrent.futures.ProcessPoolExecutor() as executer:
            f1= executer.submit(run1)
            print("run1")
            f2= executer.submit(run2)
            print("run2")