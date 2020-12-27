# import thư viện
import cv2
import numpy as np

# hàm tạo effect hdr 
def effect_hdr(img,time= 15.0,gam= 1.3):
    # Tạo ảnh hdr
    merge_debevec = cv2.createMergeDebevec()
    hdr_debevec = merge_debevec.process([img], times=np.array([time],dtype=np.float32))
    # merge_robertson = cv2.createMergeRobertson()
    # res_robertson = merge_robertson.process(img_original, times=time.copy())

    # tạo tonemap
    tonemap1 = cv2.createTonemap(gamma= gam)
    res_debevec = tonemap1.process(hdr_debevec.copy())

    # merge_mertens = cv2.createMergeMertens()
    # res_mertens = merge_mertens.process(img_original)

    # chuyển về định dạng chuẩn
    res_debevec_8bit = np.clip(res_debevec*255, 0, 255).astype('uint8')
    # res_robertson_8bit = np.clip(res_robertson*255, 0, 255).astype('uint8')
    # res_mertens_8bit = np.clip(res_mertens*255, 0, 255).astype('uint8')

    return res_debevec_8bit

# hàm chính
def main():
    # đọc ảnh
    img_ori = cv2.imread('./Test/test_2.jpg',1)

    # show ảnh gốc
    cv2.imshow('original',img_ori)

    # ảnh gốc
    cv2.imshow('original',img_ori)

    # chỉnh sửa 
    img_res = effect_hdr(img_ori)

    cv2.imshow('debevec',img_res)
    # cv2.imshow('robertson',res_robertson_8bit)
    # cv2.imshow('mertens',res_mertens_8bit)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# hàm chính
if __name__ == "__main__":
    main()
