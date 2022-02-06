# TODO (Sam) 'SEND' to Frontend
import random
import time
import datetime
import json
# import string


def payRef():
    PayDate = (time.strftime("%d/%m/%y"))

    Refpay = random.randint(20000, 709467)
    Reference = ("PR" + str(Refpay))

    PhilHealthpay = random.randint(4200, 9467)
    PhilHealthNumber = ("PH" + str(PhilHealthpay))

    payRefData = {
        "pay_date": PayDate,
        "reference": Reference,
        "philhealth_number": PhilHealthNumber,
    }
    return json.dumps(payRefData)

# COMPUTATIONS lang function dito


def MonthlySalary(map):  #ito yung map na galing sa flutter

    # TODO (Kate) gawin  yun example ko dito
    # BS = float(BasicSalary.get()) #! before
    BS = float( map["basic_salary"])  #! AFTER : example ito na yung galing kay Flutter
    DM = float(map["deminimis"])
    OT = float(map["overtime"])
    #BS = float(BasicSalary.get()) if '.' in BasicSalary.get() else str(BasicSalary.get())
    #DM = float(DeMinimis.get()) if '.' in DeMinimis.get() else str(DeMinimis.get())
    #OT = float(OverTime.get()) if '.' in OverTime.get() else str(OverTime.get())

    # TODO (Kate)
    # ! hindi na .set yung gagamitin
    # * note str() kapag di naman gagamitin sa computation

    M_SSS = ((BS + DM + OT) * 0.045)
    sss = "PHP " + str('%.2f' % (M_SSS))

    M_PhilHealthPayment = ((BS + DM + OT) * 0.04 / 12)
    philhealth_payment = "PHP " + str('%.2f' % (M_PhilHealthPayment))

    M_HDMF = (100)
    hdmf = "PHP " + str('%.2f' % (M_HDMF))

    TaxableIncome = ((BS + DM + OT) - (M_SSS + M_HDMF + M_PhilHealthPayment))
    # MTax = ((2500 + (TaxableIncome - 33333) * 0.25), 0) [BS<20000]

    MTax = 0
    if TaxableIncome > 20832 and TaxableIncome < 33333:
        MTax = (TaxableIncome - 20833) * 0.20
    elif TaxableIncome > 33333 and TaxableIncome < 66667:
        MTax = (2500 + (TaxableIncome - 33333) * 0.25)
    elif TaxableIncome > 66667 and TaxableIncome < 166667:
        MTax = (10833.33 + (TaxableIncome - 66667) * 0.30)
    elif TaxableIncome > 166667 and TaxableIncome < 666667:
        MTax = (40833.33 + (TaxableIncome - 166667) * 0.32)
    elif TaxableIncome > 666667:
        MTax = (200833.33 + (TaxableIncome - 666667) * 0.35)

    tax = "PHP " + str('%.2f' % (MTax))

    Deduct = (MTax + M_SSS + M_PhilHealthPayment + M_HDMF)
    deductions = "PHP " + str('%.2f' % (Deduct))

    gross_pay = "PHP " + str('%.2f' % (BS + DM + OT))

    NetPayAfter = (BS + DM + OT) - Deduct
    net_pay = "PHP " + str('%.2f' % (NetPayAfter))

    taxable_pay = tax
    pension_pay = sss
    other_payment_due = (str(0))

    MonthlySalaryData = {
        "sss": sss,
        "philhealth_payment": philhealth_payment,
        "hdmf": hdmf,
        "tax": tax,
        "net_pay": net_pay,
        "deductions": deductions,
        "gross_pay": gross_pay,
        "taxable_pay": taxable_pay,
        "pension_pay": pension_pay,
        "other_payment_due": other_payment_due,

    }
    return json.dumps(MonthlySalaryData)

    # TODO (Sam) yung ibang  send to database yung buong transaction na to including yung Employee name...
