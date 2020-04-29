from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Pays(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(200))
    total_cases = db.Column(db.ARRAY(str))


    def __repr__(self):
        return '<Pays %r>' % self.id


def reform(string):
    str = string[0:4]
    str1 = string[5:7]
    str2 = string[8:10]
    str3 =(str2 + '-' + str1 + '-' + str)

    return str3



@app.route('/', methods=['GET', 'POST'])
def index():
    with open('total_cases.csv', 'r')as file:
        reader = csv.reader(file)
        all = []
        for row in reader:
            all.append(row)
        print(all)
        labels = []
        for i in range(len(all)):
            if (i != 0):
                nstr = reform(all[i][0])
                labels.append(nstr)
        print(labels)
        ntable = []
        for i in range(len(all[0])):
            ndata = []
            for j in range(len(all)):
                if (i != 0):
                    if (j != 0):
                        ndata.append(all[j][i])
            if i != 0:
                ntable.append(ndata)
        print(ntable)
    return render_template('index.html', Cas=ntable, date=labels, Pays=all)


@app.route('/<country>/<total_cases>')
def ini(country, total_cases):
    Case = Pays(country=country, total_cases=total_cases)
    db.session.add(Case)
    db.session.commit()
    return '<h1>Well added</h1>'

if __name__ == '__main__':
    app.run()
