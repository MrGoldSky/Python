import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fps = 20.0
image_size = (640, 480)
video_file = 'res.avi'

# Check if the webcam is opened correctly
if not cap.isOpened():
	raise IOError("Cannot open webcam")

out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'XVID'), fps, image_size)

while True:
    # Capture the video frame
    # by frameqq
    ret, frame = cap.read()
    # Display the resulting frame
    out.write(frame)
    cv2.imshow('frame', frame)
    # the 'q' button is set as theq
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Successfully saved")