# -*- coding: utf-8 -*-
"""
 colour detection 
 Created on Tue Sep  6 15:56:45 2022

@author: Venom
"""
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
 
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    imgHSVg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    
    green_lower = np.array([36, 25, 25], np.uint8)
    green_upper = np.array([80  , 255, 255], np.uint8)
    green_mask = cv2.inRange(imgHSVg, green_lower, green_upper)
    #mask = cv2.inRange(imgHSVg, (36, 25, 25), (70, 255,255))
    kernel = np.ones((3, 3), "uint8")
    green_mask = cv2.dilate(green_mask, kernel)
    
    img_1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #g_or_b = cv2.bitwise_or(green_mask, brown_mask)
    sub_plot = cv2.subtract(img_1 , green_mask)
    #hStack = cv2.bitwise_and(img_1,green_mask)
    
    center_w = (sub_plot.shape[1])/2
    end_h = (sub_plot[0])/2
    
    x1 = 0
    y1 = math.floor(center_w)
    sub_plot[x1][y1] #point a, count goes to the right
    x2 = 0
    y2 = math.floor(center_w)
    sub_plot[x2][y2] #point b, count goes to the left
    if (sub_plot[x1][y1] != 0) and (sub_plot[x2][y2] !=0):  
        #print('this part not is black')
        if (sub_plot[x1][y1] == 0):
            y2 = y2-1
        elif (sub_plot[x2][y2] ==0):
            y1 = y1+1
        else:
            x1 = x1 + 20
            x2 = x2 + 20
        
        #drawing line
        avg_line = np.ones((frameHeight, frameWidth)) * 255
        line_thickness = 5
        cv2.line(avg_line, (x1, y1), (x2, y2), (255, 0, 0), thickness=line_thickness)
        
        midpoint = [(x1+x2)/2, (y1+y2)/2]  #mid-point
        
        #point() to mark mid_point
        
        x1 = x1+50
        x2 = x2+50
        
    print(midpoint)
    #print(sub_plot[x1][y1],sub_plot[x2][y2])
    
    
    #cv2.imshow("real", img)
    #cv2.imshow("green", green_mask)
    #cv2.imshow("brown", brown_mask)
    cv2.imshow("output",sub_plot)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()