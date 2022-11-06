from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/unko")
def hello():
    return "Hello Flask"


@app.route("/hiraizumi")
def hiraizumi():
    return "Hello ya--man"


@app.route("/user/<name>")
def heyName(name):
    return name


# http://127.0.0.1:5001/user/mina


@app.route("/user/<name>/<age>")
def heyAge(name, age):
    return name + age


# http://127.0.0.1:5001//user/age/32

# from flask import render_template
@app.route("/html")
def html():
    # return "<h1>Hello HTML</h1>"
    return render_template("index.html")


# 動的
@app.route("/html/<name>")
def htmlName(name):
    return render_template("name.html", name=name)


# http://127.0.0.1:5001/html/yae


@app.route("/html/age/<age>")
def htmlAge(age):
    return render_template("age.html", age=age)


# 動的の書き方part2!検索系に使われる
# from flask import request
@app.route("/query")
def quety():
    search_text = request.args.get("search_text")
    return search_text


# http://127.0.0.1:5001/query?search_text=yama


@app.route("/query")
def query():
    search_text = request.args("search_text")
    if search_text is not None:
        return search_text
    else:
        return ""


# http://127.0.0.1:5001/html


app.run(port=5001)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
