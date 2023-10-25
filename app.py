import os
import webbrowser

from threading import Timer
from flask import Flask, send_from_directory
from dotenv import load_dotenv
from jinja2 import Environment, PackageLoader

from data import menuItems
from ssg_utils import generateFile


load_dotenv()

app = Flask(__name__)

ENV = Environment(loader=PackageLoader('app'))

# NOTE: You (currently) have to view a page to render the flat file for it.
# Everything below is only used for generating the HTML files and viewing on dev. 
# Prod is served as flat files from /build/.

@app.route('/')
def home():
	fileName = 'index.html'
	generateFile(ENV, fileName, menuItems)
	return send_from_directory('build', fileName)
	
	
# Only used for dev. Prod is served as flat files from /build/.
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	
	def open_browser():
		if not os.environ.get("WERKZEUG_RUN_MAIN"):
			webbrowser.open_new(f'http://127.0.0.1:{ port }')
		
	Timer(.5, open_browser).start()
	app.run(host='0.0.0.0', port=port, debug=True)