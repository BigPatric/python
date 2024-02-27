import cv2
import os
# absolute path
current_directory = os.getcwd()
relative_path = os.path.join(current_directory,"images/patrick.jpg")


# 讀取圖像
image = cv2.imread(relative_path)

# 更改圖像的大小
img = cv2.resize(image,(0,0),fx = 2.0,fy =2.0)#devided by 2;

# 顯示圖像l
cv2.imshow('img',img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

# 检查是否成功讀取圖像
if image is not None:
    # 在这里可以进行图像处理操作
    cv2.imshow('Image', image)  # 显示图像
    cv2.waitKey(0)  # 等待用户按下任意键后关闭图像窗口
else:
    print("無法讀取圖像")

# 儲存圖像
cv2.imwrite('output_image.jpg', img)

# 显示保存后的图像
cv2.imshow('Saved Image', img)
cv2.waitKey(0)