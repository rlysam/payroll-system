# Gumagana na 'to, lahat ng backend calls, dito lalagay...

from crypt import methods
from flask import *
from functions.sample_file.hello import *
from functions.payroll_functions.PMS import *
from functions.security.security import *
from functions.pdf_generator.payslipgenerator import *
from functions.email.sending_email import *

# import json
import ast

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome. This is the index for InfoSec Backend. \n Visit the GitHub Repo: rlysam/payroll-system"

# # * Working
# @app.route('/testingPDFgeneratorFromFlutter', methods=['POST'])
# def generateTestPDF():
# 	create_payslip('sample') # TODO TESTING
# 	response = 'PDF Generated successfully.'
# 	return response

# TODO --- waiting for LYAH
# *DONE  --- waiting
@app.route('/getReport', methods=['POST'])
def getReport():
	securedData = {}
	if request.method=='POST':
		# ! waiting for Ryan
		# TODO waiting for Ryan
		# unsafeReports = getAllTransactionFromFirebase() # Map
		securedData = encrypt(str(unsafeReports)) # encrypted data
	response = jsonify(securedData)
	return response

# *DONE 
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

# *DONE 
@app.route('/sendPayRef', methods=['POST'])
def sendPayRef():
	unsafeData = payRef()
	securedData = encrypt(str(unsafeData))
	return jsonify(securedData)

# *DONE --- waiting
@app.route('/receiveData', methods=['POST'])
def receivePayrollAllAndProcess():
	if request.method=='POST':
		jsonData = request.get_json()
		mapData = ast.literal_eval(jsonData)
		openedData = decrypt(mapData)

		create_payslip(openedData)
		sendPaySlipToEmployeeEmail()
		# ! waiting for Ryan
		# TODO 2. Call toFirebaseDatabase(openedData) 


	response = 'Success. Sent receipt to employee email and transaction to database...'
	return response

# Ewan eto ata yung unanng titignan
if __name__ == '__main__':
	# TODO wag na DEBUG Mode pag deploy?
    app.run(debug=True)