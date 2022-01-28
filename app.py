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

# # TODO (Route) EXECUTE > Send Payslip PDF to Employee via E-Mail
# # ! NOTE: RESEND Data from Flutter, then call the payslip_generator() lastly, payslip generator will use gmail to send to employee
# @app.route('/receiveData', methods=['POST'])
# def receivePayrollAll():
# 	if request.method=='POST':
# 		jsonData = request.get_json()
# 		# print('\n\nlaman ng request.value:\n\n')
# 		# print(type(jsonData)) # str
# 		dictData = ast.literal_eval(jsonData)
# 		sayHello(dictData)
# 		# sample usage:	print(sample['employee_name'])
# 	response = 'Success'
# 	return response


# # TODO (Route) receive PayrollAll  	only needed data (BSDM)
# # TODO (Route) return 'COMPUTATIONS'
# # ! NOTE: ONLY NEEDED for computations
# # ! NOTE: BS, DM, OT, Loan
# # note: lahat ng parameters ay nasa body
# @app.route('/receiveInitialData', methods=['POST'])
# def receivePayrollAll():
# 	if request.method=='POST':
# 		jsonData = request.get_json()
# 		# print('\n\nlaman ng request.value:\n\n')
# 		# print(type(jsonData)) # str
# 		dictData = ast.literal_eval(jsonData)
# 		sayHello(dictData)
# 		# sample usage:	print(sample['employee_name'])
# 	response = 'Computations from monthly salary'
# 	return response

# * Complete *
# TODO (Route) SEND PayRef()
# ! NOTE: send PayRef
# note: lahat ng parameters ay nasa body
@app.route('/sendPayRef', methods=['POST'])
def sendPayRef():
	return jsonify(encrypt(str(payRef())))

# * Complete *
# TODO (Route) receive PayrollAll 
# TODO return nothing
# ! NOTE: ALL DATA
# ! NOTE: final before adding ENTRY TO DATABASE
# note: lahat ng parameters ay nasa body
@app.route('/receiveData', methods=['POST'])
def receivePayrollAll():
	if request.method=='POST':
		jsonData = request.get_json()
		# print('\n\nlaman ng request.value:\n\n')
		# print(type(jsonData)) # str
		dictData = ast.literal_eval(jsonData)
		sayHello(dictData)
		# sample usage:	print(sample['employee_name'])
		# call function ni Ryan
	response = 'Success'
	return response

# Ewan eto ata yung unanng titignan
if __name__ == '__main__':
    app.run(debug=True)