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

    return """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.bundle.min.js"></script>
        <title>Covid 19:visualisation des données</title>
    </head>
    <body>
        <canvas id="graphique" width="200" height="100"></canvas>
        <script>
            var ctx = document.getElementById('graphique').getContext('2d');
            var myChart = new Chart(ctx,{
                type:'bar',
                data:{
                labels: {0},
                datasets: [{
                            label: 'soumission du cours {1}',
                            data:}]
                    }
                }
            );
        </script>


    </body>
</html>""".format[label,cours,  val]
print(db_to_graph("LSINF1101-PYTHON"))
