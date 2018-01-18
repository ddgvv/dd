#30th prb

h1,m1=input("Enter first time").split()
h1,m1=int(h1),int(m1)
h2,m2=input("Enter Second time").split()
h2,m2=int(h2),int(m2)
l1=(h1*60)+m1
l2= (h2*60)+m2
tmin=abs(l1-l2)
m = tmin  % 60
hrs = (tmin - m) / 60
print (int(hrs),int(m))
