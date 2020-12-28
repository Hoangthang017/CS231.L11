# import thư viện
import skimage
import cv2 
from PIL import Image
import numpy as np


def gauss_noise(img):
    img_noise = skimage.util.random_noise(img,mode="gaussian")
    return (img_noise*255).astype(np.uint8)

def poisson_noise(img):
    img_noise = skimage.util.random_noise(img,mode="poisson")
    return (img_noise*255).astype(np.uint8)

def localvar_noise(img):
    img_noise = skimage.util.random_noise(img,mode="localvar")
    return (img_noise*255).astype(np.uint8)

def salt_noise(img):
    img_noise = skimage.util.random_noise(img,mode="salt")
    return (img_noise*255).astype(np.uint8)

def pepper_noise(img):
    img_noise = skimage.util.random_noise(img,mode="pepper")
    return (img_noise*255).astype(np.uint8)

def main():
    # đọc ảnh
    img_path="./Test/test_1.jpg"
    # img = cv2.imread(img_path)/255.0
    img = Image.open(img_path)
    img = np.array(img)/255

    # hàm tạo hiệu ứng
    img_res = poisson_noise(img)

    Image.fromarray(img_res).show()
    # # show kết quả
    # cv2.imshow("noise",img_res)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    main( )

