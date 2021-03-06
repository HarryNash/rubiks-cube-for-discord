import psycopg2
from autologging import traced
import logging


@traced(logging.getLogger("harry"))
def create_cube_if_channel_has_none(channel_id, database_connection):
    """Creates a cube in the database if there isn't one already."""
    conn, cur = connect_to_database(database_connection)
    cur.execute("SELECT * FROM cubes WHERE channel_id = %s", [channel_id])
    rows = cur.fetchall()
    if len(rows) == 0:
        cur.execute(
            "INSERT INTO cubes (channel_id, progress) VALUES (%s, '')", [channel_id],
        )
    commit_and_close_database(conn, cur)


@traced(logging.getLogger("harry"))
def delete_cube(channel_id, database_connection):
    """Deletes a cube in the database."""
    conn, cur = connect_to_database(database_connection)
    cur.execute("DELETE FROM cubes WHERE channel_id = %s", [channel_id])
    commit_and_close_database(conn, cur)


@traced(logging.getLogger("harry"))
def append_movements_to_cube(channel_id, movements, database_connection):
    """Add movements to a cube in the database and return the summation."""
    create_cube_if_channel_has_none(channel_id, database_connection)
    conn, cur = connect_to_database(database_connection)
    if movements != "":
        cur.execute(
            "UPDATE cubes SET progress = progress || ' ' || %s WHERE channel_id = %s",
            [movements.replace("'", r"''"), channel_id],
        )
    cur.execute("SELECT progress FROM cubes WHERE channel_id = %s", [channel_id])
    rows = cur.fetchall()
    progress = rows[0][0].replace("''", r"'")
    commit_and_close_database(conn, cur)
    return progress


@traced(logging.getLogger("harry"))
def connect_to_database(database_connection):
    """Connect to the cube database."""
    conn = psycopg2.connect(database_connection)
    return conn, conn.cursor()


@traced(logging.getLogger("harry"))
def commit_and_close_database(conn, cur):
    """Finalize changes and close the connection to the cube database."""
    conn.commit()
    cur.close()
    conn.close()
