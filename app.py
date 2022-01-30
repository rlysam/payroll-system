from crypt import methods
from flask import *
from functions.payroll_functions.PMS import *
from functions.security.security import *
from functions.pdf_generator.forPDF import *
from functions.email.sending_email import *
from functions.firebase_connections.append import *

# import json
import ast

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome. This is the index for InfoSec Backend. \n Visit the GitHub Repo: rlysam/payroll-system"

# # TODO --- waiting for LYAH
# # *DONE  --- waiting
# @app.route('/getReport', methods=['POST'])
# def getReport():
# 	securedData = {}
# 	if request.method=='POST':
# 		# ! waiting for Ryan
# 		# TODO waiting for Ryan
# 		# unsafeReports = getAllTransactionFromFirebase() # Map
# 		securedData = encrypt(unsafeReports) # encrypted data
# 	response = jsonify(securedData)
# 	return response

# ! Gayahin yung receivedInitial --- waiting
@app.route('/receiveAllData', methods=['POST'])
def receivePayrollAllAndProcess():
	if request.method=='POST':
		jsonData = request.get_json()
		decryptedMapFromFlutter =  decrypt(jsonData)
		create_payslip(decryptedMapFromFlutter)
		mapData = decryptedMapFromFlutter
		sendPaySlipToEmployeeEmail(mapData['email'],mapData['employee_name'],)
		appendNewEntry(mapData) # append UNSECURED Map to firebase
		appendNewEntry(encrypt(str(mapData))) # Append ENCRYPTED Map to firebase
	response = 'Success. Sent receipt to employee email and transaction to database...'
	return response

# *DONE
# *DONE
@app.route('/receiveInitialData', methods=['POST'])
def receiveBS_DM_OT_LOAN():
	securedData = {}
	if request.method=='POST':
		jsonData = request.get_json()
		decryptedMapFromFlutter =  decrypt(jsonData)
		unsafeComputedData = MonthlySalary(decryptedMapFromFlutter) # Map
		securedData = encrypt(str(unsafeComputedData)) # encrypted data
	response = jsonify(securedData)
	return response

# *DONE 
# *DONE 
@app.route('/sendPayRef', methods=['POST'])
def sendPayRef():
	unsafeData = payRef() # Dictionary
	securedData = encrypt(str(unsafeData))
	return jsonify(securedData)

# Ewan eto ata yung unanng titignan
if __name__ == '__main__':
	# TODO wag na DEBUG Mode pag deploy?
    app.run(debug=True)