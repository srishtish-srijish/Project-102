import cv2

def take_snapshot():
    videoCaptureObject=cv2.VideoCapture(cv2.CAP_DSHOW)
    result=True
    while(result):
        #Read the frames while the camera is on
        ret,frame=videoCaptureObject.read()

        #method used to save a screenshot to any storage device
        cv2.imwrite("NewPicture1.jpg",frame)
        result=False

    #releasing the camera
    videoCaptureObject.release()

    #close all the windows
    cv2.destroyAllWindows()

take_snapshot()

