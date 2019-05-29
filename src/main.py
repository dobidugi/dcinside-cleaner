from login import main as login
from boardparselist import main as boardparse
from commentparselist import main as commentparse
from boarddelete import main as boarddelete
from commentdelete import main as commentdelete
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(287, 267)
        Form.setStyleSheet("font: 9pt \"양재백두체B\";")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 171, 20))
        self.lineEdit.setStyleSheet("font: 12pt \"양재깨비체B\";")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 50, 171, 20))
        self.lineEdit_2.setStyleSheet("font: 12pt \"양재깨비체B\";")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 20, 75, 51))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.clicked.connect(self.loginbtn)
        self.pushButton.setStyleSheet("background-color: rgb(74, 87, 168);\n"
"color: rgb(224, 255, 255);\n"
"font: 16pt  \"양재깨비체B\";\n"
"")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(180, 80, 81, 16))
        self.checkBox.setStyleSheet("font: 10pt \"양재깨비체B\";")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(180, 100, 81, 16))
        self.checkBox_2.setStyleSheet("font: 10pt \"양재깨비체B\";")
        self.checkBox_2.setObjectName("checkBox_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 80, 56, 12))
        self.label.setStyleSheet("font: 10pt \"양재깨비체B\";")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 105, 56, 12))
        self.label_2.setStyleSheet("font: 10pt \"양재깨비체B\";")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 261, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(74, 87, 168);\n"
"color: rgb(224, 255, 255);\n"
"font: 13pt  \"양재깨비체B\";\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 261, 16))
        self.label_3.setStyleSheet("font: 11pt \"양재깨비체B\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 261, 16))
        self.label_4.setStyleSheet("font: 11pt \"양재깨비체B\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 77, 91, 20))
        self.label_5.setStyleSheet("font: 10pt \"양재깨비체B\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 81, 20))
        self.label_6.setStyleSheet("font: 10pt \"양재깨비체B\";")
        self.label_6.setObjectName("label_6")
        self.namelabel = QtWidgets.QLabel(Form)
        self.namelabel.setGeometry(QtCore.QRect(10, 130, 251, 16))
        self.namelabel.setStyleSheet("font: 10pt \"양재깨비체B\";")
        self.namelabel.setText("")
        self.namelabel.setObjectName("namelabel")
        self.warringlabel = QtWidgets.QLabel(Form)
        self.warringlabel.setGeometry(QtCore.QRect(10, 240, 261, 16))
        self.warringlabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.warringlabel.setText("")
        self.warringlabel.setObjectName("warringlabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "피에로 클리너 v0.6"))
        self.lineEdit.setPlaceholderText(_translate("Form", "아이디"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "비밀번호"))
        self.pushButton.setText(_translate("Form", "로그인"))
        self.checkBox.setText(_translate("Form", "작성글 삭제"))
        self.checkBox_2.setText(_translate("Form", "댓글 삭제"))
        self.label.setText(_translate("Form", "0"))
        self.label_2.setText(_translate("Form", "0"))
        self.pushButton_2.setText(_translate("Form", "삭제 시작"))
        self.label_3.setText(_translate("Form", "카카오톡 플러스친구 @피에로 를 추가해주세요"))
        self.label_4.setText(_translate("Form", "친구추가시 여러가지 소식을 받을수 있어요"))
        self.label_5.setText(_translate("Form", "총 작성글 갯수 "))
        self.label_6.setText(_translate("Form", "총 댓글 갯수 "))
    def loginbtn(self):
        id = self.lineEdit.text()
        pw = self.lineEdit_2.text()
        cookies, id = login(id,pw, self.namelabel,self.warringlabel)
        #cmtlist = commentparse(id,cookies)
        #pstlist = boardparse(id,cookies)



def ProcessSelect():
    print("========================================")
    print("원하시는 작업을 선택하고 엔터를 눌러주세요")
    print("1. 댓글만 삭제하기")
    print("2. 작성글만 삭제하기")
    print("3. 댓글,작성글 삭제하기")
    num = int(input("입력  : "))
    print("========================================")
    print("수집중입니다 잠시만 기다려주세요")
    return num

def NormalDel():
    num = ProcessSelect()
    if(num==1):
        cmtlist = commentparse(id,cookies)
        commentdelete(id,pw,cmtlist)
    elif(num==2):
        pstlist = boardparse(id,cookies)
        boarddelete(id,pw,pstlist)

    elif(num==3):
        print("none")
        #cmtlist, pstlist = boardparse(id,cookies)
        #delete(id,pw,cmtlist=cmtlist,pstlist=pstlist)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    app.exec_()
    # programe start
    print("작동이 안될시 프로그래밍갤러리 피에로를 찾아와주시거나")
    print("dobidugi@gmail.com 이쪽으로 증상과 메일을 보내주세요^^")
    id = input("ID : ")
    pw = input("PASS : ")
    cookies, id = login(id,pw)
    NormalDel()
