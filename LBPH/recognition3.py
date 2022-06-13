import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def recognition():
    def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
        if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
            img = Image.fromarray(img)
        # 创建一个可以在给定图像上绘图的对象
        draw = ImageDraw.Draw(img)
        # 字体的格式
        fontStyle = ImageFont.truetype('1.ttf', 24)
        # 绘制文本
        draw.text((left, top), text, font=fontStyle)
        # 转换回OpenCV格式
        return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


    recogizer=cv2.face.LBPHFaceRecognizer_create()
    recogizer.read('trainer/trainer0.yml')
    names=[]

    #准备识别的图片
    def face_detect_demo(img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度
        face_detector=cv2.CascadeClassifier('D:/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
        face=face_detector.detectMultiScale(gray)
        #face=face_detector.detectMultiScale(gray)
        for x,y,w,h in face:
            cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
            #cv2.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0),thickness=1)
            # 人脸识别
            label, confidence = recogizer.predict(gray[y:y + h, x:x + w])
            print('标签id:',label,'置信评分：', confidence)#越大越不可信
            if confidence > 50:
                cv2.putText(img, 'unkonw', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            else:
                if label < len(names):
                    cv2.putText(img,names[label-1], (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
                    #cv2ImgAddText(img, names[ids], x+10, y-10, textSize=16)
        cv2.imshow('result',img)
        #print('bug:',ids)

    path = './data/jm/'
    def name():
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        for imagePath in imagePaths:
            name = str(os.path.split(imagePath)[1].split('.',2)[1])
            names.append(name)
            #print(names)


    cap = cv2.VideoCapture(0)
    name()
    while True:
        flag, frame = cap.read()
        if not flag:
            break
        face_detect_demo(frame)
        if ord(' ') == cv2.waitKey(10):
            break
    cv2.destroyAllWindows()
    cap.release()


#recognition()