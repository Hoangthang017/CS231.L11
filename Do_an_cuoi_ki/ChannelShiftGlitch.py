import cv2
from PIL import Image
import numpy as np

def effect_glitch(img, n = 10, m = 20):
    # chuyển sang dạng ma trận
    img = np.array(img)
    frame = img.copy()
    # dịch chuyển kênh màu red sang NxM giá trị
    frame[:frame.shape[0] - n,:frame.shape[1] - m,0] = img[n:,m:,0] 

    # dịch chuyển kênh màu blue sang MxN giá trị
    frame[:frame.shape[0] - m,:frame.shape[1] - n,1] = img[m:,n:,1] 

    return frame

def main():
    # đọc hình ảnh
    img_ori = Image.open("./Test/test_1.jpg")
    img_ori.show()

    # áp dụng effect
    img_res = effect_glitch(img_ori)

    # show kết quả
    img_res = Image.fromarray(img_res)
    img_res.show()

if __name__ == "__main__":
    main()
