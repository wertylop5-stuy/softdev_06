from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def root():
	if request.method == "GET":
		if request.args:
			return render_template("index.html", 
				username=request.args["username"],
				requestType=request.method)
	elif request.method == "POST":
		if request.form:
			return render_template("index.html", 
				username=request.form["username"],
				requestType=request.method)
	
	return render_template("index.html")

if __name__ == "__main__":
	app.debug = True
	app.run()
