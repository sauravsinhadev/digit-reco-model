

#784 input processs 128 wx+b # output layer 10 output with wx+b
import random
import json
DIR="./data"
MODAL=DIR+"/model/sak.json"
TRAINDATA=DIR+"/traindata"

def readfile(nameoffile):
    with open(nameoffile,"r") as file:
        return file.read()



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
            value=weight[bi][ii]*i
            cal_one.append(value)

        if aactive: 
            output.append(relu(sum(cal_one)+b))  
            continue   

        output.append(sum(cal_one)+b)    

    return output;



# v=falseinput(3);

# b=falseinput(6)
# w=[]

# for i in range(1,6):
#     wi=w.append(falseinput(3))

# print(v)
# print(b)
# print(w)    

# print(neurones(v,b,w,True))


def genrateoutput(input):
    data=dict(json.loads(readfile(MODAL)))
#{"hidweight":[],"hidenbies":[],"outputbaies":[],"outputweight":[]}
    #print(data)
    hweight=data["layerdata"]["hidweight"]
    print(len(hweight))
    hbais=data["layerdata"]["hidenbies"]
    obais=data["layerdata"]["outputbaies"]
    oweight=data["layerdata"]["outputweight"]

    oinput=neurones(input,hbais,hweight,True)
    output=neurones(oinput,obais,oweight,False)
    print(output)
    cof=max(output)
    ans=output.index(cof)
    ##softmax
    
    return {"confidence":cof*100,"ans":ans}


#print(genrateoutput(falseinput(784)))






b=[[0.3,0.5],[0.5]] #BASIES
w=[[[0.2],[0.8]],[[0.5,0.4]]] #WEIGHT

def training(i,w,b,r_ans,t):
     #INPUT

    
    
    #print(v)
    print(b)
    print(w)    
    
    out=neurones(i,b[0],w[0],True)
    output=neurones(out,b[1],w[1],False)
    loss=(output[0]-r_ans)**2
    print(f"Hiden layer: {out} output layer: {output} and loss: {loss}")

    if not t:
        return 
    outgard=2/output[0]*(output[0]-r_ans)*[(output[0])/w[1][k] for k in w[1]]
    print(outgard)

    

    
    
    
    







training([2],w,b,4,True) 







            

