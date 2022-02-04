import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)


# TODO Call this from app.py,  before calling 'create_payslip(mapData)'
def dfAndSaveToExcel(openedData):  #dictionary of all entries
    # path = 'functions/pdf_generator/data/data_payslip.xlsx'
    path = 'functions/pdf_generator/data/data_payslip.xlsx'
    df = pd.read_excel(path)
    print('\n\n')
    print(df)
    print('\n\n')
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
        value = openedData[keys_of_opened_data[i]]
        df[key][0] = value
        i=i+1

    print('\n\n')
    print('NEW:::')
    print(df)
    print('\n\n')

    # save xlsx to same location
    df.to_excel(path,index=False,sheet_name='employees')
