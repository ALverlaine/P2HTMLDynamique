import sqlite3

connection = sqlite3.connect("inginious.sqlite")
cursor = connection.cursor()
#extraction
val=[]
label=[]
all=[]
cours="LEPL1402"
# TODO voir pq il n affiche pas toute la liste meme lorsque je precise l indice
#WHERE substr(submitted_on,0,8)> '2020-02-15'
for row in cursor.execute("SELECT  substr(submitted_on,0,11) from submissions WHERE course='{0}'".format(cours)):
    all.append(row[0])
    if row[0] in label:
        val[len(val)-1]+=1
    else:
        label.append(row[0])
        val.append(1)


print(all)
print(len(all))
print('2020-02-16'in all)
print('2020-02-16'>'2020-02-15')
connection.close()
print(len(label))
print(len(val))





