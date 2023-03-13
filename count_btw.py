#input from user as per instructions
n=int(input("enter the number of elements in array: "))
arr=[]
for j in range(0,n):
     x=int(input("enter the integer: "))
     arr.append(x)
low=[]
high=[]
q=int(input("enter elemnets in low: "))
for i in range(0,q):
     l=int(input("enter integer in low: "))
     low.append(l)

q=int(input("enter elemnets in high: "))
for i in range(0,q):
     h=int(input("enter integer in high: "))
     high.append(h)

#code to find the array elements are inbetween the given range
output=[]
lcount=0
hcount=0
#check range of array low
for k in range(0,n):
     if (arr[k]>= low[0]) and (arr[k]<=low[q-1]):
          lcount+=1
output.append(lcount)


#check range of array high
for k in range(0,n):
     if (arr[k]>=high[0]) and (arr[k]<=high[q-1]):
          hcount+=1
output.append(hcount)

print(output)