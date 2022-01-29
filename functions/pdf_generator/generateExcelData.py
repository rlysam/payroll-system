import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)


# TODO Call this from app.py,  before calling 'create_payslip(mapData)'
def dfAndSaveToExcel(openedData):  #dictionary of all entries
    path = r'data/data_payslip.xlsx'
    df = pd.read_excel(path)
    # TODO  ---
    keys = [
        'Pay Date - dd/mm/yy',
         'Name',
         'Address',
         'Reference',
         'Employer Name',
        
        'Email',
         'Job Status',
         'Post Code',
         'Grade',
         'Department',
        
        'De Minimis ',
         'Basic Salary',
         'Overtime',
         'Gross Pay',
         'Tax',
         'SSS',
        
        'Loan',
         'PhilHealth Payment',
         'HDMF (Pag-IBIG)',
         'Deductions',
        
        'Net Pay',
         'PhilHealth Number',
         'Taxable Pay',
         'SSS Pay',
        
        'Other Payment Due'
    ]

    keys_of_opened_data =[
 'pay_date',       
 'employee_name',
 'address',
 'reference',
 'employer_name',
 
 'email',
 'job_status',
 'postcode',
 'grade',
 'department',
 
 'deminimis',
 'basic_salary',
 'overtime',
 'gross_pay',
 'tax',
 'sss',

 'loan',
 'philhealth_payment',
 'hdmf',
 'deductions',

 'net_pay',
 'philhealth_number',
 'taxable_pay',
 'pension_pay',
 
 'other_payment_due',
    ]

    i = 0

# Lagay sa column yung bagong value
    for key in keys:
        df[key][0] = openedData[keys_of_opened_data[i]]

# # TESTING
#     for key in keys:
#         df[key][0] = keys_of_opened_data[i]+' sample value'
#         i=i+1
    
    # save xlsx to same location
    df.to_excel(path,index=False,sheet_name='employees')

# dfAndSaveToExcel(9)