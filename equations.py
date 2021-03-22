def power (X, Y):
    try:
        resultPow= 1
        i=0 
        while (i<Y):
            resultPow=resultPow*X
            i=i+1 
        return float('%0.6f' % resultPow)
    except:
        return 0.0


def factorial (X):
    try:
        resultFact= 1
        i=0
        while (i<X):
            resultFact=resultFact*(i+1)
            i=i+1 
        return float('%0.6f' % resultFact)
    except:
        return 0.0


def exponent (X):
    try:
        i=0
        resultExp= 0
        while (i<70):
            resultExp=resultExp+((power(X,i))/factorial(i))
            i=i+1 
        return float('%0.6f' % resultExp)
    except:
        return 0.0


def Ln (X):
    try:
        Yn= X-1.0
        YnPlus1= Yn+2*((X-exponent(Yn))/(X+exponent(Yn))) 
        while (Yn-YnPlus1>0.001 or YnPlus1-Yn>0.001):
            Yn=YnPlus1
            YnPlus1= Yn+2*((X-exponent(Yn))/(X+exponent(Yn)))
        return float('%0.6f' % YnPlus1)
    except:
        return 0.0


def XtimesY(X, Y):
    try:
        resultTimes= 0.0
        if X>0:
            resultTimes=exponent((Y*Ln(X)))
        return float('%0.6f' % resultTimes)
    except:
        return 0.0



def sqrt(X, Y):
    try:
        resultSqrt=0.0
        if Y > 0 :
            X=1/X
            resultSqrt=XtimesY(Y,X)
        return float('%0.6f' % resultSqrt)
    except:
        return 0.0    
    
    
    
def calculate (X):
   try:
       result= (exponent(X))*(XtimesY(7,X))*(XtimesY(X,-1))*(sqrt(X,X))
       return float('%0.6f' % result)      
   except:
        return 0.0                               