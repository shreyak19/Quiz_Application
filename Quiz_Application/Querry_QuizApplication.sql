
Show databases;

Create database quiz_application;

Use quiz_application;

create table general_details(Quiz_Name VARCHAR(50),Topics VARCHAR(70),Diff_level INT,No_questions INT,Q_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY);

create table questions(Q_ID INT NOT NULL,Ques_ID INT NOT NULL AUTO_INCREMENT,Question VARCHAR(70),PRIMARY KEY(Ques_ID),FOREIGN KEY(Q_ID) REFERENCES general_details(Q_ID));

create table options(Opt_ID INT NOT NULL AUTO_INCREMENT,QUIZ_ID INT NOT NULL,Ques_ID INT NOT NULL,Option1 VARCHAR(30),Option2 VARCHAR(30),Option3 VARCHAR(30),Option4 VARCHAR(30),Correct_Opt INT, PRIMARY KEY(opt_ID),FOREIGN KEY(Quiz_ID) REFERENCES questions(Q_ID),FOREIGN KEY(Ques_ID) REFERENCES questions(Ques_ID));

create table performance_details(Student_Name VARCHAR(30),Quiz_Id INT,Score_Obtained INT, Total_Score INT);
