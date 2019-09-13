from flask import Flask
from flask import render_template
from flask import request

import tinySearch


app = Flask(__name__)


@app.route('/',methods=["GET"])
def query():

	return render_template("query.html")



@app.route('/result',methods=["POST"])
def result():

	resultList = tinySearch.search(request.form['Search'])

	return render_template("result.html",resultList=resultList)


if __name__ == '__main__':

	app.run(debug=True)
