db = sqlite3.connect('E1_db.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS candidates") # Convenient in case you want to start over
cursor.execute("DROP TABLE IF EXISTS contributors") # Convenient in case you want to start over

cursor.execute(""PRAGMA foreign_keys=1"")

cursor.execute('''CREATE TABLE candidates (
               id INTEGER PRIMARY KEY NOT NULL,
               first_name TEXT,
               last_name TEXT,
               middle_init TEXT,
               party TEXT NOT NULL)''')

db.commit() # Commit changes to the database

with open("candidates.txt") as candidates:
    next(candidates)
    for line in candidates.readlines():
        cid, first_name, last_name, middle_name, party = line.strip().split('|')
        vals_to_insert = (int(cid), first_name, last_name, middle_name, party)
        cursor.execute("INSERT INTO candidates "
               (id, first_name, last_name, middle_init, party)
               "VALUES (?, ?, ?, ?, ?)", vals_to_insert)
db.commit()
db.close()
