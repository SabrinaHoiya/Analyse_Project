
from pylab import *
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

import math
from scipy.integrate import quad
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class mclass:

    def __init__(self, window):
        self.window = window

        varTitle = StringVar()
        varTitle.set("Intégration:Méthode des Trapèzes")
        labelTitle = Label(window, textvariable=varTitle, fg="purple", height=2,bg="pink",font=("Helvetica", 18))
        labelTitle.grid(row=0, columnspan=3, padx=10)

        var1 = StringVar()
        var1.set("La méthode des Trapèzes est une méthode de calcul approché d'intégrale") #\n
        label1 = Label(window, textvariable=var1, height=1,fg="purple", bg="pink")
        label1.grid(row=1, columnspan=3, padx=10)

        
        
        varF = StringVar()

        varF.set("La fonction, f(x) :")
        labelF = Label(window, textvariable=varF, height=2,fg="purple", bg="pink")
        labelF.grid(row=2, pady=5, padx=10)

        idF = StringVar()
        self.boxF = Entry(window, bd=4, width=30, textvariable=idF)
        self.boxF.grid(row=2, column=1, pady=5, padx=10)

        varA = StringVar()
        varA.set("La borne inférieur, a :")
        labelA = Label(window, textvariable=varA, height=2,fg="purple", bg="pink")
        labelA.grid(row=3,  pady=5, padx=10)

        idA = StringVar()
        self.boxA = Entry(window, bd=4, width=30, textvariable=idA)
        self.boxA.grid(row=3, column=1, pady=5, padx=10)

        varB = StringVar()
        varB.set("La borne supérieur, b :")
        labelB = Label(window, textvariable=varB, height=2,fg="purple", bg="pink")
        labelB.grid(row=4,  pady=5, padx=10)

        idB = StringVar()
        self.boxB = Entry(window, bd=4, width=30, textvariable=idB)
        self.boxB.grid(row=4, column=1, pady=5, padx=10)

        varN = StringVar()
        varN.set("N :")
        labelN = Label(window, textvariable=varN, height=2,fg="purple", bg="pink")
        labelN.grid(row=5, pady=5, padx=10)

        
        self.slider_N = Scale(window, from_=1, to=20, orient=HORIZONTAL,bg = "pink",fg="purple")
        self.slider_N.grid(row=5, column=1)

        self.button1 = Button(window, text="  PLOT  ", bg="purple", fg="white",width=20, command=self.plot,activeforeground="purple")
        self.button1.grid(row=6, column=0,  pady=5, padx=10)
        self.clear_button = Button(window, text="Clear ALL", command=self.clear_text,bg="purple", fg="white",width=20,activeforeground="purple")
        self.clear_button.grid(row=6, column=1,  pady=5, padx=10)
        vari = StringVar()
        vari.set("Integral Exacte  :")
        labeli = Label(window, textvariable=vari, height=2,fg="purple", bg="pink")
        labeli.grid(row=7, pady=5, padx=10)
        self.res=StringVar()
        self.res_int = Label(window,textvariable=self.res,justify=RIGHT, width=10,borderwidth=3,bg="purple")
        self.res_int.grid( row=7, column=1)
        varir = StringVar()
        varir.set("Integral Trapèze  :")
        labelir = Label(window, textvariable=varir, height=2,fg="purple", bg="pink")
        labelir.grid(row=8, pady=5, padx=10)
        self.res1=StringVar()
        self.res_intr = Label(window,textvariable=self.res1,justify=RIGHT, anchor="w", width=10,borderwidth=3,bg="purple")
        self.res_intr.grid( row=8, column=1)
        varie = StringVar()
        varie.set("Erreur Trapèze :")
        labelie = Label(window, textvariable=varie, height=2,fg="purple", bg="pink")
        labelie.grid(row=9,  pady=5, padx=10)
        self.res2=StringVar()
        self.res_er = Label(window,textvariable=self.res2,justify=RIGHT, width=10,borderwidth=3,bg="purple")
        self.res_er.grid( row=9, column=1,pady=5, padx=10)
        
        

    def clear_text(self):
        self.boxA.delete(0, 'end')
        self.boxF.delete(0, 'end')
        self.boxB.delete(0, 'end')
        self.res.set('')
        self.res1.set('')
        self.res2.set('')
        for item in self.canvas.get_tk_widget().find_all():
            self.canvas.get_tk_widget().delete(item)
        
        


    def plot(self):
        try:
            n = self.slider_N.get()
            a = float(self.boxA.get())
            b = float(self.boxB.get())
            F = self.boxF.get().lower().replace(' ', '')
            xl = np.linspace(a, b, n+1)
            f = lambda x: eval(F)   
            yl = f(xl)
            self.fig = plt.figure(figsize=(7, 5.5))
            I,r =quad(f, a, b)#calcule d'integrale exacte
            xlist_fine=np.linspace(a, b,1000)
            for i in range(n):
                x_rect = [xl[i], xl[i], xl[i+1], xl[i+1], xl[i]] # abscisses des sommets
                y_rect = [0   , yl[i], yl[i+1]  , 0     , 0   ] # ordonnees des sommets
                plot(x_rect, y_rect,"m")
            yflist_fine = f(xlist_fine)
            plt.plot(xlist_fine, yflist_fine)#plot de f(x)
            plt.plot(xl, yl,"cs")#point support
            plt.ylabel('f(x)')
            plt.title('Méthode des Trapèzes')
           
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
            self.canvas.get_tk_widget().grid(row=3, column=3, rowspan=6, pady=10, padx=10)
            self.res.set("%12.4f" % (I) )
            self.res1.set("%12.4f" %(self.integrate( f )))
            self.res2.set("%12.4f" % (I-self.integrate(f)))
            
        except ValueError:
            messagebox.showwarning("ValueError", "Veuillez vérifier votre saisie")

    def integrate ( self , f ) :
        n = self.slider_N.get()
        a = float(self.boxA.get())
        b = float(self.boxB.get())
        F = self.boxF.get().lower().replace(' ', '')
        xl = np.linspace(a, b, n+1)
        f = lambda x: eval(F) 
        x= xl
        y= f( x )
        h = float( x[1] - x[0] )
        s = y[0] + y[-1] + 2.0*sum(y[1:-1])
        return h * s / 2.0
        

if __name__ == '__main__':
    window = Tk()
    window.title('Intégration:Méthode de Simpson')
    window.resizable(width=True, height=True)
    window.geometry('+0+0')
    window.configure(bg='pink')
    start = mclass(window)
    window.mainloop()





