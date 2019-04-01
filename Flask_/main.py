from flask import Flask, session, request, render_template, redirect, flash, g, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = "BAJS"

accounts = [("felix", "123")]

@app.route("/", methods=("GET", "POST")) 
def index():
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']

		for account in accounts:
			if account[0] == username:
				if account[1] == password:
					#Användaren HAR loggat in..
					session['logged'] = True
					return redirect(url_for('logged'))

				else:
					return "Lösenord incorrect"
		
		return "Inga konton hittades"

	session.clear()
	return render_template('index.html')

@app.route("/logged")
def logged():

	if session.get('logged'):
		return "Du är inloggad"
	else:
		return "Du är INTE inloggad"
if __name__ == "__main__":
	app.run()