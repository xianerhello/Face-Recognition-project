import cv2
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont

#   路径包括
library = "E:/02Programming/应用/量化工程设计2-人脸识别/照片/2022人脸识别库/library"
camerapath = ".\\carema"
path2 = ".\\train"  #要按顺序一一对应
testpath = ".\\test"
pathf = '.\\haarcascade_frontalface_default.xml'

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
    img.show()


#   显示窗口
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(3)
    cv2.destroyAllWindows()

# 图片采集模块（单张采集）
def Camera():
    cap = cv2.VideoCapture(0)
    num = 1
    while (cap.isOpened()):  # 检测是否开启摄像头
        ret_flag, Vshow = cap.read()  # 得到图像
        cv2.imshow("camera", Vshow)  # 显示图像
        k = cv2.waitKey(1) & 0xFF  # 按键判断
        if k == ord('s'):  # s保存
            cv2.imwrite(camerapath + "\\" + str(num) + ".jpg", Vshow)
            print("已采集")
            num += 1
        elif k == ord(' '):  # space退出
            GrayChange()
            break
    cap.release()
    cv2.destroyAllWindows()


# 灰度转换，存到test文件夹
def GrayChange():
    i = 1
    for fil in os.listdir(camerapath):
        img = cv2.imread(camerapath + "\\" + fil, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (138, 168))
        cv2.imwrite(testpath + "\\" + "camera" + str(i) + ".pgm", img)
        i += 1



#   训练图片
def loaddatas(Path):

    '''
    :param Path: 训练集的路径
    :return: 训练集的矩阵
    '''

    A = []
    number = len(os.listdir(Path))
    for i in range(1, number + 1):
        img = cv2.imread(Path + '\\' + str(i) + '.pgm', cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (138,168))
        img = img.ravel()   # ravel函数是 numpy 的函数: 将多维数组中的元素变成一个一维数组
        A.append(img)
    A = np.array(A)
    return A.T


#   pca实现
def PCA(X, num):

    '''
    :param X: 训练集的矩阵
    :param num: 决定目标投影矩阵的维数
    :return: 目标投影矩阵，均值的矩阵，零均值化处理的矩阵
    '''

    mean = X.mean(axis=1)   # 对每行求均值
    mean = mean.reshape(mean.shape[0], 1)
    A = X - mean    # 零均值化处理
    # 求协方差矩阵的特征向量，由于样本维度远远大于样本数目，所以不直接求协方差矩阵
    M = np.dot(A.T, A)
    #   AT*A的特征值和特征向量
    evalue, evector = np.linalg.eig(M)
    #   A*AT的特征值和特征向量
    evector = np.mat(np.dot(A, evector))
    evalueindex = np.argsort(evalue)
    evalueindex = evalueindex[::-1]
    evalueindex = evalueindex[:num]    # 取前num个特征
    real_evector = evector[::, evalueindex]
    return real_evector, mean, A


#   预测函数
def predict(testpath, real_evector, A, mean):
    '''

    :param testpath: 测试图片的路径
    :param real_evector: 协方差矩阵的特征向量
    :param A:   均值化处理的训练集矩阵
    :param mean:
    :return: 对应测试图片的标签，测试图片矩阵
    '''
    testimg1 = cv2.imdecode(np.fromfile(testpath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)   # 读取中文路径的
    testimg1 = cv2.resize(testimg1, (138,168))
    testimg = cv2.imdecode(np.fromfile(testpath, dtype=np.uint8), cv2.IMREAD_UNCHANGED)   # 读取中文路径的
    testimg = cv2.resize(testimg, (138,168))
    testimg = np.reshape(testimg, (-1, 1))
    testimg = np.array(testimg)
    difftestimg = testimg - mean
    testimg = np.dot(real_evector.T, difftestimg)
    dataimg = np.dot(real_evector.T, A)
    distancelist = []
    # 遍历每一个特征（每一列），差值最小的一组数据即为最近，就是相对应的人脸
    for i in range(0, real_evector.shape[1]):
        data = dataimg[:, i]
        temp = np.linalg.norm(testimg - data)   # 欧式距离计算
        distancelist.append(temp)

    index = np.argmin(distancelist)
    res = int(index)/10
    cv_show('test', testimg1)
    return res, testimg1


def showname(xmlpath, imag, res):
    faceCascade = cv2.CascadeClassifier(xmlpath)
    faceCascade.load(xmlpath)
    faces = faceCascade.detectMultiScale(imag, scaleFactor=1.15, minNeighbors=3, minSize=(3, 3))
    #print("res", res)
    #print("int_res", int(res))
    testname = name[int(res)]
    print(str(testname))
    # 逐个标注人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(imag, (x, y), (x + w, y + h), (255, 255, 0), 2)
        cv2ImgAddText(imag, testname, x, y, textSize=16)
        #cv2.putText(imag, testname, (x-2, y - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 255), 1)
    # 显示结果
    #cv_show('dect', imag)


name = []
i = 0
#   获取名字列表
for dirph, dirnames, file in os.walk(library): #file是列表类型
    for files in os.listdir(dirph): #files是独立的文件名
        if files.endswith(".pgm"):
            i += 1
            if dirph.endswith("电照片"):
                # print(files[:3], ':', files)
                if i % 10 == 0:
                    name.append(files[:3])
            else :
                if dirph[-3:].startswith('\\'):
                    # print(dirph[-2:], ':', files)
                    if i % 10 == 0:
                        name.append(dirph[-2:])
                else :
                    # print(dirph[-3:], ':', files)
                    if i % 10 == 0:
                        name.append(dirph[-3:])
print(name)     # 打印名字列表
i = 1


# #主程序
# DATA = loaddatas(path2)  # 加载图片训练
# real_evector, mean, A = PCA(DATA, 290)   # 得出特征向量
# for fil in os.listdir(testpath):
#     res, testimg= predict(testpath + '\\' + fil, real_evector, A, mean)  # 预测识别图片名字
#     showname(pathf, testimg, res)


