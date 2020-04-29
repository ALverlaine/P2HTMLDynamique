import sqlite3

def db_to_graph(cours):
    """
    :param cours: une des cours de la db ->"LSINF1101-PYTHON", "LEPL1402", "LSINF1252"
    :return: str du graph
    """
    connection = sqlite3.connect("inginious.sqlite")
    cursor = connection.cursor()
    label=[]
    for row in cursor.execute("SELECT DISTINCT task from submissions WHERE course='{0}'".format(cours)):
        label.append(row[0])

    val=[]
    for i in label:
        for row in cursor.execute("SELECT count(task) from submissions WHERE task='{0}'".format(i)):
            val.append(row[0])
    connection.close()

    return [cours, label, val]
l=db_to_graph("LSINF1252")
print(l[0])
print(l[1])
print(l[2])
