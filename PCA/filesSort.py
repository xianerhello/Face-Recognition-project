import os
import shutil
path2 = ".//train"


def filesort():
    i = 1
    num = 1
    #清空文件夹
    if  os.path.exists(path2):
            shutil.rmtree(path2)
            os.mkdir(path2)
    if  os.path.exists("E:/ph/新工科"):
            shutil.rmtree("E:/ph/新工科")
            os.mkdir("E:/ph/新工科")

    #复制文件
    src="E:/02Programming/应用/量化工程设计2-人脸识别/照片/2022人脸识别库/新工科全图片"#原文件夹路径
    des="E:/ph/新工科"#目标文件夹路径
    for file in os.listdir(src):
        full_file_name = os.path.join(src, file)  # 把文件的完整路径得到
        #print("要被复制的文件路径全名:", full_file_name)
        #遍历原文件夹中的文件
        if os.path.isfile(full_file_name):#用于判断某一对象(需提供绝对路径)是否为文件
            shutil.copy(full_file_name, des)#shutil.copy函数放入原文件的路径文件全名  然后放入目标文件夹
            num += 1
    num = num-1
    print('已复制',num,'个文件')
    print('复制成功')

    #新工科
    for file in os.listdir("E:/ph/新工科"):
        os.rename("E:/ph/新工科/" + file, "E:/ph/新工科/" + str(i) + '.pgm')
        shutil.copy("E:/ph/新工科/" + str(i) + '.pgm', path2)
        i += 1

    #机电

    # i = 291
    # for file in os.listdir("E:/ph/机电"):
    #     os.rename("E:/ph/机电/" + file, "E:/ph/机电/" + str(i) + '.pgm')
    #     shutil.copy("E:/ph/机电/" + str(i) + '.pgm', path2)
    #     i += 1

    print('已复制至训练集')
