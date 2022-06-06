from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
from sql import database
import random
majorId123='0'
testId123='100'
paperId123='100'
class Login(QMainWindow):

    def __init__(self):
        super().__init__()

        
        self.text1 = QLabel('自测学习系统', self)
        self.text1.setGeometry(QRect(60, 60, 191, 61))
        self.text1.move(120, 0)
        self.text1.setFont(QFont("Roman times",20,QFont.Bold))

        '''用户名部分'''
        self.username = QLabel('登录名', self)
        self.username.move(110, 70)
        self.usernameEdit = QLineEdit(self)
        self.usernameEdit.setGeometry(170, 70, 120, 30)

        '''密码部分'''
        self.password = QLabel('登录密码', self)
        self.password.move(110, 130)
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.setGeometry(170, 130, 120, 30)

        self.btn1 = QPushButton('登录',self)
        self.btn2 = QPushButton('注册',self)
        self.btn1.move(100, 220)
        self.btn2.move(250, 220)

        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('made by cc')
        self.center()

    '''窗口居中'''
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class register(QDialog):#注册
    def __init__(self):
        super().__init__()

        self.text1 = QLabel('自测学习系统', self)
        self.text1.setGeometry(QRect(60, 60, 191, 61))
        self.text1.move(120, 0)
        self.text1.setFont(QFont("Roman times",20,QFont.Bold))

        self.username1 = QLabel('用户名', self)
        self.username1.move(110, 75)
        self.username1Edit = QLineEdit(self)
        self.username1Edit.setGeometry(170, 70, 120, 30)

        self.username2 = QLabel('英文名', self)
        self.username2.move(110, 135)
        self.username2Edit = QLineEdit(self)
        self.username2Edit.setGeometry(170, 130, 120, 30)

        self.password1 = QLabel('登录密码', self)
        self.password1.move(110, 195)
        self.password1Edit = QLineEdit(self)
        self.password1Edit.setEchoMode(QLineEdit.Password)
        self.password1Edit.setGeometry(170, 190, 120, 30)

        self.password2 = QLabel('确认密码', self)
        self.password2.move(110, 255)
        self.password2Edit = QLineEdit(self)
        self.password2Edit.setEchoMode(QLineEdit.Password)
        self.password2Edit.setGeometry(170, 250, 120, 30)

        self.major = QLabel('所属专业', self)
        self.major.move(110, 315)
        self.majorEdit = QSpinBox(self)
        self.majorEdit.setGeometry(170, 310, 120, 30)

        self.phone = QLabel('联系方式', self)
        self.phone.move(110, 375)
        self.phoneEdit = QLineEdit(self)
        self.phoneEdit.setGeometry(170, 370, 120, 30)

        self.btn1 = QPushButton('注册',self)
        self.btn1.move(100, 450)

        self.btn2 = QPushButton('返回上一级',self)
        self.btn2.move(250, 450)

        self.setGeometry(300, 600, 400, 500)
        self.setWindowTitle('made by cc')
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Control_1(QDialog):#管理员
    def __init__(self):
        super().__init__()

        self.text1 = QLabel('自测学习系统', self)
        self.text1.setGeometry(QRect(60, 60, 191, 61))
        self.text1.move(120, 0)
        self.text1.setFont(QFont("Roman times",20,QFont.Bold))

        self.btn1 = QPushButton('登录账号管理', self)
        self.btn1.setGeometry(220, 150, 150, 50)
        self.btn1.setFont(QFont("", 15, QFont.Bold))

        self.btn2 = QPushButton('题目录入管理', self)
        self.btn2.setGeometry(400, 150, 150, 50)
        self.btn2.setFont(QFont("", 15, QFont.Bold))

        self.btn3 = QPushButton('作答记录管理', self)
        self.btn3.setGeometry(220, 220, 150, 50)
        self.btn3.setFont(QFont("", 15, QFont.Bold))

        self.btn4 = QPushButton('返回登录界面', self)
        self.btn4.setGeometry(400, 220, 150, 50)
        self.btn4.setFont(QFont("", 15, QFont.Bold))

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('自测学习系统-管理员')
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Control_2(QDialog):#录题人
    def __init__(self):
        super().__init__()

        self.text1 = QLabel('自测学习系统', self)
        self.text1.setGeometry(QRect(60, 60, 191, 61))
        self.text1.move(120, 0)
        self.text1.setFont(QFont("Roman times",20,QFont.Bold))

        self.btn1 = QPushButton('题目录入管理', self)
        self.btn1.setGeometry(220, 150, 150, 50)
        self.btn1.setFont(QFont("", 15, QFont.Bold))


        self.btn3 = QPushButton('题目查看', self)
        self.btn3.setGeometry(220, 220, 150, 50)
        self.btn3.setFont(QFont("", 15, QFont.Bold))

        self.btn4 = QPushButton('返回登录界面', self)
        self.btn4.setGeometry(400, 220, 150, 50)
        self.btn4.setFont(QFont("", 15, QFont.Bold))

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('自测学习系统-录题人员')
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Control_3(QDialog):#答题人
    def __init__(self):
        super().__init__()

        self.text1 = QLabel('自测学习系统', self)
        self.text1.setGeometry(QRect(60, 60, 191, 61))
        self.text1.move(120, 0)
        self.text1.setFont(QFont("Roman times",20,QFont.Bold))

        self.major = QLabel('选择即将要测试的专业', self)
        self.major.move(110, 100)
        self.majorEdit = QSpinBox(self)
        self.majorEdit.setGeometry(300, 100, 120, 30)

        self.btn3 = QPushButton('提交', self)
        self.btn3.setGeometry(220, 220, 150, 50)
        self.btn3.setFont(QFont("", 15, QFont.Bold))

        self.btn4 = QPushButton('查看学习数据', self)
        self.btn4.setGeometry(400, 220, 150, 50)
        self.btn4.setFont(QFont("", 15, QFont.Bold))

        self.btn5 = QPushButton('返回登陆界面', self)
        self.btn5.setGeometry(310, 290, 150, 50)
        self.btn5.setFont(QFont("", 15, QFont.Bold))

        self.btn3.clicked.connect(lambda :self.r2majorEdit())

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('自测学习系统-答题人员')
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def r2majorEdit(self):

        global majorId123
        majorId123 = self.majorEdit.text()
        print(majorId123)



