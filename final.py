#Nick Menendez
#CISP 407
#Final Project


#Create Output Files
#NOTE TO PROFESSOR: As I have been doing all semester, I am coding on an Apple Mac, so I cannot save these files to C:\Temp since that is a Windows path
ER1 = open("/Users/nickmenendez/Documents/FLC/Spring 19/CISP 407/Final Project/ER1.txt", "w")
ER2 = open("/Users/nickmenendez/Documents/FLC/Spring 19/CISP 407/Final Project/ER2.txt", "w")
TR1 = open("/Users/nickmenendez/Documents/FLC/Spring 19/CISP 407/Final Project/TR1.txt", "w")
TR2 = open("/Users/nickmenendez/Documents/FLC/Spring 19/CISP 407/Final Project/TR2.txt", "w")
PR1 = open("/Users/nickmenendez/Documents/FLC/Spring 19/CISP 407/Final Project/PR1.txt", "w")
PR2 = open("/Users/nickmenendez/Documents/FLC/Spring 19/CISP 407/Final Project/PR2.txt", "w")

#create an employeeData class that holds the info from employee.txt
class employeeData:
    #Attributes
    empNum = int(0)
    lastName = ""
    firstName = ""
    workArea = int(0)
    rate = float(0)

    regHours = float(0)
    totalHours = float(0)
    otHours = float(0)

    regPay = float(0)
    otPay = float(0)
    grossPay = float(0)
    taxesDue = float(0)
    netPay = float(0)
    
    
    #Initialize
    def __init__(self,empNum, lastName, firstName, workArea, rate):
        self.empNum = empNum
        self.lastName = lastName
        self.firstName = firstName
        self.workArea = workArea
        self.rate = rate
    
    def calcTotalHours(self):
        self.totalHours = self.regHours + self.otHours

    def calcRegPay(self):
        self.regPay = self.regHours * self.rate

    def calcOtPay(self):
        self.otPay = self.otHours * (self.rate * 1.5)

    def calcGrossPay(self):
        self.grossPay = self.regPay + self.otPay

    def calcNetPay(self):
        self.netPay = self.grossPay - self.taxesDue

    

print("Welcome to Nick Menendez's Payroll Processing Program!\n")


#************************************** Phase 1 **************************************
#Create the employee report #1 - Sort By Emp ID
print("First, we will generate an Employee Report that is sorted by Employee Number.")
input("Press the ENTER key to generate ER1.txt\n")

#open employee.txt
employeeInfo = open("/Users/nickmenendez/Documents/FLC/Spring 19/CISP 407/Final Project/employee.txt")

#Create an array to hold employee Data
empData = []

#Iterate through employeeInfo and extract the employee information
for eachline in employeeInfo:
    eRecord = eachline.split(",")
    x = eRecord[4]
    empNum = int(eRecord[0])
    lastName = eRecord[1]
    firstName = eRecord[2]
    workArea = int(eRecord[3])
    rate = float(eRecord[4][0:(len(x) - 1)])
    #Construct an object of employeeData and put the object into the empData array
    empData.append(employeeData(empNum,lastName,firstName,workArea,rate))

#Now that we have the data, close employee.txt
employeeInfo.close()

#sort the array by empNum
empData.sort(key=lambda x:x.empNum)

#Write the Header
ER1.write("Employee Data\n\n")
ER1.write(f"{'Emp. Number':^20}{'Last Name':<20}{'First Name':<20}{'Work Area':^20}{'Hourly Rate':^20}\n")
ER1.write("----------------------------------------------------------------------------------------------------\n")
    
#Print the list to ER1
i = 0
while i < len(empData):
    payRate = '${:,.2f}'.format(empData[i].rate)
    ER1.write(f"{empData[i].empNum:^20}{empData[i].lastName:<20}{empData[i].firstName:<20}{empData[i].workArea:^20}{payRate:^20}\n")
    i += 1

#close ER1
ER1.close()


#********************************** Phase 2 ******************************************
#Create the Employee Report #2 - sort by Work Area then Emp Num
print("Next, we will generate an Employee Report that is sorted by Work Area, then Employee Number.")
input("Press the ENTER key to generate ER2.txt\n")

