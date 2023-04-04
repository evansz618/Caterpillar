# Caterpillar

Hello! This is the README for our ME35 robotics project. Please remember to create your own branch and work on any changes to code there. I don't anticipate us having to work on the same coding files, but it's useful to keep these around for versioning.

## Vision
The OpenMV cam currently has yet to be tested, but there is currently a program within the Vision folder that should be able to detect the color of an apple and track it. This code was pulled from an arduino tutorial: https://docs.arduino.cc/tutorials/nicla-vision/blob-detection. Since the assignment only asks to detect "something" and then the dog stops, I will record color data for an easy to detect solid color. This information is sent through the serial terminal as a 1 or a 0. Now, there are two ways to get this data to the rest of the dog.

### Sent through ESP
Using previous ME35 code, I can read the necessary information from serial on an ESP32 and then send using an MQTT script.
+ MQTT script already written.
- May be difficult to read in serial since that was a problem I had in previous projects. However, it is possible and I have done it so I could reference old code.
- A little harder to fabricate since I'd be dealing with two boards instead of one. Not a big issue though.

### Sent through Nicla
Since the Nicla has wifi capabilities, I could just publish MQTT from the board.
+ Super streamlined process for coding
+ No extra wires, less complex head design
- I'd have to learn how to connect to wifi, and I know connecting to Tufts Wireless from a microcontroller is annoying.
- Figure out how to setup MQTT on Nicla.

### Enclosure Ideas
https://thangs.com/search/arduino%20nicla%20vision?scope=all
https://www.thingiverse.com/thing:5359047
https://www.thingiverse.com/thing:5759796
