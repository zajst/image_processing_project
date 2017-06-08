# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
import itertools

cap = cv2.VideoCapture(0)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
i=0
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(20, 20)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	print("Found {0} faces!".format(len(faces)))

	# Draw a circle around the faces
	for (x, y, w, h) in faces:
		if i>1:
#			a = [[x1 for x1 in range(x-3, x+3)], [y1 for y1 in range(y-3, y+3)], [w1 for w1 in range(w-3, w+3)], [h1 for h1 in range(h-3, h+3)]]


#			if any(list(itertools.product(*a))) in faces2:
			if (x, y, w, h) in faces2 or (x-1, y-1, w, h) in faces2 or (x-1, y, w, h) in faces2 or (x-1, y+1, w, h) in faces2 or (x, y-1, w, h) in faces2 or (x, y, w, h) in faces2 or (x, y+1, w, h) in faces2 or (x+1, y-1, w, h) in faces2 or (x+1, y, w, h) in faces2 or (x+1, y+1, w, h) in faces2:
				cv2.circle(frame, (x+w/2, y+h/2), w/2, (0, 255, 0), 2)
				print('message')
				continue
			else:
				cv2.circle(frame, (x+w/2, y+h/2), w/2, (100, 255, 255), 2)






	faces2 = faces
	i+=1

	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
