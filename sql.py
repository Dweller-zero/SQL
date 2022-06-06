import pymssql
import random

def connect():
    conn = pymssql.connect(server='localhost', database='test1')
    return conn

class database(object):
    def __init__(self):
        pass

    @staticmethod
    def login_check(username, password):#判断是否在表内
        print(username, password)
        sql = "SELECT * FROM [User]"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)
        flag = 0
        for row in rows:
            print(row,row[1],row[4],type(username),type(row[1]))
            if username == row[1] and password == row[4]:
                flag = 1
                break
        print(flag)
        return flag
        conn.close()

    @staticmethod
    def check_Role(username):#判断角色
        sql = "SELECT userName,userRole,userId FROM [User]"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            if username == row[0]:
                flag = int(row[1])
                role =  row[2]
                break
        return flag,role
        conn.close()

    @staticmethod
    def insertUserInfo(username, username_English, password, major, phone):#注册新用户
        sql = "SELECT COUNT(*) FROM [User]"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        #print(rows[0][0])
        length = str(int(rows[0][0])+100)


        userRole='2'
        sql = "INSERT INTO [User] VALUES(%s, %s, %s, %s, %s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(length, username, username_English, userRole, password, phone, major))
        conn.commit()
        conn.close()

    @staticmethod
    def input_item():#将数据填充到表格中
        sql = "SELECT * FROM [User]"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def add_user():#user增加一列

        sql = "SELECT COUNT(*) FROM [User]"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        #print(rows[0][0])
        #length = str(int(10000-rows[0][0]))
        length = str(int(random.randint(100,10000)))
        sql = "INSERT INTO [User] VALUES(%s, 'test', 'test', '2', 'test',NULL,NULL)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(length))
        conn.commit()
        conn.close()
        return length

    @staticmethod

    def upgrade_user(userId,username, username_English, userRole,password, phone, major):#user更新

        sql = "UPDATE [User] set userName=%s, userEnglishName=%s, userRole=%s,passWord=%s, telephoneNumber=%s, majorId=%s where userId=%s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(username, username_English, userRole,password, phone, major,userId))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_user(userId):#user减少一列

        sql = "DELETE from [User] where userId = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(userId))
        conn.commit()
        conn.close()

#----------------------------------------------



    @staticmethod
    def input_item_title():#将数据填充到表格中
        sql = "SELECT * FROM Title"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def add_title():#title增加一列

        sql = "SELECT COUNT(*) FROM Title"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        #print(rows[0][0])
        #length = str(int(10000-rows[0][0]))
        length = str(int(random.randint(100,10000)))
        sql = "INSERT INTO Title VALUES(%s, 't', 't', '0', '0', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't')"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(length))
        conn.commit()
        conn.close()
        return length

    @staticmethod

    def upgrade_title(titleId,titleContent, titleType, majorId,knowledgeId, answer, answerDetails,points,difficultyLevel,picture,selectFlagA,selectFlagB,selectFlagC,selectFlagD,selectFlagE,selectFlagF):#title更新

        sql = "UPDATE Title set titleContent=%s, titleType=%s, majorId=%s,knowledgeId=%s, answer=%s, answerDetails=%s, points=%s, difficultyLevel=%s, picture=%s, selectFlagA=%s, selectFlagB=%s, selectFlagC=%s, selectFlagD=%s, selectFlagE=%s, selectFlagF=%s where titleId=%s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(titleContent, titleType, majorId,knowledgeId, answer, answerDetails,points,difficultyLevel,picture,selectFlagA,selectFlagB,selectFlagC,selectFlagD,selectFlagE,selectFlagF,titleId))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_title(titleId):#title减少一列

        sql = "DELETE from Title where titleId = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(titleId))
        conn.commit()
        conn.close()

#----------------------------------------------


    @staticmethod
    def title_check(majorId,knowledgeId):#录题人查看,条件查询
        sql = "SELECT titleId,titleContent, titleType, answer, answerDetails,points,difficultyLevel,picture FROM Title where majorId= %s and knowledgeId = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(majorId,knowledgeId))
        rows = cur.fetchall()
        return rows
        conn.close()




#----------------------------------------------


    @staticmethod
    def knowledge_check(majorId):#管理员查看
        sql = "SELECT knowledgeId,titleContent, answer FROM Title where majorId= %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(majorId))
        rows = cur.fetchall()
        return rows
        conn.close()


