import pickle

def create_file():
    data = [(
            "kv-52",
            [("Abduraimov", 48023, 20), ("Kovalev", 90454, 21), ("Depp", 48785, 40), ("Mocart", 90456, 90)]),
        (
            "kp-42",
            [("Ivanov", 43225, 33), ("Tolstoy", 42321, 66), ("Pushkin", 53213, 54), ("Ahmatova", 42343, 41)]),
        (
            "km-73",
            [("Hachaturyan", 53212, 70), ("Chaykovskiy", 23456, 77), ("Obama", 42399, 40)]),
        (
            "km-62",
            [("Bob", 31233, 18), ("Smith", 31234, 22), ("Trump", 94833, 60)])
    ]
    with open('d.pickle', 'wb') as f:
        pickle.dump(data, f)

create_file()
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
        view_bd(fpm)
        Menu()
    elif(check == '2'):
        add_student(fpm)
        Menu()
    elif (check == '3'):
        add_group(fpm)
        Menu()
    elif(check == '4'):
        find_group(fpm)
        Menu()
    elif(check == '5'):
        find_student(fpm)
        Menu()
    elif (check == '6'):
        del_student(fpm)
        Menu()
    elif (check == '7'):
        del_group(fpm)
        Menu()
    elif (check == '8'):
        youngest_students(fpm)
        Menu()
    elif (check == '9'):
        change_student(fpm)
        Menu()
    elif(check == '0'):
        with open('d.pickle', 'wb') as f:
            pickle.dump(db, f)
    else:
        Menu()

def view_bd(db):
    print("%10s" % "GROUP", "%20s" % "STUDENT", "%7s" % "ID", "%5s" % "AGE")
    for rec in db:
        print("%10s" % rec[0])
        for element in rec[1]:
            print("%30s" % element[0], "%7s" % element[1], "%5s" % element[2])

def find_group(db):
    p = 0
    gr = input("Please enter your group: ")
    for rec in db:
        if (rec[0]==gr):
             p = 1
             print("%30s" % "STUDENT", "%7s" % "ID", "%5s" % "AGE")
             for element in rec[1]:
                  print("%30s" % element[0], "%7d" % element[1], "%5s" % element[2])
    if (p == 0):
        print("Group ", gr, "not founded")

def find_student(db):
    p = 0
    st = input("Please enter name of student: ")
    for rec in db:
        for tmp in rec[1]:
            if (tmp[0]==st):
                p = 1
                print("%10s" % "GROUP", "%7s" % "ID", "%5s" % "AGE")
                print("%10s" % rec[0], "%7d" % tmp[1], "%5s" % tmp[2])
    if (p == 0):
        print("Student ",st, "not founded")

def add_student(db):
    st=input("Please enter name of the new student: ")
    for rec in db:
        for tmp in rec[1]:
            if (tmp[0]==st):
                print("This student present in database")
    id=int(input("Please enter id of the new student: "))
    for rec in db:
        for tmp in rec[1]:
            if (tmp[1]==id):
                print("Student with this id present in database")
    age=int(input("Please enter age of the new student: "))
    gr=input("Please enter the new student group: ")
    p = 0
    i = 0
    while i < len(db) :
        if (db[i][0] == gr):
            p = 1
            db[i][1].append((st, id))
        i = i+1
    if (p == 0):
        print("Group ", gr, " not founded, create this group or retry")
    else:
        print("Student ", st, "succesfully added to group ", gr)

def add_group(db):
    gr=input("Please enter the new group: ")
    db.append((gr,[]))

def del_student(db):
    st = input("Please enter name of the student to delete: ")
    p = 0
    i = 0
    while i < len(db):
        j = 0
        while j < len(db[i][1]):
            if (db[i][1][j][0]==st):
                p = 1
                print("Student ", st," with id ", db[i][1][j][1] ," from group ", db[i][0] ," has been deleted")
                db[i][1].remove(db[i][1][j])
            j = j+1
        i = i+1
    if (p == 0):
        print("Student ",st, "not founded")

def del_group(db):
    gr = input("Please enter the group to delete: ")
    p = 0
    i = 0
    while i < len(db):
        if (db[i][0] == gr):
            p = 1
            print("group ", gr, " was deleted with students: ")
            for rec in db[i][1]:
                print(rec[0], " id ",rec[1], " age ",rec[2])
            db.remove(db[i])
    if (p == 0):
        print("group ", gr, " not founded")

def youngest_students(db):
    for rec in db:
        min = rec[1][0]
        for tmp in rec[1]:
            if(tmp[2] < min[2]):
                min = tmp
        print("in group ", rec[0]," youngest: ", min[0], " , id = ",min[1], " , age = ",min[2])

def change_student(db):
    p = 0
    i = 0
    st = input("Please enter the name of student: ")
    while i < len(db):
        j = 0
        while j < len(db[i][1]):
            if (db[i][1][j][0]==st):
                p = 1
                print("id = ", db[i][1][j][1], ", age = ", db[i][1][j][2], ", group = ", db[i][0])
                break
            j = j+1
        if (p == 1):
            break
        i = i+1
    if (p == 0):
        print("Student ",st, "not founded")
        return
    print("Change the age of student          Press 1")
    print("Change the group of student        Press 2")
    print("Change the id of student           Press 3")
    check = input()
    if (check == '1'):
        age = db[i][1][j][2]
        age = age + 1
        idd = db[i][1][j][1]
        db[i][1].remove(db[i][1][j])
        db[i][1].append((st,idd,age))
    elif (check == '2'):
        ngr = input("Please enter new group for student: ")
        k = 0
        while (k < len(db)):
            if (db[k][0] == ngr):
                p = 1
                cash = db[i][1][j]
                db[k][1].append(cash)
                db[i][1].remove(cash)
            k = k+1
        if (p == 0):
            print("Group ", gr, "not founded")
    elif (check == '3'):
        age = db[i][1][j][2]
        idd = input("Please enter new id: ")
        db[i][1].remove(db[i][1][j])
        db[i][1].append((st, idd, age))

Menu()
