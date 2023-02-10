import cv2

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取帧
    ret, frame = cap.read()

    # 翻转图像
    frame = cv2.flip(frame, 1)

    # 显示图像
    cv2.imshow('Mirror', frame)

    # 按下 "q" 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头
cap.release()
cv2.destroyAllWindows()
