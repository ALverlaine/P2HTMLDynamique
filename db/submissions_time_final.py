import sqlite3

def subTimeOne(course):
    """
    :param course: str du cours dont on veut les statistiques
    :return: une liste des listes suivantes:
            - les labels (axe des abcsisses) : une echelle de temps precise au jour pres
            - les valeurs correspondantes (axe des ordonnees) : le nombre de soumission pour le jour donne
            le tout en veillant a bien respecter l echelle de temps
            si il n y a pas de valeur pour un temps donne la valeur par defaut est 0
    """
    connection = sqlite3.connect("inginious.sqlite")
    cursor = connection.cursor()
    #initialisation de nos 2 premieres variables
    val = []
    label = []
    #selection des dates de facon triee et du nombre de soumissions pour ces dates
    for row in cursor.execute(
            "SELECT date(substr(submitted_on,0,14) || ':00'), count(submitted_on) from submissions WHERE course='{0}' GROUP BY date(substr(submitted_on,0,14) || ':00') ORDER BY date(substr(submitted_on,0,14) || ':00')".format(
                course)):
        label.append(row[0])
        val.append(row[1])
    #selection de la fourchette de temps pour laquelle il y a des soumissions
    ti = label[0]
    tf = label[len(label)-1]
    #une grande str reprenant une grande echelle de temps continue (cad sans valeurs manquantes)
    w = weeks()
    index_debut = 0
    index_fin = 0
    for i, v in enumerate(w):
        if v == ti:
            index_debut = i
        elif v == tf:
            index_fin = i
    #on cree notre axe des abscisses final:
    #une ligne du temps sans jours manquants
    # sur toute la periode pour laquelle nous avons des soumissions pour le cours donne
    new_label = w[index_debut:index_fin]
    #on cree une liste des ordonnes de meme taille que l axe des abscisse final avec 0 comme valeur par defaut
    new_val = [0 for i in range(len(new_label))]
    #on parcourt les donnees recoltees de la db
    for i in range(len(new_label)):
        #si il y a eu des soumissions pour ce jours : new_label[i]
        if new_label[i] in label:
            #alors on cherche le bon indice pour faire correspondre les valeurs aux dates dans la nouvelle liste de valeurs
            for j in range(len(label)):
                if label[j] == new_label[i]:
                    new_val[i] = val[j]
    return [new_val, new_label]

def weeks():
    """
    pre:/
    :return:une str reprenant les dates a la precision du jour respectant l echelle temporelle
    """
    # création d'une str de 2019 à 2020
    l = []
    mois = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    s = "{:_>4}-{:_>2}-{:0>2}"
    for y in ["2019", "2020"]:
        if y == "2020":
            jours[1] = 29
        for i, mo in enumerate(mois):
            for d in range(1, jours[i] + 1):
                l.append(s.format(y, mo, str(d)))
    return l

