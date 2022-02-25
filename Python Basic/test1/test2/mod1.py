import logging as lg
lg.basicConfig(filename = "mod.log",level = lg.INFO,format = "%(asctime)s %(message)s")

               
def fn1(a):
    '''
    this function shows that given number is even or odd
    a - a is an integer
    
    '''
    lg.info("this is the starting of fn1 function")
    try:
        lg.info(str(a)+" is input")
        if a%2 == 0:
            lg.info(str(a)+" is Even")
            return "Even"
        
              
        elif a%2 != 0:
            lg.info(str(a)+" is Odd")
            return "Odd"
               
    except Exception as e:
        lg.error(e+" is the error")
        print(e," invalid input")
 
               
def fn2(a,b):
    '''
    this function shows that Greatest number
    a - a is an integer
    b - b is an integer
    
    '''
    lg.info("this is the starting of fn2 function")
    try:
        lg.info(str(a)+", "+str(b)+" is input")
        if a>b:
            lg.info(str(a)+" is Greater")
            return a
        
              
        elif b>a:
            lg.info(str(b)+" is Greater")
            return b
               
    except Exception as e:
        lg.error(e+" is the error")
        print(e," invalid input")

               
def fn3(a,b):
    '''
    this function shows that Smallest number
    a - a is an integer
    b - b is an integer
    
    '''
    lg.info("this is the starting of fn3 function")
    try:
        lg.info(str(a)+", "+str(b)+" is input")
        if a<b:
            lg.info(str(a)+" is Smallest")
            return a
        
              
        elif b<a:
            lg.info(str(b)+" is Smallest")
            return b
               
    except Exception as e:
        lg.error(e+" is the error")
        print(e," invalid input")
