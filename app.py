from crypt import methods
from flask import *
from functions.payroll_functions.PMS import *
from functions.security.security import *
from functions.pdf_generator.forPDF import *
from functions.email.sending_email import *
from functions.firebase_connections.append import *
# from functions.firebase_connections.getdata import *
import os

# import json
import ast

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome. This is the index for InfoSec Backend. \n Visit the GitHub Repo: rlysam/payroll-system"

# *DONE 
@app.route('/getAllRecords', methods=['POST'])
def sendAllRecord():
	stillEncryptedDataFromFirebase = listAllParsed() # Dictionary
	# ! String na may comman 
	jsonData = stillEncryptedDataFromFirebase
	return jsonData


# ! Gayahin yung receivedInitial --- waiting
@app.route('/receiveAllData', methods=['POST'])
def receivePayrollAllAndProcess():
	if request.method=='POST':
		data = request.get_data()
		decryptedMapFromFlutter =  decrypt(data)
		create_payslip(json.loads(decryptedMapFromFlutter))
		mapData = json.loads(decryptedMapFromFlutter)
		sendPaySlipToEmployeeEmail(mapData['email'],mapData['employee_name'],)
		dataToFirebase = encrypt(str(json.dumps(mapData)))
		appendNewEntry(dataToFirebase) # Append ENCRYPTED Map to firebase
		os.remove("*.pdf")
	response = 'Success. Sent receipt to employee email and transaction to database...'
	return response

# *DONE
# *DONE
@app.route('/receiveInitialData', methods=['POST'])
def receiveBS_DM_OT_LOAN():
	securedData = {}
	if request.method=='POST':
		data = request.get_data()
		decryptedMapFromFlutter =  decrypt(data)
		unsafeComputedData = MonthlySalary(json.loads(decryptedMapFromFlutter)) # Map
		print(unsafeComputedData)
		securedData = encrypt(str(unsafeComputedData)) # encrypted data
		# securedData='finish'
	# response = jsonify(securedData)
	return securedData

# *DONE 
# *DONE 
@app.route('/sendPayRef', methods=['POST'])
def sendPayRef():
	unsafeData = payRef() # Dictionary
	securedData = encrypt(str(unsafeData))
	return securedData

# Ewan eto ata yung unanng titignan
if __name__ == '__main__':
	# TODO wag na DEBUG Mode pag deploy?
    app.run(debug=True)