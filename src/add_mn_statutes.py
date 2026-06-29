import sqlite3

db_path = "database/data/mn_criminal_defense.db"

mn_statutes = [
    ("609.11", "609", "11", "Venue", "felony"),
    ("609.02", "609", "02", "Principals", "felony"),
    ("609.035", "609", "035", "Accomplices", "felony"),
    ("609.05", "609", "05", "Attempts", "felony"),
    ("609.175", "609", "175", "Conspiracy", "felony"),
    ("609.495", "609", "495", "Theft", "felony"),
    ("609.52", "609", "52", "Drug Possession", "felony"),
    ("609.221", "609", "221", "Assault", "felony"),
    ("609.342", "609", "342", "Criminal Sexual Conduct", "felony"),
    ("609.582", "609", "582", "Burglary", "felony"),
]

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

for code, chapter, section, title, statute_type in mn_statutes:
    try:
        cursor.execute('''
            INSERT OR IGNORE INTO statutes 
            (statute_code, chapter, section, title, full_text, statute_type)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (code, chapter, section, title, title, statute_type))
    except Exception as e:
        print(f"Error adding {code}: {e}")

conn.commit()

cursor.execute("SELECT COUNT(*) FROM statutes")
count = cursor.fetchone()[0]
print(f"✅ Total statutes in database: {count}")

conn.close()
