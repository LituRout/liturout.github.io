import matplotlib.pyplot as plt
import cv2
import os

path = 'images/'
files = os.listdir(path)
files = [file for file in files if file.endswith('png')]

print(files)
for file in files:
    print('Processing file: ', file)
    img = cv2.imread(path+file, cv2.IMREAD_UNCHANGED)
    img = cv2.resize(img, (160,160), interpolation = cv2.INTER_AREA)
    cv2.imwrite(path+file, img)

    

