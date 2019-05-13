"""
Pour lancer le serveur localement

Au sein du dossier de l'application de serveur de rapports
	cd /emplacement_du_projet/report_server

..pour lancer avec `werkzeug.serving import run_simple`
	python run_locally.py
"""

import sys
sys.path.insert(0, '..')

from report_server.app import dispatcher
  # To use the Werkzeug development server
from werkzeug.serving import run_simple

if __name__ == "__main__":
  # To use the Werkzeug development server
  run_simple('localhost', 8050, dispatcher)
