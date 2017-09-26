import psycopg2

from secret import dbname, dbuser, dbhost, dbpassword

def create_cube_if_channel_has_none(channel_id):
	"""Creates a cube in the database if there isn't one already."""
	conn, cur = connect_to_database()
	cur.execute("""SELECT *
				   FROM cubes
				   WHERE channel_id = '{:s}'""".format(channel_id))
	rows = cur.fetchall()
	if (len(rows) == 0):
		cur.execute("""INSERT INTO cubes (channel_id, progress)
					   VALUES ('{:s}', '')""".format(channel_id))
	commit_and_close_database(conn, cur)

def delete_cube(channel_id):
	"""Deletes a cube in the database."""
	conn, cur = connect_to_database()
	cur.execute("""DELETE FROM cubes
				   WHERE channel_id = '{:s}'""".format(channel_id))
	commit_and_close_database(conn, cur)

def append_movements_to_cube(channel_id, movements):
	"""Add movements to a cube in the database and return the summation."""
	create_cube_if_channel_has_none(channel_id)
	conn, cur = connect_to_database()
	if (movements != ''):
		cur.execute("""UPDATE cubes
					   SET progress = progress || ' ' || '{:s}'
					   WHERE channel_id = '{:s}'"""
					   .format(movements.replace("'", r"''"), channel_id))
	cur.execute("""SELECT progress
				   FROM cubes WHERE
				   channel_id = '{:s}'""".format(channel_id))
	rows = cur.fetchall()
	progress = rows[0][0].replace("''", r"'")
	commit_and_close_database(conn, cur)
	return progress

def connect_to_database():
	"""Connect to the cube database."""
	try:
		db_credentials = ("dbname='{:s}' "
						  "user='{:s}' "
						  "host='{:s}' "
						  "password='{:s}'"
						  .format(dbname, dbuser, dbhost, dbpassword))
		conn = psycopg2.connect(db_credentials)
		return conn, conn.cursor()
	except:
		print('I am unable to connect to the database')

def commit_and_close_database(conn, cur):
	"""Finalize changes and close the connection to the cube database."""
	conn.commit()
	cur.close()
	conn.close()
