'''
This module uses core Python to accomplish the goal of
geometric collision detection. It uses conventional axes,
so rendering directly from this module will be inverted.
Points are defined as tuples (x,y) or lists [x,y].
Lines are defined by two points, polygons by three or more.
Circles are defined by [(x,y),r] where (x,y) is the center
and r is the radius.
If an incorrect parameter is passed to a function,
such as a line in the place of a point, it will return
'None'.
'''


from math import atan
def midpoint(a):
	'''
	Returns the midpoint of a line segment.
	'''
	if len(a) != 2: return
	return ((a[0][0]+a[1][0])/2,(a[0][1]+a[1][1])/2)

#================================================================
def ppDistance(a,b):
	'''
	Returns the distance between two points, <a> and <b>.
	'''
	return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**.5

#================================================================
def plDistance(a,b):
	'''
	Finding shortest distance between a point <a> and a
	line <b>. Doesn't check if the line extends to the
	point of	closest approach.
	 |(x2 - x1)(y1 - y0) - (x1 - x0)*(y2 - y1) |
	---------------------------------------------
	      sqrt((x2 - x1)^2 + (y2 - y1)^2)			'''
	if len(b) != 2: return
	return abs((b[1][0]-b[0][0])*(b[0][1]-a[1]) -			\
		(b[0][0]-a[0])*(b[1][1]-b[0][1]))/						\
	(((b[1][0] - b[0][0])**2 + (b[1][1] - b[0][1])**2)**.5)

#================================================================
def onLine(a,b):
	'''
	Checks if point <a> is on line segment defined by <b>.
	'''
	if len(b) != 2: return
	if not\
	(a[0]>=min(b[0][0],b[1][0]) and\
	a[0]<=max(b[0][0],b[1][0]) and\
	a[1]>=min(b[0][1],b[1][1]) and\
	a[1]<=max(b[0][1],b[1][1])): return False
	
	if b[0][0] == b[1][0]:
		return a[0] == b[0][0]
	if b[0][1] == b[1][1]:
		return a[1] == b[0][1]
	
	m = float(b[0][1] - b[1][1])/float(b[0][0] - b[1][0])
	return m*float(a[0] - b[0][0]) + b[0][1] - a[1] == 0

#================================================================
def belowLine(a,b):
	'''
	To be used explicity with 'withinTriangle' because of a
	misnomer. It checks if a point is between a line
	segment and the x-axis, not the y-axis. It can be used for
	that purpose if the x and y coordinates are inverted.
	'''
	if len(b) != 2: return
	if onLine(a,b): return True
	#If the x values are exceeded, then it cannot be
	#below the line.
	x1,y1 = float(b[0][0]),float(b[0][1])
	x2,y2 = float(b[1][0]),float(b[1][1])
	if a[0] > max(x1,x2) or\
		a[0] < min(x1,x2): return False
	#If it's below the least value, it is below.
	if a[1] < min(y1,y2): return True
	#If x values are the same.
	if x1 == x2:
		return a[0] <= x1
	#Simpler case if y values are the same.
	if y1 == y2:
		return a[0] == x1
	#Calculations for the x value of the line.
	m = (y1-y2)/(x1-x2)
	y = m*(a[0]-x1) + y1
	return a[0] <= y

#================================================================
def withinTriangle(a,b):
	'''
	Checks whether <a> is within the triangle defined by <b>.
	'''
	if len(b) != 3: return
	if a in b: return True
	check = 0
	for i in range(len(b)):
		if belowLine(a,[b[i],b[i-1]]):
			check += 1
	if check == 1: return True
	return False

#================================================================
def withinPolygon(a,b):
	'''
	'''
	if len(b) < 3: return
	if len(b) < 4: return withinTriangle(a,b)
	if not checkPoly(b): return
	center = centerPoly(b)
	within = False
	for i in range(len(b)):
		within = withinTriangle(a,[b[i],b[i-1],b[i-2]])
		if within: break
	return within

#================================================================
def withinCircle(a,b):
	'''
	Checks whether the point <a> is within the circle
	defined by tuple <b>.
	'''
	if len(b) != 2: return
	if len(b[0]) != 2: return
	return ppDistance(a,b[0]) <= b[1]

#================================================================
def centerPoly(a):
	'''
	Returns the area of a closed, non-self-intersecting
	polygon whose vertices are defined clockwise (or
	counter-clockwise) by <a>.
	'''
	if len(a) < 3: return
	if not checkPoly(a): return
	x, y = [i[0] for i in a], [i[1] for i in a]
	cx,cy = 0.0,0.0
	area = areaPoly(a)
	for i in range(len(x)):
		cx += (x[i]+x[i-1])*(x[i-1]*y[i]-x[i]*y[i-1])
		cy += (y[i]+y[i-1])*(x[i-1]*y[i]-x[i]*y[i-1])
	return cx/(6*area), cy/(6*area)

