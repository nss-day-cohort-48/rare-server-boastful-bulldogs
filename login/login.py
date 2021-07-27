
import sqlite3
import json
from models import Login


def login_auth(email, password):
	with sqlite3.connect("./Rare.db") as conn:

		conn.row_factory = sqlite3.Row
		db_cursor = conn.cursor()

		db_cursor.execute("""
		SELECT
			u.id,
			u.email,
			u.password
		FROM Users u
		WHERE u.email = ?
		AND u.password = ?
		""", (email, password))

		data = db_cursor.fetchone()
		try:
			user = Login(data['email'], data['id'], True)
		except:
			print("email not found")
			user = Login("", "", False)

		return json.dumps(user.__dict__)
