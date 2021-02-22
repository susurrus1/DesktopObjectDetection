import cv2
import numpy as np
import cvlib as cv
import win32gui,win32ui,win32con
from win32api import GetSystemMetrics
from desktopmagic.screengrab_win32 import getRectAsImage
from time import sleep

# define the ROI
deviceContext = win32gui.GetDC(0)
deviceObject = win32ui.CreateDCFromHandle(deviceContext)
windowHandle = win32gui.WindowFromPoint((0,0))
monitorDimensions = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
monitorArray = list(monitorDimensions)

# define properties of focus rectangle on screen
win32gui.SystemParametersInfo(win32con.SPI_SETFOCUSBORDERWIDTH,4)
win32gui.SystemParametersInfo(win32con.SPI_SETFOCUSBORDERHEIGHT,4)

# define font properties
logicalFont = win32gui.LOGFONT()
logicalFont.lfFaceName = "Times New Roman"
logicalFont.lfHeight = 32
fontObject = win32gui.CreateFontIndirect(logicalFont)
win32gui.SelectObject(deviceContext,fontObject)

sleepTime = 0.5 # delay used to keep cpu usage down
redrawNumber = 10 # this keeps the rectangle and text long enough on screen to be easily visible

while True:
    screenshot = np.array(getRectAsImage(monitorArray))

    sleep(0.5)
    boundingBoxList,labelList,confidenceList = cv.detect_common_objects(screenshot,confidence=0.1,model="yolov3-tiny")
    print("detected %d objects"%(len(labelList)))

    for detectedIndex in range(len(labelList)):
        boundingBox = boundingBoxList[detectedIndex]
        label = labelList[detectedIndex]

        for redrawIndex in range(redrawNumber):
            deviceObject.DrawFocusRect(tuple(boundingBox))
            deviceObject.DrawText(label,boundingBox,
                           win32con.DT_SINGLELINE | win32con.DT_CENTER | win32con.DT_CENTER | win32con.DT_NOCLIP)

    win32gui.RedrawWindow(windowHandle,None,None,win32con.RDW_INVALIDATE)
