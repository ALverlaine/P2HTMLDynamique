import pandas as pd
import math

#Programme pour faciliter la récupération des données depuis le csv (lancer ce programme avec un csv à jour actualisera le html)

#dictionnaire contenant les pays et leurs données
cases = pd.read_csv("./total_cases.csv")
country = ["Belgium", "France", "Italy", "China", "United Kingdom", "United States"]
d = {}
for c in country:
    my_str = "["

    for i, x in enumerate(cases[c]):          
        if math.isnan(x):
            if i:
                my_str += ", "
            my_str += "0"
        else:
            if i:
                my_str += ", "
            my_str += str(x)
    my_str+="]"
    d["{}".format(c)] = my_str

#liste des dates
dates = "["
for x in cases["date"]:
    dates += '"' + str(x) + '",'
dates += "]"




my_code = """
<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8">
  <!-- Chargement de la librairie Javascript à utiliser -->
  
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.3/Chart.bundle.min.js"></script>
  
  <title>COVID-19 : contamination</title>
 </head>
 <body>
   
   <canvas id="graphique" width="100px" height="40px"></canvas>
   <script>
 // l'identifiant est celui du canevas
 var ctx = document.getElementById('graphique').getContext('2d');
 // création du graphique
 var myChart = new Chart(ctx, {
 type: 'line',   // le type du graphique
 data: {        // les données
  labels: """ + dates + """,
     datasets: [{
                 borderColor: "#315177",
                 backgroundColor: "rgba(168, 198, 216, 0.2)",
                 label: 'Contamination totale en Belgique',
                 data:""" + d["Belgium"] +"""
                },
                {
                  borderColor: "#cc0000",
                  backgroundColor: "rgba(255, 102, 102, 0.2)",
                  label: 'Contamination totale en France',
                  data: """ + d["France"] + """
                },
                {
                  borderColor: "#006600",
                  backgroundColor: "rgba(0, 204, 0, 0.2)",
                  label: 'Contamination totale en Italie',
                  data: """ + d["Italy"] + """
                },
                {
                  borderColor: "#400080",
                  backgroundColor: "rgba(191, 128, 255, 0.2)",
                  label: 'Contamination totale en Chine',
                  data: """ + d["China"] + """
                },
                {
                  borderColor: "#990066",
                  backgroundColor: "rgba(255, 128, 213, 0.2)",
                  label: 'Contamination totale au Royaume-Uni',
                  data: """ + d["United Kingdom"] + """
                },
                {
                  borderColor: "#b34700",
                  backgroundColor: "rgba(255, 133, 51, 0.2)",
                  label: 'Contamination totale aux Etats-Unis',
                  data: """ + d["United States"] + """
                }]
        }
      }
 );
   </script>

 </body>
</html>
"""

html_file= open("index.html","w")
html_file.write(my_code)
html_file.close()