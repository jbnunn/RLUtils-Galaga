'''
This is a utility file to detect explosions over a collection of frames

Usage:

    python detect.py explosions sample.npy

In the sample file, you can see explosions on frames 123 and 298
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys

def detect(event, file):
    events = []
    frames = np.load(file)

    if event == "explosions":

        # We're looking for an exploding hero ship based off the image in hero.png
        # (encapsulated in pixel format for you at hero.npy). The explosion animation
        # is 5 frames. We ignore the additional n + 4 frames after first detection
        
        hero = np.load('./hero.npy')
        w, h, _ = hero.shape

        for i in range(len(frames)):

            frame = frames[i][0]

            res = cv2.matchTemplate(frame, hero, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where( res >= threshold)

            if len(loc[0]) > 0:
                if len(events) == 0:
                    events.append(i)
                elif i > events[-1] + 4:
                    events.append(i)
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)

        print("Explosions found in frames: ", events)

if __name__ == "__main__":

    try:
        detect(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        exit(f'{sys.argv[1]} not found')
