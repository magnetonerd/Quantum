from pylab import *       #plot, show,xlim
from numpy import *       #linspace
from gaussquad import *   #gaussxwab
from hermitepoly import * #H
from qhowf import *       #psi

"""
There are a few things going on in this code. First
it will do a graph of multiple functions on the same
graph. Then it will Show a graph of a single 
calculated. Finally, it prints out the root mean
square of a quantum harmonic oscillator.
"""

"""
The next two functions are used to split up the 
function of the harmonic oscillator over the 
intervals (-inf,0] and [0,inf). Also, in order
to be able to integrate over on infinite range
a transformation has to be performed. For the 
neg interval x = tan(-z), and for the pos
interval x = tan(z).
"""
def neg_f(n,z):
    return pos_f(n,-z)

def pos_f(n,z):
    return tan(z)**2*psi(n,tan(z))**2/cos(z)**2

"""
Plotting the Hermite Polynomial for the values of
n = 0,1,2,3. This is done over the range x = [-4,4].
"""

for k in range(0,4):
    x = linspace(-4,4,100)
    plot(x,H(k,x))
    xlim(-4.0,4.0)

show() #Display the graph

"""
Plotting the Hermite Polynomial for n = 30 over
the range x = [-10,10].
"""

y = linspace(-10,10,100)
plot(y,H(30,y))
show()

"""
Calculating the root mean square of the position of a
quantum harmonic oscillator. Since we are considering
the infinite range of values of x we will need to
split the integral up into to intervals. The neg values
correspond to (-inf,0] and pos values correspond to the
interval [0,inf). With the transformation the intervals
become [-pi/2,0] and [0,pi/2]
"""

N = 100        #Number of steps in the integration
n = 5          #The energy level of the oscillator
neg_a = -pi/2  #Negative lower bound
neg_b = 0.0    #Negative upper bound
pos_a = neg_b  #Positive lower bound
pos_b = -neg_a #Positive upper bound

neg_x,neg_w = gaussxwab(N,neg_a,neg_b) #Getting the sample points and weights for the negative interval

"""
The integral:
   ___ 0
  |             /          1                                            \ 2
  |   tan(-z)^2 |_____________________ exp(-tan(-z)^2 /2) H_n (tan(-z))  |      dz
  |             |sqrt(2^n n! sqrt(pi))                                   |    _______
  |             \                                                       /     cos(-z)^2
___ -pi/2
"""

neg_total = 0.0 #Initializing the negative integral
for i in range(1,N):
    neg_total += neg_w[i]*neg_f(n,neg_x[i])

pos_x,pos_w = gaussxwab(N,pos_a,pos_b) #Getting the sample points and weights for the positive interval


"""
The integral:
   ___ pi/2
  |            /          1                                          \ 2
  |   tan(z)^2 |_____________________ exp(-tan(z)^2 /2) H_n (tan(z))  |       dz
  |            |sqrt(2^n n! sqrt(pi))                                 |    ________
  |            \                                                     /     cos(z)^2
___ 0
"""

pos_total = 0.0 #Initializing the positive integral
for i in range(1,N):
    pos_total += pos_w[i]*pos_f(n,pos_x[i])

#The Root Mean Square Value
RMS = sqrt(pos_total+neg_total) #Recombining the two inervals and taking there square root
print RMS

#Prints a value of about 2.345...
