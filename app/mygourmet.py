# render_templateはHTMLを表示させるための関数
from flask import Flask,render_template
import pymysql

app = Flask(__name__)

@app.route("/")
def hello():
    return "ぼくちゃん専用グルメ帳"

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)