from scapy.all import *
import random
import numpy as np
import hashlib
from datetime import datetime
from sklearn.metrics import f1_score
import json
import string
import sys


table = np.zeros((524288,), dtype=int) #tabela inicializada com 0
pipesTable = np.array([np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,), np.zeros(524288,)], dtype=int)  #tabela com hash tables (tabela dos pipes)   ###CONTADOR
coordinatorVariable = np.zeros((524288,), dtype=int) #coordenador (plano de controle)
switchCoordinator = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
coordinatorCheck = np.zeros((524288,), dtype=int)
todosValoresHash = np.zeros((524288,),dtype=int)

nPipes = 2
globalLimit = 20000
switchLimit = 10000
hash = 0
pipeLimitArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hh = 0
contadorCoordenador = 0
hash1 = 0
cont = 0
dict = {}

pipeLimit = int(switchLimit/nPipes)


#determines the limit of each pipe
def divisionLimitPipes():

    pipeLimitRest = (switchLimit % nPipes)

    if(pipeLimitRest==0):
        for i in range(len(pipeLimitArray)):
            pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((nPipes==2) and (pipeLimitRest==1)):
        pipeLimitArray[0] = int(switchLimit/nPipes)
        pipeLimitArray[1] = int(switchLimit/nPipes) + 1 

    elif((nPipes==4) and (pipeLimitRest==1)):
        for i in range(len(pipeLimitArray)):
            if(i==3):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)   

    elif((nPipes==4) and (pipeLimitRest==2)):   
        for i in range(len(pipeLimitArray)):
            if(i>=2):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((nPipes==4) and (pipeLimitRest==3)):   
        for i in range(len(pipeLimitArray)):
            if(i>=1):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((nPipes==8) and (pipeLimitRest==1)):
        for i in range(len(pipeLimitArray)):
            if(i==7):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((nPipes==8) and (pipeLimitRest==2)):
        for i in range(len(pipeLimitArray)):
            if(i>=6):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((nPipes==8) and (pipeLimitRest==3)):
        for i in range(len(pipeLimitArray)):
            if(i>=5):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)    

    elif((nPipes==8) and (pipeLimitRest==4)):
        for i in range(len(pipeLimitArray)):
            if(i>=4):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((nPipes==8) and (pipeLimitRest==5)):
        for i in range(len(pipeLimitArray)):
            if(i>=3):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
                
    elif((nPipes==8) and (pipeLimitRest==6)):
        for i in range(len(pipeLimitArray)):
            if(i>=2):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
                
    elif((nPipes==8) and (pipeLimitRest==7)):
        for i in range(len(pipeLimitArray)):
            if(i>=1):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif(nPipes==16):
        divisionLimitPipes2()

#determines the limit of each pipe
def divisionLimitPipes2():

    pipeLimitRest = (switchLimit % nPipes)


    if(pipeLimitRest==0):
        for i in range(len(pipeLimitArray)):
            pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((pipeLimitRest==1)):
        for i in range(len(pipeLimitArray)):
            if(i==15):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)   

    elif((pipeLimitRest==2)):   
        for i in range(len(pipeLimitArray)):
            if(i>=14):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==3)):
        for i in range(len(pipeLimitArray)):
            if(i>=13):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)   

    elif((pipeLimitRest==4)):   
        for i in range(len(pipeLimitArray)):
            if(i>=12):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==5)):
        for i in range(len(pipeLimitArray)):
            if(i>=11):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)   

    elif((pipeLimitRest==6)):   
        for i in range(len(pipeLimitArray)):
            if(i>=10):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==7)):
        for i in range(len(pipeLimitArray)):
            if(i>=9):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)   

    elif((pipeLimitRest==8)):   
        for i in range(len(pipeLimitArray)):
            if(i>=8):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==9)):
        for i in range(len(pipeLimitArray)):
            if(i>=7):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)   

    elif((pipeLimitRest==10)):   
        for i in range(len(pipeLimitArray)):
            if(i>=6):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==11)):   
        for i in range(len(pipeLimitArray)):
            if(i>=5):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==12)):   
        for i in range(len(pipeLimitArray)):
            if(i>=4):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((pipeLimitRest==13)):   
        for i in range(len(pipeLimitArray)):
            if(i>=3):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

    elif((pipeLimitRest==14)):   
        for i in range(len(pipeLimitArray)):
            if(i>=2):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)
    
    elif((pipeLimitRest==15)):   
        for i in range(len(pipeLimitArray)):
            if(i>=1):
                pipeLimitArray[i] = int(switchLimit/nPipes) + 1
            else:
                pipeLimitArray[i] = int(switchLimit/nPipes)

#create the hash and get the source and destination of the stream
def createHash(ip,x):

    divisionLimitPipes()
    randomPipe = random.randint(0,(nPipes-1))
    global hash
    
    hash = int(hashlib.md5((str(ip[x])).encode()).hexdigest(), 16) % 524288
    
    #packet counter in table at hash position
    pipesTable[randomPipe][hash] = pipesTable[randomPipe][hash] + 1
    todosValoresHash[hash] = todosValoresHash[hash] + 1

    checkLimit(randomPipe)

      
