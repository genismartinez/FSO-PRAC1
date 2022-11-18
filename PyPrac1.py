#! /usr/bin/env python3
import sys
import getopt
import os
from os.path import exists

fil=0
cols=0
portSize=0
f=None
minFil=10
maxFil=120

minCol=8
maxCol=36

minPort=8

minPort=8
temp=None
posFilaPal=None
posColPal=None
midaPaleta=0
posFilaPil=0
posColPil=0
velFil=-2
velCol=-2
prueba1=3

def comprobarValores(fil,cols,portSize,posFilaPal,posColPal,midaPaleta,posFilaPil,posColPil,velFil,velCol):
    contador=10
    if ((fil > 120 ) or (fil<10)):
        fil=input("Introdueix les files de nou (10-120): " )
        contador-=1
    if ((cols > 36) or (cols<10)):
        cols=input("Introdueix les columnes de nou (10-36): ")
        contador-=1
    maxPort=fil-1
    if((portSize>maxPort)or(portSize<8)):
        contador-=1
        portSize=input("Introdueix la mida de la porteria de nou (8-numFil-1): ")
    if ((posFilaPal<2) or (posFilaPal>118)):
        contador-=1
        posFilaPal=input("Introdueixi la fila on hi ha paleta de nou (2-118): ") 
    if ((posColPal<2) or (posColPal>35)):
        contador-=1
        posColPal=input("Introdueixi la columna on hi ha paleta de nou (2-35): ")
    if ((midaPaleta<2) or (midaPaleta>118)):
        contador-=1
        midaPaleta=input("Introdueixi la mida de la paleta de nou (3-numFil-1): ")
    if ((posFilaPil<2) or (posFilaPil>118)):
        contador-=1
        posFilaPil=input("Introdueixi les files on hi ha pilota de nou (2-118): ")
    if ((posColPil<2) or (posColPil>35)):
        contador-=1
        posColPil=input("Introdueixi es columnes on hi ha pilota de nou (2-35): ")
    if ((velFil<-1.0) or (velFil>1.0)):
        contador-=1
        velFil=input("Introdueixi la velocitat x de la pilota de nou (-1, 1): ")
    if ((velCol<-1.0) or (velCol>1.0)):
        contador-=1
        velCol=input("Introdueixi la velocitat y de la pilota de nou (-1, 1): ")
    return contador

def printVariables(fil,cols,portSize,posFilaPal,posColPal,midaPaleta,posFilaPil,posColPil,velFil,velCol,array1):
    print("")
    print("PRINT VARIABLES")
    print("files:" + str(fil))
    print("columnes:" + str(cols))
    print("portSize:" + str(portSize))
    print("posFilaPal:" + str(posFilaPal))
    print("posColPal:" + str(posColPal))
    print("midaPaleta:" + str(midaPaleta))
    print("posFilaPil:" + str(posFilaPil))
    print("posColPil:" + str(posColPil))
    print("velFil:" + str(velFil))
    print("velCol:" + str(velCol))
    
    for i in range(len(array1)):
        print("Pilota "+str(i)+": "+str(array1[i]))
def comprobarFichero(archivo):
    f=None
    print("COMPROBANDO FICHERO...")
    try:
        f = open(archivo)
        print("Hem pogut accedir al fitxer.")
        return True
    except (IOError, TypeError):
        f=open(archivo,'w')
        print("No s'ha pogut obrir el fitxer.")
        return False
    #finally:
    #    return False
    #    f.close()

def readFromKeyboard(temp):
    print("READ FROM KEYBOARD")
    temp=temp+1
    print("temp vale "+(str(temp)))


