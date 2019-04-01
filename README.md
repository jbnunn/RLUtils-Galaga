# RLUtils-Galaga
Reinforcement Learning Utilities for Galaga

## About

This repository provides utilities building datasets to train AI to play Galaga.

### Explosion Detection

Identifies frame(s) in which explosions of the player's ship are detected, and provides last-n moves that led to explosion.

### Kill Detection

Identifies frame(s) in which the player gets a kill, and provides last-n moves that led to explosion

### Data Format

Frames contain Numpy arrays of 3-channel pixel data as the first element and the associated "move" for each frame as the second.

* The first element of pixel data has a shape of (450, 358, 3)
* The second element is the move represented as one of the following one-hot vector encodings:
    
        [1, 0, 0, 0, ,0 ,0] # left + fire
        [0, 1, 0, 0, ,0 ,0] # right + fire
        [0, 0, 1, 0, ,0 ,0] # left
        [0, 0, 0, 1, ,0 ,0] # right
        [0, 0, 0, 0, ,1 ,0] # fire
        [0, 0, 0, 0, ,0 ,1] # (no move)
    
## Getting Started

### About the sample data

There are 498 frames of sample data in `sample.npz`. You can decompress the file to make it easier to work with:

    >>> import numpy as np
    
    >>> f = np.load('./sample.npz')
    >>> sample = f['arr_0']
    >>> np.save('sample.npy', sample)
    
 Inspect the decompressed data:
 
    # If in a new shell...
    # >>> import numpy as np
    # >>> sample = np.load('./sample.npy')
    
    >>> sample.shape
    (498, 2)
    >>> frame_0 = sample[0]
    >>> frame_0[0].shape
    (450, 358, 3)
    >>> frame_0[1]
    [0, 0, 0, 1, 0, 0] # right
 
### View the frames

![](sample.png)

Make sure you have OpenCV installed. Then, debug each frame of the sample frames with:

    python view.py sample.npy

Use the keypad `6` to step forward through the frames, and `4` to step backwards. If you don't have a keypad, or want to change the forward and back keys, you can make the changes in the `debug_frame` method.

Use `q` to exit and destroy the window.



