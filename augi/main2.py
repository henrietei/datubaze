import sqlite3 as sq

con = sq.connect("augi/augi.db")
cur = con.cursor()
cur = cur.execute(""" CREATE TABLE staditDobes(
    augs TEXT,
    dienas INTEGER, 
    dobesNr TEXT,
    kg REAL
)
""")

print("bāzē augi.db izveidota tabula staditDobes")