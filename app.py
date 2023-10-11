import os
import webbrowser
from threading import Timer
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')
	

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	
	def open_browser():
		if not os.environ.get("WERKZEUG_RUN_MAIN"):
			webbrowser.open_new(f'http://127.0.0.1:{ port }')
		
	Timer(.5, open_browser).start()
	app.run(host='0.0.0.0', port=port, debug=True)