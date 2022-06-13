import cv2
from PIL import ImageFont
import shutil
import os

#摄像头
def camera(name):

    path = ("./data/jm/")
    # if os.path.exists(path):
    #     shutil.rmtree(path)    #     os.mkdir(path)

    cap=cv2.VideoCapture(0)
    num = 1
    while(cap.isOpened()):#检测是否在开启状态
        ret_flag,Vshow = cap.read()#得到每帧图像
        cv2.imshow("Capture_Test",Vshow)#显示图像
        k = cv2.waitKey(1) & 0xFF#按键判断
        if k == ord('s'):#保存
            cv2.imwrite("./data/jm/"+str(num)+"." + name + ".jpg", Vshow)
            #cv2.imencode('.jpg', Vshow)[1].tofile(path+str(num)+"." + name + ".jpg")

            print("success to save"+str(num)+".jpg")
            print("-------------------")
            num += 1
        elif k == ord(' '):#退出
            break
    #释放摄像头
    cap.release()
    #释放内存
    cv2.destroyAllWindows()


#camera("牛子贤")
