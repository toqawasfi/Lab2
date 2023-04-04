def fibonacci(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
   
    return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
     if n==0 :
        return 2
     elif n==1:
        return 1
     return lucas(n-1)+lucas(n-2)
     
def sum_series(n,first=0,second=1):
    if first ==0 and second == 1:
        return fibonacci(n)
    
    elif first ==2 and second ==1:
     return lucas(n)
    
    return fibonacci(n) +lucas(n)
    
