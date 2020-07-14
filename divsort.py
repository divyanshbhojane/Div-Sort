import sys
def countsort(a,n,mn,mx):
	ra=[]
	l=[0]*(mx-mn+1)
	p=0
	for i in range(n):
		l[a[i]-mn]+=1
	for i in range(len(l)):
		for j in range(l[i]):
			ra.append(mn+i)
	return ra

def par(a,l,r):
	i=l-1
	pivot=a[r]
	for j in range(l,r):
		if a[j]<pivot:
			i+=1
			a[j],a[i]=a[i],a[j]
	a[i+1],a[r]=a[r],a[i+1]
	return i+1

def qs(a,l,r):
	if l<r:
		pi=par(a,l,r)

		qs(a,l,pi-1)
		qs(a,pi+1,r)


def merge(l,r):
	a=[]
	li=0
	ri=0
	nl=len(l)
	nr=len(r)
	while li<nl and ri<nr:
		if l[li]<=r[ri]:
			a.append(l[li])
			li+=1
		else:
			a.append(r[ri])
			ri+=1
	if li<nl:
		for i in range(li,nl):
			a.append(l[i])
	elif ri<nr:
		for i in range(ri,nr):
			a.append(r[i])

	return a


def divsort(a):
	#print(a)
	n=len(a)
	inc=True
	dec=True
	finc=0
	fdec=0
	mn=a[0]
	mx=a[0]
	for i in range(1,n):
		mn=min(mn,a[i])
		mx=max(mx,a[i])
		if a[i]>a[i-1]:
			dec=False
			if fdec==0:
				fdec=i
		elif a[i]<a[i-1]:
			inc=False
			if finc==0:
				finc=i

	if inc:
		return a
	
	if dec:
		return a[::-1]
	
	if fdec>n//2:
		l=a[:fdec]
		r=divsort(a[fdec:])
		return merge(l[::-1],r)

	if finc>n//2:
		l=a[:finc]
		r=divsort(a[finc:])
		return merge(l,r)

	lim=1000
	#1000*int=4000 bytes of auxilary space
	#you can increase the lim if you can use more memory
	if mx-mn<lim: 
		return countsort(a,n,mn,mx)

	qs(a,0,n-1)
	return a

def divsortmain(a,reverse=False):
	if reverse:
		return divsort(a)[::-1]
	return divsort(a)

a=[5,7,1,3,8,9,5,4,4,4,56,643,56,7,67,345,3,6554,45,64,54,5,8,8,87,87,10,87,8,3,21,5445]
#a=[1,2,3,4,5,6,7,0,-1,-2,10]
print(a)
print(divsortmain(a,reverse=True))