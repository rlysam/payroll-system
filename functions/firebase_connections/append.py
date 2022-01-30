import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("payroll-a7eda-firebase-adminsdk-1sdei-684033a636.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://payroll-a7eda-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('/')
new_employee_ref = ref.push({
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
  'other_payment_due' : 'other_payment_due'
})

employee_id = new_employee_ref.key
