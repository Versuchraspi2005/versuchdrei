import time
from picamera import PiCamera

def main():
    camera = PiCamera()
    camera.start_preview()
    for i in range(5):
        time.sleep(10)
        camera.capture("/home/pi/Pictures1/camera.jpg")
    camera.stop_preview()
    
if __name__=="__main__":
    main()