import cv2

# hàm tạo hiệu ứng
def render(img_rgb):
    numDownSamples = 2       # number of downscaling steps
    numBilateralFilters = 50  # number of bilateral filtering steps

		# -- STEP 1 --
		# downsample image using Gaussian pyramid
    img_color = img_rgb
    for _ in range(numDownSamples):
        img_color = cv2.pyrDown(img_color)
		
		# repeatedly apply small bilateral filter instead of applying
		# one large filter
    for _ in range(numBilateralFilters):
        img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
		
		# upsample image to original size
    for _ in range(numDownSamples):
        img_color = cv2.pyrUp(img_color)
		
		# -- STEPS 2 and 3 --
		# convert to grayscale and apply median blur
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 3)
		
		# -- STEP 4 --
		# detect and enhance edges
    img_edge = cv2.adaptiveThreshold(img_blur, 255,
									    cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY,9, 2)
		
		# -- STEP 5 --
		# convert back to color
    (x,y,z) = img_color.shape
    img_edge = cv2.resize(img_edge,(y,x))
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
		#cv2.imwrite("edge.png",img_edge)
    return img_edge

def main():
  # đọc ảnh 
  img_rgb = cv2.imread("./Test/test_5.png",1)
  cv2.imshow('original',img_rgb)

  # tạo hiệu ứng 
  img_sketch = render(img_rgb)

  # show kết quả
  cv2.imshow('sketch',img_sketch)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

# hàm chính
if __name__ == "__main__":
  main()