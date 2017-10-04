def view_bd(db):
    print("%10s" % "GROUP", "%20s" % "STUDENT", "%7s" % "ID", "%5s" % "AGE")
    for rec in db:
        print("%10s" % rec[0])
        for element in rec[1]:
            print("%30s" % element[0], "%7s" % element[1], "%5s" % element[2])

def youngest_students(db):
    for rec in db:
        min = rec[1][0]
        for tmp in rec[1]:
            if(tmp[2] < min[2]):
                min = tmp
        print("in group ", rec[0]," youngest: ", min[0], " , id = ",min[1], " , age = ",min[2])
