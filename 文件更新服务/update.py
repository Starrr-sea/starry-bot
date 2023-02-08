import flask

app = flask.Flask(__name__)


@app.route("/update",methods=["POST","GET"])
def updat1e():
    return "OK"


app.run(debug=True,host="0.0.0.0",port=8888)