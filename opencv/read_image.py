import cv2
# 讀取圖像
image = cv2.imread("patrick.jpg")

# 更改圖像的大小
img = cv2.resize(image,(0,0),fx = 0.5,fy =0.5)#devided by 2;

# 顯示圖像l
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 检查是否成功讀取圖像
if image is not None:
    # 在这里可以进行图像处理操作
    cv2.imshow('Image', image)  # 显示图像
    cv2.waitKey(0)  # 等待用户按下任意键后关闭图像窗口
else:
    print("無法讀取圖像")

# 儲存圖像
cv2.imwrite('output_image.jpg', image)

# 显示保存后的图像
cv2.imshow('Saved Image', image)
cv2.waitKey(0)