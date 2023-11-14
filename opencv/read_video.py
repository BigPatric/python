import cv2

# 打開影片文件
video_capture = cv2.VideoCapture('video.mp4')

while True:
    # 讀取一幀
    ret, frame = video_capture.read()

    # 如果影片結束，退出迴圈
    if not ret:
        break

    # 顯示影片
    cv2.imshow('Video', frame)

    # 按 'q' 鍵退出迴圈
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# 釋放資源
video_capture.release()
cv2.destroyAllWindows()