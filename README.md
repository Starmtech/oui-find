# oui-find

Version: 
Python 2.7

Dépendance:
Sqlite3

Ubuntu / Debian:
sudo apt-get install sqlite3

Fedora / Centos:
yum install -y sqlite 

Paquet tar.gz:
wget http://www.sqlite.org/sqlite-autoconf-3070603.tar.gz
tar xvfz sqlite-autoconf-3070603.tar.gz
cd sqlite-autoconf-3070603
./configure
make
make install

Lancement du script:

Recherche du constructeur d'une adresse-mac:
python oui-find.py -m addressemac

Recherche des adresses mac correspondant a un constructeur:
python oui-find.py -c constructeur

Mise a jours de la base de donnée:
python oui-find.py -u

Plus d'information sur le script:
python oui-find.py -h

