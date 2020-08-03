# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 


def computepay(h,r):
    if h >= 40:
        return (r*40)+(r*1.5*(h-40))
    else:
        return r*h
    
hrs = float(input("Enter Hours:"))
rates= float(input("Enter rate:"))
pay = computepay(hrs,rates)
print("Pay",pay)