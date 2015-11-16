# Vision Control
This Python2.7 package is an OpenCV tool, designed to monitor a web camera and emit OSC messages based on what it sees in that camera. Currently, it contains none of that functionality, but is slowly growing it.

## Dependencies
* OpenCV 3
* Numpy
* Scipy

# Running
Currently, only one command is implemented:

    python -m visioncontrol build

This will scan the images located in the visioncontrol/data/images folder and construct Orb-based models of those images, and save those models to visioncontrol/data/descriptors

# Next Steps
The next step is to hook this up to a camera.