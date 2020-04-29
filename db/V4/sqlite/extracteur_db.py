import sqlite3

# donnees concernant un seul cours uniquement
# x: les taches du cours
# y: le nombre de soumisssions pour chacunes des taches (de l axe des x)
def course_tasks_graph(cours):
    """
    :param cours: une str des cours de la db ->"LSINF1101-PYTHON", "LEPL1402", "LSINF1252"
    :return: une liste du type L[0]=str(type de graphique), L[1]=str(cours), L[2]=list(label), L[3]= list(valeurs)
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

    return ['bar',cours, label, val]

# donnees concernant la tache d un cours uniquement
# x: les possibilites des resultats suite a une soumission
# y: le nombre de soumissions correspondant aux differents etats
def task_result_graph(cours, task):
    """
    :param cours: Le nom du cours qui contient la tache (str)
    :param task: Le nom de la tache dont on veut voir les statistiques (str)
    :return: une liste du type L[0]=str(cours),L[1]=str(task), L[2]=list(label), L[3]= list(valeurs)
    """
    connection = sqlite3.connect("inginious.sqlite")
    cursor = connection.cursor()
    val = []
    label = ['failed', 'killed', 'success', 'overflow', 'timeout', 'crash', 'error']
    for i in label:
        for row in cursor.execute("SELECT count(task) from submissions WHERE course='{0}' and task='{1}' and result='{2}'".format(cours,task,i)):
            val.append(row[0])
    connection.close()
    return [cours,task,label,val]

# donnees concernant un cours uniquement
# x: le temps
# y:le nombre de soumissions pour chaque journees
def subm_time_graph(cours):
    """
    :param cours:
    :return:
    """
    connection = sqlite3.connect("inginious.sqlite")
    cursor = connection.cursor()
    val = []
    label = []
    #TODO voir pourquoi l'ensemble de la liste ne s'affiche pas dans la run box alors que l'info s y trouve (verification faite avec une expression boo)
    for row in cursor.execute("SELECT  substr(submitted_on,0,11) from submissions WHERE course='{0}'".format(cours)):
        if row[0] in label:
            val[len(val) - 1] += 1
        else:
            label.append(row[0])
            val.append(1)
    connection.close()
    return ['line', cours, label, val]
print(subm_time_graph('LEPL1402'))
print('2019-07-10'in subm_time_graph('LEPL1402')[2])
print(subm_time_graph('LEPL1402')[3])


