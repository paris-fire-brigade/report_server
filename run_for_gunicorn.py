"""
Pour lancer le serveur de rapport via gunicorn

Sous Linux au sein du dossier de l'application de serveur de rapports
	cd /emplacement_du_projet/report_server

..lancer gunicorn via la commande
	sudo /emplacement_d_anaconda/Anaconda3/bin/gunicorn -c /emplacement_du_projet/report_server/gunicorn.conf -b 127.0.0.1:5000 -w 4 run:dispatcher
"""

import sys
sys.path.insert(0, '..')

from report_server.app import dispatcher

if __name__ == "__main__":
  dispatcher.run()
