# SQLite Terminal App – Employee Manager

A simple terminal-based employee management application using Python and SQLite.  
This project was created as part of a learning journey in programming and working with databases.

---

## 📂 Project Structure

- `databaza_sql.py` – Creates the SQLite database and the `zamestnanci` table if it doesn't exist
- `vloz_zamestnanca.py` – Inserts a predefined list of employees into the database
- `zobraz.py` – Displays all employees stored in the database
- `menu.py` – Interactive terminal menu for adding, viewing, and searching employees
- `.gitignore` – Prevents `zamestnanci.db` and cache files from being uploaded

---

## ▶️ How to Run

1. Make sure you have **Python 3** installed
2. Clone or download the repository
3. Open a terminal in the project folder
4. Run the interactive app:

```bash
python menu.py
