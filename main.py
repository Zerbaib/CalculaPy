#--------------
#IMMPORTATION :
#--------------
from tkinter import * # Tkinter

#---------
# CLASSE :
#---------
class Calculator():
    def __init__(self): # Construction
        self.phase1 = 0 # Premier nombre
        self.phase2 = 0 # Deuxième nombre
        self.final = 0 # Valeur finale
        self.entry = StringVar() # Capte les valeurs écrit
        self.text = "" # Nombre écrir par l'utilisateur
        self.signe = "" # Type d'opération
        self.entry.set("Create by Zerbaib")
        
    def init(self): # Initialisation 
        self.phase1 = 0 # Premier nombre
        self.phase2 = 0 # Deuxième nombre
        self.final = 0 # Valeur finale
        self.text = "" # Nombre écrir par l'utilisateur
        self.signe = "" # Type d'opération
        
    def afficher_Nb(self): # Afficher les nombre sur écran 
        self.entry.set(self.text)

    def operation(self): # Vérification du type d'opération
        try : 
            if "+" in self.text:
                self.Plus()
            elif "-" in self.text:
                self.Sous()
            elif "/" in self.text:
                self.Div()
            elif "X" in self.text:
                self.Mult()
        except:
            self.entry.set("ERROR")
            self.init()

    def Plus(self): # Addition
        nb = self.text.split("+")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 + self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Sous(self): # Soustraction
        nb = self.text.split("-")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 - self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Div(self): # Division
        nb = self.text.split("/")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 / self.phase2
        self.entry.set(str(self.final))
        self.init()

    def Mult(self): # Multiplication
        nb = self.text.split("X")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 * self.phase2
        self.entry.set(str(self.final))
        self.init()
    
#------------
# FONCTIONS :
#------------
def Button1 (): # Actionnerle bouton 1
    calculatrice.text += "1"
    calculatrice.entry.set(calculatrice.text)

def Button2 (): # Actionnerle bouton 2
    calculatrice.text += "2"
    calculatrice.entry.set(calculatrice.text)

def Button3 (): # Actionnerle bouton 3
    calculatrice.text += "3"
    calculatrice.entry.set(calculatrice.text)

def Button4 (): # Actionnerle bouton 4
    calculatrice.text += "4"
    calculatrice.entry.set(calculatrice.text)
    
def Button5 (): # Actionnerle bouton 5
    calculatrice.text += "5"
    calculatrice.entry.set(calculatrice.text)

def Button6 (): # Actionnerle bouton 6
    calculatrice.text += "6"
    calculatrice.entry.set(calculatrice.text)

def Button7 (): # Actionnerle bouton 7
    calculatrice.text += "7"
    calculatrice.entry.set(calculatrice.text)

def Button8 (): # Actionnerle bouton 8
    calculatrice.text += "8"
    calculatrice.entry.set(calculatrice.text)
    
def Button9 (): # Actionnerle bouton 9
    calculatrice.text += "9"
    calculatrice.entry.set(calculatrice.text)

def Button0 (): # Actionnerle bouton 0
    calculatrice.text += "0"
    calculatrice.entry.set(calculatrice.text)

def ButtonF(): # Actionnerle bouton F
    calculatrice.text += "."
    calculatrice.entry.set(calculatrice.text)
    
def ButtonP (): # Actionnerle bouton P
    calculatrice.text += "+"
    calculatrice.entry.set(calculatrice.text)

def ButtonS (): # Actionnerle bouton S
    calculatrice.text += "-"
    calculatrice.entry.set(calculatrice.text)

def ButtonD (): # Actionnerle bouton D
    calculatrice.text += "/"
    calculatrice.entry.set(calculatrice.text)

def ButtonM (): # Actionnerle bouton M
    calculatrice.text += "X"
    calculatrice.entry.set(calculatrice.text)

def ButtonE (): # Actionnerle bouton E
    calculatrice.operation()

def ButtonC (): # Actionnerle bouton c
    calculatrice.entry.set("")
    calculatrice.init()
    
#----------
# FENETRE :
#----------
fen = Tk() # Création de a fenêtr 1e
fen.geometry("200x240") # Définition de la fenêtre
fen.title("Calculatrice") # Titre de la calculatrice
fen["bg"]= "SkyBlue2" # Coleur de la fenêtre
fen["relief"] = "raised" # Profondeur de la fenêtre
#------------
# PROGRAMME :
#------------
# Création instance
calculatrice = Calculator()

# ATTRIBUTS DE LA FENETRE
#########################
# // Ecran calculatrice //
ECRAN = Entry(fen, width=28, textvariable=calculatrice.entry, bg ="black", fg="white", relief=SUNKEN, bd=5).place(x=9, y=8)

# // Bouttons //
B1 = Button(fen, text="1", command=Button1, width=3, height=2, bg="grey", fg="white").place(x=10, y=40) # Boutton 1
B2 = Button(fen, text="2", command=Button2, width=3, height=2, bg="grey", fg="white").place(x=50, y=40) # Boutton 2
B3 = Button(fen, text="3", command=Button3, width=3, height=2, bg="grey", fg="white").place(x=90, y=40) # Boutton 3
B4 = Button(fen, text="4", command=Button4, width=3, height=2, bg="grey", fg="white").place(x=10, y=90) # Boutton 4
B5 = Button(fen, text="5", command=Button5, width=3, height=2, bg="grey", fg="white").place(x=50, y=90) # Boutton 5
B6 = Button(fen, text="6", command=Button6, width=3, height=2, bg="grey", fg="white").place(x=90, y=90) # Boutton 6
B7 = Button(fen, text="7", command=Button7, width=3, height=2, bg="grey", fg="white").place(x=10, y=140) # Boutton 7
B8 = Button(fen, text="8", command=Button8, width=3, height=2, bg="grey", fg="white").place(x=50, y=140) # Boutton 8
B9 = Button(fen, text="9", command=Button9, width=3, height=2, bg="grey", fg="white").place(x=90, y=140) # Boutton 9
BC = Button(fen, text="C", command=ButtonC, width=3, height=2, bg="gold", fg="red", relief=RIDGE).place(x=10, y=190) # Boutton C (Clear)
B0 = Button(fen, text="0", command=Button0, width=3, height=2, bg="grey", fg="white").place(x=50, y=190) # Boutton 0
BF = Button(fen, text=".", command=ButtonF, width=3, height=2, bg="grey", fg="white").place(x=90, y=190) # Boutton = (égale)

BP = Button(fen, text="+", command=ButtonP, width=4, height=2, bg="gold", fg="black", relief=GROOVE).place(x=150, y=40) # Boutton + (addition)
BS = Button(fen, text="-", command=ButtonS, width=4, height=2, bg="gold", fg="black", relief=GROOVE).place(x=150, y=80) # Boutton - (soustacrtion)
BD = Button(fen, text="/", command=ButtonD, width=4, height=2, bg="gold", fg="black", relief=GROOVE).place(x=150, y=120) # Boutton / (division)
BM = Button(fen, text="X", command=ButtonM, width=4, height=2, bg="gold", fg="black", relief=GROOVE).place(x=150, y=160) # Boutton X (multiplication)
BE = Button(fen, text="=", command=ButtonE, width=4, height=1, bg="blue", fg="white", relief=RIDGE).place(x=150, y=205) # Button = (égale)

fen.mainloop() # Garde la fenetre ouverte
