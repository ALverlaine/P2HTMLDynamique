import sqlite3

def task_result_graph(cours, task):
    """
    :param cours: Le nom du cours qui contient la tache (str)
    :param task: Le nom de la tache dont on veut voir les statistiques (str)
    :return: une liste du type L[0]=str(cours),L[1]=str(task), L[2]=list(label), L[3]= list(valeurs)
    """
    connection = sqlite3.connect("inginious.sqlite")
    cursor = connection.cursor()
    val = []
    label = []
    border = []
    back = []
    mix = [[0,'failed',"rgb(255, 99, 132)","rgba(255, 99, 132, 0.2)"],
           [0,'killed',"rgb(255, 205, 86)","rgba(255, 205, 86, 0.2)"],
           [0,'success',"rgb(75, 192, 192)","rgba(75, 192, 192, 0.2)"],
           [0,'overflow',"rgb(54, 162, 235)","rgba(54, 162, 235, 0.2)"],
           [0,'timeout',"rgb(201, 203, 207)","rgba(201, 203, 207, 0.2)"],
           [0,'crash',"rgb(153, 102, 255)","rgba(153, 102, 255, 0.2)"],
           [0,'error',"rgb(255, 159, 64)","rgba(255, 159, 64, 0.2)"]]
    for i, v in enumerate(mix):
        for row in cursor.execute("SELECT count(task) from submissions WHERE course='{0}' and task='{1}' and "
                                  "result='{2}'".format(cours, task, v[1])):
            mix[i][0] = row[0]
    connection.close()
    mix.sort()
    for i in mix:
        label.append(i[1])
        border.append(i[2])
        back.append(i[3])
        val.append(i[0])
    return [cours, task, label, val, border, back]


a = task_result_graph('LEPL1402', 'Array2D')
print(a)






