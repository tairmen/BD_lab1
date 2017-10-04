import pickle
import student
import group
import show
import create

create.create_file('d.pickle')
with open('d.pickle', 'rb') as f:
    fpm = pickle.load(f)

def Menu():
    print("\n")
    print("Show the database?                   Press 1")
    print("Add a student to the database?       Press 2")
    print("Add a group to the database?         Press 3")
    print("Find a group in the database?        Press 4")
    print("Find a student in the database?      Press 5")
    print("Delete student from database?        Press 6")
    print("Delete group from database?          Press 7")
    print("Show the yongest student in groups?  Press 8")
    print("Change the features of student?      Press 9")
    print("Exit from the program?               Press 0")
    check = input()
    if (check == '1'):
        show.view_bd(fpm)
        Menu()
    elif(check == '2'):
        student.add_student(fpm)
        Menu()
    elif (check == '3'):
        group.add_group(fpm)
        Menu()
    elif(check == '4'):
        group.find_group(fpm)
        Menu()
    elif(check == '5'):
        student.find_student(fpm)
        Menu()
    elif (check == '6'):
        student.del_student(fpm)
        Menu()
    elif (check == '7'):
        group.del_group(fpm)
        Menu()
    elif (check == '8'):
        show.youngest_students(fpm)
        Menu()
    elif (check == '9'):
        student.change_student(fpm)
        Menu()
    elif(check == '0'):
        with open('d.pickle', 'wb') as f:
            pickle.dump(fpm, f)
    else:
        Menu()

Menu()
