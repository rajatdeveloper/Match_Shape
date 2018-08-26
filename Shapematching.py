import cv2
import numpy as np

template = cv2.imread('Shapematching.jpg')
cv2.imshow('shape',template)
cv2.waitKey(0)

template_gray = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)

target = cv2.imread('shapes.jpg')
cv2.imshow('Target Image',target)
cv2.waitKey(0)

target_gray = cv2.cvtColor(target,cv2.COLOR_BGR2GRAY)

ret1,thresh1 = cv2.threshold(template_gray,127,255,0)
cv2.imshow('thresh1',thresh1)
cv2.waitKey(0)

ret2,thresh2 = cv2.threshold(target_gray,127,255,0)
cv2.imshow('thresh2',thresh2)
cv2.waitKey(0)

boolean1,contours1,hirearchy1 = cv2.findContours(thresh1,cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
sortedcontour1 = sorted(contours1,key = cv2.contourArea,reverse = True)

template_contour = sortedcontour1[1]

boolean2,contours2,hirearchy2 = cv2.findContours(thresh2,cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

min = 100
closest_contour = []
for c in contours2:
    match = cv2.matchShapes(template_contour,c,1,0.0)
    if min>match:
        min = match
        closest_contour=c

cv2.drawContours(target,[closest_contour],-1,(0,255,0),3)
cv2.imshow('targeted',target)
cv2.waitKey(0)