class EmptyDelegate(QItemDelegate):
    def __init__(self,parent):
        super(EmptyDelegate, self).__init__(parent)
    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None


class user_manage(QWidget):#登录账号管理-管理员
    def __init__(self):
        super().__init__()

        self.text1 = QLabel('自测学习系统', self)
        self.text1.setGeometry(QRect(60, 60, 191, 61))
        self.text1.move(120, 0)
        self.text1.setFont(QFont("Roman times",20,QFont.Bold))

        self.text2 = QLabel('登录账号管理', self)
        self.text2.setGeometry(QRect(60, 60, 191, 61))
        self.text2.move(10, 60)
        self.text2.setFont(QFont("Roman times",10,QFont.Bold))


        '''增加/删除节次按钮'''
        self.add = QPushButton('添加新用户', self)
        self.add.move(630, 150)

        self.remove = QPushButton('删除用户(用户编号)', self)
        self.remove.move(630, 250)
        self.removeEdit = QLineEdit(self)
        self.removeEdit.setGeometry(630, 300, 120, 30)

        self.submit = QPushButton('更新', self)
        self.submit.move(630, 450)

        '''表格'''
        self.table = QTableWidget(self)
        self.table.setGeometry(100, 100, 480, 330)
        self.table.setRowCount(80)
        self.table.setColumnCount(7)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 150)
        self.table.setColumnWidth(6, 150)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['用户编号','用户名','英文名','角色','密码','联系方式','所属专业'])
        self.table.setItemDelegateForColumn(0,EmptyDelegate(self))#第一列不能更改
        #self.tableView.setItemDelegateForColumn(1,EmptyDelegate(self))
        '''表头字体颜色'''

        rows=database.input_item()
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.table.setItem(i, j, QTableWidgetItem(rows[i][j]))

        '''添加删除按钮操作'''
        self.add.clicked.connect(lambda :self.addRow())


        '''退出界面按钮'''
        self.returnbtn = QPushButton('返回主界面', self)
        self.returnbtn.setGeometry(300, 700, 150, 40)#横、竖、横、竖
        self.returnbtn.setFont(QFont("", 10, QFont.Bold))

        self.resize(800,800)
        self.setWindowTitle('登录账号管理')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def addRow(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        rows=database.input_item()

        length=database.add_user()
        self.table.setItem(len(rows), 0, QTableWidgetItem('%s' % str(int(length))))


class Title_input(QWidget):#题目录入管理-管理员/录题人员
    def __init__(self):
        super().__init__()

        self.text1 = QLabel('自测学习系统', self)
        self.text1.setGeometry(QRect(60, 60, 191, 61))
        self.text1.move(400, 0)
        self.text1.setFont(QFont("Roman times",20,QFont.Bold))

        '''增加/删除节次按钮'''
        self.add = QPushButton('添加题目', self)
        self.add.move(200, 600)

        self.remove = QPushButton('删除题目(题目编号)', self)
        self.remove.move(400, 600)
        self.removeEdit = QLineEdit(self)
        self.removeEdit.setGeometry(400, 650, 120, 30)

        self.submit = QPushButton('更新题目', self)
        self.submit.move(600, 600)

        self.table = QTableWidget(self)
        self.table.setGeometry(100, 100, 800, 500)
        self.table.setRowCount(60)
        self.table.setColumnCount(16)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 150)
        self.table.setColumnWidth(6, 150)
        self.table.setColumnWidth(7, 150)
        self.table.setColumnWidth(8, 150)
        self.table.setColumnWidth(9, 150)
        self.table.setColumnWidth(10, 150)
        self.table.setColumnWidth(11, 150)
        self.table.setColumnWidth(12, 150)
        self.table.setColumnWidth(13, 150)
        self.table.setColumnWidth(14, 150)
        self.table.setColumnWidth(15, 150)
        self.table.setItemDelegateForColumn(0,EmptyDelegate(self))
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['题目编号','题目内容','题目类型','所属专业','所属知识点','填空答案','答案解析','分值','难度系数','图片','选项A','选项B','选项C','选项D','选项E','选项F'])

        rows=database.input_item_title()
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.table.setItem(i, j, QTableWidgetItem(str(rows[i][j])))
        self.add.clicked.connect(lambda :self.addRow())


        '''退出界面按钮'''
        self.returnbtn = QPushButton('返回主目录', self)
        self.returnbtn.setGeometry(400, 700, 150, 40)
        self.returnbtn.setFont(QFont("", 10, QFont.Bold))

        self.setGeometry(300, 300, 1000, 800)
        self.setWindowTitle('题目录入管理')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def addRow(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        rows=database.input_item_title()

        length=database.add_title()
        self.table.setItem(len(rows), 0, QTableWidgetItem('%s' % str(int(length))))
        for i in range(1,16):
            self.table.setItem(len(rows), i, QTableWidgetItem('0'))

class Answer_check(QWidget):#作答记录查看窗口-管理员

    def __init__(self):
        super().__init__()

        self.text1 = QLabel('自测学习系统', self)
        self.text1.setGeometry(QRect(60, 60, 191, 61))
        self.text1.move(120, 0)
        self.text1.setFont(QFont("Roman times",20,QFont.Bold))


        self.major = QLabel('选择即将要查看的专业', self)
        self.major.move(110, 60)
        self.majorEdit = QSpinBox(self)
        self.majorEdit.setGeometry(250, 50, 120, 30)

        '''提交按钮'''
        self.submit = QPushButton('查看', self)
        self.submit.move(400, 60)


        self.submit.clicked.connect(lambda:self.check(self.majorEdit.text()))
        self.table = QTableWidget(self)
        self.table.setGeometry(100, 100, 480, 330)
        self.table.setRowCount(80)
        self.table.setColumnCount(3)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['题目所在知识点','题目','解析'])
        self.table.setItemDelegateForColumn(0,EmptyDelegate(self))#第一列不能更改
        #self.tableView.setItemDelegateForColumn(1,EmptyDelegate(self))
        '''表头字体颜色'''

        '''退出界面按钮'''
        self.returnbtn = QPushButton('返回上一级', self)
        self.returnbtn.setGeometry(320, 450, 150, 40)
        self.returnbtn.setFont(QFont("", 10, QFont.Bold))

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('作答记录查看')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def check(self,majorId):
        self.table.clear()
        rows=database.knowledge_check(majorId)
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.table.setItem(i, j, QTableWidgetItem(rows[i][j]))
        QMessageBox.information(self, 'ok', '成功')



