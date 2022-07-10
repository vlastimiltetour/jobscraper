from flask import Flask, render_template, url_for
import sqlite3
from db import *

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT*FROM 'jobs'")
    jobs = cursor.fetchall()
    conn.close()
    return render_template('basic_table.html', title='Scraper King',jobs=jobs)


# this route will test the database connection and nothing more
'''
@app.route('/')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
'''

if __name__ == '__main__':
    app.run(debug=True)

