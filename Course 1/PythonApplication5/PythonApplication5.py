def computepay(h,r):
    p = h * r 
    return p
h = input('Enter the Hours')
r = input('Enter the rate')
h = float(h)
r = float(r)
if h <= 40 :   
    print('Its is less than 40')
else :
    p = computepay(47.5,10.50)
print("Pay",p)
