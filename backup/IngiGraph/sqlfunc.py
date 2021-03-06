import sqlite3

def course_tasks_graph(cours):
    """
    :param cours: une str des cours de la db ->"LSINF1101-PYTHON", "LEPL1402", "LSINF1252"
    :return: une liste :type de graphique, cours, label, valeurs
    """
    connection = sqlite3.connect("inginious.sqlite")
    cursor = connection.cursor()
    label = []
    val = []
    mix = []
    back = 'rgb(255, 99, 132)'
    border = 'rgb(255, 99, 132)'
    for row in cursor.execute("SELECT DISTINCT task from submissions WHERE course='{0}'".format(cours)):
        mix.append([0, row[0]])
    for i in mix:
        for row in cursor.execute("SELECT count(task) from submissions WHERE task='{0}'".format(i[1])):
            i[0] = row[0]
    connection.close()
    mix.sort()
    for i in mix:
        val.append(i[0])
        label.append(i[1])
    return ['bar', cours, label, val, border, back]

def task_result_graph(cours):
    """
    :param cours: Le nom du cours qui contient la tache (str)
    :param task: Le nom de la tache dont on veut voir les statistiques (str)
    :return: une liste :cours, tache,type de graph, les labels correspondants aux val, les val triees, couleur de bord et couleur de fond
    """
    connection = sqlite3.connect("inginious.sqlite")
    cursor = connection.cursor()
    label = []
    border = []
    full = []
    t = tasks(cours)
    for j in range(len(t)):
        val = []
        mix = [[0, 'failed', "rgb(255, 99, 132)", "rgba(255, 99, 132, 0.2)"],
               [0, 'killed', "rgb(255, 205, 86)", "rgba(255, 205, 86, 0.2)"],
               [0, 'success', "rgb(75, 192, 192)", "rgba(75, 192, 192, 0.2)"],
               [0, 'overflow', "rgb(54, 162, 235)", "rgba(54, 162, 235, 0.2)"],
               [0, 'timeout', "rgb(201, 203, 207)", "rgba(201, 203, 207, 0.2)"],
               [0, 'crash', "rgb(153, 102, 255)", "rgba(153, 102, 255, 0.2)"],
               [0, 'error', "rgb(255, 159, 64)", "rgba(255, 159, 64, 0.2)"]]
        for i, v in enumerate(mix):
            for row in cursor.execute("SELECT count('{0}') from submissions WHERE course='{1}' and task='{2}' and "
                                      "result='{3}'".format(t[j],cours, t[j], v[1])):
                mix[i][0] = row[0]
        mix.sort()
        for i in mix:
            val.append(i[0])
        full.append(val)
    connection.close()
    return [cours, 'pie',  ['error', 'overflow', 'timeout', 'killed', 'crash', 'success', 'failed'], full,
            ['rgb(255, 159, 64)', 'rgb(54, 162, 235)', 'rgb(201, 203, 207)', 'rgb(255, 205, 86)', 'rgb(153, 102, 255)',
             'rgb(75, 192, 192)', 'rgb(255, 99, 132)'],
            ['rgba(255, 159, 64, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(201, 203, 207, 0.2)',
             'rgba(255, 205, 86, 0.2)', 'rgba(153, 102, 255, 0.2)', 'rgba(75, 192, 192, 0.2)',
             'rgba(255, 99, 132, 0.2)']]


def subm_time_graph(cours,t1,t2):
    """
    :param cours:
    :param t1: temps initial de la période a traiter incluse
    :param t2: temps final de la periode a traiter excluse
    :return:
    """
    connection = sqlite3.connect("inginious.sqlite")
    cursor = connection.cursor()
    val = []
    label = []
    back = 'rgb(255, 99, 132)'
    border = 'rgb(255, 99, 132)'
    for row in cursor.execute("SELECT substr(submitted_on,0,17) from submissions WHERE course='{0}'".format(cours)):
        if t1 <= row[0] < t2:
            if row[0] in label:
                val[len(val) - 1] += 1
            else:
                label.append(row[0])
                val.append(1)
    connection.close()
    return ['line', cours, label, val, border, back]

def tasks(cours):
    t = []
    connection = sqlite3.connect("inginious.sqlite")
    cursor = connection.cursor()
    for row in cursor.execute(
            "SELECT task FROM user_tasks WHERE course = '{}' GROUP BY task HAVING SUM(tried) != 0 ORDER BY task ASC".format(cours)):
        t.append(row)
    task = [''.join(i) for i in t]
    connection.close()
    return task

def alltasks(cours):
    connection = sqlite3.connect("inginious.sqlite")
    cursor = connection.cursor()
    allt = []
    t = tasks(cours)
    for j in range(len(t)):
        for row in cursor.execute(
                "SELECT task FROM user_tasks WHERE course = '{}' AND task = '{}'".format(cours, t[j])):
            allt.append(row)
    connection.close()
    return allt

