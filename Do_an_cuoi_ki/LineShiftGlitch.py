import cv2
import random
img = cv2.imread('girl.jpg')
width = 500
height = round(width / img.shape[1] * img.shape[0])
img = cv2.resize(img,(width,height))

frame = img.copy()
# number_line = random.randint(100,500)
number_line = 200
for i in range(0,number_line):
	n = random.randint(0,img.shape[0] - 6)
	shift_n = random.randint(0,10)
	color_channel = random.randint(0,2)
	line_ = random.randint(1,6)
	if line_ == 1:
		frame[n,:frame.shape[1] - shift_n,color_channel] = img[n,shift_n:,color_channel]
	elif line_ == 2:
		frame[n,:frame.shape[1] - shift_n,color_channel] = img[n,shift_n:,color_channel]
		frame[n+1,:frame.shape[1] - shift_n,color_channel] = img[n+1,shift_n:,color_channel]
	elif line_ == 3:
		frame[n,:frame.shape[1] - shift_n,color_channel] = img[n,shift_n:,color_channel]
		frame[n+1,:frame.shape[1] - shift_n,color_channel] = img[n+1,shift_n:,color_channel]
		frame[n+2,:frame.shape[1] - shift_n,color_channel] = img[n+2,shift_n:,color_channel]
	elif line_ == 4:
		frame[n,:frame.shape[1] - shift_n,color_channel] = img[n,shift_n:,color_channel]
		frame[n+1,:frame.shape[1] - shift_n,color_channel] = img[n+1,shift_n:,color_channel]
		frame[n+2,:frame.shape[1] - shift_n,color_channel] = img[n+2,shift_n:,color_channel]
		frame[n+3,:frame.shape[1] - shift_n,color_channel] = img[n+3,shift_n:,color_channel]

	elif line_ == 5:
		frame[n,:frame.shape[1] - shift_n,color_channel] = img[n,shift_n:,color_channel]
		frame[n+1,:frame.shape[1] - shift_n,color_channel] = img[n+1,shift_n:,color_channel]
		frame[n+2,:frame.shape[1] - shift_n,color_channel] = img[n+2,shift_n:,color_channel]
		frame[n+3,:frame.shape[1] - shift_n,color_channel] = img[n+3,shift_n:,color_channel]
		frame[n+4,:frame.shape[1] - shift_n,color_channel] = img[n+4,shift_n:,color_channel]
	else:
		frame[n,:frame.shape[1] - shift_n,color_channel] = img[n,shift_n:,color_channel]
		frame[n+1,:frame.shape[1] - shift_n,color_channel] = img[n+1,shift_n:,color_channel]
		frame[n+2,:frame.shape[1] - shift_n,color_channel] = img[n+2,shift_n:,color_channel]
		frame[n+3,:frame.shape[1] - shift_n,color_channel] = img[n+3,shift_n:,color_channel]
		frame[n+4,:frame.shape[1] - shift_n,color_channel] = img[n+4,shift_n:,color_channel]
		frame[n+5,:frame.shape[1] - shift_n,color_channel] = img[n+5,shift_n:,color_channel]
    # frame[n+1,:frame.shape[1] - shift_n,color_channel] = img[n+1,shift_n:,color_channel]
cv2.imwrite('LineShiftGlitch1.jpg',frame)
cv2.imshow('demo',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()