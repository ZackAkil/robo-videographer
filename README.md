# Robo Videographer
Project for a automatic videographer system for recording sports matches.

## Technical objective
The aim is to create a computer vision tracking system that can run on a Raspberry Pi using the camera module that tracks the action happening on a rugby pitch.

## Implimentation goal
The final aim is to use the system to record a tag rugby matches with no human intervention. 

## Technology to use
* Raspberry Pi
* Raspberry Pi Camera module
* OpenCV | SimpleCV
* Video camera
* Servo

## Intial Design
1. Get OpenCV/SimpleCV working on the Raspberry Pi with the camera.
2. Build a program that tracks the pixel activity.
3. Output activity value to a servo position.

## Progress
### Software
- [x] Get OpenCV/SimpleCV working on computer
- [x] Develope simple "action tracking"
- [x] Develope simple servo control on raspberry pi
- [x] Add "smooth action tracking"
- [x] Get OpenCV/SimpleCV working on raspberry pi
- [x] Merge action tracking with servo control
- [x] Optimise action finding code to run faster 
- [x] Add concurrency between servo control and action detection using [python processes](https://docs.python.org/2/library/multiprocessing.html)

### Hardware
- [ ] Design enclosure
- [x] Source tri-pod
- [ ] Mount servo to tri-pod
