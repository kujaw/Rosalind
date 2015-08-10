__author__ = 'kujaw'


f = open('rosalind_iprb.txt')
data = list(map(float, f.read().split()))

d = data[0]
h = data[1]
r = data[2]
total = r+h+d

r_r = (r*(r-1))/(total*(total-1))
h_h = (h*(h-1))/(total*(total-1))
d_d = (d*(d-1))/(total*(total-1))
h_r = (h*r)/(total*(total-1))
recessive_probability = r_r + h_h * 0.25 + h_r
dominant_probability = 1 - recessive_probability

print('%.5f' % dominant_probability)

#def firstLaw(k,m,n):
#    N = float(k+m+n)
#    return 1 - ( m*n + .25*m*(m-1) + n*(n-1) ) / ( N*(N-1) )

