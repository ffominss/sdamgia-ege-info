import sqlite3
cur = sqlite3.connect("db.db").cursor()

def outb():
    out = cur.execute("select * from results").fetchall()
    return out

def addb(month,variant, number, result, variant_id, id):
    str = f'INSERT INTO results VALUES ("{month}", "{variant}", "{number}", "{result}", "{variant_id}", "{id}")'
    cur.execute(str)

def remb(id):
    str = f'DELETE FROM results WHERE id = "{id}";'
    cur.execute(str)


#addb("TEST", "TEST", "TEST", "TEST", "TEST")

print(outb())


