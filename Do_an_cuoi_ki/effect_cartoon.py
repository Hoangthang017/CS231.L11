import cv2

# hàm tạo hiệu ứng
def render(img_rgb):
	# số bước làm nhỏ ảnh
	numDownSamples = 1      

	# số bước sử dụng bộ lọc song phương
	numBilateralFilters = 50

	# Làm nhỏ ảnh sử dụng Gaussian Pynamids
	img_color = img_rgb
	for _ in range(numDownSamples):
		img_color = cv2.pyrDown(img_color)
	cv2.imshow("downcolor",img_color)

	# liên tục áp dụng bộ lọc 2 bên nhỏ thay vì sử dụng một bộ lọc lớn
	for _ in range(numBilateralFilters):
		img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
	cv2.imshow("bilateral filter",img_color)

	# phóng to ảnh trở lại kích thước gốc
	for _ in range(numDownSamples):
		img_color = cv2.pyrUp(img_color)
	cv2.imshow("upscaling",img_color)


	# chuyển sang dạng ảnh xám và áp dụng độ mờ trung bình
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
	img_blur = cv2.medianBlur(img_gray, 3)
	cv2.imshow("grayscale+median blur",img_blur)

	# nhận diện cạnh và tô các cạnh 
	img_edge = cv2.adaptiveThreshold(img_blur, 255,
									cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
									cv2.THRESH_BINARY,9, 10)
	cv2.imshow("edge",img_edge)

	# chuyển từ ảnh xám thành màu để nó có thể 
	(x,y,z) = img_color.shape
	img_edge = cv2.resize(img_edge,(y,x))
	img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
	# cv2.imwrite("edge.png",img_edge)
	# cv2.imshow("step 5", img_edge)

	return cv2.bitwise_and(img_color, img_edge)

# hàm chính 
def main():
	# đọc ảnh 
	img_rgb = cv2.imread("./Test/test_1.jpg",1)

	# tạo hiệu ứng
	img_vintage = render(img_rgb)

	cv2.imshow('original',img_rgb)
	cv2.imshow('cartoon',img_vintage)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

# hàm chính
if __name__ == "__main__":
	main()