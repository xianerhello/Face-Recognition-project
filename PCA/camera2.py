import cv2
import os
import shutil
import time

#清空facedata
facedata = '.\\Facedata'
facedataold = '.\\Facedata\\old'
filepath1 = facedata + "\\" + 'new'

if not os.path.exists(facedataold):
    os.mkdir(facedataold)
else:
    shutil.rmtree(facedataold)
    os.mkdir(facedataold)

# 人脸检测，采集数据
def detection(NameId, number):
    cap = cv2.VideoCapture(0)  # 0表示默认系统摄像头


    count = 1
    while True:
        ok, img = cap.read()  # 读取摄像头数据, 必须返回两个参数
        if not ok:
            break
        cv2.imshow('camera', img)
        k = cv2.waitKey(5) & 0xFF  # 按键判断, 每5ms刷新
        if k == ord(' '):  # space拍照
            cv2.imwrite('./FaceData/old/' + NameId + '_' + str(count) + '.jpg', img)
            print('采集第', count, '张成功！')
            count += 1

        elif count > number:
            print('人脸信息采集完毕！')
            break

    cap.release()  # 关闭摄像头
    cv2.destroyWindow('camera')  # 删除窗口

def GrayChange():
    i = 1
    if not os.path.exists(filepath1):
        os.mkdir(filepath1)
    else:
        shutil.rmtree(filepath1)
        os.mkdir(filepath1)

    for fil in os.listdir(facedataold):
        img = cv2.imread(facedataold + "\\" + fil, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (138, 168))
        cv2.imwrite(filepath1 + "\\" + str(i) + ".pgm", img)
        i += 1

def transfer(ID):
    src="E:/02Programming/应用/量化工程设计2-人脸识别/代码/人脸识别牛子贤/PCA - 副本/Facedata"#原文件夹路径
    des="E:/02Programming/应用/量化工程设计2-人脸识别/照片/2022人脸识别库/原库/文件夹已命名"#目标文件夹路径
    filepath2 = des + '/' + ID
    if not os.path.exists(filepath2):
        os.mkdir(filepath2)
    else:
        shutil.rmtree(filepath2)
        os.mkdir(filepath2)

    num = 1
    for file in os.listdir(filepath1):
        full_file_name = os.path.join(filepath1, file)  # 把文件的完整路径得到
        #print("要被复制的文件路径全名:", full_file_name)

        #遍历原文件夹中的文件
        if os.path.isfile(full_file_name):#用于判断某一对象(需提供绝对路径)是否为文件
            shutil.copy(full_file_name, filepath2)#shutil.copy函数放入原文件的路径文件全名  然后放入目标文件夹
            num += 1
    num = num-1
    print('已复制',num,'个文件至文件夹已命名')


# detection('1', 10) #（姓名，采集数）
# GrayChange()
# transfer('牛小贤')