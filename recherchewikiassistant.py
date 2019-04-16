# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 01:12:12 2019

@author: hp 15
"""

from tkinter import Tk,Entry,Button,Label,Canvas,LEFT,RIGHT
import asks
import anyio
import curio
import html_text
import pyttsx3
   
async def example(q):
    r = await asks.get('https://fr.wikipedia.org/wiki/'+q)
    tree = html_text.parse_html(r.text)
    cleaned_tree = html_text.cleaner.clean_html(tree)
    print(html_text.etree_to_text(cleaned_tree))
    f = html_text.etree_to_text(cleaned_tree)
    return f


def stop(event):
    engine = pyttsx3.init()
    engine.stop()
    print('Voice Stoped')

def evaluer(event):
    chaine.configure(text = " Text " )
    d = entree.get()
    f = curio.run(example(d))
    obFichier = open(d,'a', encoding="utf-8")
    obFichier.write(str(f))
    obFichier.close()
    
def readvox():
    chaine.configure(text = " Speech " )
    d = entree.get()
    f = curio.run(example(d))
    vox(f)

    
def vox(e):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('volume',1.0)
    engine.say(e)
    engine.runAndWait()
    
    
def writer():
    chaine.configure(text = " Text " )
    d = entree.get()
    f = curio.run(example(d))
    obFichier = open(d,'a', encoding="utf-8")
    obFichier.write(str(f))
    obFichier.close()


#========== Programme principal =============
# les variables suivantes seront utilisées de manière globale :
 # commutateur
# Création du widget principal ("parent") :

# création des widgets "enfants" :

if __name__ == "__main__":
    
    fenetre = Tk()
    x1, y1 = 10, 10 # coordonnées initiales
    x2, y2 = 200, 10
    x3, y3 = 125, 125
    fenetre.title("Assistant_de_recherche_wiki")
    entree = Entry(fenetre)
    entree.bind("<Return>", evaluer)
    chaine = Label(fenetre)
    can1 = Canvas(fenetre,bg='dark grey',height=250, width=250)
    oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='green')
    oval2 = can1.create_oval(x2, y2, x2+30, y2+30, width=2, fill='green')
    oval3 = can1.create_oval(x3, y3, x3+50, y3+50, width=2, fill='red')
    bou1 = Button(fenetre,text='speech',command = readvox)
    bou2 = Button(fenetre,text='Text',command = writer)
    can1.pack(side=LEFT)
    entree.pack()
    chaine.pack()
    bou1.pack(side=RIGHT)
    bou2.pack(side=LEFT)
    fenetre.mainloop()