# Gumagana na 'to, lahat ng backend calls, dito lalagay...

from crypt import methods
from flask import *
from functions.payroll_functions.PMS import *
from functions.security.security import *
from functions.pdf_generator.forPDF import *
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

# ! Gayahin yung receivedInitial --- waiting
@app.route('/receiveAllData', methods=['POST'])
def receivePayrollAllAndProcess():
	if request.method=='POST':
		jsonData = request.get_json()
		create_payslip(jsonData)
		sendPaySlipToEmployeeEmail(jsonData['email'],jsonData['employee_name'],)
		# ! waiting for Ryan
		# TODO 2. Call toFirebaseDatabase(openedData) 
	response = 'Success. Sent receipt to employee email and transaction to database...'
	return response

# TODO --- waiting for LYAH
# *DONE  --- waiting
@app.route('/getReport', methods=['POST'])
def getReport():
	securedData = {}
	if request.method=='POST':
		# ! waiting for Ryan
		# TODO waiting for Ryan
		# unsafeReports = getAllTransactionFromFirebase() # Map
		securedData = encrypt(unsafeReports) # encrypted data
	response = jsonify(securedData)
	return response

# *DONE
@app.route('/receiveInitialData', methods=['POST'])
def receiveBS_DM_OT_LOAN():
	securedData = {}
	if request.method=='POST':
		jsonData = request.get_json()
		unsafeComputedData = MonthlySalary(jsonData) # Map
		# print(unsafeComputedData)
		# securedData = encrypt(str(unsafeComputedData)) # encrypted data
	# response = jsonify(securedData)
	response = jsonify(unsafeComputedData)
	return response

# *DONE 
@app.route('/sendPayRef', methods=['POST'])
def sendPayRef():
	unsafeData = payRef()
	# securedData = encrypt(str(unsafeData))
	return jsonify(unsafeData)

# Ewan eto ata yung unanng titignan
if __name__ == '__main__':
	# TODO wag na DEBUG Mode pag deploy?
    app.run(debug=True)