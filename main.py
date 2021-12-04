import unittest
class Employee:

    def __init__(self, StaffId, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):
        self.StaffId = StaffId
        self.LastName = LastName
        self.FirstName = FirstName
        self.RegHours = int(RegHours)
        self.HourlyRate = int(HourlyRate)
        self.OTMultiple = float(OTMultiple)
        self.TaxCredit = int(TaxCredit)
        self.StandardBand = int(StandardBand)

    def computePayment(self, hours, date):
        OTRate = float(self.HourlyRate * self.OTMultiple)
        OT = 0
        if(hours > self.RegHours):
            OT = hours - self.RegHours

        RegularPay = (hours - OT) * self.HourlyRate
        OTPay = OT * OTRate
        GrossPay = RegularPay + OTPay

        HigherPay = 0
        if(GrossPay > RegularPay):
            HigherPay = GrossPay - self.StandardBand

        StdTax = self.StandardBand * 0.20

        HighTax = 0
        if(GrossPay > self.StandardBand):
            HighTax = (GrossPay - self.StandardBand) * 0.40

        TotalTax = StdTax + HighTax

        NetDeduction = TotalTax - self.TaxCredit
        NetPay = GrossPay - NetDeduction

        return {
            'name': self.FirstName+' ' + self.LastName,
            'Date': date,
            'Regular Hours Worked': self.RegHours,
            'Overtime Hours Worked': OT,
            'Regular Rate': self.HourlyRate,
            'Overtime Rate': OTRate,
            'Regular Pay': RegularPay,
            'Overtime Pay': OTPay,
            'Gross Pay': GrossPay,
            'Standard Rate Pay': self.StandardBand,
            'Higher Rate Pay': round(HigherPay, 2),
            'Standard Tax': round(StdTax, 2),
            'Higher Tax': round(HighTax, 2),
            'Total Tax': TotalTax,
            'Tax Credit': self.TaxCredit,
            'Net Deductions': round(NetDeduction, 2),
            'Net Pay': round(NetPay, 2)
        }

def computeAllPayment(empFileName, HoursFileName):
    finalResult = []
    with open(empFileName, 'r') as fobj:
        for line in fobj:
            data = line.split()
            emp = Employee(data[0], data[1], data[2], data[3],
                           data[4], data[5], data[6], data[7])
            with open(HoursFileName, 'r') as hobj:
                for hline in hobj:
                    hrs = hline.split()
                    if(hrs[0] == emp.StaffId):
                        pay = emp.computePayment(int(hrs[2]), hrs[1])
                        finalResult.append(pay)
    print(finalResult)


def main():
    computeAllPayment(r"data\employees.txt", r"data\hours.txt")


class EmployeeTest(unittest.TestCase): #creating a Employeetest class for unit test
    
    #Creating three functions named testNetLessEqualGross,testNetLessEqualGrossa,testNetLessEqualGrossb for testing the net pay is less than equal to gross pay  
    def testNetLessEqualGross(self):
        e = Employee(123456, 'Green', 'Joe', 37, 16, 1.5, 70, 700) 
        pi = e.computePayment(1,'31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])
    def testNetLessEqualGrossa(self):
        e1 = Employee(1234458, 'Shane', 'John', 39, 12, 2.6, 50, 825) 
        pi1= e1.computePayment(23,'12/11/2021')
        self.assertLessEqual(pi1['Net Pay'], pi1['Gross Pay'])
    def testNetLessEqualGrossb(self):
        e2 = Employee(923696, 'Landon', 'Steve', 39, 12, 0.5, 60, 955) 
        pi2= e2.computePayment(48,'12/11/2021')
        self.assertLessEqual(pi2['Net Pay'], pi2['Gross Pay'])
    def testNetLessEqualGrossc(self):
        e2 = Employee(007868, 'Denny', 'Davis', 40, 10, 2.00, 75, 600) 
        pi2= e2.computePayment(20,'5/12/2021')
        self.assertLessEqual(pi2['Net Pay'], pi2['Gross Pay'])