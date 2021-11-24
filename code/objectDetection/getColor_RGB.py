import cv2
import numpy as np

img = cv2.imread('./image/green1.jpg')

# height, width = img.shape[:2]
# img = img[0:height, 0:width-100]
# BGR

MaxR = 0
MaxG = 0
MaxB = 0

MinR = 999999
MinG = 999999
MinB = 999999

for i in img :
    for j in i :
        if MaxR < j[2] :
            MaxR = j[2]
        if MaxG < j[1] :
            MaxG = j[1]
        if MaxB < j[0] :
            MaxB = j[0]

        if MinR > j[2] :
            MinR = j[2]
        if MinG > j[1] :
            MinG = j[1]
        if MinB > j[0] :
            MinB = j[0]

print(MaxR)
print(MaxG)
print(MaxB)

print(MinR)
print(MinG)
print(MinB)

# red
# (46, 28, 103), (110, 110, 231)

# 92, 229, 250
# 27, 106, 122

# 159, 244, 124
# 112, 160, 80


red = cv2.inRange(img, (46, 28, 103), (130, 130, 231))
yellow = cv2.inRange(img, (27, 106, 122), (92, 229, 250))
green = cv2.inRange(img, (100, 200, 0), (160, 244, 124))

# print(red.shape)
# c = np.where(red==255)
# print(c[1])
# print(max(c[1]))
# print(min(c[1]))

value, count = np.unique(green, return_counts=True)

print(value)
print(count)

cv2.imshow('img', img)
# cv2.imshow('red', red)
# cv2.imshow('yellow', yellow)
cv2.imshow('green', green)


cv2.waitKey()
cv2.destroyAllWindows()
