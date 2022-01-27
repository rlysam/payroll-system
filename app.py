# Gumagana na 'to, lahat ng backend calls, dito lalagay...

from crypt import methods
from flask import *
from functions.sample_file.hello import *
# import json
import ast

# gawa ng Flask object
app = Flask(__name__)

# '/' meaning yung pinaka unang makikita "url.../'
@app.route('/')
def welcome():
    return "Welcome. This is the homepage"

# '/login' parang functions, ito tatawagin mismo
# note: lahat ng parameters ay nasa body
@app.route('/receiveData', methods=['POST'])
def login():
	if request.method=='POST':
		jsonData = request.get_json()
		print('\n\nlaman ng request.value:\n\n')
		print(type(jsonData)) # str
		dictData = ast.literal_eval(jsonData)
		sayHello(dictData)
	response = 'Success : 200'
	return response

# Ewan eto ata yung unanng titignan
if __name__ == '__main__':
    app.run(debug=True)