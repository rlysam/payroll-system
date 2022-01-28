	# TODO (Sam) 'SEND' to Frontend
import random
import time
import datetime
# import string

def PayRef():
	PayDate = (time.strftime("%d/%m/%y"))

	Refpay = random.randint(20000, 709467)
	Reference = ("PR" + str(Refpay))

	PhilHealthpay = random.randint(4200, 9467)
	PhilHealthNumber = ("PH" + str(PhilHealthpay))

	return 

    # COMPUTATIONS lang function dito
def MonthlySalary(map): #ito yung map na galing sa flutter

        # TODO (Kate) gawin  yun example ko dito
        # BS = float(BasicSalary.get()) #! before
        BS = float(map['basic_salary']) #! AFTER : example ito na yung galing kay Flutter
        DM = float(map['deminimis'])
        OT = float(map['overtime'])
        #BS = float(BasicSalary.get()) if '.' in BasicSalary.get() else str(BasicSalary.get())
        #DM = float(DeMinimis.get()) if '.' in DeMinimis.get() else str(DeMinimis.get())
        #OT = float(OverTime.get()) if '.' in OverTime.get() else str(OverTime.get())
    
        # TODO (Kate)
        # ! hindi na .set yung gagamitin
        # * note str() kapag di naman gagamitin sa computation

        M_SSS = ((BS + DM + OT) * 0.045)
        sss = "₱", str('%.2f' % (M_SSS))
        
        M_Loan = float(map['loan']) 
        loan = "₱", str('%.2f' % (M_Loan))

        M_PhilHealthPayment = ((BS + DM + OT) * 0.04 / 12)
        philhealth_payment = "₱", str('%.2f' % (M_PhilHealthPayment))

        M_HDMF = (100)
        hdmf = "₱", str('%.2f' % (M_HDMF))
        
        TaxableIncome = ((BS + DM + OT)-(M_SSS + M_HDMF + M_PhilHealthPayment))
        MTax = (2500 + (TaxableIncome - 33333) * 0.25)
        tax = "₱", str('%.2f' % (MTax))

        Deduct = (MTax + M_SSS + M_Loan + M_PhilHealthPayment + M_HDMF)
        deductions = "₱", str('%.2f' % (Deduct))

        gross_pay = "₱", str('%.2f' % (BS + DM + OT))

        NetPayAfter = (BS + DM + OT) - Deduct
        net_pay = "₱", str('%.2f' % (NetPayAfter))

        taxable_pay = tax
        pension_pay = sss
        other_payment_due = (0)
        
        # TODO (Sam) yung ibang  send to database yung buong transaction na to including yung Employee name...

# def writeAllDataToFirebase():
	# TODO (Sam) call yung functions na gagawin dapat ni Ryan :::
	# EmployeeName = StringVar()
	# Address = StringVar()
	# Reference = StringVar()
	# EmployerName = StringVar()
	# Email = StringVar()
	# JobStatus = StringVar()
	# DeMinimis = StringVar()
	# BasicSalary = StringVar()
	# OverTime = StringVar()
	# GrossPay = StringVar()
	# NetPay = StringVar()
	# Tax = StringVar()
	# TaxableIncome = StringVar()
	# SSS = StringVar()
	# Loan = StringVar()
	# PhilHealthPayment = StringVar()
	# HDMF = StringVar()
	# Deductions = StringVar()
	# PostCode = StringVar()
	# Gender = StringVar()
	# Grade = StringVar()
	# Department = StringVar()
	# PayDate = StringVar()
	# TaxPeriod = StringVar()
	# PhilHealthNumber = StringVar()
	# PhilHealthCode = StringVar()
	# TaxablePay = StringVar()
	# SSSPay = StringVar()
	# OtherPaymentDue = StringVar()