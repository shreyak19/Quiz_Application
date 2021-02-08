from Teacher import Teacher
from Student import Student

print("---------------Welcome to Quiz Application---------------")
#q_id=1000
username = input("Enter Username ")
password = input("Enter Password ")

while True:
    print()
    if username == "teacher" and password == "teacher":
        print("---------------Welcome to Quiz Application---------------")
        while True:
            print("\n1. Set Quiz\n2.View Results\n3.Exit")
            ch = int(input("Enter Your Choice "))
            if ch==1:
                #q_id +=1
                t = Teacher()
                t.settest()
            elif ch==2:
                t = Teacher()
                t.viewresults()
            elif ch ==3:
                exit()
            else:
                print("provide correct choice")
                break
    elif username == "student" and password == "student":
        while True:
            s = Student()
            s.view_tests()
            s.appear_for_test()
            print("Thank You")
            ch = input("Wish to appear for another test? y/n ")
            if ch=="n":
                exit()
    else:
        print("Invalid Username or Password")
        break

