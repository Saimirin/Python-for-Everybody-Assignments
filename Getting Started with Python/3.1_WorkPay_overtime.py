# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.


hrs = input("Enter Hours:")
rate = input("enter the rate:")
h = float(hrs)
r = float(rate)
if h > 40:
    ot = h-40
    ot_pay = ot*r*1.5
    total = ot_pay+(r*40)
    print(total)
else:
    total = r*h
    print(total)
