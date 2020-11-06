def fibonancie_nSum(nVal):
    a,b = 1,2
    totSum=0
    while(b<=nVal):
        if b%2==0:
            totSum+=b
        a,b= b,a+b
    return totSum  
    
fibonancie_nSum(4000000) 
