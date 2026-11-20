#modal have 28*28 =784 then hidden layer would be 128 and output layer would be 10
#784*128=100352 128 basis weight and 128*10 =1280 10 basis

import json
import os
import random
datastructure={"layershape":{"hidweight":[784,120],"hidenbies":[128,1],"outputbaies":[10,1],"outputweight":[128,10]},"layerdata":{"hidweight":[],"hidenbies":[],"outputbaies":[],"outputweight":[]}}

DIR="./data"
MODAL=DIR+"/model/sak.json"
TRAINDATA=DIR+"/traindata"

def random_weight():
    return random.randint(-50, 50) / 1000.0


def random_bias():
    return random.randint(-10, 10) / 1000.0




os.makedirs(os.path.dirname(MODAL),exist_ok=True)
os.makedirs(os.path.dirname(TRAINDATA),exist_ok=True)

def readfile(nameoffile):
    with open(nameoffile,"r") as file:
        return file.read()

def updatefile(nameoffile,data):

    with open(nameoffile,"w") as file:

        if isinstance(data,(dict,list)):
          json.dump(data,file)
        else:
           file.write(str(data)) 



updatefile(MODAL,datastructure)

getstr=dict(json.loads(readfile(MODAL)))

for key  in getstr["layershape"]:
    for i in range(1,int(getstr["layershape"][key][0])):
         
         if "b" in key:
             getstr["layerdata"][key].append(random_bias())
         else:
             keyss=[]
             for k in range(1,getstr["layershape"][key][1]+1):
                keyss.append(random_weight())
             getstr["layerdata"][key].append(keyss)
  

print(getstr)
updatefile(MODAL,getstr)             


            



 
