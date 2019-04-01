'''
This is a utility file to view a particular frame within captured frame data:

Usage:

    python view.py sample.npy

'''

import numpy as np
import cv2
import sys

def convert_encoding_to_move(encoding):

    if encoding == [1, 0, 0, 0, 0, 0]:
        return "left+fire"
    elif encoding == [0, 1, 0, 0, 0, 0]:
        return "right+fire"
    elif encoding == [0, 0, 1, 0, 0, 0]:
        return "left"
    elif encoding == [0, 0, 0, 1, 0, 0]:
        return "right"
    elif encoding == [0, 0, 0, 0, 1, 0]:
        return "fire"
    elif encoding == [0, 0, 0, 0, 0, 1]:
        return "-"

def debug_frame(frame, frame_num):

    img = frame[0]
    control = frame[1]

    label = str(frame_num) + ": " + convert_encoding_to_move(control)

    width = img.shape[1]
    height = img.shape[0]

    overlay_x = 10
    overlay_y = height - 50

    overlay_img = cv2.cvtColor(np.zeros((height, width), np.uint8),cv2.COLOR_GRAY2RGB)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(overlay_img, label, (overlay_x, overlay_y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    composite_img = cv2.addWeighted(img, 0.7, overlay_img, 0.7, 0)

    cv2.imshow('window', composite_img)
    cv2.moveWindow('window', 110, 110)

    k = cv2.waitKey(0)
    if k == ord('q'):
        cv2.destroyAllWindows()
        return "exit"
    elif k == ord('4'):
        return "step_back"
    elif k == ord('6'):
        return "step_forward"
    else:
        return None

def view(file):
    while True:
        frames = np.load(file)
        i = 0
        while i < len(frames):
            frame = frames[i]
            k = debug_frame(frame, i)
            if k == 'exit':
                cv2.destroyAllWindows()
                exit()
            elif k == 'step_back':
                i -= 1
                if i < 0:
                    i = 0
            elif k == 'step_forward':
                i += 1



if __name__=="__main__":

    try:
        view(sys.argv[1])
    except FileNotFoundError:
        exit(f'{sys.argv[1]} not found')
