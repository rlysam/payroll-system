pip install firebase_admin

import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("payroll-a7eda-firebase-adminsdk-1sdei-684033a636.json")
default_app = firebase_admin.initialize_app(cred, {
      'https://payroll-a7eda-default-rtdb.asia-southeast1.firebasedatabase.app/' :databaseURL
})

ref = db.reference('/')
ref.set({
    'employee1':{
  'employee_name' : 'employee_name',
  'address' : 'address',
  'reference' : 'reference',
  'employer_name' : 'employer_name',
  'email' : 'email',
  'job_status' : 'job_status',
  'deminis' : 'deminis',
  'basic_salary' : 'basic_salary',
  'overtime' : 'overtime',
  'gross_pay' : 'gross_pay',
  'net_pay' : 'net_pay',
  'tax' : 'tax',
  'sss' : 'sss',
  'loan' : 'loan',
  'philhealth_payment' : 'philhealth_payment',
  'hdmf' : 'hdmf',
  'deductions' : 'deductions',
  'postcode' : 'postcode',
  'gender' : 'gender',
  'grade' : 'grade',
  'department' : 'department',
  'pay_date' : 'pay_date',
  'philhealth_number' : 'philhealth_number',
  'taxable_pay' : 'taxable_pay',
  'pension_pay' : 'pension_pay',
  'other_payment_due' : 'other_payment_due',
    }
})