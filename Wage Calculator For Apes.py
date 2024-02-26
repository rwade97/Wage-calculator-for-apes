h = input("Enter Hours: ")
r = input("Enter Rate: ")
try:
        xh = float(h)
        xr = float(r)
except: 
        print ("Please enter numeric input, you silly ape.")
        quit()
if xh > 40 :
    xp = (40 + (xh - 40) * 1.5) * xr
else :
    xp = xh * xr
print("Pay:",xp)