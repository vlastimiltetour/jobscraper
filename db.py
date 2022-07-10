from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from flask import Flask
from sqlalchemy import create_engine
from indeed_scraper import *
import sqlite3


app = Flask(__name__)

db_name = 'jobs.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)
engine = create_engine(f'sqlite:///{db_name}', echo=False)

#this section is for scraping
#print(df.to_string())
#this is where scrapers end




#----
class Jobs(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   title = db.Column(db.String(100))
   company = db.Column(db.String(100))
   salary = db.Column(db.String(100))
   summary = db.Column(db.String(100))
   portal = db.Column(db.String(100))

def __init__(self, title, company, salary, summary, portal):
   self.title = title
   self.company = company
   self.salary = salary
   self.summary = summary
   self.portal = portal


conn = sqlite3.connect(db_name)
cursor = conn.cursor()
cursor.execute("DELETE FROM jobs")
conn.commit()
conn.close()

df = pd.DataFrame(joblist)
#print(df.head())
df.to_sql('jobs', con=engine, if_exists='append', index=False)

#print(df.to_string())
