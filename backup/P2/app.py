from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/cours.html')
def cours():
    return render_template('cours.html')

@app.route('/cours1.html')
def cours1():
    return render_template('cours/cours1.html')

@app.route('/cours2.html')
def cours2():
    return render_template('cours/cours2.html')

@app.route('/cours3.html')
def cours3():
    return render_template('cours/cours3.html')


if __name__ == '__main__':
    app.run(debug=True)
