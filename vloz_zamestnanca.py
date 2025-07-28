import sqlite3

conn = sqlite3.connect("zamestnanci.db")
cursor = conn.cursor()

zamestnanci = [
    ("Ján Novák", "Programátor", "IT"),
    ("Eva Horváthová", "HR manažérka", "HR"),
    ("Martin Šimek", "Analytik", "IT"),
    ("Petra Kováčová", "Účtovníčka", "Financie")
]

cursor.executemany("INSERT INTO zamestnanci (meno, pozicia, oddelenie) VALUES (?, ?, ?)", zamestnanci)

print("✅ Zamestnanci boli vložení.")
conn.commit()
conn.close()
