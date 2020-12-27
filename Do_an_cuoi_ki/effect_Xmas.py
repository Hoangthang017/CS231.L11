# import thư viện
import sys
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import cv2 
import urllib.request
from import_file.change_temperature_picture import convert_temp
import os
# hàm đọc file ảnh
def open_image_url():
    url = input()
    try:
        img = Image.open(urllib.request.urlopen(url))
    except:
        print("Lỗi đường dẫn ảnh")
        sys.exit()
    return img

def open_image_folder():
    print('nhập tên ảnh có trong thư mục test: ')
    name = input()
    try:
        img = Image.open("./Test/"+name)
    except:
        print("Lỗi đường dẫn ảnh")
        sys.exit()
    return img


# hàm tạo hiệu ứng giáng sinh
def effect_Christmas(img):
    # resize ảnh gốc và chuyển sang dạng RGBA
    # img_original_resized = img.resize((705,640)).convert('RGBA')
    img_original_resized = img.convert('RGBA')
    # img_original.show()

    # đọc file mask và background
    img_mask = Image.open("./Mask/Snowflake_2.png").resize((img.size[0],img.size[1])).convert('L')
    img_background = Image.open("./Mask/background_snowflake.png").resize((img.size[0],img.size[1]))

    # làm mở ảnh gốc
    img_original_blur = img_original_resized.filter(ImageFilter.GaussianBlur(0.5))

    # ghép ảnh gốc với mask
    result = Image.composite(img_background,img_original_blur,img_mask)

    #tăng độ tương phản cho ảnh 
    result = ImageEnhance.Contrast(result).enhance(1.1)

    # # giảm độ sáng cho ảnh
    # result = ImageEnhance.Brightness(result).enhance(0.9)

    # tăng màu sắc cho ảnh
    result = ImageEnhance.Color(result).enhance(1.4)

    result = convert_temp(result,6500)

    return result
# hàm chính 
def main():
    # show kết quả và ảnh gốc
    img_original = open_image_folder()
    # img_original = open_image_url()

    img_original.show()
    img_result = effect_Christmas(img_original)
    img_result.show()

if __name__ == "__main__":
    main()
