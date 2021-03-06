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
- [x] wire up power splitter

### Extra Software
- [x] Load via new sd card
- [x] Add script auto-run with switch
- [ ] Get Pi to act as wifi base
- [ ] Connect android to Pi by wifi
- [ ] View image from camera on android via wifi

### Other processes
- [x] Collect training data
- [x] Build tool to help label training data
- [x] Label training data

### Notes

Use `sudo modprobe bcm2835-v4l2` to activate camera.

### Resources

http://www.raspberrypi-spy.co.uk/2015/02/how-to-autorun-a-python-script-on-raspberry-pi-boot/

https://gpiozero.readthedocs.io/en/stable/recipes.html

https://en.wikipedia.org/wiki/Optical_flow

http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html

https://www.modmypi.com/blog/how-do-i-power-my-raspberry-pi

https://en.wikipedia.org/wiki/Recurrent_neural_network

### Testing 
- [ ] Compare feature engineering with prediction speed and accuracy
- [ ] Compare temporal framing sizes with prediction speed and accuracy
