#APP para convertir pies a metros usando tkinter
#Herrera Zepeda Jose Damian
#23/02/2023

from tkinter import *
from tkinter import ttk

#Se crea clase
class conversor:      

#init funciona como constructor   #Raiz es la tabla

    def __init__(self, raiz):

        raiz.title("Pies a metros")  #titulo de la pagina
      
        mainFrame= ttk.Frame(raiz) #widget transparete hasta especificar
        mainFrame.grid(column=0, row=0)
        piesEntry= ttk.Entry(mainFrame)
        piesEntry.grid()

if __name__=="__main__":
    print("este el archivo principal.")
    print("Nada  mas se mostrara si este es el principal.")
   

