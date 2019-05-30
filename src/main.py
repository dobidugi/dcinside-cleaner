from login import main as login
from boardparselist import main as boardparse
from commentparselist import main as commentparse
from boarddelete import main as boarddelete
from commentdelete import main as commentdelete
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import threading 


#gui start 
class Ui_Form(object):
    id = ""
    pw = ""
    cookies = ""
    cmtlist = []
    pstlist = []
    pstflag = False
    cmtflag = False
    loginflag = False
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(287, 268)
        Form.setStyleSheet("font: 9pt \"양재백두체B\";")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 171, 20))
        self.lineEdit.setStyleSheet("font: 12pt  ;")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 50, 171, 20))
        self.lineEdit_2.setStyleSheet("font: 12pt  ;")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 20, 75, 51))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.clicked.connect(self.loginbtn)
        self.pushButton.setStyleSheet("background-color: rgb(74, 87, 168);\n"
"color: rgb(224, 255, 255);\n"
"font: 16pt   ;\n"
"")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 90, 56, 12))
        self.label.setStyleSheet("font: 10pt  ;")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 56, 12))
        self.label_2.setStyleSheet("font: 10pt  ;")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 210, 261, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(254,255, 255);\n"
"color: rgb(160, 160, 160);\n"
"font: 13pt   ;\n"
"")
        self.pushButton_2.clicked.connect(self.deletestart)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 261, 16))
        self.label_3.setStyleSheet("font: 11pt  ;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 261, 16))
        self.label_4.setStyleSheet("font: 11pt  ;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 82, 91, 20))
        self.label_5.setStyleSheet("font: 10pt  ;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 81, 20))
        self.label_6.setStyleSheet("font: 10pt  ;")
        self.label_6.setObjectName("label_6")
        self.namelabel = QtWidgets.QLabel(Form)
        self.namelabel.setGeometry(QtCore.QRect(10, 130, 251, 16))
        self.namelabel.setStyleSheet("font: 10pt  ;")
        self.namelabel.setText("")
        self.namelabel.setObjectName("namelabel")
        self.warringlabel = QtWidgets.QLabel(Form)
        self.warringlabel.setGeometry(QtCore.QRect(10, 240, 261, 16))
        self.warringlabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.warringlabel.setText("")
        self.warringlabel.setObjectName("warringlabel")
        self.restcmt = QtWidgets.QPushButton(Form)
        self.restcmt.setGeometry(QtCore.QRect(160, 105, 101, 16))
        self.restcmt.setStyleSheet("background-color: rgb(254, 255, 255);\n"
"color: rgb(160, 160, 160);")
        self.restcmt.setEnabled(False)
        self.restcmt.setObjectName("restcmt")
        self.restcmt.clicked.connect(self.clickcmtbtn)
        self.respst = QtWidgets.QPushButton(Form)
        self.respst.setGeometry(QtCore.QRect(160, 80, 101, 16))
        self.respst.setStyleSheet("background-color: rgb(254, 255, 255);\n"
"color: rgb(160, 160, 160);")
        self.respst.setObjectName("respst")
        self.respst.clicked.connect(self.clickpstbtn)
        self.respst.setEnabled(False)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "피에로 클리너 v0.6"))
        self.lineEdit.setPlaceholderText(_translate("Form", "아이디"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "비밀번호"))
        self.pushButton.setText(_translate("Form", "로그인"))
        self.label.setText(_translate("Form", "0"))
        self.label_2.setText(_translate("Form", "0"))
        self.pushButton_2.setText(_translate("Form", "삭제 시작"))
        self.label_3.setText(_translate("Form", "카카오톡 플러스친구 @피에로 를 추가해주세요"))
        self.label_4.setText(_translate("Form", "친구추가시 여러가지 소식을 받을수 있어요"))
        self.label_5.setText(_translate("Form", "총 작성글 개수 "))
        self.label_6.setText(_translate("Form", "총 댓글 개수 "))
        self.restcmt.setText(_translate("Form", "업데이트"))
        self.respst.setText(_translate("Form", "업데이트"))

    def loginbtn(self):
        self.id = self.lineEdit.text()
        self.pw = self.lineEdit_2.text()
        self.cookies , self.id = login(self.id,self.pw,self.namelabel,self.warringlabel)
        if self.cookies != False:
            self.lineEdit.setDisabled(True)
            self.lineEdit_2.setDisabled(True)
            self.loginflag = True
            self.restcmt.setEnabled(True)
            self.respst.setEnabled(True)
            self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(160, 160, 160);\n"
"font: 16pt   ;\n"
"")

            self.respst.setStyleSheet("background-color: rgb(74, 87, 168);\n"
"color: rgb(224, 255, 255);\n"
"font: 10pt   ;\n"
"")
            self.restcmt.setStyleSheet("background-color: rgb(74, 87, 168);\n"
"color: rgb(224, 255, 255);\n"
"font: 10pt   ;\n"
"")

