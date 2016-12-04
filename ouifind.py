#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################
#           OuiFInd               #
#      langage : Python 2.7       # 
#         date : 25/11/16         #
#          version : 1.1          #
#        auteur : devkort         #
###################################

import sqlite3
import os
import sys
import urllib

def search(l, value):
   try:
       conn = sqlite3.connect('/usr/share/ouifind/src/oui.db')
       cursor = conn.cursor()
       if value == '-m':
          t = l.replace(':','')
          m = t[0:5]
          cursor.execute(" SELECT * FROM oui WHERE mac like ?", ('%' + m + '%', )) 

       elif value == '-c':
          cursor.execute(" SELECT * FROM oui WHERE constructeur like ?", ('%' + l + '%', )) 
       print coloriage(" MAC   :  Constructeur", 'blue', True)
       for row in cursor:
          print coloriage('{1} : {2}'.format(row[0], row[1], row[2]), 'green', False)

       conn.commit()
   except Exception as e:
       conn.rollback()
   finally:
       conn.close()

def coloriage(s, color, bold=False):
   colors = {'red': 31, 'green': 32, 'yellow': 33,
             'blue': 34, 'magenta' : 36}
   if os.getenv('ANSI_COLORS_DISABLED') is None and color in colors:
       if bold:
           return '\033[1m\033[%dm%s\033[0m' % (colors[color], s)
       else:
           return '\033[%dm%s\033[0m' % (colors[color], s)
   else:
       return s

def help():
   print("\n")
   print coloriage("                    Aide pour l'utilisation de la commande OuiFind:", "blue", True)
   print("\n")
   print coloriage(" ouifind.py -m    permet de chercher le constructeur a qui appartient l'adresse mac", "green", False)
   print coloriage(" ouifind.py -c   permet d'afficher les adresses mac correspondant on constructeur", "green", False)
   print coloriage(" ouifind.py -h     permet de connaitre les commandes du script et obtenir de l'aide", "green", False)
   print coloriage(" ouifind.py -u     mise a jours de la base de donnée", "green", False)
   print("\n")

def update():
   try:   
      print coloriage("Mise a jours de la base de donnée", "green", False)
      urllib.urlretrieve('http://88.164.14.125/oui.db', '/usr/share/ouifind/src/oui.db')
      print coloriage("Base de donnée mise a jours.", "green", False)
   except:
      print coloriage("Mise a jours Impossible", "red", False)  
      pass

def argu():
   if len(sys.argv) >= 1:
      if sys.argv[1] == "-m":
         if len(sys.argv) == 3:
            vendors = sys.argv[2]
            arg = sys.argv[1]
            search(vendors,arg)
         else:
            vendors = raw_input("Entrez une adresse mac : ")
            arg = sys.argv[1]
            search(vendors, arg)

      elif sys.argv[1] == "-c":
         if len(sys.argv) == 3:
            vendors = sys.argv[2]
            arg = sys.argv[1]
            search(vendors,arg)
         else:
            vendors = raw_input("Entrez un constructeur : ")
            arg = sys.argv[1]
            search(vendors, arg)

      elif sys.argv[1] == "-h":
         help()

      elif sys.argv[1] == "-u":
         update()
      else:
         print("Mauvaise commande taper --help pour plus d'information")


if __name__ == '__main__':
   argu()
