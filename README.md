# DesktopObjectDetection
Detects and identifies objects in real time in anything visible on the Windows desktop

***Motivation***

I have been playing with cvlib to identify objects in images and videos using TensorFlow with the YOLOv3 model, but I wanted to draw a bounding box and label for the objects directly on the original video, rather than pop up a new window (e.g., using opencv) and draw them there.  My initial motivation was to be able to display this kind of information directly on a game displayed on the desktop.

***Installation***

The code was written in Python 3.7 on Windows 10.  You will need to first install the necessary modules (or you can download them from pypi.org):

*pip install opencv-python*
*pip install numpy*
*pip install tensorflow*
*pip install cvlib*
*pip install pywin32*
*pip install Desktopmagic*

Installing *pywin32* should give you access to the *win32gui*, *win32ui*, *win32con*, and *win32api* libraries.  The *time* module should be part of the standard python library and you shouldn't have to install it.  The program uses the yolov3-tiny model instead of the full yolov3 model because it is meant to run with limited resources (i.e. CPU instead of GPU).

***Usage***

Once the libraries are installed, just run the main code, e.g. by executing

*python DesktopDet.py*

from a command line, or start it from an IDE if you use one.  If you have two monitors, the code will read from and plot to the main monitor so you could run your code in the second monitor so it's not in the way (or alternately minimize whatever window or IDE it's running in).  If you start a youtube video on the main monitor for example, the code will try to detect objects in that video, provided the window containing the video is on top and not hidden behind another window or minimized.

If you want to use the program to detect objects in a video game, you will need to run the game in windowed mode (by pressing ALT-ENTER), and no fullscreen.  This is because when in full screen, most games will use DirectX to control the display, which my code does not do and therefore you will not see anything displayed on top of the game.  If the game looks choppy, you can reduce the CPU usage of the code by increasing the value of the *sleepTime* variable (currently set at 0.5 seconds), and if the rectangle and text label do not remain displayed long enough to be seen, you can increase the *redrawNumber* variable (currently set at 10).

Note: in principle, pressing the "q" key should stop the program, but this does not appear to work properly at this time.  The program can still be stopped using CTRL-C if it's running from a command prompt, or however you normally stop programs if it's running in an IDE.

***Credits***

My motivation to use cvlib for object detection came from this blog post: https://towardsdatascience.com/object-detection-with-less-than-10-lines-of-code-using-python-2d28eebc5b11

I figured out how to draw to the desktop thanks to this entry: https://stackoverflow.com/questions/62341134/how-to-draw-an-empty-rectangle-on-screen-with-python

