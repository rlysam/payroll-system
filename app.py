# Gumagana na 'to, lahat ng backend calls, dito lalagay...

from crypt import methods
from flask import *
from functions.sample_file.hello import *

# gawa ng Flask object
app = Flask(__name__)

# '/' meaning yung pinaka unang makikita "url.../'
@app.route('/')
def welcome():
    return "Welcome. This is the homepage"

# '/login' parang functions, ito tatawagin mismo
# note: lahat ng parameters ay nasa body
@app.route('/login', methods=['POST', 'GET'])
def login():
# GET kapag nasa URL yung se-send na data, wala ata tayo gagamitin na ganito para SECURE :D
  if request.method=='GET':
	  return 'mali yung request type'
# If POST ang tinawag, gagawin to
  if request.method=='POST':
	#  no need to make a MODEL CLASS
    jsonData = request.get_json()
    print('\n\nlaman ng request.value')
    print(jsonData)

    return jsonify(jsonData) #converted na sa as JSON

# Ewan eto ata yung unanng titignan
if __name__ == '__main__':
    app.run(debug=True)