class Title_check(QWidget):#题目查看管理-录题人员
    def __init__(self):
        super().__init__()

        self.text1 = QLabel('自测学习系统', self)
        self.text1.setGeometry(QRect(60, 60, 191, 61))
        self.text1.move(120, 0)
        self.text1.setFont(QFont("Roman times",20,QFont.Bold))

        self.username1 = QLabel('所属专业', self)
        self.username1.move(10, 75)
        self.username1Edit = QLineEdit(self)
        self.username1Edit.setGeometry(170, 70, 120, 30)

        self.username2 = QLabel('所属知识点', self)
        self.username2.move(10, 135)
        self.username2Edit = QLineEdit(self)
        self.username2Edit.setGeometry(170, 130, 120, 30)


        self.table = QTableWidget(self)
        self.table.setGeometry(300, 75, 480, 330)
        self.table.setRowCount(8)
        self.table.setColumnCount(8)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setColumnWidth(4, 150)
        self.table.setColumnWidth(5, 150)
        self.table.setColumnWidth(6, 150)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['题目编号','题目内容','题目类型','填空答案','答案解析','分值','难度系数','图片'])


        '''提交按钮'''
        self.submit = QPushButton('查看', self)
        self.submit.setGeometry(10, 300, 100, 40)


        '''退出界面按钮'''
        self.returnbtn = QPushButton('返回主界面', self)
        self.returnbtn.setGeometry(150, 300, 100, 40)


        self.setGeometry(600, 600, 800, 500)
        self.setWindowTitle('题目录入管理')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Answer1(QWidget):#作答界面-答题人
    def __init__(self):
        super().__init__()

        # global majorId123

        # self.majorId = majorId123
        # print(self.majorId,'!')
        #self.majorId = '0'

        self.text1 = QLabel('自测学习系统', self)
        self.text1.setGeometry(QRect(60, 60, 191, 61))
        self.text1.move(120, 0)
        self.text1.setFont(QFont("Roman times",20,QFont.Bold))
        self.testId=1
        self.paperId=1
        '''表格'''
        self.table = QTableWidget(self)
        self.table.setGeometry(100, 100, 480, 330)
        self.table.setRowCount(11)
        self.table.setColumnCount(2)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['题目','填入区'])
        self.table.setItemDelegateForColumn(0,EmptyDelegate(self))#第一列不能更改
        #self.tableView.setItemDelegateForColumn(1,EmptyDelegate(self))
        '''表头字体颜色'''

        # rows=database.Answer1_check(self.majorId)
        # for i in range(len(rows)):
        #     for j in range(len(rows[i])):
        #         self.table.setItem(i, j, QTableWidgetItem(rows[i][j]))


        self.submit = QPushButton('提交', self)
        self.submit.setGeometry(620, 300, 150, 40)
        self.submit.clicked.connect(self.up)

        self.begain = QPushButton('开始', self)
        self.begain.setGeometry(20, 200, 50, 40)
        self.begain.clicked.connect(lambda :self.ttt())

        '''退出界面按钮'''
        self.returnbtn = QPushButton('返回上一级', self)
        self.returnbtn.setGeometry(620, 380, 150, 40)


        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('作答界面')
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def ttt(self):
        self.table.clear()
        global majorId123
        rows=database.Answer1_check(majorId123)
        print(rows)
        self.table.setHorizontalHeaderLabels(['题目','填入区'])
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                self.table.setItem(i, j, QTableWidgetItem(rows[i][j]))
                print(self.table.item(i,j).text())

    def up(self):
        global majorId123,testId123,paperId123
        testId123 = str(int(random.randint(100,10000)))
        paperId123 = str(int(random.randint(100,10000)))
        rows=database.Answer1_check(majorId123)
        l=['']*10
        for i in range(len(rows)):
            l[i]=self.table.item(i, 1).text()
        # ml=myLogin()
        # print(l)
        #database.up_answer(str(self.testId),str(ml.role),str(self.paperId),l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9])

        database.up_answer(str(testId123),str(majorId123),'1',l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9])
        QMessageBox.information(self, '成功', '提交成功')


