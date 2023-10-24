import os

import shutil
from distutils.dir_util import copy_tree

import webbrowser
from threading import Timer
from flask import Flask, send_from_directory
from dotenv import load_dotenv
from jinja2 import Environment, PackageLoader

from data import menuItems
 
load_dotenv()

app = Flask(__name__)


def generateFiles():
	# Blow away build dir and create new clean build.
	shutil.rmtree('./build')
	os.makedirs('./build/static')
	copy_tree('./static', './build/static')
	
	# Render index page template and save as file in build dir.
	env = Environment(loader=PackageLoader('app'))
	template = env.get_template('index.html')
 	
	root = os.path.dirname(os.path.abspath(__file__))
	filename = os.path.join(root, 'build', 'index.html')
 	
	with open(filename, 'w') as fh:
		fh.write(template.render(data=menuItems))
 	
 	
@app.route('/')
def home():
	generateFiles()
	
	return send_from_directory('build', 'index.html')
	

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	
	def open_browser():
		if not os.environ.get("WERKZEUG_RUN_MAIN"):
			webbrowser.open_new(f'http://127.0.0.1:{ port }')
		
	Timer(.5, open_browser).start()
	app.run(host='0.0.0.0', port=port, debug=True)