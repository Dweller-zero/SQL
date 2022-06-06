from manage import *
import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    '''实例化'''
    l = myLogin()#开始界面
    r1 = myRegister()#注册界面
    c1 = myControl_1()#超级管理员
    c2 = myControl_2()#录题人
    c3 = myControl_3()#答题人
    um = myUser_manage()#登录账号管理-管理员
    ti = myTitle_input()#题目录入管理-管理员/录题人员
    ac = myAnswer_check()#作答记录查看窗口-管理员
    tc = myTitle_check()#题目查看管理-录题人员
    a1 = myAnswer1()#作答界面-答题人
    a1c = myAnswer1_check()#作答后界面-做题人查看做题数据


    '''显示登录界面'''
    l.show()
    '''跳转不同身份对应控制界面'''
    l.close_register_1.connect(r1.show)#注册
    l.close_signal_1.connect(c1.show)#超级管理员
    l.close_signal_2.connect(c2.show)#录题人
    l.close_signal_3.connect(c3.show)#答题人

    '''注册页面'''
    r1.change4_sign.connect(l.show)#返回

    '''管理员界面'''
    c1.change4_sign.connect(l.show)#返回
    c1.change1_sign.connect(um.show)#返回登录账号管理-管理员
    c1.change2_sign.connect(ti.show)#返回题目录入管理-管理员/录题人员
    c1.change3_sign.connect(ac.show)#返回作答记录查看窗口-管理员
    um.change3_sign.connect(c1.show)#返回
    ti.change3_sign.connect(l.show)#返回
    ac.change3_sign.connect(c1.show)#返回

    '''录题人员页面'''
    c2.change1_sign.connect(ti.show)
    c2.change2_sign.connect(tc.show)#题目查看管理-录题人员
    c2.change3_sign.connect(l.show)

    tc.change3_sign.connect(c2.show)


    '''答题人员页面'''

    c3.change3_sign.connect(a1.show)
    c3.change4_sign.connect(a1c.show)
    c3.change5_sign.connect(l.show)

    a1.change3_sign.connect(c3.show)
    a1c.change1_sign.connect(a1.show)
    a1c.change3_sign.connect(c3.show)


    app.exec_()

