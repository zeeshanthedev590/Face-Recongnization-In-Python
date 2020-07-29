import cv2

# Loading The Cascade File
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Reading the Input Image
image = cv2.imread('WIN_20200729_02_15_38_Pro.jpg')

# Resizing the Image
img = cv2.resize(image, None, fx=0.6, fy=0.6)

# Converting the image into grayscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting The Faces
faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

# Pointing The Faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Displaying The Output Image
cv2.imshow('The Master Piese By Zeeshan', img)
cv2.waitKey()
