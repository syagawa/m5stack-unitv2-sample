import cv2
from datetime import datetime as dt


size = 3 #0-3
device_id = 0
dir = "/media/sdcard/"

camera = cv2.VideoCapture(device_id)
print(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

if size == 0:
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
elif size == 1:
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
elif size == 2:
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
elif size == 3:
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# elif size == 4:
#   camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#   camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

print(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
print(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

ret, frame = camera.read()

if ret:
    print('Captured')
    d = dt.now()
    filename = "image_" + d.strftime("%Y-%m%d-%H%M%S") + ".jpg"
    print(filename)
    cv2.imwrite(dir + filename, frame)
else:
    print('Could not captured!')