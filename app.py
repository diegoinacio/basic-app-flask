import sqlite3
from flask import Flask, render_template, g


app = Flask(__name__)


MENU = [
    {'title': 'Home page', 'page': 'home'},
    {'title': 'About', 'page': 'about'},
    {'title': 'Contact', 'page': 'contact'}
]


@app.route('/')
@app.route('/home.html')
def home():
    TITLE, PAGE = MENU[0]['title'], MENU[0]['page']
    return render_template(f'{PAGE}.html', TITLE=TITLE, MENU=MENU)

@app.route('/about.html')
def about():
    TITLE, PAGE = MENU[1]['title'], MENU[1]['page']
    ############
    # Database #
    ############
    db_connect = sqlite3.connect('database/people.db')
    cursor = db_connect.cursor()
    query = cursor.execute('SELECT * FROM person;')
    rows = query.fetchall()
    PEOPLE = [{e[0]: row[i] for i, e in enumerate(cursor.description)} for row in rows]
    return render_template(f'{PAGE}.html', TITLE=TITLE, MENU=MENU, PEOPLE=PEOPLE)

@app.route('/contact.html')
def contact():
    TITLE, PAGE = MENU[2]['title'], MENU[2]['page']
    return render_template(f'{PAGE}.html', TITLE=TITLE, MENU=MENU)


if __name__ == '__main__':
    app.run(debug=True)