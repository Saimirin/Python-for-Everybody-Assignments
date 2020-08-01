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
