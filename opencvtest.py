import cv2
import numpy as np

def main():
    folder_path = "E:\opencv\standard_test_images"
    img_path = folder_path + "\lake.tif"
    img = cv2.imread(img_path, 0)
    print (img)
    cv2.imshow("gray", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
