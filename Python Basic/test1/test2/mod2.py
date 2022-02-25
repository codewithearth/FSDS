import logging as lg
lg.basicConfig(filename = "mod.log",level = lg.INFO,format = "%(asctime)s %(message)s")

               
def fn21(a):
    '''
    this function shows the area of square
    a - a is an integer
    
    '''
    lg.info("this is the starting of fn21 function")
    try:
        lg.info(str(a)+" is input")
        if type(a) == int:
            lg.info(str(a*a)+" is area of Square")
            return a*a
 
    except Exception as e:
        lg.error(e+" is the error")
        print(e," invalid input")
 
               
def fn22(a):
    '''
    this function shows the area of circle
    a - a is an integer
    
    '''
    lg.info("this is the starting of fn22 function")
    try:
        lg.info(str(a)+" is input")
        if type(a) == int:
            c = (22/7)*a*a
            lg.info(str(c)+" is the area of circle")
            return c
        
    except Exception as e:
        lg.error(e+" is the error")
        print(e," invalid input")

               
def fn23(a,b):
    '''
    this function shows the area of rectangle
    a - a is an integer
    b - b is an integer
    
    '''
    lg.info("this is the starting of fn23 function")
    try:
        lg.info(str(a)+", "+str(b)+" is input")
        if type(a) and type(b) == int:
            lg.info(str(a*b)+" is the area of rectangle")
            return a*b
        
    except Exception as e:
        lg.error(e+" is the error")
        print(e," invalid input")
