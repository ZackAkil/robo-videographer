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
- [x] Source tri-pod
- [x] Mount servo to tri-pod
- [x] Mount camera to tri-pod
- [x] Mount Pi to tri-pod
- [x] Mount Power to tri-pod
- [x] 3D model case
- [ ] wire up power splitter

### Extra Software
- [ ] Load via new sd card
- [ ] Get Pi to act as wifi base
- [ ] Connect android to Pi by wifi
- [ ] View image from camera on android via wifi

### Notes

Use `sudo modprobe bcm2835-v4l2` to activate camera.
