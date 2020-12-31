
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sys
import os





class DemoSplashScreen:
   
    def __init__(self, parent):
        self.parent = parent
        self.imageSplash()
        self.setWindow()
    def imageSplash(self):
        # import image 
        self.image = Image.open('welcome.png')
        self.imgSplash = ImageTk.PhotoImage(self.image)
    def setWindow(self):
        # prendre la taille du fichier image
        largeur, hauteur = self.image.size
 
        demi_large = (self.parent.winfo_screenwidth()-largeur)//2
        demi_haut = (self.parent.winfo_screenheight()-hauteur)//2
 
        #ajuster la position de la fenêtre au milieu de l'écran
        self.parent.geometry("%ix%i+%i+%i" %(largeur, hauteur,demi_large,demi_haut))
 
        # définir l'image via le composant d'étiquette
        Label(self.parent, image=self.imgSplash).pack()
         
if __name__ == '__main__':
    root = Tk()
 
    # supprime le titre de la fenêtre et les bordures du cadre
    root.overrideredirect(True)
    style = ttk.Style()
    style.theme_use('default')
    style.configure("grey.Horizontal.TProgressbar", background='purple')
    progressbar = ttk.Progressbar(orient=HORIZONTAL, length=10000, mode='determinate', style='grey.Horizontal.TProgressbar')
    progressbar.pack(side="bottom")
    app = DemoSplashScreen(root)
    progressbar.start()
    def main_window():
        root1= Tk()

        root1.title("Interpolation polynomiale & Integration numérique")
        root1.geometry("1080x500")
        haut = Frame (root1, bg ="pink", height = 100, width =100)
        haut.pack(fill=X)
        func_txt=StringVar()
        func_txt.set("Choisir une Méthode")
        label_func=Label(haut, textvariable=func_txt,bg ="pink",font=("Helvetica", 40),fg ="purple")
        label_func.pack()
        fond = Frame (root1)
        fond.pack(fill=BOTH, expand=1)
        b1=Button (root1, text = " Quitter ",font=("Helvetica", 15),fg ="purple",command = root1.quit,bg="pink",activeforeground="purple")
        b1.pack()

        def helloCallBack():
            os.system('python Lagrange_Method.py')
        def CallBack():
            os.system('python Rec.py')
        def CallBack1():
            os.system('python Simpson_Method.py')
        def CallBack2():
            os.system('python Milieu_Method.py')
        def CallBack3():
            os.system('python Tra_Method.py')
        def CallBack4():
            os.system('python inter.py')
        interpolation = Label(fond, text="Interpolation Polynomiale " , font=("Helvetica", 20), fg ="#DC143C" )
        interpolation.place(y=20, x=50)
        
        lagrange= Button(fond,text="Méthode de Lagrange", font='none 14', width= 20 , background = "#f05c79",activeforeground="purple",fg ="purple",command=helloCallBack)
        lagrange.place(y=140, x=50)
        inter= Button(fond,text="Interpolation", font='none 14', width= 20 , background = "#f05c79",activeforeground="purple",fg ="purple",command=CallBack4)
        inter.place(y=220, x=50)
       

        integration = Label(fond, text="Intégration Numérique" , font=("Helvetica", 20), fg ="#DC143C" )
        integration.place(y=20, x=750)

        trapez= Button(fond,text="Méthode des Trapèzes", font='none 14', width= 20 , background = "#f05c79",activeforeground="purple",fg ="purple",command=CallBack3)
        trapez.place(y=140, x=750)


        simpson= Button(fond,text=" Méthode de Simpson", font='none 14', width= 20 , background = "#f05c79",activeforeground="purple",fg ="purple",command=CallBack1)
        simpson.place(y=180, x=750)

        point_milieu =Button(fond,text="Méthode de PointMilieu", font='none 14', width= 20 , background = "#f05c79",activeforeground="purple",fg ="purple",command=CallBack2)
        point_milieu.place(y=220, x=750)
        rectangles=Button(fond,text="Méthode des Réctangles", font='none 14', width= 20 , background = "#f05c79",activeforeground="purple",fg ="purple",command=CallBack)
        rectangles.place(y=260, x=750)

        root1.mainloop()
    def call_mainroot():
        root.destroy()
        main_window()
        
        
root.after(5000,call_mainroot)
 
root.mainloop()

