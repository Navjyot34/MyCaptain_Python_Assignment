#Fibonacci Numbers

nterms=int(input("how many terms ?"))
n1=0
n2=1
start=0
if nterms<=0:
    print("More than zerooo")
elif nterms==1:
    print("Fibonacci Number",nterms,":")
    print (n1)
else:
    print("Fibonacci:")
    while start<nterms:
        print (n1)
        i= n1 + n2
        n1 = n2
        n2 = i
        start += 1
        

        
            






    

    


    
    
    
    

