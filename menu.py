import sqlite3

def connect_db():
    try:
        conn = sqlite3.connect("zamestnanci.db")
        return conn
    except sqlite3.Error as e:
        print(f"❌ Chyba pri pripájaní k databáze: {e}")
        return None

def vytvor_tabulku():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS zamestnanci (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                meno TEXT NOT NULL,
                pozicia TEXT NOT NULL,
                oddelenie TEXT
            )
        """)
        conn.commit()
        conn.close()

def pridaj_zamestnanca():
    meno = input("Zadaj meno: ")
    pozicia = input("Zadaj pozíciu: ")
    oddelenie = input("Zadaj oddelenie: ")

    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO zamestnanci (meno, pozicia, oddelenie) VALUES (?, ?, ?)", (meno, pozicia, oddelenie))
        conn.commit()
        conn.close()
        print("✅ Zamestnanec bol pridaný.\n")

def zobraz_zamestnancov():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM zamestnanci")
        zamestnanci = cursor.fetchall()
        conn.close()

        print("\n📋 Zoznam zamestnancov:")
        for z in zamestnanci:
            print(f"ID: {z[0]} | Meno: {z[1]} | Pozícia: {z[2]} | Oddelenie: {z[3]}")
        print("")

def vyhladaj_zamestnanca():
    meno = input("Zadaj meno na vyhľadanie: ")

    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM zamestnanci WHERE meno LIKE ?", ('%' + meno + '%',))
        vysledky = cursor.fetchall()
        conn.close()

        if vysledky:
            print("\n🔍 Výsledky vyhľadávania:")
            for z in vysledky:
                print(f"ID: {z[0]} | Meno: {z[1]} | Pozícia: {z[2]} | Oddelenie: {z[3]}")
        else:
            print("⚠️ Nenašli sa žiadne výsledky.\n")

# Spustenie a menu
vytvor_tabulku()

while True:
    print("=== MENU ===")
    print("1 – Pridať zamestnanca")
    print("2 – Zobraziť všetkých zamestnancov")
    print("3 – Vyhľadať zamestnanca podľa mena")
    print("0 – Ukončiť")
    volba = input("Zvoľ možnosť: ")

    if volba == "1":
        pridaj_zamestnanca()
    elif volba == "2":
        zobraz_zamestnancov()
    elif volba == "3":
        vyhladaj_zamestnanca()
    elif volba == "0":
        print("👋 Končím program. Dovidenia.")
        break
    else:
        print("❌ Neplatná voľba, skús znova.\n")
