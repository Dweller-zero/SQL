from login import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal
from sql import database
from PyQt5.QtWidgets import *
class myLogin(Login, QMainWindow):
    close_signal_1 = pyqtSignal()
    close_signal_2 = pyqtSignal()
    close_signal_3 = pyqtSignal()
    close_register_1 = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.btn1.clicked.connect(lambda:self.login_btn1(self.usernameEdit.text(), self.passwordEdit.text()))
        self.btn2.clicked.connect(lambda:self.register_btn())

    def login_btn1(self, username, password):
        flag1=database.login_check(username,password)
        print(flag1)
        if flag1==1:
            flag2,role1=database.check_Role(username)
            if flag2==0:#超级管理员
                self.close_signal_1.emit()
                self.close()
            elif flag2==1:#录题人员
                self.close_signal_2.emit()
                self.close()
            elif flag2==2:#答题者
                self.role=role1
                self.close_signal_3.emit()
                self.close()
        else:
            QMessageBox.information(self, '无法登陆', '密码错误或不存在该用户')

    def register_btn(self):
        self.close_register_1.emit()
        self.close()


class myRegister(register, QDialog):


    change4_sign = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.btn1.clicked.connect(lambda:self.register_new(self.username1Edit.text(), self.username2Edit.text(), self.password1Edit.text(), self.majorEdit.text(), self.phoneEdit.text()))
        self.btn2.clicked.connect(self.returnLogin)

    def register_new(self, username, username_English, password, major, phone):
        database.insertUserInfo(username, username_English, password, major, phone)
        QMessageBox.information(self, 'made by cc', '注册成功')
        self.change4_sign.emit()
        self.close()

    def returnLogin(self):
        self.change4_sign.emit()
        self.close()

class myControl_1(Control_1, QDialog):
    change1_sign = pyqtSignal()
    change2_sign = pyqtSignal()
    change3_sign = pyqtSignal()
    change4_sign = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.btn1.clicked.connect(self.um)
        self.btn2.clicked.connect(self.ti)
        self.btn3.clicked.connect(self.ac)
        self.btn4.clicked.connect(self.returnLogin)

    def um(self):
        self.change1_sign.emit()
        self.close()

    def ti(self):
        self.change2_sign.emit()
        self.close()

    def ac(self):
        self.change3_sign.emit()
        self.close()

    def returnLogin(self):
        self.change4_sign.emit()
        self.close()

class myControl_2(Control_2, QDialog):
    change1_sign = pyqtSignal()
    change2_sign = pyqtSignal()
    change3_sign = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.btn1.clicked.connect(self.ti)#题目录入管理
        self.btn3.clicked.connect(self.tc)#题目查看管理
        self.btn4.clicked.connect(self.returnLogin)

    def ti(self):
        self.change1_sign.emit()
        self.close()

    def tc(self):
        self.change2_sign.emit()
        self.close()

    def returnLogin(self):
        self.change3_sign.emit()
        self.close()

class myControl_3(Control_3, QDialog):
    change3_sign = pyqtSignal()
    change4_sign = pyqtSignal()
    change5_sign = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.btn3.clicked.connect(self.a1)
        self.btn4.clicked.connect(self.a1c)
        self.btn5.clicked.connect(self.returnLogin)


    def a1(self):
        self.change3_sign.emit()
        self.close()

    def a1c(self):
        self.change4_sign.emit()
        self.close()

    def returnLogin(self):

        self.change5_sign.emit()
        self.close()

class myUser_manage(user_manage, QDialog):#登录账号管理-管理员
    change1_sign = pyqtSignal()
    change2_sign = pyqtSignal()
    change3_sign = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.remove.clicked.connect(lambda:self.Remove(self.removeEdit.text()))
        self.submit.clicked.connect(self.Update)
        self.returnbtn.clicked.connect(self.returnLogin)

    def Remove(self,removeId):
        print(removeId)
        row_count = self.table.rowCount()
        print(row_count)
        print(self.table.item(0, 0).text())

        if removeId=='':
            QMessageBox.information(self, '错误', '用户编号不能为空')
        else:
            rows=database.input_item()
            for i in range(len(rows)):
                if self.table.item(i, 0).text()==removeId:
                    a=i
                    break
            self.table.removeRow(a)
            database.delete_user(removeId)
            QMessageBox.information(self, 'OK', '成功删除')

    def Update(self):
        rows=database.input_item()
        for i in range(len(rows)):
            database.upgrade_user(self.table.item(i, 0).text(),self.table.item(i, 1).text(),self.table.item(i, 2).text(),self.table.item(i, 3).text(),self.table.item(i, 4).text(),self.table.item(i, 5).text(),self.table.item(i, 6).text())
        QMessageBox.information(self, '成功', '更新成功')




    def returnLogin(self):
        self.change3_sign.emit()
        self.close()


