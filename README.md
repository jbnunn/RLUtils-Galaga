# RLUtils-Galaga
Reinforcement Learning Utilities for Galaga

## About

This repository provides utilities building datasets to train AI to play Galaga:

### Explosion Detection

Identifies frame(s) in which explosions of the player's ship are detected, and provides last-n moves that led to explosion.

### Kill Detection

Identifies frame(s) in which the player gets a kill, and provides last-n moves that led to explosion

### Data Format

* Input frames should be Numpy arrays of 3-channel pixel data


