from PIL import Image, ImageEnhance
from glob import glob
import cv2
import numpy as np

def effect_hdr(imgs):
    # hợp nhất các ảnh phơi sáng bằng thuật toán Mertens
    merge_mertens = cv2.createMergeMertens()
    res_mertens = merge_mertens.process(imgs)

    # chuyển về định dạng chuẩn
    res_mertens_8bit = np.clip(res_mertens*255, 0, 255).astype('uint8')
    return res_mertens_8bit

def hdr(img, rg = 1.8):
    # tạo list ảnh và độ sáng của nó 
    times = []
    i = 0.5
    while(i <= rg):
        times.append(i)
        i = i + 0.1

    img_list = []
    for time in times:
        # điều chỉnh độ sáng của hình ảnh
        result = ImageEnhance.Brightness(img).enhance(time)
        img_temp = np.array(result)
        img_list.append(img_temp)

    # áp dụng effect 
    res = effect_hdr(img_list)

    # convert cv qua pillow
    res = Image.fromarray(res)

    return res 

def main():
    # đọc hình ảnh
    img_ori = Image.open("./Test/test_1.jpg")
    img_ori.show()

    # khởi tạo hiệu ứng 
    img_res = hdr(img_ori)

    # show kết quả
    img_res.show()

if __name__ == "__main__":
    main()


