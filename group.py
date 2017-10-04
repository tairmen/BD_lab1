def add_group(db):
    gr=input("Please enter the new group: ")
    db.append((gr,[]))


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
        i = i+1
    if (p == 0):
        print("group ", gr, " not founded")
