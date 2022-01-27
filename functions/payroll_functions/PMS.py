	# TODO (Sam) 'SEND' to Frontend
def PayRef():
	PayDate.set(time.strftime("%d/%m/%y"))
	#PayDate.set(time.strftime("%x"))

	Refpay = random.randint(20000, 709467)
	Refpaid = ("PR" + str(Refpay))
	Reference.set(Refpaid)

	PhilHealthpay = random.randint(4200, 9467)
	PhilHealthpaid = ("PH" + str(PhilHealthpay))
	PhilHealthNumber.set(PhilHealthpaid)

# COMPUTATIONS lang function dito
def MonthlySalary(map): #ito yung map na galing sa flutter

		# TODO (Kate) gawin  yun example ko dito
	# BS = float(BasicSalary.get()) #! before
	BS = float(map['basic_salary']) #! AFTER : example ito na yung galing kay Flutter
	DM = float(DeMinimis.get())
	OT = float(OverTime.get())
	#BS = float(BasicSalary.get()) if '.' in BasicSalary.get() else str(BasicSalary.get())
	#DM = float(DeMinimis.get()) if '.' in DeMinimis.get() else str(DeMinimis.get())
	#OT = float(OverTime.get()) if '.' in OverTime.get() else str(OverTime.get())

	M_SSS = ((BS + DM + OT) * 0.045)
	MM_SSS = "₱", str('%.2f' % (M_SSS))

	# TODO (Kate)
	# ! hindi na .set yung gagamitin
	# SSS.set(MM_SSS)
	# * note str() kapag di naman gagamitin sa computation
	sss = str(map['sss'])
	# M_Loan = float(Loan.get()) #! before
	M_Loan = float(map['loan']) #!After

	MM_Loan = "₱", str('%.2f' % (M_Loan))
	Loan.set(MM_Loan)

	M_PhilHealthPayment = ((BS + DM + OT) * 0.04 / 12)
	MM_PhilHealthPayment = "₱", str('%.2f' % (M_PhilHealthPayment))
	PhilHealthPayment.set(MM_PhilHealthPayment)
	
	M_HDMF = (100)
	MM_HDMF = "₱", str('%.2f' % (M_HDMF))
	HDMF.set(MM_HDMF)
	
	TaxableIncome = ((BS + DM + OT)-(M_SSS + M_HDMF + M_PhilHealthPayment))
	MTax = (2500 + (TaxableIncome - 33333) * 0.25)
	TTax = "₱", str('%.2f' % (MTax))
	Tax.set(TTax)

	Deduct = (MTax + M_SSS + M_Loan + M_PhilHealthPayment + M_HDMF)
	Deduct_Payment = "₱", str('%.2f' % (Deduct))
	Deductions.set(Deduct_Payment)

	Gross_Pay = "₱", str('%.2f' % (BS + DM + OT))
	GrossPay.set(Gross_Pay)

	NetPayAfter = (BS + DM + OT) - Deduct
	NetAfter = "₱", str('%.2f' % (NetPayAfter))
	NetPay.set(NetAfter)

	TaxablePay.set(TTax)
	SSSPay.set(MM_SSS)
	OtherPaymentDue.set("0")
	
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