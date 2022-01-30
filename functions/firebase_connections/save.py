import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("payroll-a7eda-firebase-adminsdk-1sdei-684033a636.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://payroll-a7eda-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

def addEntryToDatabase(mapData):
	#save data
	ref = db.reference('/')
	ref.set(mapData)