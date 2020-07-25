import psycopg2 as psql

db = None

try:
	db = psql.connect(
		user="bboi",
		password="passwd",
		host="db",
		port="5432",
		database="bboi"
		)

	print(f"DNS Info: - {db.get_dsn_parameters()}")

	cursor = db.cursor()

	cursor.execute("select version();")

	record = cursor.fetchone()

	print(f"You are connected to - {record}")

except (Exception, psql.Error) as err:
	print(err)
finally:
	if db:
		cursor.close()
		db.close()
		print("Closed connection to the DB.")