class Answer1_check(QWidget):#作答后界面-做题人查看做题数据
    def __init__(self):
        super().__init__()


        self.text1 = QLabel('自测学习系统', self)
        self.text1.setGeometry(QRect(60, 60, 191, 61))
        self.text1.move(120, 0)
        self.text1.setFont(QFont("Roman times",20,QFont.Bold))

        self.table = QTableWidget(self)
        self.table.setGeometry(100, 100, 480, 330)
        self.table.setRowCount(11)
        self.table.setColumnCount(4)
        self.table.setColumnWidth(0, 150)
        self.table.setColumnWidth(1, 150)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 150)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderLabels(['题目','解析','填入区','分值'])
        self.table.setItemDelegateForColumn(0,EmptyDelegate(self))#第一列不能更改
        # rows=database.Answer1_check_2(self.majorId)
        # for i in range(len(rows)):
        #     for j in range(len(rows[i])):
        #         self.table.setItem(i, j, QTableWidgetItem(rows[i][j]))



        self.begain = QPushButton('查看', self)
        self.begain.setGeometry(20, 200, 50, 40)
        self.begain.clicked.connect(lambda :self.ttt())

        self.btn1 = QPushButton('再来一次', self)
        self.btn1.setGeometry(120, 500, 150, 40)
        self.btn1.setFont(QFont("", 10, QFont.Bold))

        '''退出界面按钮'''
        self.returnbtn = QPushButton('返回上一级', self)
        self.returnbtn.setGeometry(320, 500, 150, 40)
        self.returnbtn.setFont(QFont("", 10, QFont.Bold))


        self.setGeometry(500, 600, 800, 800)
        self.setWindowTitle('作答界面')
        self.center()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def ttt(self):
        self.table.clear()
        global majorId123,testId123
        rows=database.Answer1_check_3(majorId123)
        print(rows)
        self.table.setHorizontalHeaderLabels(['题目','解析','填入区','分值'])
        for i in range(len(rows)):
            for j in range(2):
                self.table.setItem(i, j, QTableWidgetItem(rows[i][j]))
                print(self.table.item(i,j).text())
        rows1=database.Answer1_check_4(testId123)
        print(rows1)
        for i in range(len(rows1[0])):
            self.table.setItem(i, 2, QTableWidgetItem(rows1[0][i]))

        for i in range(len(rows)):
            if self.table.item(i,0)!='':
                if self.table.item(i,1).text()==self.table.item(1,2).text():
                    self.table.setItem(i,3,QTableWidgetItem('1'))
                else:
                    self.table.setItem(i,3,QTableWidgetItem('0'))