class myTitle_input(Title_input, QDialog):#题目录入管理-管理员/录题人员
    change1_sign = pyqtSignal()
    change2_sign = pyqtSignal()
    change3_sign = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.remove.clicked.connect(lambda:self.Remove(self.removeEdit.text()))
        self.submit.clicked.connect(self.Update)
        self.returnbtn.clicked.connect(self.returnLogin)

    def Remove(self,removeId):
        print(removeId)
        row_count = self.table.rowCount()
        print(row_count)
        print(self.table.item(0, 0).text())

        if removeId=='':
            QMessageBox.information(self, '错误', '题目编号不能为空')
        else:
            rows=database.input_item_title()
            for i in range(len(rows)):
                if self.table.item(i, 0).text()==removeId:
                    a=i
                    break
            self.table.removeRow(a)
            database.delete_title(removeId)
            QMessageBox.information(self, 'OK', '成功删除')

    def Update(self):
        rows=database.input_item_title()
        for i in range(len(rows)):
            print(len(rows))
            #l=[self.table.item(i, 0).text(),self.table.item(i, 1).text(),self.table.item(i, 2).text(),self.table.item(i, 3).text(),self.table.item(i, 4).text(),self.table.item(i, 5).text(),self.table.item(i, 6).text(),self.table.item(i, 7).text(),self.table.item(i, 8).text(),bytes(self.table.item(i, 9).text().encode()),self.table.item(i, 10).text(),self.table.item(i, 11).text(),self.table.item(i, 12).text(),self.table.item(i, 13).text(),self.table.item(i, 14).text(),self.table.item(i, 15).text()]
            #print(l)
            database.upgrade_title(self.table.item(i, 0).text(),self.table.item(i, 1).text(),self.table.item(i, 2).text(),self.table.item(i, 3).text(),self.table.item(i, 4).text(),self.table.item(i, 5).text(),self.table.item(i, 6).text(),self.table.item(i, 7).text(),self.table.item(i, 8).text(),bytes(self.table.item(i, 9).text().encode()),self.table.item(i, 10).text(),self.table.item(i, 11).text(),self.table.item(i, 12).text(),self.table.item(i, 13).text(),self.table.item(i, 14).text(),self.table.item(i, 15).text())
        QMessageBox.information(self, '成功', '更新成功')




    def returnLogin(self):
        self.change3_sign.emit()
        self.close()



class myAnswer_check(Answer_check, QDialog):#作答记录查看窗口-管理员
    change1_sign = pyqtSignal()
    change2_sign = pyqtSignal()
    change3_sign = pyqtSignal()
    def __init__(self):
        super().__init__()
        # self.btn1.clicked.connect(self.changeTeacher)
        # self.btn3.clicked.connect(self.changeQueryLesson)
        self.returnbtn.clicked.connect(self.returnLogin)

    # def changeTeacher(self):
    #     self.change1_sign.emit()
    #     self.close()

    # def changeQueryLesson(self):
    #     self.change2_sign.emit()
    #     self.close()

    def returnLogin(self):
        self.change3_sign.emit()
        self.close()



class myTitle_check(Title_check, QDialog):##题目查看管理-录题人员
    change1_sign = pyqtSignal()
    change2_sign = pyqtSignal()
    change3_sign = pyqtSignal()
    def __init__(self):
        super().__init__()

        # self.btn1.clicked.connect(self.changeTeacher)
        self.submit.clicked.connect(lambda:self.check(self.username1Edit.text(), self.username2Edit.text()))
        self.returnbtn.clicked.connect(self.returnLogin)

    # def changeTeacher(self):
    #     self.change1_sign.emit()
    #     self.close()

    def check(self,majorId,knowledgeId):
        if majorId =='' or knowledgeId == '':
            QMessageBox.information(self, '错误', '专业或知识点不能为空')
        else:
            self.table.clear()
            self.table.setHorizontalHeaderLabels(['题目编号','题目内容','题目类型','填空答案','答案解析','分值','难度系数','图片'])
            rows=database.title_check(majorId,knowledgeId)
            for i in range(len(rows)):
                for j in range(len(rows[i])):
                    self.table.setItem(i, j, QTableWidgetItem(str(rows[i][j])))
            QMessageBox.information(self, '成功', '查看成功')

    def returnLogin(self):
        self.change3_sign.emit()
        self.close()

class myAnswer1(Answer1, QDialog):#作答界面-答题人
    change1_sign = pyqtSignal()
    change2_sign = pyqtSignal()
    change3_sign = pyqtSignal()

    def __init__(self):
        super().__init__()
        # self.btn1.clicked.connect(self.changeTeacher)
        
        self.returnbtn.clicked.connect(self.returnLogin)

    # def changeTeacher(self):
    #     self.change1_sign.emit()
    #     self.close()




    def returnLogin(self):

        self.change3_sign.emit()
        self.close()

class myAnswer1_check(Answer1_check, QDialog):#作答后界面-做题人查看做题数据
    change1_sign = pyqtSignal()
    change2_sign = pyqtSignal()
    change3_sign = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.btn1.clicked.connect(self.changeTeacher)
        # self.btn3.clicked.connect(self.changeQueryLesson)
        self.returnbtn.clicked.connect(self.returnLogin)

    def changeTeacher(self):
        self.change1_sign.emit()
        self.close()

    # def changeQueryLesson(self):
    #     self.change2_sign.emit()
    #     self.close()

    def returnLogin(self):
        self.change3_sign.emit()
        self.close()