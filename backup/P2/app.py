from flask import Flask, render_template, url_for
from sqlfunc import course_tasks_graph
import html.parser as htmlparser
app = Flask(__name__)

parser = htmlparser.HTMLParser()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/cours.html')
def cours():
    return render_template('cours.html')

@app.route('/cours1.html')
def cours1():
    l = course_tasks_graph("LSINF1252")
    labels = l[1]
    cours = '{}'.format(l[0])
    val = l[2]
    print(cours)
    print(labels)
    print(val)
    return render_template('cours/cours1.html', label=labels, cours=cours, val=val)

@app.route('/cours2.html')
def cours2():
    return render_template('cours/cours2.html')

@app.route('/cours3.html')
def cours3():
    return render_template('cours/cours3.html')


if __name__ == '__main__':
    app.run(debug=True)
