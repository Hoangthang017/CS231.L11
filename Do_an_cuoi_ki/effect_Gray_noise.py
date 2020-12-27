# import thư viện
from PIL import Image, ImageEnhance, ImageFilter
from import_file.effect_noise import poisson_noise
import cv2 
import numpy as np

# hàm effect
def effect_old_gray(img,contrast= 1.7, blur = 0.5):
    # chuyển sang ảnh xám 
    img = ImageEnhance.Color(img).enhance(0.0)

    # tăng độ tương phải cho ảnh 
    img = ImageEnhance.Contrast(img).enhance(contrast)

    # làm mờ ảnh
    img = img.filter(ImageFilter.GaussianBlur(blur))

    # chuyển sang dạng mảng
    img = np.array(img)

    # thêm nhiễu
    img_res = poisson_noise(img/255.0)

    # trả về
    return img_res

# hàm chính
def main():
    # đọc ảnh
    img_ori = Image.open("./Test/Test_1.jpg").convert('RGBA')
    img_ori.show()

    # chỉnh ảnh
    img_res = effect_old_gray(img_ori)

    # show ảnh
    cv2.imshow("res",img_res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# hàm chính
if __name__ == "__main__":
    main()