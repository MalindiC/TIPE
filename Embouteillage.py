### Cl�ment Malindi TIPE
import random as ra
from tkinter import *
from tkinter.filedialog import *
from math import *
import numpy as np
import time
import matplotlib.pyplot as plt
###
#variable global
indice1=0
indice2=0
indice3=0
avancer=0
prem=3
actu=0
dep=0
arret=1
moyenne=0
ok=0
freinplus=0
#liste utile aux programmes
MOYENNE=[]
VOITEMBOUDROITE=[]
VOITEMBOUGAUCHE=[]
TEMPSDEPARCOURS=[]
embouteillagevoie=[[],[],[]]
embouteillagevoie2=[[],[]]
evolutionembouteillagevoie=[]
#liste vou�e à contenir des informations sur les voitures
VOIT=[]
#variable de temps
temps=time.time()
temps1=time.time()




#cration de l'interface
root=Tk()
can=Canvas(root,height=600,width=900,bg='white')
can.create_rectangle(0,250,900,350,fill='#E6E6E6',outline='White')
voiedinsert=can.create_rectangle(335,350,900,380,fill='white',outline='white')



#Liste de calcul
FLUX=[700,180*4,800,850,180*5,950,1000,180*6,1100,180*7,1350,180*8,1500,180*9,180*10,2000]
TEMBOUTEILLA=[41,36,28,22,19,16,14,11,10.4,10,7,6,6,4,4,3]



#Scales
P1=Scale(root,orient='horizontal',from_=1,to=20,length=350,label='Fluxinitial')
P2=Scale(root,orient='horizontal',from_=25,to=50,label='vitessemax',length=350) 
P3=Scale(root,orient='horizontal',from_=5,to=15,length=350,label='temps de freinage/arret')
P4=Scale(root,orient='horizontal',from_=1,to=20,resolution=1,length=350,label='intensit� freinage')
P5=Scale(root,orient='horizontal',from_=0,to=20,length=350,label='dispersion de vitesse')
P6=Scale(root,orient='horizontal',from_=600,to=2000,length=350,label='1/Fluxdelavoiedinsetion')
### Mod�lisation de la circulation
#MOUVEMENT DE CHAQUE VOITURE
        
