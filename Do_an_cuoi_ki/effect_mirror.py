import cv2
import numpy as np
from PIL import Image

# option và mode có 2 chế độ 
# option 0 : ảnh ngang
# option 1 : ảnh dọc
#  mode = 0 : nhìn vào nhau , mode 1 : ngược lại
def effect_mirror(img,option=0,mode=0):
  #get original image size
  img_size = img.size

  #option = 0: horizontally
  if option == 0:
    #flip image horizontally
    hor_flippedImg = img.transpose(Image.FLIP_LEFT_RIGHT)

    #create a new image
    new_img = Image.new('RGB',(2*img_size[0], img_size[1]), (250,250,250))

    #merge 2 images
    #mode 0: original image placed left
    #mode 1: original image placed right
    if mode == 0:
      img1 = img
      img2 = hor_flippedImg
    else:
      img1 = hor_flippedImg
      img2 = img
    new_img.paste(img1,(0,0))
    new_img.paste(img2,(img_size[0],0))
    return new_img

  #option = 1: vertically 
  if option == 1:
    #flip image vertically
    ver_flippedImg = img.transpose(Image.FLIP_TOP_BOTTOM)

    #create a new image
    new_img = Image.new('RGB',(img_size[0], 2*img_size[1]), (250,250,250))

    #merge 2 images
    #mode 0: original image placed upper
    #mode 1: original image placed lower
    if mode == 0:
      img1 = img
      img2 = ver_flippedImg
    else:
      img1 = ver_flippedImg
      img2 = img
    new_img.paste(img1,(0,0))
    new_img.paste(img2,(0,img_size[1]))
    return new_img

def main():
    #read image
    img_org = Image.open('./Test/test_1.jpg')
    # img_org = np.array(img_org)
  
    # cv2.imshow("origin",img_org)

    img_res = effect_mirror(img_org)
    
    img_res.show()

if __name__ == "__main__":
  main()