#Create a list that will hold lists for each work area
empDataWA = [[],[],[],[],[],[],[],[]]

#populate the lists inside of empDataWA by work area
i = 0
while i < len(empDataWA):
    for emp in empData:
        if ((emp.workArea - 1) == i):
            empDataWA[i].append(emp)
    i += 1

#Now sort by employee ID
i = 0
while i < len(empDataWA):
    empDataWA[i].sort(key=lambda x:x.empNum)
    i += 1

#Write Header
ER2.write("Employee Data\n\n")

#Write to ER2.txt the sorted lists and title each with the work area   
i = 0
while i < len(empDataWA):
    ER2.write("Work area " + str(i + 1) + "\n")
    ER2.write("----------------------------------------------------------------------------------------------------\n")
    ER2.write(f"{'Emp. Number':^20}{'Last Name':<20}{'First Name':<20}{'Hourly Rate':^20}\n")
    ER2.write("----------------------------------------------------------------------------------------------------\n")
    j = 0
    while j < len(empDataWA[i]):
        payRate = '${:,.2f}'.format(empDataWA[i][j].rate)
        ER2.write(f"{empDataWA[i][j].empNum:^20}{empDataWA[i][j].lastName:<20}{empDataWA[i][j].firstName:<20}{payRate:^20}\n")
        j += 1
    ER2.write("\n")
    i += 1

#Close ER2
ER2.close()


#********************************** Phase 3 ******************************************
#Create Time Report #1 - Sort by Employee Number
print("Next, we will generate a Time Report that is sorted by Employee Number.")
input("Press the ENTER key to generate TR1.txt\n")

#Write Header
TR1.write("Time Report\n\n")
TR1.write(f"{'Emp. Number':^20}{'Last Name':<20}{'First Name':<20}{'Total Hours':^20}{'OT Hours':^20}\n")
TR1.write("----------------------------------------------------------------------------------------------------\n")

for emp in empData:
    dailyHours = [0,0,0,0,0,0,0]
    timecard = open("/Users/nickmenendez/Documents/FLC/Spring 19/CISP 407/Final Project/timecard.txt")

    for eachline in timecard:
        record = eachline.split(",")
        eNum = int(record[0])
        day = record[1]
        hours = float(record[2][0:(len(record[2])-1)])
        
        if (emp.empNum == eNum):
            if (day == "MON"):
                dailyHours[0] = hours
            elif(day == "TUE"):
                dailyHours[1] = hours
            elif(day == "WED"):
                dailyHours[2] = hours
            elif(day == "THU"):
                dailyHours[3] = hours
            elif(day == "FRI"):
                dailyHours[4] = hours
            elif(day == "SAT"):
                dailyHours[5] = hours
            elif(day == "SUN"):
                dailyHours[6] = hours
    #close timecard.txt since we have extracted the useful information
    timecard.close()
    #print(dailyHours)

    #Calculate the regHours, otHours, and totalHours for each employee - save in the object
    dailyOT = 0
    weeklyOT = 0
    totOT = 0
    regularHours = 0
    totHours = 0

    for day in dailyHours:
        #Calculate the total hours worked (Add the daily hours to the total)
        totHours += day
        #Count the number of daily OT hours
        if (day > 8):
            dailyOT += (day - 8)

    if (totHours > 40):
        weeklyOT = totHours - (40 + dailyOT) 
    else:
        weeklyOT = 0

    totOT = dailyOT + weeklyOT
    regularHours = totHours - totOT

    emp.regHours = regularHours
    emp.otHours = totOT
    emp.totalHours = totHours

    #print(str(emp.regHours) + " " + str(emp.otHours) + " " + str(emp.totalHours) + "\n")

    TR1.write(f"{emp.empNum:^20}{emp.lastName:<20}{emp.firstName:<20}{emp.totalHours:^20}{emp.otHours:^20}\n")

TR1.close()