#================================================================
def areaPoly(a):
	'''
	Returns the area enclosed by a close, non-self-
	intersecting polygon whose verticies are defined
	clockwise (or counterclockwise) by <a>.
	'''
	if len(a) < 3: return
	xs, ys = [i[0] for i in a], [i[1] for i in a]
	area = 0
	for i in range(len(xs)):
		area += (xs[i]+xs[i-1])*(ys[i-1]-ys[i])
	return abs(area/2)

#================================================================
def angle(a,b):
	'''
   Returns the smallest positive angle between two lines.
   Accounts for undefined and zero slopes. Doesn't check
   for intersection.
             m1 - m2
   tan a =  ---------
            1 - m1*m2	'''
	if len(a) != 2 or len(b) != 2: return
	#Assigning variables to simplify calculation.
	a_x,a_y = float(a[0][0]), float(a[0][1])
	a_x_2,a_y_2 = float(a[1][0]), float(a[1][1])
	b_x,b_y = float(b[0][0]), float(b[0][1])
	b_x_2,b_y_2 = float(b[1][0]), float(b[1][1])
	#Avoiding undefined slope problem.
	if a_x == a_x_2:
		if b_x == b_x_2:
			return
		return abs(atan((b_y-b_y_2)/(b_x-b_x_2)))
	if b_x == b_x_2:
		if a_x == a_x_2:
			return
		return abs(atan((a_y-a_y_2)/(a_x-a_x_2)))

	m_a = (a_y-a_y_2)/(a_x-a_x_2)
	m_b = (b_y-b_y_2)/(b_x-b_x_2)
	#Accounting for 0 slope, return angle of line to horizontal.
	if m_a == 0:
		if m_b == 0:
			return
		return abs(atan(m_b))
	if m_b == 0:
		if m_a == 0:
			return
		return abs(atan(m_a))

	return abs(atan((m_b-m_a)/(1+m_a*m_b)))

#================================================================
def intersect(a,b):
	'''
	Returns the point of intersection of two line segments.
	Checks that the point exists on the lines.
	Accounts for undefined slope.
	'''
	if len(a) != 2 or len(b) != 2: return
	#Assigning variables to simplify calculation.
	ax,ay = float(a[0][0]), float(a[0][1])
	ax2,ay2 = float(a[1][0]), float(a[1][1])
	bx,by = float(b[0][0]), float(b[0][1])
	bx2,by2 = float(b[1][0]), float(b[1][1])
	#Avoiding undefined slope problem.
	if ax-ax2 == 0:
		if bx-bx2 == 0:
			return
		point = ax, int(round((ax-bx)*(by-by2)/(bx-bx2)+by))
		if onLine(point,a) and onLine(point,b): return point
		return
	#Required because each can cause a problem,
	#so they cannot be checked independently.
	if bx-bx2 == 0:
		if ax-ax2 == 0:
			return
		point = bx,int(round((bx-ax)*(ay-ay2)/(ax-ax2)+ay))
		if onLine(point,a) and onLine(point,b): return point
		return
	#Math.
	ma = (ay-ay2)/(ax-ax2)
	mb = (by-by2)/(bx-bx2)
	if ma == mb: return
	#More intense math.
	x = (by - ay + ma * ax - mb * bx) / (ma - mb)
	y = (ma*(bx*mb - by) - mb*(ax*ma - ay)) / (mb - ma)
	#Cannot escape the two line segments.
	if (onLine((x,y),a) and onLine((x,y),b)):
		return int(round(x)),int(round(y))
	else:
		print "This is where.",x,y
		return
	return

#================================================================
def checkPoly(a):
	'''
	Checks to ensure that <p> is not self-intersecting.
	'''
	if len(a) < 3: return False
	if len(a) < 4: return True
	#Check for line intersections. Avoids the adjacent
	#lines because there will be an intersection.
	lin = [[a[i-1],a[i]] for i in range(len(a))]
	l = len(lin)
	for i in range(l):
		for j in range(l):
			print i, j, lin[i],lin[j]
			print intersect(lin[i],lin[j])
			if abs(j-i) <= 1: continue
			if (i,j) == (0,l) or (j,i) == (0,l): continue
			#if abs(j%l-i) == 1: continue
			inter = intersect(lin[i],lin[j])
			if inter:
				if not (inter in a):
					return False
	return True
  
  def isEven(n):
        #if n % 2 == 0: return True
        return n % 2 == 0

def isPrime(n):
	#if a in primesErat(a+1): return True
	if n == 1: return False
	elif n == 2 or n == 3: return True
	elif n%2 == 0 or n%3 == 0: return False
	elif n < 9: return True
	else:
		for i in range(5,int(n**.5)+1,6):
			if n%i == 0: 
				return False
				break
			if n%(i+2) == 0: 
				return False
				break
	return True

