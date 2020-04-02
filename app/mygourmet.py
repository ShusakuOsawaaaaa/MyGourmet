# render_templateはHTMLを表示させるための関数
from flask import Flask,render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def view_home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_evaluation():
    connect = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = '',
        password = '',
        database = 'MyGourmet',
        charset = 'utf8'
    )
    cursor = connect.cursor()
    cursor.execute('insert into my_evaluation (name, date, locate, price, genre, good, bad, evaluate) values (%s, %s, %s, %d, %s, %s, %s, %d), (name, date, locate, price, genre, good, bad, evaluate);')
    admin_users = cursor.fetchall()

    cursor.close()
    connect.close()
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)