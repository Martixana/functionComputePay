def computepay (h, r):
    # print 'In computepay', h, r
    if h <=40:
        p = r*h
    else:
        p = r*40 + (r * 1.5 * (h-40))
    print "Final_Pay: ", p
    return p
    
    
try:
    inp = raw_input ("Enter hours: ")
    hours = float(inp)
    inp = raw_input ("Enter rate: ")
    rate = float (inp)
except: 
    print "Error, please enter numbers"
    quit()
    
pay = computepay (hours, rate)
print pay
     