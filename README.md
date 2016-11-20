# Robo Videographer
Project for a automatic videographer system for recording sports matches.

## Technical objective
The aim is to create a computer vision tracking system that can run on a Raspberry Pi using the camera module that tracks the action happening on a rugby pitch.

## Implimentation goal
The final aim is to use the system to record a tag rugby matches with next to no human intervention. 

## Technology to use
* Raspberry Pi
* Raspberry Pi Camera module
* OpenCV | SimpleCV
* Video camera
* Servo

## Intial Design
1. Get OpenCV/SimpleCV working on the Raspberry Pi with the camera.
2. Build a program that tracks the pixel activity (with directional momentum).
3. Output activity value to a servo position.

## Progress
- [x] Get OpenCV/SimpleCV working on computer
- [x] Develope simple "action tracking"
- [ ] Develope simple servo control on raspberry pi
- [ ] Add "smooth action tracking"
- [ ] Get OpenCV/SimpleCV working on raspberry pi
- [ ] Merge action tracking with servo control
