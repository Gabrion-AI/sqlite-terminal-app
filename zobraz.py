import sqlite3

conn = sqlite3.connect("zamestnanci.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM zamestnanci")
vysledky = cursor.fetchall()

print(f"🔢 Záznamov v databáze: {len(vysledky)}\n")

for z in vysledky:
    print(f"ID: {z[0]} | Meno: {z[1]} | Pozícia: {z[2]} | Oddelenie: {z[3]}")

conn.close()
