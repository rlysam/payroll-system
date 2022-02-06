import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("payroll-a7eda-firebase-adminsdk-1sdei-684033a636.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://payroll-a7eda-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

#retrieve data
ref = db.reference('/')

data = ref.get()

def listAllParsed():
	for key in data:
		print(key, data[key])
		print('\n\n')

def deleteAll():
	for key, value in data.items():
		ref.child(key).set({})

listAllParsed()
# deleteAll()