#********************************** Phase 4 ******************************************
#Create Time Report #2 - Sort by Work Area then Employee Number
print("Next, we will generate a Time Report that is sorted by Work Area, then Employee Number.")
input("Press the ENTER key to generate TR2.txt\n")

#Write Header
TR2.write("Time Report\n\n")

i = 0
while i < len(empDataWA):
    TR2.write("Work area " + str(i + 1) + "\n")
    TR2.write("----------------------------------------------------------------------------------------------------\n")
    TR2.write(f"{'Emp. Number':^20}{'Last Name':<20}{'First Name':<20}{'Total Hours':^20}{'OT Hours':^20}\n")
    TR2.write("----------------------------------------------------------------------------------------------------\n")
    j = 0
    while j < len(empDataWA[i]):
        TR2.write(f"{empDataWA[i][j].empNum:^20}{empDataWA[i][j].lastName:<20}{empDataWA[i][j].firstName:<20}{empDataWA[i][j].totalHours:^20}{empDataWA[i][j].otHours:^20}\n")
        j += 1
    TR2.write("\n")
    i += 1

TR2.close()


#********************************** Phase 5 ******************************************
#Create Payroll Report #1 - Sort by Employee Number
print("Next, we will generate a Payroll Report that is sorted by Employee Number.")
input("Press the ENTER key to generate PR1.txt\n")

#Write Header
PR1.write("Weekly Payroll\n\n")
PR1.write(f"{'Emp. Number':^15}{'Regular Pay':<15}{'Overtime Pay':^15}{'Gross Pay':^15}{'Taxes Due':^15}{'Net Pay':^15}\n")
PR1.write("----------------------------------------------------------------------------------------------------\n")

#Open tactable.txt to extract information
taxtable = open("/Users/nickmenendez/Documents/FLC/Spring 19/CISP 407/Final Project/taxtable.txt")
#Create a list of lists to hold taxtable info
taxList = [[],[],[],[],[],[],[],[],[],[],[],[]]
i = 0
for eachline in taxtable:
    record = eachline.split(",")
    lower = float(record[0])
    upper = float(record[1])
    tax = float(record[2][0:(len(record[2])-1)])

    taxList[i].append(lower)
    taxList[i].append(upper)
    taxList[i].append(tax)
    i += 1

#Close taxtable since we have the information now
taxtable.close()

for emp in empData:
    #calculate the regular pay
    emp.calcRegPay()
    #calculate the overtime pay
    emp.calcOtPay()
    #calculate the gross pay
    emp.calcGrossPay()
    #Look up the taxes due
    for record in taxList:
        if emp.grossPay >= record[0] and emp.grossPay <= record[1]:
            emp.taxesDue = record[2]
    #Calculate the Net Pay
    emp.calcNetPay()

    #Write to file
    rPay =  '${:,.2f}'.format(emp.regPay)
    oPay = '${:,.2f}'.format(emp.otPay)
    gPay = '${:,.2f}'.format(emp.grossPay)
    taxD = '${:,.2f}'.format(emp.taxesDue)
    nPay = '${:,.2f}'.format(emp.netPay)
    PR1.write(f"{emp.empNum:^15}{rPay:^15}{oPay:^15}{gPay:^15}{taxD:^15}{nPay:^15}\n")

#Close PR1
PR1.close()


#********************************** Phase 6 ******************************************
#Create Payroll Report #2 - Sort by Employee Number
print("Next, we will generate another Payroll Report that is sorted by Employee Number.")
input("Press the ENTER key to generate PR2.txt\n")

#Write Header
PR2.write("Weekly Payroll\n\n")
PR2.write(f"{'Emp. Number':^20}{'Last Name':<20}{'First Name':<20}{'Work Area':^20}{'Net Pay':^20}\n")
PR2.write("----------------------------------------------------------------------------------------------------\n")

for emp in empData:
    nPay = '${:,.2f}'.format(emp.netPay)
    PR2.write(f"{emp.empNum:^20}{emp.lastName:<20}{emp.firstName:<20}{emp.workArea:^20}{nPay:^20}\n")

#Close PR2
PR2.close()










