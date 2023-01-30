import cv2

camera_index = 0
camera = cv2.VideoCapture(camera_index)
while True:
    available, _ = camera.read()
    if not available:
        camera_index += 1
        camera = cv2.VideoCapture(camera_index)
    else:
        print(f"Camera device {camera_index} is available.")
        break
camera.release()
