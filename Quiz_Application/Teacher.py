from Student import Student

import mysql.connector
cnx = mysql.connector.connect(user='root', password='7767', host='localhost', database='quiz_application')
mycursor = cnx.cursor()

class Teacher:
    '''def __init__(self,id=0):
        self.q_id = id'''
    def settest(self):
        quiz = input("Enter Quiz Name ")
        topics = input("Topics for quiz ")
        difficulty_level = int(input("Enter difficulty level for the quiz "))
        no = int(input("Number of question present in quiz "))
        mycursor.execute("INSERT INTO general_details(Quiz_Name,Topics,Diff_level,No_questions) VALUES(%s,%s,%s,%s)",(quiz,topics,difficulty_level,no))
        Q_ID = mycursor.lastrowid
        cnx.commit()
        q_no = 0
        for i in range(no):
            q_no+=1
            ques = input("Enter question no "+str(q_no)+" ")
            mycursor.execute("INSERT INTO questions(Q_ID,Question) VALUES(%s,%s)",(Q_ID,ques))
            Ques_ID = mycursor.lastrowid
            cnx.commit()
            opt1 = input("Enter Option 1: ")
            opt2 = input("Enter Option 2: ")
            opt3 = input("Enter Option 3: ")
            opt4 = input("Enter Option 4: ")
            corect_opt = input("Enter Correct Option Number: 1/2/3/4 ")
            mycursor.execute("INSERT INTO options(Quiz_ID,Ques_ID,Option1,Option2,Option3,Option4,Correct_Opt) VALUES(%s,%s,%s,%s,%s,%s,%s)",(Q_ID,Ques_ID,opt1,opt2,opt3,opt4,corect_opt))
            cnx.commit()



    def viewresults(self):
        s = Student()
        s.view_tests()
        id = int(input("Enter Quiz id to see performance "))
        mycursor.execute("SELECT * FROM performance_details WHERE Quiz_Id = %s",(id,))
        myresult = mycursor.fetchall()
        print()
        for row in myresult:
            print()
            print("Student Name: ",row[0])
            print("Score Obtained: ",row[2])
            print("Total Score: ",row[3])

        print()
