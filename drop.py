import sqlite3

def drop_table():
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    cur.execute('DROP TABLE app_d_club')
    conn.commit()
    conn.close()
drop_table()

# on oublie pas de delete la migrations

# def rename_colonne():
#     conn = sqlite3.connect('db.sqlite3')
#     cur = conn.cursor()
#     cur.execute('ALTER TABLE Produit RENAME nom TO designation')
#     conn.commit()
#     conn.close()
# rename_colonne()