# Gumagana na 'to, lahat ng backend calls, dito lalagay...

from crypt import methods
from flask import *
from functions.sample_file.hello import *
from functions.payroll_functions.PMS import *
from functions.security.security import *

# import json
import ast

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome. This is the index for InfoSec Backend. \n Visit the GitHub Repo: rlysam/payroll-system"

@app.route('/receiveInitialData', methods=['POST'])
def receiveBS_DM_OT_LOAN():
	securedData = {}
	if request.method=='POST':
		jsonData = request.get_json()
		mapData = ast.literal_eval(jsonData)
		unsafeComputedData = MonthlySalary(mapData) # Map
		securedData = encrypt(str(unsafeComputedData)) # encrypted data
	response = jsonify(securedData)
	return response

# * Complete *
@app.route('/sendPayRef', methods=['POST'])
def sendPayRef():
	unsafeData = payRef()
	securedData = encrypt(str(unsafeData))
	return jsonify(securedData)

# * Complete * ALMOST
@app.route('/receiveData', methods=['POST'])
def receivePayrollAllAndProcess():
	if request.method=='POST':
		jsonData = request.get_json()
		mapData = ast.literal_eval(jsonData)
		# sayHello(mapData)
		# TODO 1. Call openedData = decrypt(mapData)
		# TODO 2. Call toExcelAndSendToEmail(openedData)
		# TODO 3. Call toFirebaseDatabase(openedData)

	response = 'Success. Sent receipt to employee email and transaction to database...'
	return response

# Ewan eto ata yung unanng titignan
if __name__ == '__main__':
    app.run(debug=True)