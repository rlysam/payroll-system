def PayRef():
    PayDate.set(time.strftime("%d/%m/%y"))
    #PayDate.set(time.strftime("%x"))

    Refpay = random.randint(20000, 709467)
    Refpaid = ("PR" + str(Refpay))
    Reference.set(Refpaid)

    PhilHealthpay = random.randint(4200, 9467)
    PhilHealthpaid = ("PH" + str(PhilHealthpay))
    PhilHealthNumber.set(PhilHealthpaid)


def MonthlySalary():

    BS = float(BasicSalary.get())
    DM = float(DeMinimis.get())
    OT = float(OverTime.get())
    #BS = float(BasicSalary.get()) if '.' in BasicSalary.get() else str(BasicSalary.get())
    #DM = float(DeMinimis.get()) if '.' in DeMinimis.get() else str(DeMinimis.get())
    #OT = float(OverTime.get()) if '.' in OverTime.get() else str(OverTime.get())

    M_SSS = ((BS + DM + OT) * 0.045)
    MM_SSS = "₱", str('%.2f' % (M_SSS))
    SSS.set(MM_SSS)

    M_Loan = float(Loan.get())
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