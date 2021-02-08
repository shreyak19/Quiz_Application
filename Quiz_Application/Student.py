import mysql.connector
cnx = mysql.connector.connect(user='root', password='7767', host='localhost', database='quiz_application')
mycursor = cnx.cursor()

class Student:
    def __init__(self):
        self.score =0
    def view_tests(self):
        mycursor.execute("SELECT * FROM general_details")
        myresult = mycursor.fetchall()
        print("Total Quizes count = ",mycursor.rowcount)
        print()
        for row in myresult:
            print()
            print("Quiz Name: ",row[0])
            print("Topics covered: ",row[1])
            print("Difficulty level: ",row[2])
            print("Number of Questions: ",row[3])
            print("Quiz ID: ",row[4])
        print()
    def appear_for_test(self):
        Name = input("Enter your name: ")
        quiz_id = int(input("Enter Quiz Id"))
        mycursor.execute("Select Question,Option1,Option2,Option3,Option4,Correct_Opt FROM questions INNER JOIN options ON (questions.Q_ID = options.Quiz_ID AND  questions.Ques_ID = options.Ques_ID) WHERE questions.Q_ID= %s",(quiz_id,))
        myresult = mycursor.fetchall()
        print("Total Question count = ", mycursor.rowcount)
        n = mycursor.rowcount
        print()
        for row in myresult:
            print("Question: ", row[0])
            print("Option 1: ", row[1])
            print("Option 2: ", row[2])
            print("Option 3: ", row[3])
            print("Option 4: ", row[4])
            print()
            ans = int(input("Your Answer: "))
            if ans == row[5]:
                self.score += 1
            print()
        print("------------------------------------------")

        print("Your Score: "+str(self.score)+"/"+str(mycursor.rowcount))
        mycursor.execute("INSERT INTO performance_details(Student_Name,Quiz_ID,Score_Obtained,Total_Score)Values(%s,%s,%s,%s)",(Name,quiz_id,self.score,n))
        cnx.commit()


