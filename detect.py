'''
This is a utility file to detect explosions over a collection of frames

Usage:

    python detect.py deaths sample.npy # Detect all player deaths within a file of numpy array data

    or

    python detect.py kills sample.npy # Detect all alien kills within a file of numpy array data

* In the sample file, you can see explosions on frames 123 and 298
* Alien deaths occur in frames 97, 
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys

# Setup score ROI
SCORE_X1 = 0
SCORE_Y1 = 0
SCORE_X2 = 120
SCORE_Y2 = 13

'''
Grabs the current score by selecting the score ROI
'''
def get_score(frame):
    score = cv2.cvtColor(frame[SCORE_Y1:SCORE_Y2, SCORE_X1:SCORE_X2], cv2.COLOR_BGR2GRAY)
    return score

def detect(event, file):
    events = []
    frames = np.load(file)

    if event == "kills":

        # Kills may overlap, making them difficult to detect. They can be roughly detected by lowering
        # the detection threshold, but a more reliable method will be to look for changes in score. 
        # In most cases, a change in score reflects a kill. (During the Challenge Stages, a bonus is 
        # given for total kills. I'm willing to live with this for now.)

        last_score = get_score(frames[0][0])

        for i in range(len(frames)):
            
            frame = frames[i][0]
            current_score = get_score(frame)

            is_different = not np.array_equal(current_score, last_score)
            if is_different:
                events.append(i)
            
            last_score = current_score

        print(f"Alien deaths found in frames:", events)

    elif event == "deaths":

        # We're looking for an exploding hero ship based off the image in hero_explosion.png
        # (encapsulated in pixel format for you at hero_explosion.npy). The explosion animation
        # is 5 frames. We ignore the additional n + 4 frames after first detection
        
        hero_exp = np.load('./hero_explosion.npy')
        w, h, _ = hero_exp.shape

        for i in range(len(frames)):

            frame = frames[i][0]

            res = cv2.matchTemplate(frame, hero_exp, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            loc = np.where(res >= threshold)

            if len(loc[0]) > 0:
                if len(events) == 0:
                    events.append(i)
                elif i > events[-1] + 4:
                    events.append(i)
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)

                # plt.imshow(frame)
                # plt.show()

        print("Hero death found in frames: ", events)

    else:
        exit(f"Unable to look for {event}")

if __name__ == "__main__":

    try:
        detect(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        exit(f'{sys.argv[1]} not found')
