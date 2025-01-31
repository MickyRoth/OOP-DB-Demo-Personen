import sqlite3

# Definiere eine Klasse für die Objekte
class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self): # Spezial-Methode zum printen des Objektes
        return f"{self.id:2}    {self.name:8} {self.age:2}"

# Verbindung zur SQLite-Datenbank herstellen (Datei-basiert)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()  # SQL-Datenbankcursor-Objekt erzeugen

# Tabelle erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL )
""")

# Mehrere Datensätze einfügen mit cursor.executemany(liste)

cursor.execute("INSERT INTO persons (name, age) VALUES ('Otto',22)")
               
cursor.executemany("INSERT INTO persons (name, age) VALUES (?, ?)",
   [("Alice", 30), ("Bob", 25), ("Charlie", 35)] )

conn.commit()  # Änderungen speichern (Transaktionsbestätigung)

# Datensätze per SQL abrufen
cursor.execute("SELECT * FROM persons")
daten = cursor.fetchall() # Ergebnis der Abfrage in Variable daten kopieren

conn.close() # Nicht vergessen die DB-Verbindung zu schließen

# Datensätz in Objekte einlesen
persons = []      # Leere Liste für die Objekte
for row in daten: # Mit for durch das Ergebnis der Abfrage
    id = row[0]   # Erstes Datenfeld
    name = row[1] # Zweites Datenfeld
    age = row[2]  # Drittes Datenfeld
    persons.append(Person(id,name,age))  # Person-Objekt erzeugen und an Liste anhängen

# Objekte ausgeben
for row in persons:
    print(row)  # Dank der Methode __repr__() klappt das Objekt-printen

