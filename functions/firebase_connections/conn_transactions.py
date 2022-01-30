pip install firebase_admin

import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("path/to/serviceAccountKey.json")
default_app = firebase_admin.initialize_app(cred, {
      'https://payroll-a7eda-default-rtdb.asia-southeast1.firebasedatabase.app/' :databaseURL
})

def set (key):

  'employee_name' : key['employee_name'],
  'address' : key['address'],
  'reference' : key['reference'],
  'employer_name' : key['employer_name'],
  'email' : key['email'],
  'job_status' : key['job_status'],
  'deminis' : key['deminis'],
  'basic_salary' : key['basic_salary'],
  'overtime' : key['overtime'],
  'gross_pay' : key['gross_pay'],
  'net_pay' : key['net_pay'],
  'tax' : key['tax'],
  'sss' : key['sss'],
  'loan' : key['loan'],
  'philhealth_payment' : key['philhealth_payment'],
  'hdmf' : key['hdmf'],
  'deductions' : key['deductions'],
  'postcode' : key['postcode'],
  'gender' : key['gender'],
  'grade' : key['grade'],
  'department' : key['department'],
  'pay_date' : key['pay_date'],
  'philhealth_number' : key['philhealth_number'],
  'taxable_pay' : key['taxable_pay'],
  'pension_pay' : key['pension_pay'],
  'other_payment_due' : key['other_payment_due'],
  
  return file
  
  def main():
  ref = db.reference("/")
  with open("data.json", "r") as f:
	file_contents = json.load(f)
  ref.set(file_contents)
  
  main()
