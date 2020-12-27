# from PIL import Image, ImageDraw, ImageFilter, ImageOps

# RADIUS = 10

# # Open an image
# img_ori = Image.open("./Test/test_1.jpg").convert("RGBA")

# def img_blur_borded(im):

#     # Paste image on white background
#     diam = 2*RADIUS
#     back = Image.new('RGB', (im.size[0]+diam, im.size[1]+diam), (200,200,200))
#     back.paste(im, (RADIUS, RADIUS))

#     back.show()

#     # Create blur mask
#     mask = Image.new('L', (im.size[0]+diam, im.size[1]+diam), 255)
#     blck = Image.new('L', (im.size[0]-diam, im.size[1]-diam), 0)
#     mask.paste(blck, (diam, diam)) 
#     mask.show()
#     # Draw rectangle 
#     img_rec = ImageDraw.Draw(back)
#     img_rec.rectangle(((diam,diam),(im.size[0]-1, im.size[1]-1)),width=2,outline='black')

#     # Blur image and paste blurred edge according to mask
#     blur = back.filter(ImageFilter.GaussianBlur(RADIUS/2))
#     back.paste(blur, mask=mask)

#     return back

# def rotate_blur_borded(im, diam = 40):
#     im = im.resize((600,600))
#     angle = 30
#     shape = im.size
#     # Rotation image

#     # Paste image on white background
#     # back = Image.new('RGB', (shape[0]+diam, shape[1]+diam), (200,200,200))
#     # mask = Image.new("L",back.size,255)
#     # mask = mask.rotate(angle,expand=True)
#     # back = back.rotate(angle,expand=True)
#     # back.paste(im, (RADIUS, RADIUS))

#     # Create blur mask
#     mask = Image.new('L', (im.size[0] , im.size[1]), 255)
#     blck = Image.new('L', (im.size[0]-diam, im.size[1]-diam), 0)
#     mask.paste(blck, (diam//2, diam//2)) 
#     mask.show()

#     # rotate_mask = rotate_no_back(mask)
#     # rotate_mask = rotate_mask.resize((600,600))
#     # rotate_mask = ImageOps.invert(rotate_mask)
#     # print(rotate_mask.size)
#     # rotate_mask.show()

#     # mask_rectangle = Image.open("./Mask/mask_rectangle.jpg").convert("L")
#     # mask_rectangle.show()
#     # mask_rectangle = mask_rectangle.resize((600,600))
#     # Draw rectangle 
#     img_rec = ImageDraw.Draw(im)
#     img_rec.rectangle(((diam//2,diam//2),(im.size[0]-diam//2 -1 , im.size[1]-diam//2 -1 )),width=2,outline='black')

#     # Blur image and paste blurred edge according to mask
#     blur = im.filter(ImageFilter.GaussianBlur(5))
#     im.paste(blur, mask=mask)

#     return im

# def rotate_no_back(img, angle = 30):
#     mask = Image.new("L",img.size,255)
#     mask = mask.rotate(angle,expand=True)
#     return mask

# # shape = (int(img_ori.size[0]*2/3),int(img_ori.size[0]*2/3))

# # img_new = Image.new('L',shape,color='black')
# # img_new = img_blur_borded(img_new)
# # img_new.show()

# # img_sub,mask = rotate_no_back(img_new)

# # # img_sub = img_ori.crop((0,0,img_sub.size[0],img_sub.size[1]))

# # img_ori.paste(img_sub,mask)

# # img_ori.show()


# img_res = rotate_blur_borded(img_ori)
# img_res.show()
