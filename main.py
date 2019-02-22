from flask import Flask
import argparse
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Short sample app')
	parser.add_argument('port')
	args = parser.parse_args()
	app.run(port=args.port)
