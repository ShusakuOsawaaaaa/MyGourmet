# importしているものについて
# Flask：PythonのWebアプリ向けフレームワーク
# render_template：HTMLを表示させるために使われる関数
# url_for：指定されたendpoint(関数)へのURLを生成する関数
# redirect：引数のURLにリダイレクトさせる関数。url_forとセットでルーティングに使われる
# request：GETやPOSTで受け取るパラメータを扱うことができるようになる
from flask import Flask, render_template, url_for, redirect, request
import pymysql.cursors

app = Flask(__name__)

# HOME画面の関数
@app.route("/")
def view_home():
    # テンプレートに渡す引数の配列を定義
    props = {'title': '私のグルメ帳'}
    # viewとして返すhtmlと引数の情報を渡す
    return render_template("index.html", props=props)

@app.route("/add", methods=["POST"])
def add_evaluation():
    connect = pymysql.connect(
        host = 'localhost',
        port = 3306,
        user = '',
        password = '',
        database = 'mygourmet',
        charset = 'utf8'
    )
    name = request.form["name"]
    date = request.form["date"]
    locate = request.form["locate"]
    price = request.form["price"]
    genre = request.form["genre"]
    good = request.form["good"]
    bad = request.form["bad"]
    evaluate = request.form["evaluate"]

    print(name)
    print(date)
    print(locate)
    print(price)
    print(genre)
    print(good)
    print(bad)
    print(evaluate)

    cursor = connect.cursor()
    # プレースホルダは数値型も文字列型も全部%sでいいらしい。自動で適切な形に展開してくれるとのこと。
    sql = """
        insert into my_evaluation (name, date, locate, price, genre, good, bad, evaluate)
        values (%s, %s, %s, %s, %s, %s, %s, %s);
        """
    cursor.execute(sql ,(name, date, locate, price, genre, good, bad, evaluate))
    admin_users = cursor.fetchall()

    # これがないとInsert文の結果がDBに反映されない、詳細調査する
    connect.commit()

    cursor.close()
    connect.close()
    return redirect(url_for("view_home"))

@app.route("/add")
def add():
    return render_template("add.html")

# 存在しないURLへのアクセスがきたらview_home関数を呼び出し、HOME画面にリダイレクトする
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for("view_home"))

if __name__ == "__main__":
    app.run(debug=True)