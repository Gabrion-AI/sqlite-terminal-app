import sqlite3

conn = sqlite3.connect("zamestnanci.db")
cursor = conn.cursor()

# Zmažeme existujúcu tabuľku (iba pri vývoji)
cursor.execute("DROP TABLE IF EXISTS zamestnanci")

cursor.execute("""
CREATE TABLE zamestnanci (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meno TEXT NOT NULL,
    pozicia TEXT NOT NULL,
    oddelenie TEXT
)
""")

print("✅ Tabuľka 'zamestnanci' bola vytvorená nanovo.")
conn.commit()
conn.close()
