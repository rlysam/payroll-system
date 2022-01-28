#library to import the excel file
import openpyxl
#libraries to create the pdf file and add text to it
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
#libraries to merge pdf files
import os
from PyPDF2 import PdfFileReader, PdfFileMerger


#import the sheet from the excel file
# wb = openpyxl.load_workbook('data/data_payslip.xlsx')
wb = openpyxl.load_workbook('data/data_payslip.xlsx')
sheet = wb.get_sheet_by_name('employees')

#convert the font so it is compatible
pdfmetrics.registerFont(TTFont('Ayar','ayar.ttf'))

#Page information
page_width = 2156
page_height = 3050
spread = 100
start = 200
start_2 = 700

#Payslip variables
company_name = 'Sample Company Name Inc.'
month_year = 'January 2022'

def create_payslip():
    for i in range (2, 42):
        #eading values from excel file
        emp_name = sheet.cell(row = i, column = 1).value
        emp_last_name = sheet.cell(row = i, column = 2).value
        address = sheet.cell(row = i, column = 3).value
        refer = sheet.cell(row = i, column = 4).value
        empyer_name = sheet.cell(row = i, column = 5).value
        email = sheet.cell(row = i, column = 6).value
        job_stats = sheet.cell(row = i, column = 7).value
        post_code = sheet.cell(row = i, column = 8).value
        gender = sheet.cell(row = i, column = 9).value
        grade = sheet.cell(row = i, column = 10).value
        department = sheet.cell(row = i, column = 11).value
        dmWeight = sheet.cell(row = i, column = 12).value
        bscSalary = sheet.cell(row = i, column = 13).value
        ovrtime = sheet.cell(row = i, column = 14).value
        grssPay = sheet.cell(row = i, column = 15).value
        netPay = sheet.cell(row = i, column = 16).value
        tax = sheet.cell(row = i, column = 17).value
        SSS = sheet.cell(row = i, column = 18).value
        loan = sheet.cell(row = i, column = 19).value
        philhealth_payment = sheet.cell(row = i, column = 20).value
        pagIBIG = sheet.cell(row = i, column = 21).value
        deductions = sheet.cell(row = i, column = 22).value
        payDate = sheet.cell(row = i, column = 23).value
        taxPeriod = sheet.cell(row = i, column = 24).value
        philhealth_number = sheet.cell(row = i, column = 25).value
        philhealth_code = sheet.cell(row = i, column = 26).value
        taxablePay = sheet.cell(row = i, column = 27).value
        sssPay = sheet.cell(row = i, column = 28).value
        other_pay_due = sheet.cell(row = i, column = 29).value





        #Saving the pdf file
        c.save()



# # basura ata to...
# def merge_pdfs():
#     files_dir = 'tutorial' #Select the directory where the pdf files are located
#     pdf_files = [f for f in os.listdir(files_dir) if f.endswith('.pdf')] #Get all files in the directory that end with '.pdf'
#     merger = PdfFileMerger() #Create an empty file
#     for filename in pdf_files:
#         merger.append(PdfFileReader(os.path.join(files_dir,filename),'rb')) #Add every pdf to the empty file
#     merger.write(os.path.join(files_dir,'merged_pdfs.pdf')) #Save the file

create_payslip()
# merge_pdfs()
