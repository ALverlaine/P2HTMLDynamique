import sqlite3

connection = sqlite3.connect("inginious.sqlite")
cursor = connection.cursor()

#1ere table: submissions
#dico LSINF1101-PYTHON : lst(taches)
d={}
label_lsinf1101=[]
for row in cursor.execute("SELECT DISTINCT task from submissions WHERE course='LSINF1101-PYTHON'"):
    label_lsinf1101.append(row[0])

val_lsinf1101=[]
for i in label_lsinf1101:
    for row in cursor.execute("SELECT count(task) from submissions WHERE task='{0}'".format(i)):
        val_lsinf1101.append(row[0])
print(label_lsinf1101)
print( val_lsinf1101)





connection.close()
