import os
import webbrowser
from threading import Timer
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def home():
	data = {
		'cookies': [
			{
				'color': 'oat',
				'name': 'Vanilla',
				'descr': 'vanilla and white chocolate cookie with white chocolate drizzle'
			},
			{
				'color': 'mint',
				'name': 'S\'mores',
				'descr': 'milk chocolate cookie with marshmallows and grahams'
			},
			{
				'color': 'oat',
				'name': 'Pumpkin pie',
				'descr': 'vanilla pumpkin cookie with cinnamon and spice topped with a candy corn'
			},
			{
				'color': 'mint',
				'name': 'Apple fritter',
				'descr': 'vanilla cookie with apple chunks,cinnamon and cider glaze'
			},
			{
				'color': 'oat',
				'name': 'Maple pecan',
				'descr': 'vanilla maple cookie with chopped pecans and maple glaze'
			},
			{
				'color': 'mint',
				'name': 'Peanut butter & Nutelly',
				'descr': 'classic chocolate cookie with peanut butter and nutella'
			},
			{
				'color': 'oat',
				'name': 'Chocolate toffee',
				'descr': 'semisweet chocolate cookie with toffee bits and toffee topping'
			},
			{
				'color': 'mint',
				'name': 'Chocolate coconut',
				'descr': 'semisweet chocolate cookie with coconut flakes and coconut topping'
			},
			{
				'color': 'oat',
				'name': 'Hot chocolate',
				'descr': 'milk chocolate cookie with mini marshmallows'
			},
		],
		'floofs': [
			{
				'color': 'armygreen',
				'name': 'Confetti floof',
				'descr': 'vanilla cookies with sprinkle filling'
			},
			{
				'color': 'armygreen',
				'name': 'Lemon floof',
				'descr': 'vanilla cookies with lemon filling'
			},
			{
				'color': 'armygreen',
				'name': 'Seasonal floof',
				'descr': 'seasonal'
			},
		],
		'cookieDoughs': [
			{
				'staticImage': 'cookie_doh.png',
				'color': 'blue',
				'name': 'Chocolate chip',
				'descr': 'TBD'
			}
		],
		'beverages': [
			{
				'omitRollover': True,
				'color': 'pink',
				'name': 'Apple pie slushie',
				'descr': 'apple pie filling in apple slushie, topped with strussel crumble'
			},
			{
				'omitRollover': True,
				'color': 'pink',
				'name': 'Frozen hot chocolate',
				'descr': 'chocolate frapé topped with whipped cream & chocolate shavings'
			}
		]
	}
	return render_template('index.html', data=data)
	

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	
	def open_browser():
		if not os.environ.get("WERKZEUG_RUN_MAIN"):
			webbrowser.open_new(f'http://127.0.0.1:{ port }')
		
	Timer(.5, open_browser).start()
	app.run(host='0.0.0.0', port=port, debug=True)