#CREATION DE CHAQUE VOITURE
def voiture():
    vitesse=ra.randint(P2.get()-P5.get()//2,P2.get()+int(P5.get()/2))
    L=[can.create_oval(5,340,13,348,fill='black'),vitesse,vitesse,time.time()]   
    VOIT.append(L) 
    move(L[0],L[1])
    can.after(int(1/(P1.get()/10000)),voiture)
  
    
def move(voit0,voit1):
    #liste contenant la voiture de devant si elle la distance avec celle-çi est plus petite que la distance de s�curit�
    voituredevant=list(can.find_overlapping(list(can.coords(VOIT[voit0-3][0]))[0]+20,list(can.coords(VOIT[voit0-3][0]))[1],list(can.coords(VOIT[voit0-3][0]))[2]+20,list(can.coords(VOIT[voit0-3][0]))[3]))
    if 1 in voituredevant:
        voituredevant.remove(1)
    if 2 in voituredevant:
        voituredevant.remove(2)
    if voit0 in voituredevant:
        voituredevant.remove(voit0)
        
        
    # faire ralentir la voiture si elle ne peut pas d�passer celle de devant
    if len(voituredevant)>=1 :
        VOIT[voit0-3][1]=VOIT[voit0-4][1]+freinplus
        can.itemconfigure(VOIT[voit0-3][0],fill='red')
        
        
    #les voiture qui subissent un ralentissement sont rouges
    if VOIT[voit0-3][1]<VOIT[voit0-3][2]:
        can.itemconfigure(VOIT[voit0-3][0],fill='red')
        if voit0 not in VOITEMBOUGAUCHE:
            VOITEMBOUGAUCHE.append(voit0)
        
    else:
        can.itemconfigure(VOIT[voit0-3][0],fill='black')

    can.move(VOIT[voit0-3][0],1,0)
    #arreter la fonction si la voiture n'est plus sur la route
    if can.coords(VOIT[voit0-3][0])[0]<1000:
        can.after(int(1000/VOIT[voit0-3][1]),move,voit0,voit1)  
#CREATION DE CHAQUE VOITURE 

def voiture2():
    vitesse=ra.randint(P2.get(),P2.get()+P5.get())
    L=[can.create_oval(5,340,15,350,fill='black'),vitesse,vitesse,0,0,time.time()] 
    #L est une liste de la forme [tag de la voiture, vitesse de la voiture,vitesse de la voiture, d�placement vertical, 0 si la voiture est sur la file de droite 1 sinon]  
    VOIT.append(L) 
    move2(L[0],L[1],L[3])
    can.after(int(1/(P1.get()/10000)),voiture2)



    
def move2(voit0,voit1,voit3):#voit0 tag de la voiture,voit1 sa vitesse, voit3 son d�placement vertical
    pastouch�=0
    
    #liste contenant la voiture de devant si elle la distance avec celle-çi est plus petite que la distance de s�curit�
    voituredevant=list(can.find_overlapping(list(can.coords(VOIT[voit0-3][0]))[0]+10,list(can.coords(VOIT[voit0-3][0]))[1],list(can.coords(VOIT[voit0-3][0]))[2]+10,list(can.coords(VOIT[voit0-3][0]))[3]))
    if 1 in voituredevant:
        voituredevant.remove(1)
    if 2 in voituredevant:
        voituredevant.remove(2)
    if voit0 in voituredevant:
        voituredevant.remove(voit0)
        
        
    #liste contenant la voiture à gauche si elle existe 
    voitureagauche=list(can.find_overlapping(list(can.coords(VOIT[voit0-3][0]))[0]-10,list(can.coords(VOIT[voit0-3][0]))[1]-50,list(can.coords(VOIT[voit0-3][0]))[2]+10,list(can.coords(VOIT[voit0-3][0]))[3]-20))
    if 1 in voitureagauche:
        voitureagauche.remove(1)
    if 2 in voitureagauche:
        voitureagauche.remove(2)
    if voit0 in voitureagauche:
        voitureagauche.remove(voit0)
        
    #liste contenant la voiture à droite si elle existe     
    voitureadroite=list(can.find_overlapping(list(can.coords(VOIT[voit0-3][0]))[0]-20,list(can.coords(VOIT[voit0-3][0]))[1]+50,list(can.coords(VOIT[voit0-3][0]))[2]+20,list(can.coords(VOIT[voit0-3][0]))[3]+30 ))
    if 1 in voitureadroite:
        voitureadroite.remove(1)
    if 2 in voitureadroite:
        voitureadroite.remove(2)
    if voit0 in voitureadroite:
        voitureadroite.remove(voit0)

    
    
    # faire ralentir la voiture si elle ne peut pas d�passer celle de devant
    if len(voituredevant)>=1 and VOIT[voit0-3][4]==1:
        VOIT[voit0-3][1]=VOIT[voituredevant[0]-3][1]
        can.itemconfigure(VOIT[voit0-3][0],fill='red')
        if voit0 not in VOITEMBOUDROITE:
            VOITEMBOUDROITE.append(voit0)
        
    
    
    #faire ralentir la voiture car elle ne peut pas d�passer
    if (len(voituredevant)>=1 and len(voitureagauche)!=0 and VOIT[voit0-3][4]==0) or (len(voituredevant)>=1 and VOIT[voit0-3][4]==-1):
        VOIT[voit0-3][1]=VOIT[voituredevant[0]-3][1]

        
    
    
    
    
    # faire se rabattre la voiture sur la file de droite si c'est possible
    if len(voitureadroite)==0 and VOIT[voit0-3][4]==1:
        voit3=30
        VOIT[voit0-3][4]=0
        pastouch�=1
    
    
    # d�passer la voiture de devant si la voie de gauche est libre
    if len(voituredevant)>=1 and len(voitureagauche)==0 and  VOIT[voit0-3][4]==0 and pastouch�==0:
        voit3=-30
        VOIT[voit0-3][4]=1
    
    
    # si il n'y a pas de voiture trop proche reprendre la vitesse initiale
    if len(voituredevant)==0:
        VOIT[voit0-3][1]=VOIT[voit0-3][2]
        
    #Rentrer sur la voie de droite s c'est possible    
    if VOIT[voit0-3][4]==-1 and len(voitureagauche)==0 and time.time()-VOIT[voit0-3][5]>=1:
        VOIT[voit0-3][4]=0
        r=ra.randint(P2.get(),P2.get()+P5.get())
        VOIT[voit0-3][1]=r
        VOIT[voit0-3][2]=r
        voit3=-30
        
    #S'arrêter si la voiture ne peut pas rentrer    
    if can.coords(VOIT[voit0-3][0])[0]>=250 and VOIT[voit0-3][4]==-1:
       VOIT[voit0-3][1]=100000
       print(voitureagauche)
       if len(voitureagauche)==0:
           voit3=-30

       
    
        
    
    #les voiture qui subissent un ralentissement sont rouges
    if VOIT[voit0-3][1]<VOIT[voit0-3][2]:
        can.itemconfigure(VOIT[voit0-3][0],fill='red')
        if voit0 not in VOITEMBOUGAUCHE:
            VOITEMBOUGAUCHE.append(voit0)
    else:
        can.itemconfigure(VOIT[voit0-3][0],fill='black')
        
        
        
    if VOIT[voit0-3][1]>VOIT[voit0-3][2]:
        can.itemconfigure(VOIT[voit0-3][0],fill='red')
        if voit0 not in embouteillagevoie[VOIT[voit0-3][4]]:
            embouteillagevoie[VOIT[voit0-3][4]].append(voit0)
            evolutionembouteillagevoie.append([len(i) for i in embouteillagevoie])
    
    #d�placer la voiture
    can.move(VOIT[voit0-3][0],1,voit3)
    
    
    if 903>can.coords(VOIT[voit0-3][0])[0]>900:
        TEMPSDEPARCOURS.append([voit0,VOIT[voit0-3][2],time.time()-VOIT[voit0-3][5]])

    #arreter la fonction si la voiture n'est plus sur la route
    if can.coords(VOIT[voit0-3][0])[0]<1000:
        can.after(int(1/VOIT[voit0-3][1]*1000),move2,voit0,voit1,VOIT[voit0-3][3])    




#CREATION DE CHAQUE VOITURE


def voiture3():
    vitesse=ra.randint(P2.get(),P2.get()+P5.get())
    L=[can.create_oval(5,340,15,350,fill='black'),vitesse,vitesse,0,0,time.time()]   
    VOIT.append(L) 
    move3(L[0],L[1],L[3])
    can.after(int(1/(P1.get()/10000)),voiture3)


def move3(voit0,voit1,voit3):#voit0 tag de la voiture,voit1 sa vitesse, voit3 son d�placement vertical
    pastouch�=0
    
    #liste contenant la voiture de devant si elle la distance avec celle-çi est plus petite que la distance de s�curit�
    voituredevant=list(can.find_overlapping(list(can.coords(VOIT[voit0-3][0]))[0]+10,list(can.coords(VOIT[voit0-3][0]))[1],list(can.coords(VOIT[voit0-3][0]))[2]+10,list(can.coords(VOIT[voit0-3][0]))[3]))
    if 1 in voituredevant:
        voituredevant.remove(1)
    if 2 in voituredevant:
        voituredevant.remove(2)
    if voit0 in voituredevant:
        voituredevant.remove(voit0)
        
        
    #liste contenant la voiture à gauche si elle existe 
    voitureagauche=list(can.find_overlapping(list(can.coords(VOIT[voit0-3][0]))[0]-10,list(can.coords(VOIT[voit0-3][0]))[1]-50,list(can.coords(VOIT[voit0-3][0]))[2]+10,list(can.coords(VOIT[voit0-3][0]))[3]-20))
    if 1 in voitureagauche:
        voitureagauche.remove(1)
    if 2 in voitureagauche:
        voitureagauche.remove(2)
    if voit0 in voitureagauche:
        voitureagauche.remove(voit0)
        
    #liste contenant la voiture à droite si elle existe     
    voitureadroite=list(can.find_overlapping(list(can.coords(VOIT[voit0-3][0]))[0]-40,list(can.coords(VOIT[voit0-3][0]))[1]+50,list(can.coords(VOIT[voit0-3][0]))[2]+40,list(can.coords(VOIT[voit0-3][0]))[3]+30 ))
    if 1 in voitureadroite:
        voitureadroite.remove(1)
    if 2 in voitureadroite:
        voitureadroite.remove(2)
    if voit0 in voitureadroite:
        voitureadroite.remove(voit0)

    
        
   
   
   
    #faire ralentir la voiture car elle ne peut pas d�passer
    if len(voituredevant)>=1 and VOIT[voit0-3][4]==2:
        VOIT[voit0-3][1]=VOIT[voituredevant[0]-3][1]
        
        
    #faire ralentir la voiture car elle ne peut pas d�passer
    if len(voituredevant)>=1 and VOIT[voit0-3][4]==1:
        VOIT[voit0-3][1]=VOIT[voituredevant[0]-3][1]
    
    
    
    
    
    #faire ralentir la voiture car elle ne peut pas d�passer
    if (len(voituredevant)>=1 and len(voitureagauche)!=0 and VOIT[voit0-3][4]==0) or (len(voituredevant)>=1 and VOIT[voit0-3][4]==-1):
        VOIT[voit0-3][1]=VOIT[voituredevant[0]-3][1]


    
    
    
    
    # faire se rabattre la voiture sur la file de droite si c'est possible
    if len(voitureadroite)==0 and VOIT[voit0-3][4]==1:
        voit3=30
        VOIT[voit0-3][4]=0
        pastouch�=1
        
        
        
    # faire se rabattre la voiture sur la file de droite si c'est possible
    if len(voitureadroite)==0 and VOIT[voit0-3][4]==2:
        voit3=30
        VOIT[voit0-3][4]=1    
        pastouch�=1
        
        
        
    # depasser la voiture de devant si la voie 2 est libre
    if len(voituredevant)>=1 and len(voitureagauche)==0 and VOIT[voit0-3][4]==1:
        voit3=-30
        VOIT[voit0-3][4]=2
    
    
    # d�passer la voiture de devant si la voie de gauche est libre
    if len(voituredevant)>=1 and len(voitureagauche)==0 and  VOIT[voit0-3][4]<2 and pastouch�==0:
        voit3=-30
        VOIT[voit0-3][4]=1


    
    
    # si il n'y a pas de voiture trop proche reprendre la vitesse initiale
    if len(voituredevant)==0:
        VOIT[voit0-3][1]=VOIT[voit0-3][2]
        
    #Rentrer sur la voie de droite s c'est possible    
    if VOIT[voit0-3][4]==-1 and len(voitureagauche)==0 and time.time()-VOIT[voit0-3][5]>=1:
        VOIT[voit0-3][4]=0
        r=ra.randint(P2.get(),P2.get()+P5.get())
        VOIT[voit0-3][1]=r
        VOIT[voit0-3][2]=r
        voit3=-30
        
    #S'arrêter si la voiture ne peut pas rentrer    
    if can.coords(VOIT[voit0-3][0])[0]>=250 and VOIT[voit0-3][4]==-1:
       VOIT[voit0-3][1]=100000
       print(voitureagauche)
       if len(voitureagauche)==0:
           voit3=-30

       
    
        
    
    #les voiture qui subissent un ralentissement sont rouges
    if VOIT[voit0-3][1]<VOIT[voit0-3][2]:
        can.itemconfigure(VOIT[voit0-3][0],fill='red')
        if voit0 not in VOITEMBOUGAUCHE:
            VOITEMBOUGAUCHE.append(voit0)
    else:
        can.itemconfigure(VOIT[voit0-3][0],fill='black')
    
    #d�placer la voiture

    can.move(VOIT[voit0-3][0],1,voit3)
    
    
    if 905>can.coords(VOIT[voit0-3][0])[0]>900:
        TEMPSDEPARCOURS.append([voit0,VOIT[voit0-3][2],time.time()-VOIT[voit0-3][5]])
    #arreter la fonction si la voiture n'est plus sur la route
    if can.coords(VOIT[voit0-3][0])[0]<1000:
        can.after(int(1/VOIT[voit0-3][1]*1000),move3,voit0,voit1,VOIT[voit0-3][3]) 
### Cr�ation embouteillage
#CREATION DU FREINAGE
def premiere():# choix de la voiture qui freine en premiere
    global prem
    if list(can.coords(prem))[0]>=500:
        prem+=1
    can.after(10,premiere)
def ok1():# automatisation du freinage
    global ok,temps

    if can.coords(prem)[0]>=300 and ok==0:
        arret()
        ok=1
        temps=time.time()
        actu=prem
    if time.time()-temps>P3.get() and ok==1:
        #can.itemconfig(feu,fill='green')
        depart()
        ok=2
    can.after(500,ok1)


def arret():#freinage de la premiere voiture
    global freinplus
    VOIT[prem-3][1]=P4.get()
    freinplus=-5
def depart():#red���marrages des voitures qui ont frein�es
    global dep
    VOIT[dep+actu][1]=VOIT[dep+actu][2]
    move(VOIT[dep+actu][0],VOIT[dep+actu][1])
    if dep+1<len(VOIT):
        dep+=1
        can.after(500,depart)
def ok2():
    premiere()
    ok1()
        
###Graphes
def modifier_dispertion():
    global avancer
    P1.set(400+avancer)
    if len(TEMPSDEPARCOURS) !=0:
        moyenne=sum([i[2] for i in TEMPSDEPARCOURS])/len(TEMPSDEPARCOURS)
        MOYENNE.append(moyenne)
    moyenne=0
    avancer+=100
    
    can.after(60000,modifier_dispertion)
    
"""plt.plot(TEMBOUTEILLA,[1/(i) for i in FLUX ])
plt.title("Temps de resorbation de l'embouteillage en fonction du flux(10 s))")
plt.show()"""

def graphe3():
    plt.plot([i for i in range(len(evolutionembouteillagevoie))],[i[0] for i in evolutionembouteillagevoie])
    plt.plot([i for i in range(len(evolutionembouteillagevoie))],[i[1] for i in evolutionembouteillagevoie])
    plt.plot([i for i in range(len(evolutionembouteillagevoie))],[i[2] for i in evolutionembouteillagevoie])
    plt.title('Voiture ralentie sur chaque voie en foction du temps')
    plt.show()
    
def graphe2():
    plt.plot([i for i in range(len(evolutionembouteillagevoie))],[i[0] for i in evolutionembouteillagevoie])
    plt.plot([i for i in range(len(evolutionembouteillagevoie))],[i[1] for i in evolutionembouteillagevoie])
    plt.title('Voiture ralentie sur chaque voie en foction du temps')
    plt.show()
    

def graphe():
    M=[[] for i in range(21)]
    L=[[] for i in range(21)]
    for i in range(len (VOIT)):
        M[VOIT[i][2]-25].append(1)
    for i in VOITEMBOUGAUCHE:
        L[VOIT[i-3][2]-25].append(VOIT[i-3][0])
    print((L,M))
    ''''for i in VOITEMBOUDROITE:
        if VOIT[i-3][0] not in L[VOIT[i-3][2]-10]:
            L[VOIT[i-3][2]-10].append(1)'''
    plt.plot([i*3.6 for i in range (25,46)],[len(L[i])/len(M[i]) for i in range(len(L))])
    plt.title("voiture embouteill�es en fonction de la vitesse")
    plt.show()
    '''plt.plot([i for i in (MOYENNE)],[(4+i)*100 for i in range(0,len(MOYENNE))])
    plt.show()'''
###
def Demarrer():
    
    if indice1==1:
        voiture()
        
    if indice3==1:
        voiture3()
        
    if indice2==1:
        voiture2()

    
def modif1():
    global indice1,indice2,indice3
    indice1=1
    indice2=0
    indice3=0
def modif2():
    global indice1,indice2,indice3
    indice2=1
    indice1=0
    indice3=0
    
def modif3():
    global indice1,indice2,indice3
    indice3=1
    indice1=0
    indice2=0 
 
    
   
###
But=Button(root,command=Demarrer,text='Demarrer')
But2=Button(root,command=ok2,text='Freinage')
But3= Button(root,command=graphe,text='graphe')
CB1 = Checkbutton(root, text='une voie',command=modif1)
CB2= Checkbutton(root, text='deux voies',command=modif2)
CB3= Checkbutton(root, text="trois voies",command=modif3)
###
P1.grid(row=0,column=2)
P6.grid(row=1,column=2)
P2.grid(row=2,column=2)
#P3.grid(row=2,column=2)
P4.grid(row=3,column=2)
P5.grid(row=4,column=2)

can.grid(row=0,rowspan=4,column=1)
But.grid(row=3,column=0)
But2.grid(row=4,column=1)
But3.grid(row=4,column=0)

CB1.grid(row=0,column=0)
CB2.grid(row=1,column=0)
CB3.grid(row=2,column=0)



root.mainloop()

