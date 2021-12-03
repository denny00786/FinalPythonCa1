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