from flask import Flask, render_template, url_for
from sqlfunc import course_tasks_graph, task_result_graph, subm_time_graph, tasks
import html.parser as htmlparser
app = Flask(__name__)

parser = htmlparser.HTMLParser()

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/cours.html')
def cours():
    return render_template('cours.html')


#COURS 1 _______________________________________________________________


@app.route('/cours1_G1.html')
def cours1_G1():
    l = course_tasks_graph("LSINF1252")
    g = tasks("LSINF1252")
    return render_template('cours/cours1/cours1_G2.html', label=l[2], cours=l[1], val=l[3], type=l[0], bordercolor=l[4], background=l[5], tasks=g)


@app.route('/cours1_G2.html')
def cours1_G2():
    l = task_result_graph("LSINF1252")
    g = tasks("LSINF1252")
    return render_template('cours/cours1/cours1_G1.html', label=l[2], cours=l[0], val=l[3], type=l[1], bordercolor=l[4], background=l[5], tasks=g)


@app.route('/cours1_G3.html')
def cours1_G3():
    l = subm_time_graph("LSINF1252", "2020-01-15T00:00", "2020-3-22T00:00")
    return render_template('cours/cours1/cours1_G2.html', label=l[2], cours=l[1], val=l[3], type=l[0], bordercolor=l[4],
                           background=l[5])

#______________________________________________________________________

#COURS 2_______________________________________________________________


@app.route('/cours2_G1.html')
def cours2_G1():
    l = course_tasks_graph("LEPL1402")
    return render_template('cours/cours1/cours1_G2.html', label=l[2], cours=l[1], val=l[3], type=l[0], bordercolor=l[4],
                           background=l[5])


@app.route('/cours2_G2.html')
def cours2_G2():
    l = task_result_graph("LEPL1402")
    g = tasks("LEPL1402")
    return render_template('cours/cours1/cours1_G1.html', label=l[2], cours=l[0], val=l[3], type=l[1], bordercolor=l[4],
                           background=l[5], tasks=g)


@app.route('/cours2_G3.html')
def cours2_G3():
    l = subm_time_graph("LEPL1402", "2020-02-15T00:00", "2020-02-22T00:00")
    return render_template('cours/cours1/cours1_G2.html', label=l[2], cours=l[1], val=l[3], type=l[0], bordercolor=l[4],
                           background=l[5])


#______________________________________________________________________

#COURS 3 ______________________________________________________________
@app.route('/cours3_G1.html')
def cours3_G1():
    l = course_tasks_graph("LSINF1101-PYTHON")
    return render_template('cours/cours1/cours1_G2.html', label=l[2], cours=l[1], val=l[3], type=l[0], bordercolor=l[4],
                           background=l[5])


@app.route('/cours3_G2.html')
def cours3_G2():
    l = task_result_graph("LSINF1101-PYTHON")
    g = tasks("LSINF1101-PYTHON")
    return render_template('cours/cours1/cours1_G1.html', label=l[2], cours=l[0], val=l[3], type=l[1], bordercolor=l[4],
                           background=l[5], tasks=g)


@app.route('/cours3_G3.html')
def cours3_G3():
    l = subm_time_graph("LSINF1101-PYTHON", "2020-02-15T00:00", "2020-02-22T00:00")
    return render_template('cours/cours1/cours1_G2.html', label=l[2], cours=l[1], val=l[3], type=l[0], bordercolor=l[4],
                           background=l[5])


#______________________________________________________________________


if __name__ == '__main__':
    app.run(debug=True)
