"""
Calculating the nth Hermite Polynomial H(x) using
the recursive definition of Hermite Polynomials. 
"""
def H(n,x):
    H0 = 1 #Initializing H_0
    H1 = 2*x #Initializing H_1
    for k in range(1,n):
        H0,H1 = H1,2*x*H1-2*k*H0 #Recursive call of definition

    return H1 #The nth Hermite Polynomial
