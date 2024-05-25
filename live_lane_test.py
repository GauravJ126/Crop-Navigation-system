# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:49:35 2022

@author: Venom
"""

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

vid = cv2.VideoCapture("live_4.mp4") #vedio calling variable
Q_y = []
Q_x = []    


while True: 
    ret,img = vid.read()
    
    
    # img = cv2.imread("test_img_2.jpg", cv2.IMREAD_UNCHANGED)
    imgHSVg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    green_lower = np.array([36, 25, 25], np.uint8)
    green_upper = np.array([80  , 255, 255], np.uint8)
    green_mask = cv2.inRange(imgHSVg, green_lower, green_upper)
    #mask = cv2.inRange(imgHSVg, (36, 25, 25), (70, 255,255))
    kernel = np.ones((3, 3), "uint8")
    green_mask = cv2.dilate(green_mask, kernel)
    
    img_1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sub_plot = cv2.subtract(img_1 , green_mask)
    #sub_plot = cv2.cvtColor(sub_plot,cv2.GRAY2BGR)
    #hStack = cv2.bitwise_and(img_1,green_mask)
    
    mid_h = (sub_plot.shape[0])/2 #height of image = 276
    mid_w = (sub_plot.shape[1])/2 #width of image = 231
    # print(sub_plot.shape[1])
    
    max_h = (sub_plot.shape[0])-1
    
    x = (sub_plot.shape[0]) #max height
    y1 = math.floor(mid_w) #half width
    #sub_plot[x][y1] point a, count goes to the right
    y2 = math.floor(mid_w) #half width
    #sub_plot[x][y2] point b, count goes to the left
    
    for x in range((max_h),(int(mid_h)),-10):
        y1 = math.floor(mid_w)
        y2 = math.floor(mid_w)
        while (sub_plot[x][y1] != 0) or (sub_plot[x][y2] !=0):
            #print('this part not is black')
            while (sub_plot[x][y1] != 0):
                y1 = y1+1 #to check right side
                if (y1 == sub_plot.shape[1]):
                    print('turn right')
                    break
            while (sub_plot[x][y2] !=0):
                y2 = y2-1 #to check left side
                if (y2 == 0):
                    print('turn left')
                    break
    
        y = math.floor((y1+y2)/2) #midppoint defined in array  #print(mid_point)
        # print(y)
        cv2.circle(img , (y,x) , (3) , (255, 255, 255),-20) #to put a dot on the midpoint #(width,height)
        cv2.imshow("input",img)
        #cv2.imshow("output",sub_plot)
        Q_y.append(y)
        Q_x.append(x)
        
    for p in range (1):
        x = Q_x
        y = Q_y 
        '''
        y_noise = 2 * np.random.normal(size = len(x))
        ydata = y + y_noise

        plt.plot( ydata,x,  'bo')
        plt.plot(y, x, 'r')
        plt.imshow(img)
        plt.show()
        print(Q_y)
        '''
        #y = 1*(x**3) + 1*(x**2) + 1 * x + 3
        y_noise = 20 * np.random.normal(size = len(x))
        ydata = y + y_noise
        plt.plot( ydata,x,  'bo')
        plt.plot( y,x, 'r')
        plt.ylabel('Dependent Variable')
        plt.xlabel('Independent Variable')
        plt.imshow(img)
        plt.show()
        Q_y.clear() 
        Q_x.clear() 
        
            #print('after',x,Q)
            #Q.clear()
              
        
    cv2.imshow("real", img)
    # cv2.imshow("green", green_mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()    
img.release()
img.destroyAllWindows()
cv2.destroyAllWindows()
