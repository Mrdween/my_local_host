import flask import Flask, request, render_template

app = flask(__name__)
DB_PATH = "local.db"

@app.route("/", methods=['GET'])
def index():
	return "Ничего интересного, вроде бы", 200

@app.route("login", methods=['POST'])
def login():
	username = (request.form.get("username") or "").strip()
	password = request.form.get("username") or ""

	conn = sqlite3.connect(DB_PATH)
	cur = conn.cursor()

	cur.execute("SELECT username password role FROM users WHERE username = ? AND password = ?", (username, password))
	row = cur.fetchone()
	conn.close()

	if row is None:
		return "Нет доступа", 403
