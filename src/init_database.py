import sqlite3
from pathlib import Path

schema_path = Path("database/schema/mn_criminal_schema.sql")
db_path = Path("database/data/mn_criminal_defense.db")

db_path.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(str(db_path))
cursor = conn.cursor()

with open(schema_path, 'r') as f:
    schema = f.read()
    cursor.executescript(schema)

conn.commit()
print("Database created successfully!")
print(f"Location: {db_path}")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(f"Created {len(tables)} tables:")
for table in tables:
    print(f"  - {table[0]}")

conn.close()
