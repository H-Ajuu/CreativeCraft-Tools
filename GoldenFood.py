import numpy as np
import os
import cv2
import os.path
import glob
def processIMG(filename):
    imgname=os.path.basename(filename)
    src=cv2.imread("C:/Users/zyw/Desktop/PStest/MC/food/"+imgname,cv2.IMREAD_UNCHANGED)#读取png图片
	
    w=src.shape[0]#获取图片的宽高
    h=src.shape[1]
	
    zero = np.zeros((src.shape), dtype=np.uint8)#获得原图大小的空白图层
    mask=cv2.rectangle(zero, (0,0), (w,h), (0,255,255), -1)#在图层上绘制滤镜
    mask_img = cv2.addWeighted(src, 1, mask, 0.35, 0)#在原图上叠加滤镜
    cv2.imwrite("C:/Users/zyw/Desktop/PStest/MC/food/output/"+imgname,mask_img,[cv2.IMWRITE_PNG_COMPRESSION,9])#保存修改后的图片

for filename in glob.glob(r'C:/Users/zyw/Desktop/PStest/MC/food/*.png'):
    processIMG(filename)#循环读取目标文件夹下的指定图片类型并调用修图函数