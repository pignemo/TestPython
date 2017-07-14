# 
# Monte Carlo valuation of European call options with NumPy (log version)
# mcs_full_vector_numpy.py
#
import math
from numpy import *
from time import time

random.seed(20000)
t0=time()

# Parameters
S0=100. # initial value
K=105. # strike price
T=1.0 # maturity
r=0.05 # riskless short rate
sigma=0.2 # volatility
M=50 # number of time steps
dt=T/M # length of time interval
I=250000 # number of paths

S=S0*exp(cumsum((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*random.standard_normal((M+1,I)), axis=0))
S[0]=S0

C0=math.exp(-r*T)*sum(maximum(S[-1]-K,0))/I

tnp2=time()-t0
print "European Option Value %7.3f" % C0
print "Duration in Seconds   %7.3f" % tnp2




