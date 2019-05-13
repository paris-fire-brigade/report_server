"""
Application Flask et portail web serveur de rapport
"""


from flask import Flask, render_template
from werkzeug.wsgi import DispatcherMiddleware

import os, sys
# add to sys.path relative to the current running script
sys.path.append(os.path.join(os.path.dirname(__file__), ""))
# add the parent-parent directory
sys.path.append('../..')

from views import general
from common.common import common
from reports.demo.F01_hello_world.app import app as F01_hello_world
from reports.demo.F02_simple_app.app import app as F02_simple_app
from reports.demo.F03_complex_app.app import app as F03_complex_app
from reports.demo.D01_simple_app.app import app as D01_simple_app
from reports.demo.D02_simple_graphique.app import app as D02_simple_graphique
#from reports.demo.D03_dashboard_sklearn.app import app as D03_dashboard_sklearn

app = Flask(__name__, template_folder='templates')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from report_server.app.views import general 
app.register_blueprint(general.mod)

dispatcher = DispatcherMiddleware(app, {
    '/common': common,   
    '/demo/F01_hello_world': F01_hello_world,  
    '/demo/F02_simple_app': F02_simple_app,  
  	'/demo/F03_complex_app': F03_complex_app,  
    '/demo/D01_simple_app': D01_simple_app.server,  
    '/demo/D02_simple_graphique': D02_simple_graphique.server,   
    #'/demo/D03_dashboard_sklearn': D03_dashboard_sklearn.server,  
})

