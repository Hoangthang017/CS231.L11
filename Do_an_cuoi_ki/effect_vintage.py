# import thư viện
import cv2
from PIL import Image, ImageEnhance
import numpy as np
from import_file.effect_noise import poisson_noise

# hàm tạo effect
def effect_yellow_pic(img_rgb):
    newImage = img_rgb.copy()		
    i, j, k = img_rgb.shape
    for x in range(i):
        for y in range(j):
            R = img_rgb[x,y,2] * 0.393 + img_rgb[x,y,1] * 0.769 + img_rgb[x,y,0] * 0.189
            G = img_rgb[x,y,2] * 0.349 + img_rgb[x,y,1] * 0.686 + img_rgb[x,y,0] * 0.168
            B = img_rgb[x,y,2] * 0.272 + img_rgb[x,y,1] * 0.534 + img_rgb[x,y,0] * 0.131
            if R > 255:
                newImage[x,y,2] = 255
            else:
                newImage[x,y,2] = R
            if G > 255:
                newImage[x,y,1] = 255
            else:
                newImage[x,y,1] = G
            if B > 255:
                newImage[x,y,0] = 255
            else:
                newImage[x,y,0] = B
    
    newImage = cv2.cvtColor(newImage, cv2.COLOR_BGR2RGB)
    return newImage

# hàm tạo effect
def effect_old_pic(img,blur= 1):
    # đọc texture
    effect_film = Image.open('./Mask/old_noise_film.jpg').convert('L')
    effect_broken = Image.open("./Mask/old_paper.jpg").convert('L')

    # resize texture 
    effect_broken = effect_broken.resize(img.size)
    effect_film = effect_film.resize(img.size)

    # apply textture
    img.paste(effect_film,mask=effect_film)
    img.paste(effect_broken,mask= effect_broken)

    # # show
    # img.show()

    # convert array
    img = np.array(img)

    # make noise
    img_noise = poisson_noise(img)

    # blur
    img_noise = cv2.GaussianBlur(img_noise,(blur,blur),0)

    # render vintage 
    img_vintage = effect_yellow_pic(img_noise)

    return img_vintage

# hàm chính
def main():
    # đọc ảnh 
    img_ori = Image.open('./Test/test_5.png').convert('RGBA')
    img_ori.show()

    # tạo hiệu ứng
    img_res = effect_old_pic(img_ori)

    # im kết quả 
    img_res = Image.fromarray(img_res)
    img_res.show()

# hàm chính
if __name__ == "__main__":
    main()


