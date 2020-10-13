import sqlite3

conn = sqlite3.connect('InstagramBot.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE pessoasMarcaveis (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
""")
cursor.execute("""
CREATE TABLE pessoasExcluidas (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
""")
print("bd criado!")
conn.close()
