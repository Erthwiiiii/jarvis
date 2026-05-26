import cv2
from PIL import ImageGrab

# OPEN WEBCAM

def open_camera():

    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read()

        cv2.imshow("JARVIS CAMERA", frame)

        key = cv2.waitKey(1)

        if key == 27:
            break

    cap.release()

    cv2.destroyAllWindows()


# TAKE SCREENSHOT

def take_screenshot():

    image = ImageGrab.grab()

    image.save("screenshot.png")

    return "Screenshot saved."