# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:51:24 2022

@author: Venom
"""

import cv2
import numpy as np
 
frameWidth = 640
frameHeight = 480
#cap = cv2.VideoCapture(0)
#cap.set(3, frameWidth)
#cap.set(4, frameHeight)

def empty(a):
    pass

cv2.namedWindow("TrackBars for green")
cv2.resizeWindow("TrackBars for green",640,240)
cv2.createTrackbar("Hue Min","TrackBars for green",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars for green",19,179,empty)
cv2.createTrackbar("Sat Min","TrackBars for green",110,255,empty)
cv2.createTrackbar("Sat Max","TrackBars for green",240,255,empty)
cv2.createTrackbar("Val Min","TrackBars for green",153,255,empty)
cv2.createTrackbar("Val Max","TrackBars for green",255,255,empty)

while True:
    #success, img = cap.read()
    img = cv2.imread("mask.jpg", cv2.IMREAD_COLOR)
    imgHSVg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #imgHSVb = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    h_ming = cv2.getTrackbarPos("Hue Min","TrackBars for green")
    s_ming = cv2.getTrackbarPos("Sat Min","TrackBars for green")
    v_ming = cv2.getTrackbarPos("Val Min","TrackBars for green")
    h_maxg = cv2.getTrackbarPos("Hue Max","TrackBars for green")
    s_maxg = cv2.getTrackbarPos("Sat Max","TrackBars for green")
    v_maxg = cv2.getTrackbarPos("Val Max","TrackBars for green")
    print(h_ming,h_maxg,s_ming,s_maxg,v_ming,v_maxg)
    
    lowerg = np.array([h_ming,s_ming,v_ming])
    upperg = np.array([h_maxg,s_maxg,v_maxg])
    maskg = cv2.inRange(imgHSVg,lowerg,upperg)
    #maskg = cv2.cvtColor(maskg,cv2.COLOR_GRAY2BGR)
    imgResultg = cv2.bitwise_and(img,imgHSVg,maskg)
    
    f_result = cv2.bitwise_and(img,imgResultg)
    #hStack = np.hstack([img,maskg,maskb,imgResultg,imgResultb])
    
    
    #cv2.imshow("real", img)
    cv2.imshow("hsvg", imgHSVg)
    #cv2.imshow("hsvb", imgHSVb)
    cv2.imshow("maskg", maskg)
    #cv2.imshow("maskb", maskb)
    cv2.imshow("output green", imgResultg)
    #cv2.imshow("output", imgResultb)
    cv2.imshow("output mask",f_result)
    #cv2.imshow("stacked output", hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
img.release()
cv2.destroyAllWindows()
 