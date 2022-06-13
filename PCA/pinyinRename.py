import os
import shutil

def Rename():
    #文件夹整体拷贝
    source_path = os.path.abspath("E:/02Programming/应用/量化工程设计2-人脸识别/照片/2022人脸识别库/原库/文件夹已命名") #原文件夹路径
    target_path = os.path.abspath("E:/02Programming/应用/量化工程设计2-人脸识别/照片/2022人脸识别库/library") #目标文件夹路径

    if not os.path.exists(target_path):
        # 如果目标路径不存在原文件夹的话就创建
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree(target_path)

    shutil.copytree(source_path, target_path)
    print('copy dir to library finished!')


    #图片重命名
    path = "E:/02Programming/应用/量化工程设计2-人脸识别/照片/2022人脸识别库/library"

    #获取文件数量
    file_count = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_count = file_count + 1

    print('file_count',file_count)

    totalperson = file_count // 10
    print('totalperson',totalperson)
    dirname0 = []

    #Rename
    class getOutOfLoop(Exception):
        pass

    try:
        for dirph, dirname, file0 in os.walk(path): #file是列表类型
            #print('dirname:', dirname)
            #print('dirph:', dirph)
            if dirname != []:
                dirname0 = dirname
                dirname0.reverse()
                print('dirname0:',dirname0)

            for num in range(0,totalperson): #第二个参数填总人数（文件夹数）即可
                deep_dirph = dirph + '/' + dirname0[num]
                i = 1
                for file1 in os.listdir(deep_dirph):
                    #print('file1:', file1)
                    os.rename(deep_dirph + '/' + file1, deep_dirph+'/' + dirname0[num]+str(i)+'.pgm')
                    i += 1
            raise getOutOfLoop()  # 抛出一个异常，就会跳出所有循环

    except getOutOfLoop:
        pass
    print('Rename done')


    #文件夹下的所有文件（包括子目录文件）拷贝到目标文件夹下
    source_path = os.path.abspath("E:/02Programming/应用/量化工程设计2-人脸识别/照片/2022人脸识别库/library")
    target_path = os.path.abspath(r'E:\02Programming\应用\量化工程设计2-人脸识别\照片\2022人脸识别库\新工科全图片')

    #清空文件夹
    if  os.path.exists(target_path):
            shutil.rmtree(target_path)
            os.mkdir(target_path)

    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)
                shutil.copy(src_file, target_path)
                #print(src_file)

    print('copy files to 新工科全图片 finished!')