# 게시글 업데이트 버튼  클릭시 처리 루프 시작 

    def updatepst(self): 
        self.pstlist = boardparse(self.id,self.cookies)
        self.label.setText(str(len(self.pstlist)))
        self.pushButton_2.setStyleSheet("background-color: rgb(74, 87, 168);\n"
"color: rgb(224, 255, 255);\n"
"font: 16pt   ;\n"
"")
        self.warringlabel.setText("")
        self.pstflag=True

    def clickpstbtn(self): # 게시글 업데이트 버튼 클릭시 
        self.respst.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.warringlabel.setText("수집중....")
        self.respst.setEnabled(False)
        self.respst.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(160, 160, 160);\n"
"font: 10pt   ;\n"
"")
        t = threading.Thread(target=self.updatepst)
        t.start()
#게시글 업데이트 버튼 클릭시 처리 루프 끝

#댓글 업데이트 버튼 클릭시 처리 루프 시작 
    def updatecmt(self):
        self.cmtlist = commentparse(self.id,self.cookies)
        self.label_2.setText(str(len(self.cmtlist)))
        self.pushButton_2.setStyleSheet("background-color: rgb(74, 87, 168);\n"
"color: rgb(224, 255, 255);\n"
"font: 16pt   ;\n"
"")
        self.warringlabel.setText("")
        self.cmtflag=True

    def clickcmtbtn(self): # 댓글 업데이트 버튼 클릭시
        self.restcmt.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.warringlabel.setText("수집중....")
        self.restcmt.setEnabled(False)
        self.restcmt.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(160, 160, 160);\n"
"font: 10pt   ;\n"
"")
        t = threading.Thread(target=self.updatecmt)
        t.start()
#댓글 업데이트 버튼 클릭시 처리 루프 끝

    def deletestart(self):
        if self.pstflag == True: # 게시글 수집완료시
            t = threading.Thread(target=boarddelete, args=(self.id,self.pw,self.pstlist,self.warringlabel))
            t.start()
            self.respst.setEnabled(True)
            self.respst.setStyleSheet("background-color: rgb(74, 87, 168);\n"
"color: rgb(254, 255, 255);\n"
"font: 10pt   ;\n"
"")
        if self.cmtflag == True: # 댓글 수집완료시
            t = threading.Thread(target=commentdelete, args=(self.id,self.pw,self.cmtlist,self.warringlabel))
            t.start()
            self.restcmt.setEnabled(True)
            self.restcmt.setStyleSheet("background-color: rgb(74, 87, 168);\n"
"color: rgb(254, 255, 255);\n"
"font: 10pt   ;\n"
"")

def NormalDel():
    num = 0
    if(num==1):
        print("none")
        #commentdelete(id,pw,cmtlist)
    elif(num==2):
        print("none")
        #boarddelete(id,pw,pstlist)

    elif(num==3):
        print("none")
        #cmtlist, pstlist = boardparse(id,cookies)
        #delete(id,pw,cmtlist=cmtlist,pstlist=pstlist)

# gui end 
if __name__ == "__main__":
    import sys
    #gui load start 
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    #gui load end
    app.exec_()