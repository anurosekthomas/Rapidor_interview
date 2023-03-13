#function to find the given strings Pangram or not
def isPangram(string,n):
    output=""
    for j in range(0,n):
        #difine hash table to check the characters
        dict={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        for i in string[j]:
            if i in dict:
                dict[i]+=1
        if 0 in dict.values():
            output=output+"0"
        else:
           output=output+"1"
    return(output)

#function calling code
string=[]
#input from userend
n = int(input("number of strings in array"))
for m in range(0,n):
    st=str(input("enter string"))
    string.append(st)
#call and print function
print(isPangram(string,n))