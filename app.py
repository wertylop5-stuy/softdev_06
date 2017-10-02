from flask import Flask, render_template
import flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def root():
	#for get requests
	#print flask.request.args.get("foo")
	
	#for post requests
	print flask.request.form.get("foo")
	return render_template("index.html")

if __name__ == "__main__":
	app.debug = True
	app.run()
