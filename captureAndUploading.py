import cv2
import random
import dropbox
import time

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result=True
    while(result):
        #Read the frames while the camera is on
        ret,frame=videoCaptureObject.read()

        img_name="img"+str(number)+".png"

        #method used to save an image to any storage device
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False

    return img_name
    print("SnapShot taken")


    #releasing the camera
    videoCaptureObject.release()

    #close all the windows
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_Token="aWjd3wahwLUAAAAAAAAAAfNpkfY7SpJYBUiAIAJkLkUURbj60AsIgKVD2fiRb0T8"
    file=img_name
    file_from=file
    file_to="/testfolder/"+(img_name)
    dbx=dropbox.Dropbox (access_Token)

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print ("FileUploaded")

def main():
    while (True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)



main()

