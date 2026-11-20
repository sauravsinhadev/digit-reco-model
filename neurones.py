

#784 input processs 128 wx+b # output layer 10 output with wx+b
import random

def randominput():
    return random.randint(0,1)



def falseinput(t):
    key=[]

    for i in range(1,t+1):
        key.append(randominput())

    return key
def relu(k):
    return max(0,k)
    
def neurones(input,bias,weight,aactive):
    output=[]
    for bi, b in enumerate(bias):

        cal_one=[]

        for ii, i in enumerate(input):
            value=weight[bi-1][ii]*i
            cal_one.append(value)

        if aactive: 
            output.append(relu(sum(cal_one)+b))  
            continue   

        output.append(sum(cal_one)+b)    

    return output;



v=falseinput(3);

b=falseinput(6)
w=[]

for i in range(1,6):
    wi=w.append(falseinput(3))

print(v)
print(b)
print(w)    

print(neurones(v,b,w,True))





            

