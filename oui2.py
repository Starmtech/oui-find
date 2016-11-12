#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import urllib2
import re
import sqlite3

def get_mac_table_file(filename="oui.txt"):
	request = urllib2.urlopen("http://standards-oui.ieee.org/oui/oui.txt")
	print "Fichier oui.txt telechargé"
	with open(filename, "w") as f:
		for line in request:
			f.write(line)
			print "*",
def parse_mac_table_file(filename="oui.txt"):
	ven_arr = []
	with open(filename, "rw") as f:
		for line in f:
			if "(base 16)" not in line:
				continue
			ven = tuple(re.sub("\s*([0-9a-zA-Z]+)[\s\t]*\(base 16\)[\s\t]*(.*)\n", r"\1;;\2", line).split(";;"))
			ven_arr.append(ven)
	return ven_arr

def list_to_database(ven_arr, filename="oui.db"):
	try:
		os.unlink(filename)
	except OSError:
		pass
	db = sqlite3.connect(filename)
	cur = db.cursor()
	create_q = "CREATE TABLE oui(id INTEGER PRIMARY KEY, mac TEXT, constructeur TEXT);"
	cur.execute(create_q)
	query_pr = "INSERT INTO oui (`mac`,`constructeur`) VALUES "
	query = ""
	for ind, ven in enumerate(ven_arr):
		query = query_pr + '("%s", "%s")\n'% (ven[0], ven[1].replace("\"", "\"\""))
		try:
			cur.execute(query)
		except Exception as e:
			print "Error: %s" % e
			db.close()
			sys.exit()
	db.commit()
	db.close()

def play():
	print "Téléchargement du fichier oui.txt"
	get_mac_table_file()
	print "Parse du fichier oui.txt et insertion dans macvendors.db"
	list_to_database(parse_mac_table_file())
	print "Fin"
        os.remove("oui.txt")
        print "Fichié supprimé"
