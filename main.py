import cv2 as cv

cp = cv.VideoCapture("TestVid.mp4")

ht = int(cp.get(cv.CAP_PROP_FRAME_HEIGHT))
wt = int(cp.get(cv.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)

path = "SlowedVideo.mp4"
fcc = cv.VideoWriter_fourcc(*'mp4v')

output = cv.VideoWriter(path, fcc, 2,
						(wit, ht))

while True:
	ret, frame = cp.read()
	cv2.imshow("frame", frame)
	output.write(frame)
	k = cv.waitKey(24)
	if k == ord("q"):
		break

cp.release()
output.release()
cv.destroyAllWindows()
