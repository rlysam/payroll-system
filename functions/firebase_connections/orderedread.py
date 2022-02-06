import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("payroll-a7eda-firebase-adminsdk-1sdei-684033a636.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://payroll-a7eda-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('/')
#'pay_date' variable is encryted dunno if this will be able to read it by using
#ref.order_by_child(), this function is used to order the data retrieve by date
#start_at(input the date here) and end_at(input ending date here) is used to
#limit where the data will come from, used ranging instead coz theres no function to retrieve specific data
snapshot = ref.order_by_child('pay_date').start_at(starting date inpuut).end_at(ending date inpuut).get()
for key in snapshot:
    print(key)