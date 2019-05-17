import numpy as np
import cv2

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        ret, frame2 = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        d = cv2.absdiff(frame, frame2)
        cv2.imshow('d', d)

main()