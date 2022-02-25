import logging as lg
lg.basicConfig(filename = "mo1.log",level = lg.INFO,format = "%(asctime)s %(message)s")


def even_number(a):
    '''
    this function is use to print all the even numbers from 0 to a
    a -  is an integer
    
    '''
    
    lg.info("this is a starting of function")
    try:
        lg.info("check weather input is integer or not")
        lg.info('you enter :'+str(a))
        for i in range(a+1):
            if i%2 == 0:
                print(i,end = " ")
        lg.info("printing even numbers")
    except Exception as e:
        lg.error(str(e)+" : not integer in input")
        return e," : not integer in input"
    finally:
        lg.info("this function is closed")
        pass