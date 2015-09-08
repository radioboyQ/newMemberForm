#Main router for simpleForm

from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)
#Adder server functionality
manager = Manager(app)

@app.route('/')
def index():
	return "Hello World"

if __name__ == '__main__':
	#app.run()
	manager.run()