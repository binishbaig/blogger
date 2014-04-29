from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello, World!"

@app.route('/binish/baig')
def say_my_name():
	return "Hello, This is Binish's page! Thank you for visiting"	

if __name__ == "__main__":
	app.run(port=1337)