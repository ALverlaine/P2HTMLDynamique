import sqlite3

connection = sqlite3.connect("inginious.sqlite")
cursor = connection.cursor()
#extraction
val=[]
label=['failed','killed','success','overflow','timeout','crash','error']
for i in label:
    for row in cursor.execute("SELECT count(task) from submissions WHERE course='LEPL1402' and task='BubbleSortInvariant' and result='{0}'".format(i)):
        val.append(row[0])
print(val)

connection.close()



