#moadele daraje 2#
def m():
    print("calculate >>> a*(x)**2+(b*x)+c")

    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=int(input("Enter c:"))

    delta=(b**2)-(4*a*c)

    if a==0:
        print("EROR")


    elif delta<0:
        print('NO ANSWER')
        print("DELTA IS:",delta)
            
    elif delta>0:
        x=(-b+(delta)**0.5)/(2*a)
        y=(-b-(delta)**0.5)/(2*a)
        print("THE ANSWERS ARE:",x,'and',y)
        print("DELTA IS:",delta)
        
    else:
        z=(-b)/(2*a)
        print('THE ANSWER IS:',z)
        print("DELTA IS:",delta)

    print('Done')


    input("Press any key...")


    if int(input('Press 1 to continue":')==1:
           def m()
    else int(input('Press 0 to exit":')==0:
             
       input("Press any key...")
    return()

m()



       
