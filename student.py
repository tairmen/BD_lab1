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
            db[i][1].append((st, id, age))
        i = i+1
    if (p == 0):
        print("Group ", gr, " not founded, create this group or retry")
    else:
        print("Student ", st, "succesfully added to group ", gr)


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
        print("age succesfully increased")
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
            print("Group ", ngr, "not founded")
        else:
            print("group of student ", st,"succesfully changed to ", ngr)
    elif (check == '3'):
        age = db[i][1][j][2]
        idd = int(input("Please enter new id: "))
        db[i][1].remove(db[i][1][j])
        db[i][1].append((st, idd, age))
        print("id of student succesfully changed")
