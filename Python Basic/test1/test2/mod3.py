import logging as lg
lg.basicConfig(filename = "mod.log",level = lg.INFO,format = "%(asctime)s %(message)s")

               
def fn31(a,b):
    '''
    this function shows the sum 
    a - a is an integer
    b - b is an integer
    
    '''
    lg.info("this is the starting of fn31 function")
    try:
        lg.info(str(a)+", "+str(b)+" is input")
        if type(a) and type(b) == int:
            lg.info(str(a+b)+" is the sum")
            return a+b
             
    except Exception as e:
        lg.error(e+" is the error")
        print(e," invalid input")
 
               
def fn32(a,b):
    '''
    this function shows the multiplication 
    a - a is an integer
    b - b is an integer
    
    '''
    lg.info("this is the starting of fn32 function")
    try:
        lg.info(str(a)+", "+str(b)+" is input")
        if type(a) and type(b) == int:
            lg.info(str(a*b)+" is the multiplication")
            return a*b
               
    except Exception as e:
        lg.error(e+" is the error")
        print(e," invalid input")

               
def fn33(a,b):
    '''
    this function shows the division
    a - a is an integer
    b - b is an integer
    
    '''
    lg.info("this is the starting of fn33 function")
    try:
        lg.info(str(a)+", "+str(b)+" is input")
        if type(a) and type(b) == int:
            lg.info(str(a/b)+" is the Division")
            return a/b
               
    except Exception as e:
        lg.error(e+" is the error")
        print(e," invalid input")
