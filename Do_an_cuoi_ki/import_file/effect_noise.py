# import thư viện
import skimage
import cv2 
from PIL import Image
import numpy as np


def gauss_noise(img):
    img_noise = skimage.util.random_noise(img,mode="gaussian")
    return img_noise

def poisson_noise(img):
    img_noise = skimage.util.random_noise(img,mode="poisson")
    return img_noise

def localvar_noise(img):
    img_noise = skimage.util.random_noise(img,mode="localvar")
    return img_noise

def salt_noise(img):
    img_noise = skimage.util.random_noise(img,mode="salt")
    return img_noise

def pepper_noise(img):
    img_noise = skimage.util.random_noise(img,mode="pepper")
    return img_noise

def main():
    # đọc ảnh
    img_path="./Test/test_1.jpg"
    img = cv2.imread(img_path)/255.0

    # hàm tạo hiệu ứng
    img_res = poisson_noise(img)

    # show kết quả
    cv2.imshow("noise",img_res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

