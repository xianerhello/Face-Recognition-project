from PyQt5 import QtCore, QtWidgets
import sys
import capture1
import train2
import recognition3


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(369, 262)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(11, 11, 351, 91))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(11, 110, 351, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(11, 160, 351, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(11, 210, 351, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        #采集
        def slot1():
            capture1.camera("niuzixian")

        #训练
        def slot2():
            train2.train()
            print("训练完毕")

        #识别
        def slot3():
            recognition3.recognition()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(slot1)
        self.pushButton_2.clicked.connect(slot2)
        self.pushButton_3.clicked.connect(slot3)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "face_recognition"))
        self.label.setText(_translate("Form", "人脸识别测试"))
        self.pushButton.setText(_translate("Form", "采集数据"))
        self.pushButton_2.setText(_translate("Form", "开始训练"))
        self.pushButton_3.setText(_translate("Form", "开始识别"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_Form()
    w.setFixedSize(375, 265)
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