def primesErat(n):
	sieve=[True]*(n+1)
	for i in range(2,n+1):
		if sieve[i]: sieve[2*i::i]=[False]*((n/i)-1)
	return [x for x in range(2,n) if sieve[x]]

def primesEratFile(n):
	import os
	f = open("primesEratFileDat","w+")
	length = len(str(n+1))
	for i in range(n+1):
		f.write('1')
	for i in range(2,n+1):
		f.seek(i,0)
		if f.read(1) == '1':
			for j in range(2*i,n+1,i):
				f.seek(j,0)
				f.write('0')
	f.seek(2,0)
	primes = []
	for i in range(2,n+1):
		f.seek(i,0)
		if f.read(1) == '1':
			primes.append(i)
	f.close()
	os.remove("primesEratFileDat")
	return primes

def primesSund(n):
	sieve=[True]*(n//2)
	for i in range(1,n//2):
		if sieve[i] and i < n//6: sieve[3*i+1::2*i+1]=[False]*(((n//2)//(2*i+1))-1+(n//2)%(2*i+1))
	return [2*x+1 for x in range(1,n//2) if sieve[x]]

def primeFactorize(n):
	primelist = primesErat(long(n)+1)
	divList = []
	for i in primelist:
		if i > n: break
		times = 0
		if n%i==0:
			while n%i==0:
				n = n/i
				times +=1
			divList.append([i,times])
	return divList

def factorize(n):
	primefacts = primeFactorize(n)
	primefactors = [i[0] for i in primefacts for j in xrange(i[1])]
	
	return [1] + inclusivePermute(primefactors)

def factorize2(n):
	primefactors = [i[0] for i in n for j in xrange(i[1])]
	return [1] + inclusivePermute(primefactors)

def inclusivePermute(a):
	perm = list(a)
	if len(a) > 2:
		t = a.pop(0)
		toperm = inclusivePermute(a)
		for i in toperm:
			perm.append(i)
			perm.append(t*i)
	elif len(a) == 2: perm.append(perm[0]*perm[1])
	retlist = []
	for i in perm:
		if not i in retlist: retlist.append(i)
	return sorted(retlist)

def fibIt(inp):
	a,b = 1,1
	for i in range(2,inp+1):
		b,a = a,b+a
	return a

'''
def fibCalc(inp):
	GR = (1+5**.5)/2.0
	return long((GR**inp - (1/GR)**inp)/(5**.5))
'''

def factorial(n):
	fact = 1
	for i in range(2,n+1):
		fact *= i
	return fact

#=================================== FINANCIAL (NON-GEOMETRIC) MATH ===================================

# Valuation of European call options in Black-Scholes-Merton model
# incl. Vega function and implied volatility estimation.

# Analytical Black-Scholes-Merton (BSM) Formula

def bsm_call_value(S0, K, T, r, sigma):
''' Valuation of European call option in BSM model.
    Analytical formula.
    Parameters
    ==========
    S0 : float
    initial stock/index level
    K : float
    strike price
    T : float
    maturity date (in year fractions)
    r : float
    constant risk-free short rate
    sigma : float
    volatility factor in diffusion term
    Returns
    =======
    value : float
    present value of the European call option
'''

	from math import log, sqrt, exp
	from scipy import stats
	S0 = float(S0)
	d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
	d2 = (log(S0 / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
	value = (S0 * stats.norm.cdf(d1, 0.0, 1.0)
	K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))

	# stats.norm.cdf —> cumulative distribution function
	# for normal distribution
	return value

# Vega function
def bsm_vega(S0, K, T, r, sigma):
''' Vega of European option in BSM model.
    Parameters
    ==========
    S0 : float
    initial stock/index level
    K : float
    strike price
    T : float
    maturity date (in year fractions)
    r : float
    constant risk-free short rate
    sigma : float
    volatility factor in diffusion term
    Returns
    =======
    vega : float
    partial derivative of BSM formula with respect
    to sigma, i.e. Vega
    www.it-ebooks.info
'''

	from math import log, sqrt
	from scipy import stats
	S0 = float(S0)
	d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T / (sigma * sqrt(T))
	vega = S0 * stats.norm.cdf(d1, 0.0, 1.0) * sqrt(T)
	return vega
	      
# Implied volatility function
def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est, it=100):
''' Implied volatility of European call option in BSM model.
    Parameters
    ==========
    S0 : float
    initial stock/index level
    K : float
    strike price
    T : float
    maturity date (in year fractions)
    r : float
    constant risk-free short rate
    sigma_est : float
    estimate of impl. volatility
    it : integer
    number of iterations
    Returns
    =======
    simga_est : float
    numerically estimated implied volatility
'''
	      
	for i in range(it):
	sigma_est -= ((bsm_call_value(S0, K, T, r, sigma_est) - C0) / bsm_vega(S0, K, T, r, sigma_est))
	return sigma_est
