def EMI(p,t,r):
    print('Enter the principle amount:',p)
    print('Enter the no of Months:',t)
    print('Enter the annual interest rate: ',r)
    r=R/(12*100)
    emi=p*r*((1+r)**t)/((1+r)**t-1)

    print('MONTHLY EMi is',emi)

P=float(input("enter the principle amount"))
T=float(input("enter the time period"))
R=float(input("enter the rate"))

EMI(P,T,R)
