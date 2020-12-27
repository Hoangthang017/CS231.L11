import cv2

# lấy bản phác thảo 
def dodgeV2(x, y):
    return cv2.divide(x, 255 - y, scale=256)

def effect_sketch(img):
    # chuyển sang dạng ảnh xám
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # đảo ngược màu sắc của hình ảnh
    img_invert = cv2.bitwise_not(img_gray)

    # làm mờ ảnh
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)

    # hình ảnh bút chì 
    final_img = dodgeV2(img_gray, img_smoothing)

    return final_img

# hàm chính
def main():
    # đọc file
    img = cv2.imread('./Test/test_1.jpg',1)

    # tạo hiệu ứng
    img_res = effect_sketch(img)

    # show kết quả
    cv2.imshow('original',img)
    cv2.imshow("final",img_res)
    cv2.waitKey(0)

# hàm chính
if __name__ == "__main__":
    main()