def main():
    
    fil=0
    cols=0
    portSize=0
    midaPaleta=0
    posFilaPil=0
    posColPil=0
    posColPal=0
    posFilaPal=0
    velFil=-2
    velCol=-2
    pilotes=None
    i=0
    #prueba1=3
    firstCorrect=False
    Nflag=None
    Fflag=None
    Cflag=None
    Pflag=None
    Mflag=None
    Oflag=None
    Oneflag=None
    archivo=None
    posFilaPal=None
    args=sys.argv[1:]
    #arg_list1b=['-n','params312.txt','-f','30']
    try:
        opts, args=getopt.getopt(args,"n:f:c:p:m:0:1:",["arxiu=","files=","columnes=","porteria=","mida=","zero=","one="])
    except getopt.GetoptError as error_message:
        print(error_message)
        #return False
    array1=[]
    for opt,arg in opts:
        if opt in ['-n','--arxiu']:
            Nflag=True
            archivo=arg
            
        elif opt in ['-f','--files']:
            Fflag=True
            try:
                fil=int(arg)  
            except:
                fil=int(input("Introdueix les files de nou: "))
        elif opt in ['-c','--columnes']:
            Cflag=True
            cols=int(arg)
        elif opt in ['-p','--porteria']:
            Pflag=True
            portSize=int(arg)
        elif opt in ['-m','--mida']:
            Mflag=True
            midaPaleta=int(arg)
        elif opt in ['-0','--zero']:
            Oflag=True
            posFilaPal=int(arg.split(",")[0])
            posColPal=int(arg.split(",")[1])
        elif opt in ['-1','--one']:
            Oneflag=True
            try:
                i=0
                while (i<8) and (i<len(args)):
                    array1.append(args[i].split(","))
                    #print(array1)
                    i+=1
                
                #print("data: "+str(arg.split(" ")))
                posFilaPil=int(arg.split(",")[0])
                posColPil=int(arg.split(",")[1])
                velFil=float(arg.split(",")[2])
                velCol=float(arg.split(",")[3])
                #print("llega"+ string)
            except Exception as e:
                print(e)
                print("Dades incorrectes")
    if Nflag==None:
        archivo=raw_input("Introdueix el nom de l`arxiu: ") 
   

    comprobarFichero(archivo)
    index=0
    print("Comencem a imprimir")
    
    try: 
        
        f=open(archivo)
        with f:
        #with open(archivo,'r'):
            for line in f:
                if index==0:
                    line=line.replace('\n','')
                    string=line.split(" ")
                    if len(string)==3:
                        firstCorrect=True
                        fil=int(line.split(" ")[0])
                        cols=int(line.split(" ")[1])
                        portSize=int(line.split(" ")[2])
                    else:
                        print("Falten parametres a la primera linea:")
                        fil=0
                        cols=0
                        portSize=0
                    #print("Fil: "+str(fil)+", col: "+str(cols)+", portsize: "+str(portSize))
                
                if index==1:
                    line=line.replace('\n','')
                    string=line.split(" ")
                    if len(string)==3:
                        posFilaPal=int(line.split(" ")[0])
                        posColPal=int(line.split(" ")[1])
                        midaPaleta=int(line.split(" ")[2])
                if index == 2:
                    line=line.replace('\n','')
                    string=line.split(" ")
                    
                    if len(string)==4:
                        posFilaPil=int(line.split(" ")[0])
                        posColPil=int(line.split(" ")[1])
                        velFil=float(line.split(" ")[2])
                        velCol=float(line.split(" ")[3])
                if (index>2) and (index<8):
                    line=line.replace('\n','')
                    string=line.split(" ")
                    if len(string)!=0:
                        
                        array1.append(string)
                index=index+1      
    except Exception as e: 
        print(e)
    #print("length is : "+str(len(array1[0])))
    #try:
    #    printVariables(fil,cols,portSize,posFilaPal,posColPal,midaPaleta,posFilaPil,posColPil,velFil,velCol,array1)
    #except UnboundLocalError:
    #    print("Els parametres a imprimir encara no tenen valors")
    contador=10
    correct=0
    AllCorrect=False
    if fil==25:
        print("si")
    while ((fil > 120 ) or (fil<10)):
        fil=input("Introdueix les files de nou (10-120): " )
        contador-=1
    while ((cols > 36) or (cols<10)):
        cols=input("Introdueix les columnes de nou (10-36): ")
        contador-=1
    maxPort=fil-1
    while((portSize>maxPort)or(portSize<8)):
        contador-=1
        portSize=input("Introdueix la mida de la porteria de nou (8-numFil-1): ")
    while ((posFilaPal<2) or (posFilaPal>118)):
        contador-=1
        posFilaPal=input("Introdueixi la fila on hi ha paleta de nou (2-118): ") 
    while ((posColPal<2) or (posColPal>35)):
        contador-=1
        posColPal=input("Introdueixi la columna on hi ha paleta de nou (2-35): ")
    while ((midaPaleta<2) or (midaPaleta>118)):
        contador-=1
        midaPaleta=input("Introdueixi la mida de la paleta de nou (3-numFil-1): ")
    while ((posFilaPil<2) or (posFilaPil>118)):
        contador-=1
        posFilaPil=input("Introdueixi les files on hi ha pilota de nou (2-118): ")
    while ((posColPil<2) or (posColPil>35)):
        contador-=1
        posColPil=input("Introdueixi les columnes on hi ha pilota de nou (2-35): ")
    while ((velFil<-1.0) or (velFil>1.0)):
        contador-=1
        velFil=input("Introdueixi la velocitat x de la pilota de nou (-1, 1): ")
    while ((velCol<-1.0) or (velCol>1.0)):
        contador-=1
        velCol=input("Introdueixi la velocitat y de la pilota de nou (-1,1): ")
        
            
        
    printVariables(fil,cols,portSize,posFilaPal,posColPal,midaPaleta,posFilaPil,posColPil,velFil,velCol,array1)
    
    try:
        #if comprobarFichero(archivo):
        #    f=open(archivo,'w')
        #    f.close()
        #else:    
            f=open(archivo, 'w')
            f.write(str(fil) +" " + str(cols) +" "+ str(portSize) +'\n')
            f.write(str(posFilaPal)+" "+ str(posColPal)+" "+str(midaPaleta)+'\n')
            f.write(str(posFilaPil)+" "+str(posColPil)+" "+str(velFil)+" "+str(velCol)+'\n')
            for i in range(len(array1)):
                first=True
                for j in range(len(array1[i])):
                    if first==False:
                        f.write(" ")
                    f.write(str(array1[i][j]))
                    first=False
                f.write('\n')
            
            if len(args)!=0:

                    print("Hem afegit pilotes extra a l'arxiu")
                    string=args[0].split(",")
                    #f.write(string[1]+" "+string[2]+" "+string[3]+" "+string[4])
    except (TypeError,IOError):
        print("Hi ha hagut un error amb el fitxer")

    
if __name__ == "__main__":
    main()
    