#----------------------

    @staticmethod
    def Answer1_check(majorId):#做题人查看,条件查询
        sql = "SELECT titleId FROM Title where majorId=%s"

        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(majorId))
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def up_answer(testId,userId,paperId,result1,result2,result3,result4,result5,result6,result7,result8,result9,result10):#做题人交卷子
        sql = "INSERT into Answer(testId,userId,paperId,result1,result2,result3,result4,result5,result6,result7,result8,result9,result10) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(testId,userId,paperId,result1,result2,result3,result4,result5,result6,result7,result8,result9,result10))
        conn.commit()
        conn.close()



#------------------------



    @staticmethod
    def Answer1_check_2(majorId,paperId,userId):#做题人查看,条件查询,前2个是paper，后1个是题目，前2个对于前2个后一个对应后1个，分值做判断赋值
        sql = "SELECT title1,title2,title3,title4,title5,title6,title7,title8,title9,title10 FROM Paper where majorId=%s and paperId=%s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(majorId,paperId))
        rows1 = cur.fetchall()
        print(rows1)
        sql = "SELECT result1,result2,result3,result4,result5,result6,result7,result8,result9,result10 FROM Paper where userId=%s and paperId=%s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(userId,paperId))
        rows2 = cur.fetchall()
        return rows
        conn.close()



    @staticmethod
    def Answer1_check_3(majorId):#做题人查看,查询答案与分值
        sql = "SELECT titleId,answerDetails,answer FROM Title where majorId=%s"

        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(majorId))
        rows = cur.fetchall()
        return rows
        conn.close()

    def Answer1_check_4(testId):#做题人查看,查询答案与分值
        sql = "SELECT result1,result2,result3,result4,result5,result6,result7,result8,result9,result10 FROM Answer where testId=%s"

        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(testId))
        rows = cur.fetchall()
        return rows
        conn.close()



    @staticmethod
    def insertClassInfo(classid, classSection, classGrade, classNo, classRoomNo):
        sql = "INSERT INTO Class VALUES(%d, %s, %s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,(classid, classSection, classGrade,classNo, classRoomNo))
        conn.commit()
        conn.close()

    def queryClassId_isExist(ClassId):
        sql = "SELECT classId FROM Class"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        flag = 0
        for row in rows:
            if ClassId == row[0]:
                flag = 1
                break
        return flag
        conn.close()

    def updateClassInfo(classId, classRoomNo):
        sql = "UPDATE Class SET classRoomNo = %s WHERE classId = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (classRoomNo, classId))
        conn.commit()
        conn.close()

    def queryClassId(self):
        sql = "SELECT classId FROM Class"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def insertTeacherInfo(teacherName, teachSubject, subjectId):
        sql = "INSERT INTO Teacher(teacherName, teachSubject, subjectId) VALUES(%s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (teacherName, teachSubject, subjectId))
        conn.commit()
        conn.close()

    @staticmethod
    def querySchedule_by_timeId(id):
        sql = "SELECT timeId FROM Schedule"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        flag = 0
        for row in rows:
            if id == row[0]:
                flag = 1
                break
        return flag
        conn.close()

    @staticmethod
    def updateScheduleInfo(id, startTime, endTime):
        sql = "UPDATE Schedule SET startTime = %s, endTime = %s WHERE timeId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (startTime, endTime, id))
        conn.commit()
        conn.close()

    @staticmethod
    def insertScheduleInfo(timeId, setion, startTime, endTime):
        sql = "INSERT INTO Schedule VALUES(%d, %s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (timeId, setion, startTime, endTime))
        conn.commit()
        conn.close()

    @staticmethod
    def querySubjectNo_by_subjectName(subjectName):
        sql = "SELECT subjectNo FROM Subjects WHERE subjectName = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,subjectName)
        id = cur.fetchone()
        return id[0]
        conn.close()

    @staticmethod
    def queryPeriod(id):
        sql = "SELECT periodId FROM Period"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        flag = 0

        for row in rows:
            if id == row[0]:
                flag = 1
                break
        return flag
        conn.close()

    @staticmethod
    def updatePeriodInfo(periodNumber,id):
        sql = "UPDATE Period SET periodNumber = %s WHERE periodId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (periodNumber, id))
        conn.commit()
        conn.close()

    @staticmethod
    def insertPeriodInfo(periodId, setion, subjectName, periodNumber):
        sql = "INSERT INTO Period VALUES(%d, %s, %s, %s)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (periodId, setion, subjectName, periodNumber))
        conn.commit()
        conn.close()

    def queryAllSubject(self):
        sql = "SELECT subjectName FROM Subjects"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
        conn.close()

    def queryAllTeacher(self):
        sql = "SELECT teacherName FROM Teacher"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
        conn.close()

    def queryTeacherId_by_teacherName(teacherName):
        sql = "SELECT teacherId FROM Teacher WHERE teacherName = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,teacherName)
        id = cur.fetchone()
        return id[0]
        conn.close()

    @staticmethod
    def insertSubjectGroup(groupName, leaderId):
        sql = "INSERT INTO SubjectGroup VALUES (%s, %d)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (groupName, leaderId))
        conn.commit()
        conn.close()

    def queryAllSubjectGroup(self):
        sql = "SELECT SubjectGroupName FROM SubjectGroup"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def updateSubjectsInfo(subjectName, subjectGroupNo):
        sql = "UPDATE Subjects SET subjectGroupNo = %d WHERE subjectName = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (subjectGroupNo, subjectName))
        conn.commit()
        conn.close()

    def querySubjectGroupId_by_SubjectGroupName(subjectGroupName):
        sql = "SELECT subjectGroupId FROM SubjectGroup WHERE subjectGroupName = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,subjectGroupName)
        id = cur.fetchone()
        print(id[0])
        return id[0]
        conn.close()

    @staticmethod
    def queryClass_by_Section(section):
        sql = "SELECT classId FROM Class WHERE classSection = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, section)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def queryTeacherName_by_subject(subject):
        sql = "SELECT teacherName FROM Teacher WHERE teachSubject = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql,subject)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def insertLectureForm(lectureId, semesterNo, teacherId, subjectName, classId):
        sql = "INSERT INTO LectureForm VALUES (%d, %d, %d, %s, %d)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (lectureId, semesterNo, teacherId, subjectName, classId))
        conn.commit()
        conn.close()

    @staticmethod
    def queryTeacherId_by_LectureId(lectureId):
        sql = "SELECT lectureId FROM LectureForm"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        flag = 0
        for row in rows:
            if lectureId == row[0]:
                flag = 1
                break
        return flag
        conn.close()

    @staticmethod
    def updateLectureForm(teacherId, lectureId):
        sql = "UPDATE LectureForm SET teacherId = %d WHERE lectureId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (teacherId, lectureId))
        conn.commit()
        conn.close()

    @staticmethod
    def querySection_by_classId(classId):
        sql = "SELECT classSection FROM Class WHERE classId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, classId)
        row = cur.fetchone()
        return row
        conn.close()

    @staticmethod
    def queryTimeId_by_Section(section):
        sql = "SELECT timeId FROM Schedule WHERE section = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, section)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def queryPeriod_by_Section(section):
        sql = "SELECT subjectName,periodNumber FROM Period WHERE section = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, section)
        rows = cur.fetchall()
        return rows
        conn.close()

    @staticmethod
    def insertLesson(courseId, lectureId, weekNo, timeId):
        sql = "INSERT INTO Lesson VALUES (%d, %d, %s, %d)"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (courseId, lectureId, weekNo, timeId))
        conn.commit()
        conn.close()

    @staticmethod
    def updateLesson(courseId, lectureId):
        sql = "UPDATE Lesson SET lectureId = %d WHERE courseId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (lectureId, courseId))
        conn.commit()
        conn.close()

    @staticmethod
    def queryLectureId_by_courseId(courseId):
        sql = "SELECT lectureId FROM Lesson WHERE courseId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, courseId)
        row = cur.fetchone()
        return row
        conn.close()

    @staticmethod
    def querySubjectId_by_lectureId(lectureId):
        sql = "SELECT subjectId FROM LectureForm WHERE lectureId = %d"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, lectureId)
        row = cur.fetchone()
        return row
        conn.close()

    @staticmethod
    def querySubjectName_by_Id(Id):
        sql = "SELECT subjectName FROM Subjects WHERE subjectNo = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, Id)
        row = cur.fetchone()
        return row
        conn.close()

    @staticmethod
    def queryLessonId_isExist(courseId):
        sql = "SELECT courseId FROM Lesson"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        flag = 0
        for row in rows:
            if courseId == row[0]:
                flag = 1
                break
        return flag
        conn.close()

    def updateTeacher_subjectGroupId_by_subjectName(subjectGroupId, teachSubject):
        sql = "UPDATE Teacher SET subjectGroupId = %d WHERE teachSubject = %s"
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (subjectGroupId, teachSubject))
        conn.commit()
        conn.close()


