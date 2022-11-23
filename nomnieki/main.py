import sqlite3 as db

#con = db.connect('noma.db')
#con.close




with db.connect("noma.db") as con:
    cur = con.cursor
    cur = con.execute("""
    CREATE TABLE IF NOT EXISTS noma (
	id_produkts	INTEGER,
	id_nomnieks	INTEGER,
	sak_datums	TEXT,
	beig_datums	TEXT,
	PRIMARY KEY(id_produkts,id_nomnieks)
) """)

with db.connect("nomnieks.db") as con:
    cur = con.cursor
    cur = con.execute("""
    CREATE TABLE IF NOT EXISTS nomnieks (
	id_nomnieks	INTEGER,
	vards	TEXT,
	uzvards	TEXT,
	p_k	INTEGER,
	tel_nr	INTEGER,
	PRIMARY KEY(id_nomnieks)
) """)

with db.connect("kategorija.db") as con:
    cur = con.cursor
    cur = con.execute("""
    CREATE TABLE IF NOT EXISTS kategorija (
	id_kategorija	INTEGER,
	kategorija	TEXT,
	PRIMARY KEY(id_kategorija)
) """)

with db.connect("nosaukums.db") as con:
    cur = con.cursor
    cur = con.execute("""
    CREATE TABLE IF NOT EXISTS nosaukums (
	id_nosaukums	INTEGER,
	nosaukums	TEXT,
	PRIMARY KEY(id_nosaukums)
) """)

with db.connect("produkts.db") as con:
    cur = con.cursor
    cur = con.execute("""
    CREATE TABLE IF NOT EXISTS produkts (
	id_produkts	INTEGER,
	id_kategorija	TEXT,
	id_nosaukums	TEXT,
    id_tehn_raksturojumi	TEXT,
	nomas_cena_diena	REAL,
	PRIMARY KEY(id_produkts)
) """)

with db.connect("noma.db") as con:
    cur = con.cursor
    cur = con.execute("""
    CREATE TABLE IF NOT EXISTS tehn_raksturojums (
	id_tehn_rakst	INTEGER,
	tehn_rakst	TEXT,
	PRIMARY KEY(id_tehn_rakst)
) """)