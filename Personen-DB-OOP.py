import sqlite3

# Definiere eine Klasse für die Objekte
class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self): # Spezial-Methode zum printen des Objektes
        return f"Person(ID={self.id}, Name='{self.name}', Alter={self.age})"

# Verbindung zur SQLite-Datenbank herstellen (Datei-basiert)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Tabelle erstellen
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL )
""")

# Mehrere Datensätze einfügen mit cursor.executemany(liste)
cursor.executemany("INSERT INTO persons (name, age) VALUES (?, ?)",
   [("Alice", 30), ("Bob", 25), ("Charlie", 35)] )

conn.commit()  # Änderungen speichern

# Datensätze per SQL abrufen
cursor.execute("SELECT * FROM persons")
daten = cursor.fetchall() # Ergebnis der Abfrage in Variable daten kopieren

conn.close() # Nicht vergessen die DB-Verbindung zu schließen

# Datensätz in Objekte einlesen
persons = []
for row in daten:
    id = row[0]   # Erstes Datenfeld
    name = row[1] # Zweites Datenfeld
    age = row[2]  # Drittes Datenfeld
    persons.append(Person(id,name,age))  # Person-Objekt erzeugen

# Objekte ausgeben
for person in persons:
    print(person)  # Dank der Methode __repr__() klappt das Objekt-printen