def checkLimit(randomPipe):

    if (pipesTable[randomPipe][hash] == pipeLimitArray[randomPipe]):
        coordinator(hash,randomPipe) #coordinator(hash,pipeLimit) 
        switchCoordinator[randomPipe] = switchCoordinator[randomPipe] + pipesTable[randomPipe][hash]
        pipesTable[randomPipe][hash] = 0      
        if (switchCoordinator[randomPipe] >= switchLimit):
            switchCoordinator[randomPipe] = 0

        now = datetime.now()
        timestamp = datetime.timestamp(now)
        date_time = datetime.fromtimestamp(timestamp)
        str_time = date_time.strftime("%I:%M:%S, ")
        with open ("arquivoHH.txt","a",newline="") as arquivo:
            arquivo.writelines ([str(hash), " ", str(randomPipe)," ", str_time+ '\n'])
            arquivo.close()
     
  
       
def coordinator(hash,randomPipe):

    global contadorCoordenador

    coordinatorVariable[hash] = coordinatorVariable[hash] + pipesTable[randomPipe][hash]
    contadorCoordenador = contadorCoordenador + 1
    #print("Chave enviada para o COORDENADOR")
    #print("Hash: ", hash)
    #print("Limite por PIPE: ",pipeLimitArray)
    #print("Valor armazenado por enquanto no Coordenador -> ", coordinatorVariable[hash])
    #print("\n")

     
def pipesCheck():

    y = 0
    a = 0
    x = 0
    var = 0
    reachedValue = 0
    global hh
    total = 0

    
    for a in range(len(coordinatorVariable)):
        if(coordinatorVariable[a]!= 0):
            coordinatorCheck[y] = a 
            y = y+1

    while(coordinatorCheck[x]!=0):
        hash = coordinatorCheck[x]
        for var in range(nPipes):
            reachedValue = reachedValue + pipesTable[var][hash]
        
        if((reachedValue + coordinatorVariable[hash]) >= switchLimit):                     
            hh = hh + 1

            now = datetime.now()
            timestamp = datetime.timestamp(now)
            date_time = datetime.fromtimestamp(timestamp)
            str_time = date_time.strftime("%I:%M:%S, ")
            with open ("arquivoHH.txt","a") as arquivo:
                #arquivo.write(str_time)
                arquivo.writelines (["IIII ", str(hash), " ", str(total)," ", str_time + '\n'])
                arquivo.close()   
        reachedValue = 0
        x = x+1     

#creating the hash in the dict
def createHashDict(ip2,x):
    global hash1
    global cont

    cont = 0
    if (ip2[x] in dict):     
        cont = (dict.get(ip2[x]))
        cont = cont + 1
        dict[ip2[x]] = (cont)
    else:
        dict[ip2[x]] = (1)
    x = x+1

#check hash in dict
def checkLimitDict(ip2):

    i = 0
    hh=0
    j=0
    x=0
    
    array=list(dict.values())

    for x in range(len(array)):
        if(array[x]>=switchLimit):
            hh = hh+1

    return array

def main():

    print("Codigo iniciado")
    now = datetime.now()
    divisionLimitPipes()     
    #sniff(offline="caida18-16x.pcap", filter = "ip and tcp", prn=createHash, store = 0) ###"caida18-16x.pcap"

    arquivo = open("srcIPs.txt", "r") #610919
    ip = arquivo.readlines()
    arquivo.close()
    for x in range(len(ip)):
        createHash(ip,x)
    
    pipesCheck()
    print("Quantidade de HH identificados -> ",hh)


    arquivo2 = open("srcIPs.txt", "r") 
    ip2 = arquivo2.readlines()
    arquivo2.close()
    for x in range(len(ip2)):
        createHashDict(ip2,x)
    array=checkLimitDict(ip2)

    vp = 0
    vn = 0
    fp = 0
    fn = 0


    for chave in dict.keys():
        hash = int(hashlib.md5((str(chave)).encode()).hexdigest(), 16) % 524288
        
        if((dict[chave]>=switchLimit) and (todosValoresHash[hash]>=switchLimit)):
            vp = vp +1
        if((dict[chave]<=switchLimit) and (todosValoresHash[hash]<=switchLimit)):
            vn = vn+1
        if((dict[chave]<=switchLimit) and (todosValoresHash[hash]>=switchLimit)):
            fp = fp +1
        if((dict[chave]>=switchLimit) and (todosValoresHash[hash]<=switchLimit)):
            fn=fn+1 

    print("\n")
    print("VP=",vp)
    print("VN=",vn)
    print("FP=",fp)
    print("FN=",fn)

    precision = vp/hh 
    recall = vp / (vp + fn)
    f1Score = (2 * (precision * recall)) / (precision + recall) 

    print("precision",precision)
    print("recall",recall)
    print("f1Score",f1Score)
    print("--------------\n")
    print("contadorCoordenador = ",contadorCoordenador)

   
if __name__ == '__main__':
    main()   

