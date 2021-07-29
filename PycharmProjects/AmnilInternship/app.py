from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template,url_for


#Python sets the __name__ variable to the module name,
app= Flask(__name__)

#creating databse test.db
app.config['SQLALCHEMY_DATABASE_URI']='sql-lite:////test.db'

#Inilitising database
db=SQLAlchemy(app)

#Creating database table
class User(db.Model):
    ID=db.Column(db.Integer,primary_key=True)
    Name= db.Column(db.String(50), nullable=False)
    Address= db.Column(db.String(50), nullable=False)
    Phone =  db.Column(db.String(50), nullable=False)


# map the specific URL with the associated function
@app.route('/')

#importing index.html
def index():
    return render_template('index.html')

if __name__== "__main__":
    app.run(debug=True)