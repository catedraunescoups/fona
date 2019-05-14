from tkinter import *
import tkinter as tix
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from itertools import count
import threading
import pygame
from pygame.locals import *
import time
import sched
from random import randint

import webbrowser as wb
import subprocess as sp
import random
import os



pygame.init()
pygame.mixer.get_init()
global contador

#FUNCIONES PARA LLAMAR A LAS LETRAS
def entrar():
    pygame.mixer.music.pause()
    ventana.destroy()
    menuu()
    

def regresarmenuR1():
    menuR.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuR2():
    R1.destroy()
    pygame.mixer.music.pause()
    menuu()

def regresarmenuS1():
    menuS.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuS2():
    S1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuT1():
    menuT.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuT2():
    T1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuM1():
    menuM.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuM2():
    M1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuL1():
    menuL.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuL2():
    L1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuBL1():
    menuBL.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuBL2():
    BL1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuCL1():
    menuCL.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuCL2():
    CL1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuFL1():
    menuFL.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuFL2():
    FL1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuGL1():
    menuGL.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuGL2():
    GL1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuPL1():
    menuPL.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuPL2():
    PL1.destroy()
    pygame.mixer.music.pause()
    menuu()

def regresarmenuBR1():
    menuBR.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuBR2():
    BR1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuCR1():
    menuCR.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuCR2():
    CR1.destroy()
    pygame.mixer.music.pause()
    menuu()

def regresarmenuDR1():
    menuDR.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuDR2():
    DR1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuFR1():
    menuFR.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuFR2():
    FR1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuGR1():
    menuGR.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuGR2():
    GR1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuPR1():
    menuPR.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuPR2():
    PR1.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuTR1():
    menuTR.destroy()
    pygame.mixer.music.pause()
    menuu()
def regresarmenuTR2():
    TR1.destroy()
    pygame.mixer.music.pause()
    menuu()



#MENU GENERAL
def menuu():
    global numerodefrases23
    numerodefrases23=1
    global menu
    menu=tix.Tk()
    menu.geometry("800x450")
    menu.config(bg="sky blue")
    menu.attributes("-fullscreen", True)
    letram=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/m.png", master=menu)
    letrar=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/r.png", master=menu)
    letras=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/s.png", master=menu)
    letrat=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/t.png", master=menu)
    letral=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/l.png", master=menu)
    letrabr=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/br.png", master=menu)
    letrabl=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/bl.png", master=menu)
    letracr=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/cr.png", master=menu)
    letracl=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/cl.png", master=menu)
    letradr=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/dr.png", master=menu)
    letrafl=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/fl.png", master=menu)
    letrafr=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/fr.png", master=menu)
    letragl=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/gl.png", master=menu)
    letragr=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/gr.png", master=menu)
    letrapl=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/pl.png", master=menu)
    letrapr=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/pr.png", master=menu)
    
## BOTONES
    reconocer=Button(menu,text="Iniciar",command=speech,width=10, height=5, bg="sky blue").place(x=100,y=450)
    letratr=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/tr.png", master=menu)
    m= tix.Button(menu,image=letram,command=entrarM,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=14,y=45)
    r= tix.Button(menu,image=letrar,command=entrarR,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=238,y=45)
    s= tix.Button(menu,image=letras,command=entrarS,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=350,y=45)
    t= tix.Button(menu,image=letrat,command=entrarT,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=126,y=45)
    l= tix.Button(menu,image=letral,command=entrarL,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=462,y=45)
    br= tix.Button(menu,image=letrabr,command=entrarBR,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=462,y=190)
    bl= tix.Button(menu,image=letrabl,command=entrarBL,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=686,y=45)
    cr= tix.Button(menu,image=letracr,command=entrarCR,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=574,y=190)
    cl= tix.Button(menu,image=letracl,command=entrarCL,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=14,y=190)
    dr= tix.Button(menu,image=letradr,command=entrarDR,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=238,y=335)
    fl= tix.Button(menu,image=letrafl,command=entrarFL,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=126,y=190)
    fr= tix.Button(menu,image=letrafr,command=entrarFR,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=686,y=190)
    gl= tix.Button(menu,image=letragl,command=entrarGL,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=238,y=190)
    gr= tix.Button(menu,image=letragr,command=entrarGR,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=14,y=335)
    pl= tix.Button(menu,image=letrapl,command=entrarPL,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=574,y=45)
    pr= tix.Button(menu,image=letrapr,command=entrarPR,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=350,y=190)
    tr= tix.Button(menu,image=letratr,command=entrarTR,width=100, height=100, bg="sky blue", relief="flat",border=0).place(x=126,y=335)
    
    menu.mainloop()

def speech():
    proceso = sp.Popen(['python3','-m','http.server','8000'])
    path = 'imagenes/'
    files = os.listdir(path)
    
    name = files[random.randint(0,len(files)-1)]
    img = '<center><img src=\''+path+'/'+name+'\' /><center>'

        
        
    text = """
            <html>
            <body bgcolor="#d6d7c6">
            <audio id=\'sonidook'>
                 <source src=\'claudia.mp3\' type=\'audio/mpeg\' />
            </audio>
            
            <form name=\'f1\' action=\'\' >
                <p align=\'center\'>
                <input type=\'text\' id=\'txtRes\' name=\'txtRes\' value=\' \' />
                </p>
            </form>
            <div id=\'transcript\'></div>

            <script language='javascript'>

            

            const recognition = new webkitSpeechRecognition();

            var control = document.getElementById(\'sonidook\');
            //playsound();

            var transcript = document.getElementById('txtRes');
            var objectName = \'"""+name[0:name.index('.')]+"""\';

        
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.onresult = function(event) {
                console.log(event.results[0][0].transcript);
                if (event.results[0][0].transcript){
                    transcript.value = event.results[0][0].transcript;
                    if (event.results[0][0].transcript == objectName){
                        playsound();
                        //alert('Muy bien, acertaste!');
                        
                        recognition.stop();
                    }
                }
                if (event.results[0].isFinal) {
                    //console.log(event.results[0][0].transcript);
                
                    //alert('Terminó'+event.results[0][0].transcript);
                    
                    //transcript.innerHTML='<strong>event.results[0][0].transcript</strong>';
                    if (event.results[0][0].transcript == objectName){
                        aclaudialegustanlosgirasoles()
                        alert('Muy bien, acertaste!');
                        recognition.stop();
                    }
                
                    recognition.stop();
                }
            }

            function playsound(){
                 control.play();
            }
        
            recognition.onaudiostart = e => {
                console.log("audio capture started");
            }
        
            recognition.onaudioend = e => {
                console.log("audio capture ended");
                recognition.stop();
            }
            
            recognition.onspeechend = function() {
                recognition.stop();
            }
            
            recognition.start();
            </script>


            """

    text += img+'</body></html>'
        
        
    url = 'http://localhost:8000/SpeechRecognition.html'
    _file = open('SpeechRecognition.html','w')
    _file.write(text)
    _file.close()
    #wb.open_new_tab(url)
    sp.Popen(['/usr/bin/chromium-browser', url])
        


#INGRESO DE LOS AUDIOS
def aclaudialegustanlosgirasoles():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/A-claudia-le-gusta-los-girasoles.mp3")
    pygame.mixer.music.play(1)
def numero():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/numero.wav")
    pygame.mixer.music.play(1)
def peru():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/peru.wav")
    pygame.mixer.music.play(1)
def caminar():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/caminar.wav")
    pygame.mixer.music.play(1)
def aguila():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/aguila.wav")
    pygame.mixer.music.play(1)
def aji():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/aji.wav")
    pygame.mixer.music.play(1)
def alpiratalegusta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/al-pirata-le-gusta.wav")
    pygame.mixer.music.play(1)
def aplaude():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/aplaude.wav")
    pygame.mixer.music.play(1)
def aplaudoalpayaso():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/aplaudo-al-payaso.wav")
    pygame.mixer.music.play(1)
def aprendeapronunciarcompuestas():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/Aprender-pronunciar-compuestas.wav")
    pygame.mixer.music.play(1)
def araña():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/araña.wav")
    pygame.mixer.music.play(1)
def aplaude():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/aplaude.wav")
    pygame.mixer.music.play(1)
def aprenderapronunciarcompuestas():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/Aprender-pronunciar-compuestas.wav")
    pygame.mixer.music.play(1)
def arbol():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arbol.wav")
    pygame.mixer.music.play(1)
def atun():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/atun.wav")
    pygame.mixer.music.play(1)
def avion():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/avion.wav")
    pygame.mixer.music.play(1)
def beso():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/beso.wav")
    pygame.mixer.music.play(1)
def bicicleta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/bicicleta.wav")
    pygame.mixer.music.play(1)
def BLBLBLBLBLBL():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/bl.wav")
    pygame.mixer.music.play(1)
def bla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/bla.wav")
    pygame.mixer.music.play(1)
def ble():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/ble.wav")
    pygame.mixer.music.play(1)
def bli():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/bli.wav")
    pygame.mixer.music.play(1)
def blo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/blo.wav")
    pygame.mixer.music.play(1)
def blu():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/blu.wav")
    pygame.mixer.music.play(1)
def blusa():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/blusa.wav")
    pygame.mixer.music.play(1)
def borrego():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/borrego.wav")
    pygame.mixer.music.play(1)
def BRBRBRBRBRBR():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/br.wav")
    pygame.mixer.music.play(1)
def bra():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/bra.wav")
    pygame.mixer.music.play(1)
def brazo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/brazo.wav")
    pygame.mixer.music.play(1)
def bre():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/bre.wav")
    pygame.mixer.music.play(1)
def bri():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/bri.wav")
    pygame.mixer.music.play(1)
def bro():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/bro.wav")
    pygame.mixer.music.play(1)
def bru():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/bru.wav")
    pygame.mixer.music.play(1)
def bruja():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/bruja.wav")
    pygame.mixer.music.play(1)
def bufanda():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/bufanda.wav")
    pygame.mixer.music.play(1)
def buo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/buo.wav")
    pygame.mixer.music.play(1)
def burro():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/burro.wav")
    pygame.mixer.music.play(1)
def cable():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cable.wav")
    pygame.mixer.music.play(1)
def caja():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/caja.wav")
    pygame.mixer.music.play(1)
def cama():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cama.wav")
    pygame.mixer.music.play(1)
def camisa():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/camisa.wav")
    pygame.mixer.music.play(1)
def cangrejo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cangrejo.wav")
    pygame.mixer.music.play(1)
def caramelo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/caramelo.wav")
    pygame.mixer.music.play(1)
def casa():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/casa.wav")
    pygame.mixer.music.play(1)
def cerdo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cerdo.wav")
    pygame.mixer.music.play(1)
def cerveza():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cerveza.wav")
    pygame.mixer.music.play(1)
def chancho():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/chancho.wav")
    pygame.mixer.music.play(1)
def chicle():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/chicle.wav")
    pygame.mixer.music.play(1)
def chino():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/chino.wav")
    pygame.mixer.music.play(1)
def chocolate():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/chocolate.wav")
    pygame.mixer.music.play(1)
def chompa():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/chompa.wav")
    pygame.mixer.music.play(1)
def chupon():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/chupon.wav")
    pygame.mixer.music.play(1)
def CLCLCLCLCLCL():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cl.wav")
    pygame.mixer.music.play(1)
def cla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cla.wav")
    pygame.mixer.music.play(1)
def clase():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/clase.wav")
    pygame.mixer.music.play(1)
def clavel():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/clavel.wav")
    pygame.mixer.music.play(1)
def clavo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/clavo.wav")
    pygame.mixer.music.play(1)
def cle():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cle.wav")
    pygame.mixer.music.play(1)
def cli():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cli.wav")
    pygame.mixer.music.play(1)
def clo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/clo.wav")
    pygame.mixer.music.play(1)
def clu():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/clu.wav")
    pygame.mixer.music.play(1)
def cocodrilo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cocodrilo.wav")
    pygame.mixer.music.play(1)
def coliflor():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/coliflor.wav")
    pygame.mixer.music.play(1)
def columpio():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/columpio.wav")
    pygame.mixer.music.play(1)
def come():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/come.wav")
    pygame.mixer.music.play(1)
def condor():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/condor.wav")
    pygame.mixer.music.play(1)
def conflex():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/conflex.wav")
    pygame.mixer.music.play(1)
def contarcuentos():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/contarcuentos.wav")
    pygame.mixer.music.play(1)
def corazon():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/corazon.wav")
    pygame.mixer.music.play(1)
def cortoelarbol():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cortoelarbol.wav")
    pygame.mixer.music.play(1)
def CRCRCRCRCRCR():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cr.wav")
    pygame.mixer.music.play(1)
def cra():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cra.wav")
    pygame.mixer.music.play(1)
def craneo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/craneo.wav")
    pygame.mixer.music.play(1)
def cre():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cre.wav")
    pygame.mixer.music.play(1)
def cri():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cri.wav")
    pygame.mixer.music.play(1)
def cro():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cro.wav")
    pygame.mixer.music.play(1)
def cromo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cromo.wav")
    pygame.mixer.music.play(1)
def cru():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cru.wav")
    pygame.mixer.music.play(1)
def cruz():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cruz.wav")
    pygame.mixer.music.play(1)
def cuandollueve():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cuando-llueve.wav")
    pygame.mixer.music.play(1)
def cuentoLLLLLL():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cuento-L.wav")
    pygame.mixer.music.play(1)
def cuentoMMMMMM():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cuentomm.wav")
    pygame.mixer.music.play(1)
def cuentoRRRRRR():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cuento-R.wav")
    pygame.mixer.music.play(1)
def cuentoSSSSSS():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cuento-s.wav")
    pygame.mixer.music.play(1)
def cuentoTTTTTT():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cuentoT.wav")
    pygame.mixer.music.play(1)
def cuna():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/cuna.wav")
    pygame.mixer.music.play(1)
def dinero():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/dinero.wav")
    pygame.mixer.music.play(1)
def doctora():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/doctora.wav")
    pygame.mixer.music.play(1)
def DRDRDRDRDRDR():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/dr.wav")
    pygame.mixer.music.play(1)
def dra():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/dra.wav")
    pygame.mixer.music.play(1)
def dre():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/dre.wav")
    pygame.mixer.music.play(1)
def dri():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/dri.wav")
    pygame.mixer.music.play(1)
def dro():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/dro.wav")
    pygame.mixer.music.play(1)
def dru():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/dru.wav")
    pygame.mixer.music.play(1)
def duerme():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/duerme.wav")
    pygame.mixer.music.play(1)
def elabuelole():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/el-abuelo-le.wav")
    pygame.mixer.music.play(1)
def elaguilatiene():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/el-aguila-tiene.wav")
    pygame.mixer.music.play(1)
def elcablede():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/El-cable-de.wav")
    pygame.mixer.music.play(1)
def elcocodriloquiere():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/el-cocodrilo.quiere.wav")
    pygame.mixer.music.play(1)
def elconejosalta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/el-conejo-salta.wav")
    pygame.mixer.music.play(1)
def elefante():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/elefante.wav")
    pygame.mixer.music.play(1)
def eliglues():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/el-iglu-es.wav")
    pygame.mixer.music.play(1)
def elniñoestamuyfeliz():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/el-niño-esta-muy-feliz.wav")
    pygame.mixer.music.play(1)
def elosocome():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/el-oso-come.wav")
    pygame.mixer.music.play(1)
def escalera():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/escalera.wav")
    pygame.mixer.music.play(1)
def escucharsilabas():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/escuchalassilabasyrepite.wav")
    pygame.mixer.music.play(1)
def escuchapalabrasM():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/escuchapalabrasconmmm.wav")
    pygame.mixer.music.play(1)
def escuchapalabrasR():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/escucha-palabras-r-repitelas.wav")
    pygame.mixer.music.play(1)
def escuchapalabrasS():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/escucha-palabras-sss.wav")
    pygame.mixer.music.play(1)
def escuchayrepite():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/escuchayrepite.wav")
    pygame.mixer.music.play(1)
def repiteelsonido():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/escucha-y-repite.wav")
    pygame.mixer.music.play(1)
def estrella():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/estrella.wav")
    pygame.mixer.music.play(1)
def excelente():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/excelente.wav")
    pygame.mixer.music.play(1)
def familia():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/familia.wav")
    pygame.mixer.music.play(1)
def FLFLFLFLFLFL():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/fl.wav")
    pygame.mixer.music.play(1)
def fla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/fla.wav")
    pygame.mixer.music.play(1)
def flaco():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/flaco.wav")
    pygame.mixer.music.play(1)
def flauta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/flauta.wav")
    pygame.mixer.music.play(1)
def fle():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/fle.wav")
    pygame.mixer.music.play(1)
def flecha():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/flecha.wav")
    pygame.mixer.music.play(1)
def fli():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/fli.wav")
    pygame.mixer.music.play(1)
def flo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/flo.wav")
    pygame.mixer.music.play(1)
def flores():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/flores.wav")
    pygame.mixer.music.play(1)
def flu():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/flu.wav")
    pygame.mixer.music.play(1)
def foco():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/foco.wav")
    pygame.mixer.music.play(1)
def FRFRFRFRFRFR():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/fr.wav")
    pygame.mixer.music.play(1)
def fra():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/fra.wav")
    pygame.mixer.music.play(1)
def frasco():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/frasco.wav")
    pygame.mixer.music.play(1)
def fre():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/fre.wav")
    pygame.mixer.music.play(1)
def fri():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/fri.wav")
    pygame.mixer.music.play(1)
def frio():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/frio.wav")
    pygame.mixer.music.play(1)
def fro():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/fro.wav")
    pygame.mixer.music.play(1)
def fru():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/fru.wav")
    pygame.mixer.music.play(1)
def fruta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/fruta.wav")
    pygame.mixer.music.play(1)
def frutas():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/frutas.wav")
    pygame.mixer.music.play(1)
def frutilla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/frutilla.wav")
    pygame.mixer.music.play(1)
def fuego():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/fuego.wav")
    pygame.mixer.music.play(1)
def galleta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/galleta.wav")
    pygame.mixer.music.play(1)
def gallina():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gallina.wav")
    pygame.mixer.music.play(1)
def gallo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gallo.wav")
    pygame.mixer.music.play(1)
def girasol():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/girasol.wav")
    pygame.mixer.music.play(1)
def GLGLGLGLGLGL():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gl.wav")
    pygame.mixer.music.play(1)
def gla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gla.wav")
    pygame.mixer.music.play(1)
def gle():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gle.wav")
    pygame.mixer.music.play(1)
def gli():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gli.wav")
    pygame.mixer.music.play(1)
def glo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/glo.wav")
    pygame.mixer.music.play(1)
def globo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/globo.wav")
    pygame.mixer.music.play(1)
def gloton():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gloton.wav")
    pygame.mixer.music.play(1)
def glu():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/glu.wav")
    pygame.mixer.music.play(1)
def GRGRGRGRGRGR():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gr.wav")
    pygame.mixer.music.play(1)
def gra():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gra.wav")
    pygame.mixer.music.play(1)
def gre():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gre.wav")
    pygame.mixer.music.play(1)
def gri():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gri.wav")
    pygame.mixer.music.play(1)
def grillo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/grillo.wav")
    pygame.mixer.music.play(1)
def grita():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/grita.wav")
    pygame.mixer.music.play(1)
def gro():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gro.wav")
    pygame.mixer.music.play(1)
def gru():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gru.wav")
    pygame.mixer.music.play(1)
def grua():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/grua.wav")
    pygame.mixer.music.play(1)
def guineo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/guineo.wav")
    pygame.mixer.music.play(1)
def guineos():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/guineos.wav")
    pygame.mixer.music.play(1)
def guitarra():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/guitarra.wav")
    pygame.mixer.music.play(1)
def gusano():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/gusano.wav")
    pygame.mixer.music.play(1)
def habla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/habla.wav")
    pygame.mixer.music.play(1)
def hacha():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/hacha.wav")
    pygame.mixer.music.play(1)
def helado():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/helado.wav")
    pygame.mixer.music.play(1)
def hola():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/hola.wav")
    pygame.mixer.music.play(1)
def iglesia():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/iglesia.wav")
    pygame.mixer.music.play(1)
def iglu():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/iglu.wav")
    pygame.mixer.music.play(1)
def intentalodenuevo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/intentalo-de-nuevo.wav")
    pygame.mixer.music.play(1)
def intentalootravez():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/intentalo-otra-vez.wav")
    pygame.mixer.music.play(1)
def jarra():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/jarra.wav")
    pygame.mixer.music.play(1)
def jirafa():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/jirafa.wav")
    pygame.mixer.music.play(1)
def kiwi():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/kiwi.wav")
    pygame.mixer.music.play(1)
def la():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/la.wav")
    pygame.mixer.music.play(1)
def ladrillo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/ladrillo.wav")
    pygame.mixer.music.play(1)
def lagartija():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lagratija.wav")
    pygame.mixer.music.play(1)
def lapiz():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lapiz.wav")
    pygame.mixer.music.play(1)
def le():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/le.wav")
    pygame.mixer.music.play(1)
def leche():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/leche.wav")
    pygame.mixer.music.play(1)
def lechuga():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lechuga.wav")
    pygame.mixer.music.play(1)
def lechuza():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lechuza.wav")
    pygame.mixer.music.play(1)
def lee():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lee.wav")
    pygame.mixer.music.play(1)
def li():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/li.wav")
    pygame.mixer.music.play(1)
def libro():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/libro.wav")
    pygame.mixer.music.play(1)
def licuadora():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/licuadora.wav")
    pygame.mixer.music.play(1)
def limon():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/limon.wav")
    pygame.mixer.music.play(1)
def llama():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/llama.wav")
    pygame.mixer.music.play(1)
def llevaimagenesm():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-mm.wav")
    pygame.mixer.music.play(1)
def llevaimagenesl():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lleva-imagenes-L.wav")
    pygame.mixer.music.play(1)
def llevaimagenesr():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lleva-imagen-r.wav")
    pygame.mixer.music.play(1)
def llevaimageness():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lleva-image-s.wav")
    pygame.mixer.music.play(1)
def llevaimagenesbl():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-bl.wav")
    pygame.mixer.music.play(1)
def llevaimagenesbr():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-br.wav")
    pygame.mixer.music.play(1)
def llevaimagenescl():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-cl.wav")
    pygame.mixer.music.play(1)
def llevaimagenescr():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-cr.wav")
    pygame.mixer.music.play(1)
def llevaimagenesdr():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-dr.wav")
    pygame.mixer.music.play(1)
def llevaimagenesfl():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-fl.wav")
    pygame.mixer.music.play(1)
def llevaimagenesfr():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-fr.wav")
    pygame.mixer.music.play(1)
def llevaimagenesgl():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-gl.wav")
    pygame.mixer.music.play(1)
def llevaimagenesgr():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-gr.wav")
    pygame.mixer.music.play(1)
def llevaimagenespl():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-pl.wav")
    pygame.mixer.music.play(1)
def llevaimagenespr():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-pr.wav")
    pygame.mixer.music.play(1)
def llevaimagenestr():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/arrastra-a-tr.wav")
    pygame.mixer.music.play(1)
def LLLLLL():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/LLL.wav")
    pygame.mixer.music.play(1)
def lluvia():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lluvia.wav")
    pygame.mixer.music.play(1)
def lo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lo.wav")
    pygame.mixer.music.play(1)
def lobo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lobo.wav")
    pygame.mixer.music.play(1)
def loro():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/loro.wav")
    pygame.mixer.music.play(1)
def lu():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lu.wav")
    pygame.mixer.music.play(1)
def luna():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/luna.wav")
    pygame.mixer.music.play(1)
def lunallena():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/luna-llena.wav")
    pygame.mixer.music.play(1)
def lupa():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/lupa.wav")
    pygame.mixer.music.play(1)
def ma():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/ma.wav")
    pygame.mixer.music.play(1)
def madre():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/madre.wav")
    pygame.mixer.music.play(1)
def maleta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/maleta.wav")
    pygame.mixer.music.play(1)
def mama():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/mama.wav")
    pygame.mixer.music.play(1)
def manguera():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/manguera.wav")
    pygame.mixer.music.play(1)
def manilla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/.wav")
    pygame.mixer.music.play(1)
def manzana():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/manzana.wav")
    pygame.mixer.music.play(1)
def mariposa():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/mariposa.wav")
    pygame.mixer.music.play(1)
def me():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/me.wav")
    pygame.mixer.music.play(1)
def melon():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/melon.wav")
    pygame.mixer.music.play(1)
def mesa():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/mesa.wav")
    pygame.mixer.music.play(1)
def mi():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/mi.wav")
    pygame.mixer.music.play(1)
def microfono():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/microfono.wav")
    pygame.mixer.music.play(1)
def mina():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/mina.wav")
    pygame.mixer.music.play(1)
def MMMMMM():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/mmm.wav")
    pygame.mixer.music.play(1)
def mo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/mo.wav")
    pygame.mixer.music.play(1)
def mochila():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/mochila.wav")
    pygame.mixer.music.play(1)
def molino():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/molino.wav")
    pygame.mixer.music.play(1)
def mono():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/mono.wav")
    pygame.mixer.music.play(1)
def monstruo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/monstruo.wav")
    pygame.mixer.music.play(1)
def moto():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/moto.wav")
    pygame.mixer.music.play(1)
def mu():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/mu.wav")
    pygame.mixer.music.play(1)
def muleta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/muleta.wav")
    pygame.mixer.music.play(1)
def muñeca():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/muñeca.wav")
    pygame.mixer.music.play(1)
def murcielago():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/murcielago.wav")
    pygame.mixer.music.play(1)
def muybien1():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/muy-bien.wav")
    pygame.mixer.music.play(1)
def naranjilla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/naranjilla.wav")
    pygame.mixer.music.play(1)
def navidad():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/navidad.wav")
    pygame.mixer.music.play(1)
def oso():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/oso.wav")
    pygame.mixer.music.play(1)
def paloma():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/paloma.wav")
    pygame.mixer.music.play(1)
def pantera():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pantera.wav")
    pygame.mixer.music.play(1)
def payaso():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/payaso.wav")
    pygame.mixer.music.play(1)
def peces():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/peces.wav")
    pygame.mixer.music.play(1)
def pelea():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pelea.wav")
    pygame.mixer.music.play(1)
def pelo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audios/pelo.wav")
    pygame.mixer.music.play(1)
def pelota():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pelota.wav")
    pygame.mixer.music.play(1)
def pera():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pera.wav")
    pygame.mixer.music.play(1)
def pescado():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pezcado.wav")
    pygame.mixer.music.play(1)
def pez():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pez.wav")
    pygame.mixer.music.play(1)
def piedra():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/piedra.wav")
    pygame.mixer.music.play(1)
def piña():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/piña.wav")
    pygame.mixer.music.play(1)
def pirata():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pirata.wav")
    pygame.mixer.music.play(1)
def pito():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pito.wav")
    pygame.mixer.music.play(1)
def PLPLPLPLPLPL():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/PL.wav")
    pygame.mixer.music.play(1)
def pla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pla.wav")
    pygame.mixer.music.play(1)
def plato():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/plato.wav")
    pygame.mixer.music.play(1)
def playa():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/playa.wav")
    pygame.mixer.music.play(1)
def ple():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/ple.wav")
    pygame.mixer.music.play(1)
def pli():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pli.wav")
    pygame.mixer.music.play(1)
def plo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/plo.wav")
    pygame.mixer.music.play(1)
def plu():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/plu.wav")
    pygame.mixer.music.play(1)
def pluma():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pluma.wav")
    pygame.mixer.music.play(1)
def pollito():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pollito.wav")
    pygame.mixer.music.play(1)
def pozo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pozo.wav")
    pygame.mixer.music.play(1)
def PRPRPRPRPRPR():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pr.wav")
    pygame.mixer.music.play(1)
def pra():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pra.wav")
    pygame.mixer.music.play(1)
def pradera():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pradera.wav")
    pygame.mixer.music.play(1)
def pre():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pre.wav")
    pygame.mixer.music.play(1)
def premio():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/premio.wav")
    pygame.mixer.music.play(1)
def preso():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/preso.wav")
    pygame.mixer.music.play(1)
def pri():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pri.wav")
    pygame.mixer.music.play(1)
def princesa():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/princesa.wav")
    pygame.mixer.music.play(1)
def pro():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pro.wav")
    pygame.mixer.music.play(1)
def profesora():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/profesora.wav")
    pygame.mixer.music.play(1)
def pru():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/pru.wav")
    pygame.mixer.music.play(1)
def queso():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/queso.wav")
    pygame.mixer.music.play(1)
def ra():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/ra.wav")
    pygame.mixer.music.play(1)
def rama():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/rama.wav")
    pygame.mixer.music.play(1)
def raqueta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/raqueta.wav")
    pygame.mixer.music.play(1)
def raton():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/raton.wav")
    pygame.mixer.music.play(1)
def re():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/re.wav")
    pygame.mixer.music.play(1)
def red():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/red.wav")
    pygame.mixer.music.play(1)
def refrigeradora():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/refrigeradora.wav")
    pygame.mixer.music.play(1)
def regla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/regla.wav")
    pygame.mixer.music.play(1)
def reloj():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/reloj.wav")
    pygame.mixer.music.play(1)
def repitelaoracion():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/repite la oracion.wav")
    pygame.mixer.music.play(1)
def resbaladera():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/resbaladera.wav")
    pygame.mixer.music.play(1)
def ri():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/ri.wav")
    pygame.mixer.music.play(1)
def rie():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/rie.wav")
    pygame.mixer.music.play(1)
def rio():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/rio.wav")
    pygame.mixer.music.play(1)
def ro():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/ro.wav")
    pygame.mixer.music.play(1)
def rompecabezas():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/rompecabezas.wav")
    pygame.mixer.music.play(1)
def rosa():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/rosa.wav")
    pygame.mixer.music.play(1)
def RRRRRR():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/rrr.wav")
    pygame.mixer.music.play(1)
def ru():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/ru.wav")
    pygame.mixer.music.play(1)
def rueda():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/rueda.wav")
    pygame.mixer.music.play(1)
def sa():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/sa.wav")
    pygame.mixer.music.play(1)
def sable():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/sable.wav")
    pygame.mixer.music.play(1)
def sal():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/sal.wav")
    pygame.mixer.music.play(1)
def sandia():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/sandia.wav")
    pygame.mixer.music.play(1)
def se():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/se.wav")
    pygame.mixer.music.play(1)
def secadora():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/secadora.wav")
    pygame.mixer.music.play(1)
def señalalosdibujos():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/señala-las-imagenes-q-corresponden.wav")
    pygame.mixer.music.play(1)
def sepillo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/sepillo.wav")
    pygame.mixer.music.play(1)
def serpiente():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/serpiente.wav")
    pygame.mixer.music.play(1)
def si():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/si.wav")
    pygame.mixer.music.play(1)
def siesta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/siesta.wav")
    pygame.mixer.music.play(1)
def silla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/silla.wav")
    pygame.mixer.music.play(1)
def so():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/so.wav")
    pygame.mixer.music.play(1)
def sobre():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/sobre.wav")
    pygame.mixer.music.play(1)
def sol():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/sol.wav")
    pygame.mixer.music.play(1)
def sopla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/sopla.wav")
    pygame.mixer.music.play(1)
def SSSSSS():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/sss.wav")
    pygame.mixer.music.play(1)
def su():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/su.wav")
    pygame.mixer.music.play(1)
def sube():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/sube.wav")
    pygame.mixer.music.play(1)
def sucio():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/sucio.wav")
    pygame.mixer.music.play(1)
def ta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/ta.wav")
    pygame.mixer.music.play(1)
def tabla():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tabla.wav")
    pygame.mixer.music.play(1)
def tambor():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tambor.wav")
    pygame.mixer.music.play(1)
def taza():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/taza.wav")
    pygame.mixer.music.play(1)
def te():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/te.wav")
    pygame.mixer.music.play(1)
def telaraña():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/telaraña.wav")
    pygame.mixer.music.play(1)
def telefono():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/telefono.wav")
    pygame.mixer.music.play(1)
def teta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/teta.wav")
    pygame.mixer.music.play(1)
def ti():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/ti.wav")
    pygame.mixer.music.play(1)
def tijera():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tijera.wav")
    pygame.mixer.music.play(1)
def tigre():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tigre.wav")
    pygame.mixer.music.play(1)
def timbre():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/timbre.wav")
    pygame.mixer.music.play(1)
def to():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/to.wav")
    pygame.mixer.music.play(1)
def tocaimagenrepite():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/toca-imagen-repite.wav")
    pygame.mixer.music.play(1)
def tomate():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tomate.wav")
    pygame.mixer.music.play(1)
def topo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/topo.wav")
    pygame.mixer.music.play(1)
def torero():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/torero.wav")
    pygame.mixer.music.play(1)
def toro():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/toro.wav")
    pygame.mixer.music.play(1)
def torta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/torta.wav")
    pygame.mixer.music.play(1)
def tortuga():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tortuga.wav")
    pygame.mixer.music.play(1)
def TRTRTRTRTRTR():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tr.wav")
    pygame.mixer.music.play(1)
def tra():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tra.wav")
    pygame.mixer.music.play(1)
def tre():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tre.wav")
    pygame.mixer.music.play(1)
def trebol():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/trebol.wav")
    pygame.mixer.music.play(1)
def tren():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tren.wav")
    pygame.mixer.music.play(1)
def tri():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tri.wav")
    pygame.mixer.music.play(1)
def triangulo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/triangulo.wav")
    pygame.mixer.music.play(1)
def tro():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tro.wav")
    pygame.mixer.music.play(1)
def trompeta():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/trompeta.wav")
    pygame.mixer.music.play(1)
def tru():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tru.wav")
    pygame.mixer.music.play(1)
def TTTTTT():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/ttt.wav")
    pygame.mixer.music.play(1)
def tu():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tu.wav")
    pygame.mixer.music.play(1)
def tubo():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tubo.wav")
    pygame.mixer.music.play(1)
def tucan():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tucan.wav")
    pygame.mixer.music.play(1)
def tunel():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/tunel.wav")
    pygame.mixer.music.play(1)
def uña():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/uña.wav")
    pygame.mixer.music.play(1)
def uva():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/uva.wav")
    pygame.mixer.music.play(1)
def vamosacontarcuento():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/vamos-a-contar-cuento.wav")
    pygame.mixer.music.play(1)
def vela():
    pygame.mixer.music.load("/home/pi/Desktop/tesis/audio/vela.wav")
    pygame.mixer.music.play(1)


#FUNCION DRAG AND DROP
class CreateCanvasObject(object):
    def __init__(self, canvas, image_name, xpos, ypos):
        self.canvas = canvas
        self.image_name = image_name
        self.xpos, self.ypos = xpos, ypos
 
        self.tk_image = tk.PhotoImage(
            file="{}{}".format(IMAGE_PATH, image_name))
        self.image_obj= canvas.create_image(
            xpos, ypos, image=self.tk_image)
         
        canvas.tag_bind(self.image_obj, '<Button1-Motion>', self.move)
        canvas.tag_bind(self.image_obj, '<ButtonRelease-1>', self.release)
        self.move_flag = False
        
    def move(self, event):
        if self.move_flag:
            new_xpos, new_ypos = event.x, event.y
             
            self.canvas.move(self.image_obj,
                new_xpos-self.mouse_xpos ,new_ypos-self.mouse_ypos)
            
            self.mouse_xpos = new_xpos
            self.mouse_ypos = new_ypos
        else:
            self.move_flag = True
            self.canvas.tag_raise(self.image_obj)
            self.mouse_xpos = event.x
            self.mouse_ypos = event.y

              #letra r  
        if(numerodeimagenes==10):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo2()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo2()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo2()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo2()
            if(self.image_obj==9):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo2()
            if(self.image_obj==10):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
        #letra t      
        if(numerodeimagenes==11):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo4()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo4()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo4()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo4()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==9):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==10):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo4()
        #letra l
        
        if(numerodeimagenes==12):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo5()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo5()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
                            
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo5()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo5()
            if(self.image_obj==9):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==10):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
        #letra s
        if(numerodeimagenes==8):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            intentalodenuevo3()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo3()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo3()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo3()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo3()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo3()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
        #letra m
        if(numerodeimagenes==9):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            intentalodenuevo6()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo6()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo6()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo6()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==9):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo6()
        #letra bl
        if(numerodeimagenes==13):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo7()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo7()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo7()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo7()

        #letra cl
        if(numerodeimagenes==14):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            intentalodenuevo8()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo8()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo8()
            
        #letra fl
        if(numerodeimagenes==15):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo9()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo9()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo9()
            
        #letra gl
        if(numerodeimagenes==16):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            intentalodenuevo10()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo10()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo10()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo10()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            
        #letra pl
        if(numerodeimagenes==17):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            intentalodenuevo11()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo11()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo11()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo11()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo11()
#letra br
        if(numerodeimagenes==18):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo12()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo12()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo12()
            if(self.image_obj==9):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo12()
 
#letra cr
        if(numerodeimagenes==19):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            intentalodenuevo13()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo13()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo13()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo13()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==9):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo13()
            if(self.image_obj==10):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo13()
#letra dr
        if(numerodeimagenes==20):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            intentalodenuevo14()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo14()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo14()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo14()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==9):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo14()
            if(self.image_obj==10):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo14()
#letra fr
        if(numerodeimagenes==21):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            intentalodenuevo15()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo15()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo15()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo15()
            if(self.image_obj==9):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo15()
            if(self.image_obj==10):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo15()
#letra gr
        if(numerodeimagenes==22):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo16()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo16()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo16()

#letra pr
        if(numerodeimagenes==23):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            intentalodenuevo17()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo17()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo17()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo17()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()

#letra tr
        if(numerodeimagenes==24):
            if(self.image_obj==1):
                if(event.x>325):
                    if(event.x<500):
                        if(event.y>380):
                            intentalodenuevo19()
            if(self.image_obj==2):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo19()
            if(self.image_obj==3):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo19()
                                                         
            if(self.image_obj==4):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo19()
            if(self.image_obj==5):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo19()
            if(self.image_obj==6):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==7):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==8):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==9):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            muybien1()
            if(self.image_obj==10):
                if(event.x>300):
                    if(event.x<525):
                        if(event.y>380):
                            intentalodenuevo19()

 
    def release(self, event):
        self.move_flag = False
                     
class Application(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)
        
        self.canvas = tk.Canvas(self,bg='white')
        self.canvas.pack(fill="both", expand=True)
        #letra r
        if (numerodeimagenes==10):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 100, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 250, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 400, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 550, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 700, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 100, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 250, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 400, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_9 =CreateCanvasObject(self.canvas, q9, 550, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_10 =CreateCanvasObject(self.canvas, q10, 700, 200)
        #letra s
        if (numerodeimagenes==8):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 150, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 350, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 500, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 650, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 150, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 350, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 500, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 650, 200)
            #letra t
        if (numerodeimagenes==11):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 100, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 250, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 400, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 550, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 700, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 100, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 250, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 400, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_9 =CreateCanvasObject(self.canvas, q9, 550, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_10 =CreateCanvasObject(self.canvas, q10, 700, 200)
            #letra l
        if (numerodeimagenes==12):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 100, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 250, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 400, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 550, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 700, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 100, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 250, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 400, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_9 =CreateCanvasObject(self.canvas, q9, 550, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_10 =CreateCanvasObject(self.canvas, q10, 700, 200)
            #letra m
        if (numerodeimagenes==9):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 100, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 250, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 400, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 550, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 700, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 100, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 250, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 400, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_9 =CreateCanvasObject(self.canvas, q9, 550, 200)
        #letra bl
        if (numerodeimagenes==13):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 100, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 250, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 400, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 550, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 700, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 100, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 250, 200)
#letra cl
        if (numerodeimagenes==14):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 100, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 250, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 400, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 550, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 700, 75)
#letra fl
        if (numerodeimagenes==15):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 100, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 250, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 400, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 550, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 700, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 100, 200)
#letra gl
        if (numerodeimagenes==16):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 150, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 350, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 500, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 650, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 150, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 350, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 500, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 650, 200)
#letra pl
        if (numerodeimagenes==17):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 150, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 300, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 450, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 600, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 150, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 300, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 450, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 600, 200)
#letra br
        if (numerodeimagenes==18):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 100, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 250, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 400, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 550, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 700, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 100, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 250, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 400, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_9 =CreateCanvasObject(self.canvas, q9, 550, 200)
        #letra cr
        if (numerodeimagenes==19):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 100, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 250, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 400, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 550, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 700, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 100, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 250, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 400, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_9 =CreateCanvasObject(self.canvas, q9, 550, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_10 =CreateCanvasObject(self.canvas, q10, 700, 200)
        #letra dr
        if (numerodeimagenes==20):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 100, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 250, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 400, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 550, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 700, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 100, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 250, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 400, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_9 =CreateCanvasObject(self.canvas, q9, 550, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_10 =CreateCanvasObject(self.canvas, q10, 700, 200)
        #letra fr
        if (numerodeimagenes==21):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 100, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 250, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 400, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 550, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 700, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 100, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 250, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 400, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_9 =CreateCanvasObject(self.canvas, q9, 550, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_10 =CreateCanvasObject(self.canvas, q10, 700, 200)
        #letra gr
        if (numerodeimagenes==22):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 150, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 300, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 450, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 600, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 150, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 300, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 450, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 600, 200)

        #letra pr
        if (numerodeimagenes==23):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 150, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 300, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 450, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 600, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 150, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 300, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 450, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 600, 200)

        #letra tr
        if (numerodeimagenes==24):
            self.canvas.bind("<Button-1>", callback2)
            self.image_1 = CreateCanvasObject(self.canvas, q, 100, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_2 =CreateCanvasObject(self.canvas, q2, 250, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_3 =CreateCanvasObject(self.canvas, q3, 400, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_4 =CreateCanvasObject(self.canvas, q4, 550, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_5 =CreateCanvasObject(self.canvas, q5, 700, 75)
            self.canvas.bind("<Button-1>", callback2)
            self.image_6 =CreateCanvasObject(self.canvas, q6, 100, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_7 =CreateCanvasObject(self.canvas, q7, 250, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_8 =CreateCanvasObject(self.canvas, q8, 400, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_9 =CreateCanvasObject(self.canvas, q9, 550, 200)
            self.canvas.bind("<Button-1>", callback2)
            self.image_10 =CreateCanvasObject(self.canvas, q10, 700, 200)
        
def callback(event):
    if (event.x>0):
        muybien.destroy()
def callback3(event):
    if (event.x>0):
        entrar()
def callback1(event):
    if (event.x>0):
        muymal.destroy()
def callback2(event):
    if(numerodeaudios==1):
        if (event.x>50):
            if (event.x<150):
                if (event.y>25):
                    if (event.y<125):
                        pygame.mixer.music.load(sonido)
                        pygame.mixer.music.play(1)
                    
        if (event.x>200):
            if (event.x<300):
                if (event.y>25):
                    if (event.y<125):
                        pygame.mixer.music.load(sonido2)
                        pygame.mixer.music.play(1)

        if (event.x>350):
            if (event.x<450):
                if (event.y>25):
                    if (event.y<125):
                        pygame.mixer.music.load(sonido3)
                        pygame.mixer.music.play(1)
                    
        if (event.x>500):
            if (event.x<600):
                if (event.y>25):
                    if (event.y<125):
                        pygame.mixer.music.load(sonido4)
                        pygame.mixer.music.play(1)

        if (event.x>650):
            if (event.x<750):
                if (event.y>25):
                    if (event.y<125):
                        pygame.mixer.music.load(sonido5)
                        pygame.mixer.music.play(1)

        if (event.x>50):
            if (event.x<150):
                if (event.y>150):
                    if (event.y<250):
                        pygame.mixer.music.load(sonido6)
                        pygame.mixer.music.play(1)
                    
        if (event.x>200):
            if (event.x<300):
                if (event.y>150):
                    if (event.y<250):
                        pygame.mixer.music.load(sonido7)
                        pygame.mixer.music.play(1)

        if (event.x>350):
            if (event.x<450):
                if (event.y>150):
                    if (event.y<250):
                        pygame.mixer.music.load(sonido8)
                        pygame.mixer.music.play(1)

        if (event.x>500):
            if (event.x<600):
                if (event.y>150):
                    if (event.y<250):
                        pygame.mixer.music.load(sonido9)
                        pygame.mixer.music.play(1)

        if (event.x>650):
            if (event.x<750):
                if (event.y>150):
                    if (event.y<250):
                        pygame.mixer.music.load(sonido10)
                        pygame.mixer.music.play(1)
    if(numerodeaudios==2):
        if (event.x>100):
            if (event.x<200):
                if (event.y>25):
                    if (event.y<125):
                        pygame.mixer.music.load(sonido)
                        pygame.mixer.music.play(1)
                    
        if (event.x>250):
            if (event.x<350):
                if (event.y>25):
                    if (event.y<125):
                        pygame.mixer.music.load(sonido2)
                        pygame.mixer.music.play(1)

        if (event.x>400):
            if (event.x<500):
                if (event.y>25):
                    if (event.y<125):
                        pygame.mixer.music.load(sonido3)
                        pygame.mixer.music.play(1)
                    
        if (event.x>550):
            if (event.x<650):
                if (event.y>25):
                    if (event.y<125):
                        pygame.mixer.music.load(sonido4)
                        pygame.mixer.music.play(1)

        if (event.x>100):
            if (event.x<200):
                if (event.y>150):
                    if (event.y<250):
                        pygame.mixer.music.load(sonido5)
                        pygame.mixer.music.play(1)

        if (event.x>250):
            if (event.x<350):
                if (event.y>150):
                    if (event.y<250):
                        pygame.mixer.music.load(sonido6)
                        pygame.mixer.music.play(1)
                    
        if (event.x>400):
            if (event.x<500):
                if (event.y>150):
                    if (event.y<250):
                        pygame.mixer.music.load(sonido7)
                        pygame.mixer.music.play(1)

        if (event.x>550):
            if (event.x<650):
                if (event.y>150):
                    if (event.y<250):
                        pygame.mixer.music.load(sonido8)
                        pygame.mixer.music.play(1)
    

                    
    

#MUY BIEN
def muybienhecho():
    muybien1()
    global muybien
    muybien=tix.Toplevel()
    muybien.geometry("800x480")
    muybien.config(bg="gray88")
    muybien.attributes("-fullscreen", True)
    lbl = ImageLabel(muybien)
    lbl.bind("<Button-1>", callback)
    lbl.pack()
    lbl.load('/home/pi/Desktop/tesis/gestos/Alegria.gif')
    muybien.mainloop()

#MUY MAL
def muymalhecho():
    intentalootravez()
    global muymal
    muymal=tix.Toplevel()
    muymal.geometry("800x480")
    muymal.config(bg="gray88")
    muymal.attributes("-fullscreen", True)
    lbl = ImageLabel(muymal)
    lbl.bind("<Button-1>", callback1)
    lbl.pack()
    lbl.load('/home/pi/Desktop/tesis/gestos/tristeza/tristeza.gif')
    muymal.mainloop()

#color aleatorio letras drag and drop

def coloraleatorio():
    global colorboton
    ale=randint(1, 20)
    if (ale==1):
        colorboton='pink'
    if (ale==2):
        colorboton='sky blue'
    if (ale==3):
        colorboton='light yellow'
    if (ale==4):
        colorboton='light cyan'
    if (ale==5):
        colorboton='pink'
    if (ale==6):
        colorboton='pink'
    if (ale==7):
        colorboton='azure'
    if (ale==8):
        colorboton='rosybrown'
    if (ale==9):
        colorboton='olivedrab2'
    if (ale==10):
        colorboton='plum2'
    if (ale==11):
        colorboton='salmon'
    if (ale==12):
        colorboton='lemon chiffon'
    if (ale==13):
        colorboton='navajo white'
    if (ale==14):
        colorboton='tomato2'
    if (ale==15):
        colorboton='gold2'
    if (ale==16):
        colorboton='light goldenrod'
    if (ale==17):
        colorboton='cyan2'
    if (ale==18):
        colorboton='mediumorchid1'
    if (ale==19):
        colorboton='brown1'
    if (ale==20):
        colorboton='orange'

    global colorboton2
    ale2=randint(1, 20)
    if (ale2==2):
        colorboton2='pink'
    if (ale2==3):
        colorboton2='sky blue'
    if (ale2==4):
        colorboton2='light yellow'
    if (ale2==5):
        colorboton2='light cyan'
    if (ale2==6):
        colorboton2='pink'
    if (ale2==7):
        colorboton2='pink'
    if (ale2==8):
        colorboton2='azure'
    if (ale2==9):
        colorboton2='rosybrown'
    if (ale2==10):
        colorboton2='olivedrab2'
    if (ale2==11):
        colorboton2='plum2'
    if (ale2==12):
        colorboton2='salmon'
    if (ale2==13):
        colorboton2='lemon chiffon'
    if (ale2==14):
        colorboton2='navajo white'
    if (ale2==15):
        colorboton2='tomato2'
    if (ale2==16):
        colorboton2='gold2'
    if (ale2==17):
        colorboton2='light goldenrod'
    if (ale2==18):
        colorboton2='cyan2'
    if (ale2==19):
        colorboton2='mediumorchid1'
    if (ale2==20):
        colorboton2='brown1'
    if (ale2==1):
        colorboton2='orange'

    global colorboton3
    ale3=randint(1, 20)
    if (ale3==3):
        colorboton3='pink'
    if (ale3==4):
        colorboton3='sky blue'
    if (ale3==5):
        colorboton3='light yellow'
    if (ale3==6):
        colorboton3='light cyan'
    if (ale3==7):
        colorboton3='pink'
    if (ale3==8):
        colorboton3='pink'
    if (ale3==9):
        colorboton3='azure'
    if (ale3==10):
        colorboton3='rosybrown'
    if (ale3==11):
        colorboton3='olivedrab2'
    if (ale3==12):
        colorboton3='plum2'
    if (ale3==13):
        colorboton3='salmon'
    if (ale3==14):
        colorboton3='lemon chiffon'
    if (ale3==15):
        colorboton3='navajo white'
    if (ale3==16):
        colorboton3='tomato2'
    if (ale3==17):
        colorboton3='gold2'
    if (ale3==18):
        colorboton3='light goldenrod'
    if (ale3==19):
        colorboton3='cyan2'
    if (ale3==20):
        colorboton3='mediumorchid1'
    if (ale3==1):
        colorboton3='brown1'
    if (ale3==2):
        colorboton3='orange'
    global colorboton4
    ale4=randint(1, 20)
    if (ale4==4):
        colorboton4='pink'
    if (ale4==5):
        colorboton4='sky blue'
    if (ale4==6):
        colorboton4='light yellow'
    if (ale4==7):
        colorboton4='light cyan'
    if (ale4==8):
        colorboton4='pink'
    if (ale4==9):
        colorboton4='pink'
    if (ale4==10):
        colorboton4='azure'
    if (ale4==11):
        colorboton4='rosybrown'
    if (ale4==12):
        colorboton4='olivedrab2'
    if (ale4==13):
        colorboton4='plum2'
    if (ale4==14):
        colorboton4='salmon'
    if (ale4==15):
        colorboton4='lemon chiffon'
    if (ale4==16):
        colorboton4='navajo white'
    if (ale4==17):
        colorboton4='tomato2'
    if (ale4==18):
        colorboton4='gold2'
    if (ale4==19):
        colorboton4='light goldenrod'
    if (ale4==20):
        colorboton4='cyan2'
    if (ale4==1):
        colorboton4='mediumorchid1'
    if (ale4==2):
        colorboton4='brown1'
    if (ale4==3):
        colorboton4='orange'
    

          

#MENU LETRA R

def entrarR():
    menu.destroy()
    menuR2()
def menuR2():
    repiteelsonido()
    global R1
    R1=tix.Tk()
    R1.geometry("800x480")
    R1.config(bg="white")
    R1.attributes("-fullscreen", True)
    imR1=PhotoImage(file="/home/pi/Desktop/tesis/imagen/Rlabios.png", master=R1)
    imR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=R1)
    imR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=R1)
    letrar=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/r.png", master=R1)
    letrar2=Label(R1,image=letrar,height=100, width=100, bg="white").place(x=365,y=20)
    botonR1=Button(R1, image=imR1, command=RRRRRR, height=125, width=125).place(x=350,y=120)
    siguienteR1=tix.Button(R1,text="Siguiente",command=entrarmenuR,width=20, height=3).place(x=590,y=300)
    regresarR1=tix.Button(R1,text="Regresar",command=regresarmenuR2,width=20, height=3).place(x=30,y=300)
    siguienteR12=tix.Button(R1,image=imR2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarR12=tix.Button(R1,image=imR3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    R1.mainloop()
def entrarmenuR():
    pygame.mixer.music.pause()
    R1.destroy()
    menuR1()
def menuR1():
    coloraleatorio()
    coloraleatorio()
    global menuR
    menuR=tix.Tk()
    menuR.geometry("800x480")
    menuR.config(bg='white')
    menuR.attributes("-fullscreen", True)
    silabaR= tix.Button(menuR,text="Silabas",command=entrarsilabasR,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasR= tix.Button(menuR,text="Palabras",command=entrarpalabrasR,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenR= tix.Button(menuR,text="Discriminacion Fonetica",command=entrarmenuimagenR,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoR= tix.Button(menuR,text="Cuento",command=entrarmenucuentoR,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirR= tix.Button(menuR,text="Regresar",command=regresarmenuR1,width=20, height=3).place(x=600,y=350)
    menuR.mainloop()
def entrarmenucuentoR():
    menuR.destroy()
    menucuentoR()
def entrarsilabasR():
    menuR.destroy()
    SilabaR1()
def SilabaR1():
    escucharsilabas()
    global silabaR
    silabaR=tix.Tk()
    silabaR.geometry("800x480")
    silabaR.config(bg="white")
    silabaR.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/silabas/ra.png", master=silabaR)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/silabas/re.png", master=silabaR)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/silabas/ri.png", master=silabaR)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/silabas/ro.png", master=silabaR)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/silabas/ru.png", master=silabaR)
    imR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaR)
    imR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaR)
    siguienteR12=tix.Button(silabaR,image=imR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarR12=tix.Button(silabaR,image=imR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaR, image=r11, command=ra, height=150, width=150).place(x=50,y=50)
    re1=Button(silabaR, image=r12, command=re, height=150, width=150).place(x=250,y=50)
    ri1=Button(silabaR, image=r13, command=ri, height=150, width=150).place(x=450,y=50)
    ro1=Button(silabaR, image=r14, command=ro, height=150, width=150).place(x=50,y=250)
    ru1=Button(silabaR, image=r15, command=ru, height=150, width=150).place(x=250,y=250)
    regresarR1=Button(silabaR,text="Regresar",command=regresarmenuR3,width=15, height=10).place(x=450,y=250)
    silabaR.mainloop()
def regresarmenuR3():
    pygame.mixer.music.pause()
    silabaR.destroy()
    menuR1()
def entrarpalabrasR():
    menuR.destroy()
    tocaimagenrepite()
    menupalabrasR1()
def menupalabrasR1():
    global palabrasR1
    palabrasR1=tix.Tk()
    palabrasR1.geometry("800x480")
    palabrasR1.config(bg="white")
    palabrasR1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/1raton.png", master=palabrasR1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/2raqueta.png", master=palabrasR1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/3reloj.png", master=palabrasR1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/4resbaladera.png", master=palabrasR1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/5red.png", master=palabrasR1)
    palabrar16=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/6rio.png", master=palabrasR1)
    palabrar17=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/7rompe.png", master=palabrasR1)
    palabrar18=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/9rueda.png", master=palabrasR1)
    palabrar19=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/8rueda.png", master=palabrasR1)
    palabrar110=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/10rama.png", master=palabrasR1)
    imR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasR1)
    imR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasR1)
    palabrasr11=Button(palabrasR1, image=palabrar11, command=raton, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasR1, image=palabrar12, command=raqueta, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasR1, image=palabrar13, command=reloj, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasR1, image=palabrar14, command=resbaladera, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasR1, image=palabrar15, command=red, height=125, width=125,bg="white").place(x=620,y=10)
    palabrasr16=Button(palabrasR1, image=palabrar16, command=rio, height=125, width=125,bg="white").place(x=20,y=145)
    palabrasr17=Button(palabrasR1, image=palabrar17, command=rompecabezas, height=125, width=125,bg="white").place(x=170,y=145)
    palabrasr18=Button(palabrasR1, image=palabrar18, command=rosa, height=125, width=125,bg="white").place(x=320,y=145)
    palabrasr19=Button(palabrasR1, image=palabrar19, command=rueda, height=125, width=125,bg="white").place(x=470,y=145)
    palabrasr110=Button(palabrasR1, image=palabrar110, command=rama, height=125, width=125,bg="white").place(x=620,y=145)
    siguienteR11=Button(palabrasR1,text="Siguiente",command=entrarpalabrasR1,width=20, height=3).place(x=230,y=420)
    regresarR11=Button(palabrasR1,text="Regresar",command=regresarmenuR4,width=20, height=3).place(x=30,y=420)
    siguienteR12=tix.Button(palabrasR1,image=imR2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarR12=tix.Button(palabrasR1,image=imR3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasR1.mainloop()
def entrarpalabrasR1():
    pygame.mixer.music.pause()
    palabrasR1.destroy()
    menupalabrasR2()
def regresarmenuR4():
    pygame.mixer.music.pause()
    palabrasR1.destroy()
    menuR1()
def menupalabrasR2():
    global palabrasR2
    palabrasR2=tix.Tk()
    palabrasR2.geometry("800x480")
    palabrasR2.config(bg="white")
    palabrasR2.attributes("-fullscreen", True)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/17caramelo.png", master=palabrasR2)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/18loro.png", master=palabrasR2)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/19flor.png", master=palabrasR2)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/20doctora.png", master=palabrasR2)
    palabrar110=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/11pera.png", master=palabrasR2)
    palabrar111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/12tijera.png", master=palabrasR2)
    palabrar112=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/13maestra.png", master=palabrasR2)
    palabrar113=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/14dinero.png", master=palabrasR2)
    palabrar114=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/15toro.png", master=palabrasR2)
    palabrar115=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/palabras/16torero.png", master=palabrasR2)
    imR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasR2)
    imR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasR2)
    palabrasr12=Button(palabrasR2, image=palabrar110, command=pera, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr13=Button(palabrasR2, image=palabrar115, command=torero, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr14=Button(palabrasR2, image=palabrar111, command=sobre, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr15=Button(palabrasR2, image=palabrar13, command=mariposa, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr110=Button(palabrasR2, image=palabrar114, command=toro, height=125, width=125,bg="white").place(x=620,y=10)
    palabrasr111=Button(palabrasR2, image=palabrar12, command=caminar, height=125, width=125,bg="white").place(x=20,y=145)
    palabrasr112=Button(palabrasR2, image=palabrar15, command=peru, height=125, width=125,bg="white").place(x=170,y=145)
    palabrasr113=Button(palabrasR2, image=palabrar112, command=numero, height=125, width=125,bg="white").place(x=320,y=145)
    palabrasr114=Button(palabrasR2, image=palabrar113, command=tambor, height=125, width=125,bg="white").place(x=470,y=145)
    ##palabrasr115=Button(palabrasR2, image=palabrar115, command=torero, height=125, width=125,bg="white").place(x=620,y=145)
    siguienteR11=Button(palabrasR2,text="Finalizar",command=regresarmenuR5,width=20, height=3).place(x=230,y=420)
    regresarR11=Button(palabrasR2,text="Regresar",command=regresarpalabrasR2,width=20, height=3).place(x=30,y=420)
    siguienteR12=tix.Button(palabrasR2,image=imR2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarR12=tix.Button(palabrasR2,image=imR3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasR2.mainloop()
def regresarpalabrasR2():
    pygame.mixer.music.pause()
    palabrasR2.destroy()
    menupalabrasR1()
def regresarmenuR5():
    pygame.mixer.music.pause()
    palabrasR2.destroy()
    menuR1()
def intentalodenuevo2():
    global contador
    a.destroy()
    contador=2
    menuimagenR()
def entrarmenuimagenR():
    global contador
    contador=1
    menuR.destroy()
    menuimagenR()
def regresarmenuR6():
    pygame.mixer.music.pause()
    a.destroy()
    menuR1()
def menuimagenR():
    coloraleatorio()
    if (contador==1):
        llevaimagenesr()
    if (contador==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=1
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=10
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaR/imagenes/"
    q="1ir.png"
    q2="2ir.png"
    q3="3ir.png"
    q4="4ir.png"
    q5="5ir.png"
    q6="6ir.png"
    q7="7ir.png"
    q8="8ir.png"
    q9="9ir.png"
    q10="10ir.png"
    sonido="/home/pi/Desktop/tesis/audio/araña.wav"
    sonido2="/home/pi/Desktop/tesis/audio/raton.wav"
    sonido3="/home/pi/Desktop/tesis/audio/avion.wav"
    sonido4="/home/pi/Desktop/tesis/audio/caramelo.wav"
    sonido5="/home/pi/Desktop/tesis/audio/guineo.wav"
    sonido6="/home/pi/Desktop/tesis/audio/gallo.wav"
    sonido7="/home/pi/Desktop/tesis/audio/pera.wav"
    sonido8="/home/pi/Desktop/tesis/audio/blusa.wav"
    sonido9="/home/pi/Desktop/tesis/audio/caja.wav"
    sonido10="/home/pi/Desktop/tesis/audio/rueda.wav"
    a = tk.Tk()
    a.title("DRAG AND DROP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuR6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="R",  height=3, width=10, bg=colorboton,font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
def menucuentoR():
    global cuentoR
    cuentoR=tix.Tk()
    vamosacontarcuento()
    cuentoR.geometry("800x480")
    cuentoR.config(bg="white")
    cuentoR.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/CuentoR/1cuentor.png", master=cuentoR)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/CuentoR/2cuentor.png", master=cuentoR)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/CuentoR/3cuentor.png", master=cuentoR)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/CuentoR/4cuentor.png", master=cuentoR)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/CuentoR/5cuentor.png", master=cuentoR)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/CuentoR/6cuentor.png", master=cuentoR)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/CuentoR/7cuentor.png", master=cuentoR)
    cuento181=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/CuentoR/8cuentor.png", master=cuentoR)
    cuento191=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/CuentoR/9cuentor.png", master=cuentoR)
    cuento112=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/CuentoR/10cuentor.png", master=cuentoR)
    cuento113=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaR/CuentoR/11cuentor.png", master=cuentoR)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoR)
    cuento1=Label(cuentoR, text="En un lugar lleno de",height=3, width=15,font=("Helvetica",12), bg="white").place(x=20,y=20)
    cuento2=Button(cuentoR, image=cuento111, command=rosa, height=50, width=50).place(x=160,y=20)
    cuento3=Label(cuentoR, text="y", height=3, width=1,font=("Helvetica",12), bg="white").place(x=205,y=20)
    cuento4=Button(cuentoR, image=cuento121, command=girasol ,height=50, width=50).place(x=223,y=20)
    cuento5=Label(cuentoR, text="vivia el",  height=3, width=7,font=("Helvetica",12), bg="white").place(x=270,y=20)
    cuento6=Button(cuentoR, image=cuento131, command=loro, height=50, width=50).place(x=330,y=20)
    cuento7=Label(cuentoR, text="Sapay. Todas las mañanas se posaba sobre la", height=3, width=38,font=("Helvetica",12), bg="white").place(x=385,y=20)
    cuento8=Button(cuentoR, image=cuento141, command=rama ,height=50, width=50).place(x=730,y=20)
    cuento9=Label(cuentoR, text="del", height=3, width=3,font=("Helvetica",12), bg="white").place(x=20,y=90)
    cuento10=Button(cuentoR, image=cuento151, command=arbol,height=50, width=50).place(x=60,y=90)
    cuento11=Label(cuentoR, text="de capulí. Desde allí,  miraba al inquieto", height=3, width=31,font=("Helvetica",12), bg="white").place(x=120,y=90)
    cuento12=Button(cuentoR, image=cuento161 ,command=raton ,height=50, width=50).place(x=400,y=90)
    cuento13=Label(cuentoR, text="subir y bajar la", height=3, width=12,font=("Helvetica",12), bg="white").place(x=450,y=90)
    cuento14=Button(cuentoR, image=cuento171, command=resbaladera, height=50, width=50).place(x=560,y=90)
    cuento15=Label(cuentoR, text="del parque. Muy triste,", height=3,width=20,font=("Helvetica",12), bg="white").place(x=610,y=90)
    cuento16=Label(cuentoR, text="se puso cuando vió que su amigo", height=3, width=28,font=("Helvetica",12), bg="white").place(x=20,y=160)
    cuento17=Button(cuentoR, image=cuento181, command=toro, height=50, width=50).place(x=265,y=160)
    cuento18=Label(cuentoR, text="iba a ser sacrificado por él", height=3, width=21,font=("Helvetica",12), bg="white").place(x=314,y=160)
    cuento20=Button(cuentoR, image=cuento191, command=torero, height=50, width=50).place(x=510,y=160)
    cuento18=Label(cuentoR, text=". Alto, señor", height=3, width=9,font=("Helvetica",12), bg="white").place(x=575,y=160)
    cuento20=Button(cuentoR, image=cuento191, command=torero, height=50, width=50).place(x=660,y=160)
    cuento18=Label(cuentoR, text="dijo el", height=3, width=7,font=("Helvetica",12), bg="white").place(x=715,y=160)
    cuento20=Button(cuentoR, image=cuento131, command=loro, height=50, width=50).place(x=20,y=230)
    cuento18=Label(cuentoR, text="yo te doy todo mi", height=3, width=15,font=("Helvetica",12), bg="white").place(x=80,y=230)
    cuento20=Button(cuentoR, image=cuento112, command=dinero, height=50, width=50).place(x=220,y=230)
    cuento18=Label(cuentoR, text="y si es necesario mi", height=3, width=16,font=("Helvetica",12), bg="white").place(x=280,y=230)
    cuento20=Button(cuentoR, image=cuento113, command=corazon, height=50, width=50).place(x=430,y=230)
    cuento18=Label(cuentoR, text=", pero no mate a mi amigo el grandulón.", height=3, width=31,font=("Helvetica",12), bg="white").place(x=500,y=230)
    cuento21=Button(cuentoR, text="Regresar", command=regresarmenuR7, height=3, width=10).place(x=20,y=320)
    c50=Button(cuentoR, image=cuento188, command=cuentoRRRRRR, height=50, width=50).place(x=700,y=320)
    cuentoR.mainloop()
def regresarmenuR7():
    cuentoR.destroy()
    pygame.mixer.music.pause()
    menuR1()


#MENU LETSA S

def entrarS():
    menu.destroy()
    menuS2()
def menuS2():
    escuchayrepite()
    global S1
    S1=tix.Tk()
    S1.geometry("800x480")
    S1.config(bg="white")
    S1.attributes("-fullscreen", True)
    imS1=PhotoImage(file="/home/pi/Desktop/tesis/imagen/Slabios.png", master=S1)
    imS2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=S1)
    imS3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=S1)
    letrar=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/s.png", master=S1)
    letrar2=Label(S1,image=letrar,height=100, width=100, bg="white").place(x=365,y=20)
    botonS1=Button(S1, image=imS1, command=SSSSSS, height=125, width=125).place(x=350,y=120)
    siguienteS1=tix.Button(S1,text="Siguiente",command=entrarmenuS,width=20, height=3).place(x=600,y=300)
    regresarS1=tix.Button(S1,text="Regresar",command=regresarmenuS2,width=20, height=3).place(x=30,y=300)
    siguienteS12=tix.Button(S1,image=imS2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarS12=tix.Button(S1,image=imS3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    S1.mainloop()
def entrarmenuS():
    pygame.mixer.music.pause()
    S1.destroy()
    menuS1()
def menuS1():
    coloraleatorio()
    global menuS
    menuS=tix.Tk()
    menuS.geometry("800x480")
    menuS.config(bg="white")
    menuS.attributes("-fullscreen", True)
    silabaS= tix.Button(menuS,text="Silabas",command=entrarsilabasS,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasS= tix.Button(menuS,text="Palabras",command=entrarpalabrasS,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenS= tix.Button(menuS,text="Discriminacion Fonetica",command=entrarmenuimagenS,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoS= tix.Button(menuS,text="Cuento",command=entrarmenucuentoS,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirS= tix.Button(menuS,text="Regresar",command=regresarmenuS1,width=23, height=3).place(x=600,y=350)
    menuS.mainloop()
def entrarmenucuentoS():
    menuS.destroy()
    menucuentoS()
def entrarsilabasS():
    menuS.destroy()
    SilabaS1()
def SilabaS1():
    escucharsilabas()
    global silabaS
    silabaS=tix.Tk()
    silabaS.geometry("800x480")
    silabaS.config(bg="white")
    silabaS.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/silabas/sa.png", master=silabaS)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/silabas/se.png", master=silabaS)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/silabas/si.png", master=silabaS)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/silabas/so.png", master=silabaS)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/silabas/su.png", master=silabaS)
    imS2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaS)
    imS3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaS)
    siguienteS12=tix.Button(silabaS,image=imS2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarS12=tix.Button(silabaS,image=imS3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaS, image=r11, command=sa, height=150, width=150).place(x=50,y=50)
    re1=Button(silabaS, image=r12, command=se, height=150, width=150).place(x=250,y=50)
    ri1=Button(silabaS, image=r13, command=si, height=150, width=150).place(x=450,y=50)
    ro1=Button(silabaS, image=r14, command=so, height=150, width=150).place(x=50,y=250)
    ru1=Button(silabaS, image=r15, command=su, height=150, width=150).place(x=250,y=250)
    regresarS1=Button(silabaS,text="Regresar",command=regresarmenuS3,width=15, height=10).place(x=450,y=250)
    silabaS.mainloop()
def regresarmenuS3():
    pygame.mixer.music.pause()
    silabaS.destroy()
    menuS1()
def entrarpalabrasS():
    menuS.destroy()
    tocaimagenrepite()
    menupalabrasS1()
def menupalabrasS1():
    global palabrasS1
    palabrasS1=tix.Tk()
    palabrasS1.geometry("800x480")
    palabrasS1.config(bg="white")
    palabrasS1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/1sandia.png", master=palabrasS1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/2sal.png", master=palabrasS1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/3secadora.png", master=palabrasS1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/4sepillo.png", master=palabrasS1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/5silla.png", master=palabrasS1)
    palabrar16=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/6sol.png", master=palabrasS1)
    palabrar17=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/7carta.png", master=palabrasS1)
    palabrar18=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/8subir.png", master=palabrasS1)
    palabrar19=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/9roncar.png", master=palabrasS1)
    imS2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasS1)
    imS3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasS1)
    palabrasr11=Button(palabrasS1, image=palabrar11, command=sandia, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasS1, image=palabrar12, command=sal, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasS1, image=palabrar13, command=secadora, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasS1, image=palabrar14, command=sepillo, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasS1, image=palabrar15, command=silla, height=125, width=125,bg="white").place(x=620,y=10)
    palabrasr16=Button(palabrasS1, image=palabrar16, command=sol, height=125, width=125,bg="white").place(x=20,y=145)
    palabrasr17=Button(palabrasS1, image=palabrar17, command=sobre, height=125, width=125,bg="white").place(x=170,y=145)
    palabrasr18=Button(palabrasS1, image=palabrar18, command=sube, height=125, width=125,bg="white").place(x=320,y=145)
    palabrasr19=Button(palabrasS1, image=palabrar19, command=siesta, height=125, width=125,bg="white").place(x=470,y=145)
    siguienteS11=Button(palabrasS1,text="Siguiente",command=entrarpalabrasS1,width=20, height=3).place(x=230,y=420)
    regresarS11=Button(palabrasS1,text="Regresar",command=regresarmenuS4,width=20, height=3).place(x=30,y=420)
    siguienteS12=tix.Button(palabrasS1,image=imS2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarS12=tix.Button(palabrasS1,image=imS3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasS1.mainloop()
def entrarpalabrasS1():
    pygame.mixer.music.pause()
    palabrasS1.destroy()
    menupalabrasS2()
def regresarmenuS4():
    pygame.mixer.music.pause()
    palabrasS1.destroy()
    menuS1()
def menupalabrasS2():
    global palabrasS2
    palabrasS2=tix.Tk()
    palabrasS2.geometry("800x480")
    palabrasS2.config(bg="white")
    palabrasS2.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/16peces.png", master=palabrasS2)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/17murcielago.png", master=palabrasS2)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/18iglesia.png", master=palabrasS2)
    palabrar110=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/10casa.png", master=palabrasS2)
    palabrar111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/11mariposa.png", master=palabrasS2)
    palabrar112=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/12camisa.png", master=palabrasS2)
    palabrar113=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/13payaso.png", master=palabrasS2)
    palabrar114=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/14oso.png", master=palabrasS2)
    palabrar115=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/palabras/15queso.png", master=palabrasS2)
    imS2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasS2)
    imS3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasS2)
    palabrasr11=Button(palabrasS2, image=palabrar11, command=peces, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasS2, image=palabrar12, command=murcielago, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasS2, image=palabrar13, command=iglesia, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr110=Button(palabrasS2, image=palabrar110, command=casa, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr111=Button(palabrasS2, image=palabrar111, command=mariposa, height=125, width=125,bg="white").place(x=620,y=10)
    palabrasr112=Button(palabrasS2, image=palabrar112, command=camisa, height=125, width=125,bg="white").place(x=20,y=145)
    palabrasr113=Button(palabrasS2, image=palabrar113, command=payaso, height=125, width=125,bg="white").place(x=170,y=145)
    palabrasr114=Button(palabrasS2, image=palabrar114, command=oso, height=125, width=125,bg="white").place(x=320,y=145)
    palabrasr115=Button(palabrasS2, image=palabrar115, command=queso, height=125, width=125,bg="white").place(x=470,y=145)
    siguienteS11=Button(palabrasS2,text="Finalizar",command=regresarmenuS5,width=20, height=3).place(x=230,y=420)
    regresarS11=Button(palabrasS2,text="Regresar",command=regresarpalabrasS2,width=20, height=3).place(x=30,y=420)
    siguienteS12=tix.Button(palabrasS2,image=imS2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarS12=tix.Button(palabrasS2,image=imS3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasS2.mainloop()
def regresarpalabrasS2():
    pygame.mixer.music.pause()
    palabrasS2.destroy()
    menupalabrasS1()
def regresarmenuS5():
    pygame.mixer.music.pause()
    palabrasS2.destroy()
    menuS1()

def intentalodenuevo3():
    global contador2
    a.destroy()
    contador2=2
    menuimagenS()
def entrarmenuimagenS():
    global contador2
    contador2=1
    menuS.destroy()
    menuimagenS()
def regresarmenuS6():
    pygame.mixer.music.pause()
    a.destroy()
    menuS1()
def menuimagenS():
    coloraleatorio()
    if (contador2==1):
        llevaimageness()
    if (contador2==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=2
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global IMAGE_PATH
    numerodeimagenes=8
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaS/imagenes/"
    q="1is.png"
    q2="2is.png"
    q3="3is.png"
    q4="4is.png"
    q5="5is.png"
    q6="6is.png"
    q7="7is.png"
    q8="8is.png"
    sonido="/home/pi/Desktop/tesis/audio/globo.wav"
    sonido2="/home/pi/Desktop/tesis/audio/gusano.wav"
    sonido3="/home/pi/Desktop/tesis/audio/caramelo.wav"
    sonido4="/home/pi/Desktop/tesis/audio/vela.wav"
    sonido5="/home/pi/Desktop/tesis/audio/manguera.wav"
    sonido6="/home/pi/Desktop/tesis/audio/kiwi.wav"
    sonido7="/home/pi/Desktop/tesis/audio/atun.wav"
    sonido8="/home/pi/Desktop/tesis/audio/beso.wav"
    global sonido9
    global sonido10
    sonido9="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido10="/home/pi/Desktop/tesis/audio/silencio.mp3"
    a = tk.Tk()
    a.title("DSAG AND DSOP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuS6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="S",  height=3, width=10,bg=colorboton,font=("Helvetica",30), ).place(x=300,y=350)
    a.mainloop()
    
def menucuentoS():
    global cuentoS
    cuentoS=tix.Tk()
    vamosacontarcuento()
    cuentoS.geometry("800x480")
    cuentoS.config(bg="white")
    cuentoS.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/cuentoS/1cs.png", master=cuentoS)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/cuentoS/2cs.png", master=cuentoS)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/cuentoS/3cs.png", master=cuentoS)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/cuentoS/4cs.png", master=cuentoS)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/cuentoS/5cs.png", master=cuentoS)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaS/cuentoS/6cs.png", master=cuentoS)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoS)
    cuento1=Label(cuentoS, text="En una noche de",height=3, width=15,font=("Helvetica",12),bg="white").place(x=20,y=10)
    cuento2=Button(cuentoS, image=cuento111, command=lunallena, height=50, width=50).place(x=150,y=10)
    cuento3=Label(cuentoS, text="el", height=3, width=2,font=("Helvetica",12),bg="white").place(x=205,y=10)
    cuento4=Button(cuentoS, image=cuento121, command=oso ,height=50, width=50).place(x=228,y=10)
    cuento5=Label(cuentoS, text="salió a pasear. Cuando vió al",  height=3, width=22,font=("Helvetica",12),bg="white").place(x=288,y=10)
    cuento6=Button(cuentoS, image=cuento131, command=aguila, height=50, width=50).place(x=495,y=10)
    cuento7=Label(cuentoS, text="y al", height=3, width=3,font=("Helvetica",12),bg="white").place(x=550,y=10)
    cuento8=Button(cuentoS, image=cuento141, command=murcielago, height=50, width=50).place(x=581,y=10)
    cuento9=Label(cuentoS, text="volar, recordó a su vieja amiga la", height=3, width=26,font=("Helvetica",12),bg="white").place(x=20,y=80)
    cuento10=Button(cuentoS, image=cuento151, command=lechuza,height=50, width=50).place(x=253,y=80)
    cuento11=Label(cuentoS, text="con quien solia las tardes jugar.", height=3, width=25,font=("Helvetica",12),bg="white").place(x=318,y=80)
    cuento12=Label(cuentoS, text="Con voz susurrada dijo", height=3, width=18,font=("Helvetica",12),bg="white").place(x=553,y=80)
    cuento13=Label(cuentoS, text="-quisiera volar como ellos-y recorrer todos los cielos para a mi amiga ", height=3, width=53,font=("Helvetica",12),bg="white").place(x=20,y=150)
    cuento14=Button(cuentoS, image=cuento151, command=lechuza, height=50, width=50).place(x=500,y=150)
    cuento15=Label(cuentoS, text="encontrar. Entonces preguntó al", height=3,width=24,font=("Helvetica",12),bg="white").place(x=550,y=150)
    cuento18=Button(cuentoS, image=cuento131, command=aguila, height=50, width=50).place(x=20,y=220)
    cuento17=Label(cuentoS, text="y al", height=3, width=3,font=("Helvetica",12),bg="white").place(x=70,y=220)
    cuento18=Button(cuentoS, image=cuento141, command=murcielago, height=50, width=50).place(x=100,y=220)
    cuento19=Label(cuentoS, text="¿cómo pueden ustedes volar?. Ellos contestaron-tenemos grandes alas que nos permiten", height=3, width=70,font=("Helvetica",12),bg="white").place(x=160,y=220)
    cuento20=Label(cuentoS, text="los cielos surcar. El", height=3, width=15,font=("Helvetica",12),bg="white").place(x=20,y=290)
    cuento21=Button(cuentoS, image=cuento121,command=oso ,height=50, width=50).place(x=160,y=290)
    cuento22=Label(cuentoS, text="se quedó pensando por un momento y dijo-yo no puedo volar-pero mi amigo", height=3, width=58,font=("Helvetica",12),bg="white").place(x=220,y=290)
    cuento23=Button(cuentoS, image=cuento161,command=condor,height=50, width=50).place(x=10,y=345)
    cuento24=Label(cuentoS, text="puede hacerlo. Entonces lo llamó y le pidió que vuele sobre los mares y cielos para su amiga ", height=3, width=74,font=("Helvetica",12),bg="white").place(x=60,y=345)
    cuento25=Button(cuentoS, image=cuento151, command=lechuza, height=50, width=50).place(x=730,y=345)
    cuento26=Label(cuentoS, text="encontrar.", height=3, width=7,font=("Helvetica",12),bg="white").place(x=20,y=415)
    cuento27=Button(cuentoS, text="Regresar", command=regresarmenuS7, height=3, width=10).place(x=500,y=430)
    c50=Button(cuentoS, image=cuento188, command=cuentoSSSSSS, height=50, width=50).place(x=700,y=430)
    cuentoS.mainloop()
def regresarmenuS7():
    cuentoS.destroy()
    pygame.mixer.music.pause()
    menuS1()

#MENU LETRA T

def entrarT():
    menu.destroy()
    menuT2()
def menuT2():
    escuchayrepite()
    global T1
    T1=tix.Tk()
    T1.geometry("800x480")
    T1.config(bg="white")
    T1.attributes("-fullscreen", True)
    imT1=PhotoImage(file="/home/pi/Desktop/tesis/imagen/Tlabios.png", master=T1)
    imT2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=T1)
    imT3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=T1)
    letrar=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/t.png", master=T1)
    letrar2=Label(T1,image=letrar,height=100, width=100, bg="white").place(x=365,y=20)
    botonT1=Button(T1, image=imT1, command=TTTTTT, height=125, width=125).place(x=350,y=120)
    siguienteT1=tix.Button(T1,text="Siguiente",command=entrarmenuT,width=20, height=3).place(x=600,y=300)
    regresarT1=tix.Button(T1,text="Regresar",command=regresarmenuT2,width=20, height=3).place(x=30,y=300)
    siguienteT12=tix.Button(T1,image=imT2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarT12=tix.Button(T1,image=imT3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    T1.mainloop()
def entrarmenuT():
    pygame.mixer.music.pause()
    T1.destroy()
    menuT1()
def menuT1():
    coloraleatorio()
    global menuT
    menuT=tix.Tk()
    menuT.geometry("800x480")
    menuT.config(bg="white")
    menuT.attributes("-fullscreen", True)
    silabaT= tix.Button(menuT,text="Silabas",command=entrarsilabasT,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasT= tix.Button(menuT,text="Palabras",command=entrarpalabrasT,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenT= tix.Button(menuT,text="Discriminacion Fonetica",command=entrarmenuimagenT,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoT= tix.Button(menuT,text="Cuento",command=entrarmenucuentoT,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirT= tix.Button(menuT,text="Regresar",command=regresarmenuT1,width=23, height=3).place(x=600,y=350)
    menuT.mainloop()
def entrarmenucuentoT():
    menuT.destroy()
    menucuentoT()
def entrarsilabasT():
    menuT.destroy()
    TilabaT1()
def TilabaT1():
    escucharsilabas()
    global silabaT
    silabaT=tix.Tk()
    silabaT.geometry("800x480")
    silabaT.config(bg="white")
    silabaT.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/silabas/ta.png", master=silabaT)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/silabas/te.png", master=silabaT)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/silabas/ti.png", master=silabaT)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/silabas/to.png", master=silabaT)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/silabas/tu.png", master=silabaT)
    imT2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaT)
    imT3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaT)
    siguienteT12=tix.Button(silabaT,image=imT2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarT12=tix.Button(silabaT,image=imT3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaT, image=r11, command=ta, height=150, width=150).place(x=50,y=50)
    re1=Button(silabaT, image=r12, command=te, height=150, width=150).place(x=250,y=50)
    ri1=Button(silabaT, image=r13, command=ti, height=150, width=150).place(x=450,y=50)
    ro1=Button(silabaT, image=r14, command=to, height=150, width=150).place(x=50,y=250)
    ru1=Button(silabaT, image=r15, command=tu, height=150, width=150).place(x=250,y=250)
    regresarT1=Button(silabaT,text="Regresar",command=regresarmenuT3,width=15, height=10).place(x=450,y=250)
    silabaT.mainloop()
def regresarmenuT3():
    pygame.mixer.music.pause()
    silabaT.destroy()
    menuT1()
def entrarpalabrasT():
    menuT.destroy()
    tocaimagenrepite()
    menupalabrasT1()
def menupalabrasT1():
    global palabrasT1
    palabrasT1=tix.Tk()
    palabrasT1.geometry("800x480")
    palabrasT1.config(bg="white")
    palabrasT1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/1pt.png", master=palabrasT1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/2pt.png", master=palabrasT1)
    palabrar16=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/telaraña.png", master=palabrasT1)
    palabrar18=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/timbre.png", master=palabrasT1)
    palabrar110=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/torta.png", master=palabrasT1)
    palabrar112=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/tubo.png", master=palabrasT1)
    palabrar115=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/9pt.png", master=palabrasT1)
    palabrar111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/10pt.png", master=palabrasT1)
    imT2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasT1)
    imT3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasT1)
    palabrasr111=Button(palabrasT1, image=palabrar111, command=tunel, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr11=Button(palabrasT1, image=palabrar11, command=tambor, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasT1, image=palabrar13, command=teta, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr16=Button(palabrasT1, image=palabrar16, command=telaraña, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr18=Button(palabrasT1, image=palabrar18, command=timbre, height=125, width=125,bg="white").place(x=470,y=145)
    palabrasr110=Button(palabrasT1, image=palabrar110, command=torta, height=125, width=125,bg="white").place(x=20,y=145)
    palabrasr112=Button(palabrasT1, image=palabrar112, command=tubo, height=125, width=125,bg="white").place(x=170,y=145)
    palabrasr115=Button(palabrasT1, image=palabrar115, command=tijera, height=125, width=125,bg="white").place(x=320,y=145)
    siguienteT11=Button(palabrasT1,text="Siguiente",command=entrarpalabrasT1,width=20, height=3).place(x=230,y=420)
    regresarT11=Button(palabrasT1,text="Regresar",command=regresarmenuT4,width=20, height=3).place(x=30,y=420)
    siguienteT12=tix.Button(palabrasT1,image=imT2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarT12=tix.Button(palabrasT1,image=imT3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasT1.mainloop()
def entrarpalabrasT1():
    pygame.mixer.music.pause()
    palabrasT1.destroy()
    menupalabrasT2()
def regresarmenuT4():
    pygame.mixer.music.pause()
    palabrasT1.destroy()
    menuT1()
def menupalabrasT2():
    global palabrasT2
    palabrasT2=tix.Tk()
    palabrasT2.geometry("800x480")
    palabrasT2.config(bg="white")
    palabrasT2.attributes("-fullscreen", True)
    imT2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasT2)
    imT3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasT2)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/atun.png", master=palabrasT2)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/galleta.png", master=palabrasT2)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/3pt.png", master=palabrasT2)
    palabrar17=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/4pt.png", master=palabrasT2)
    palabrar19=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/5pt.png", master=palabrasT2)
    palabrar111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/6pt.png", master=palabrasT2)
    palabrar113=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/7pt.png", master=palabrasT2)
    palabrar114=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/palabras/8pt.png", master=palabrasT2)
    palabrasr12=Button(palabrasT2, image=palabrar12, command=atun, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr14=Button(palabrasT2, image=palabrar14, command=galleta, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr15=Button(palabrasT2, image=palabrar15, command=pelota, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr17=Button(palabrasT2, image=palabrar17, command=chocolate, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr19=Button(palabrasT2, image=palabrar19, command=pito, height=125, width=125,bg="white").place(x=470,y=145)
    palabrasr111=Button(palabrasT2, image=palabrar111, command=moto, height=125, width=125,bg="white").place(x=20,y=145)
    palabrasr113=Button(palabrasT2, image=palabrar113, command=pantera, height=125, width=125,bg="white").place(x=170,y=145)
    palabrasr114=Button(palabrasT2, image=palabrar114, command=tortuga, height=125, width=125,bg="white").place(x=320,y=145)
    siguienteT11=Button(palabrasT2,text="Finalizar",command=regresarmenuT5,width=20, height=3).place(x=230,y=420)
    regresarT11=Button(palabrasT2,text="Regresar",command=regresarpalabrasT2,width=20, height=3).place(x=30,y=420)
    siguienteT12=tix.Button(palabrasT2,image=imT2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarT12=tix.Button(palabrasT2,image=imT3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasT2.mainloop()
def regresarpalabrasT2():
    pygame.mixer.music.pause()
    palabrasT2.destroy()
    menupalabrasT1()
def regresarmenuT5():
    pygame.mixer.music.pause()
    palabrasT2.destroy()
    menuT1()
def intentalodenuevo4():
    global contador3
    a.destroy()
    contador3=2
    menuimagenT()
def entrarmenuimagenT():
    global contador3
    contador3=1
    menuT.destroy()
    menuimagenT()
def regresarmenuT6():
    pygame.mixer.music.pause()
    a.destroy()
    menuT1()
def menuimagenT():
    coloraleatorio()
    if (contador3==1):
        llevaimagenesr()
    if (contador3==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=1
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=11
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaT/imagenes/"
    q="1it.png"
    q2="2it.png"
    q3="3it.png"
    q4="4it.png"
    q5="5it.png"
    q6="6it.png"
    q7="7it.png"
    q8="8it.png"
    q9="9it.png"
    q10="10it.png"
    sonido="/home/pi/Desktop/tesis/audio/pirata.wav"
    sonido2="/home/pi/Desktop/tesis/audio/pozo.wav"
    sonido3="/home/pi/Desktop/tesis/audio/hacha.wav"
    sonido4="/home/pi/Desktop/tesis/audio/chocolate.wav"
    sonido5="/home/pi/Desktop/tesis/audio/galleta.wav"
    sonido6="/home/pi/Desktop/tesis/audio/navidad.wav"
    sonido7="/home/pi/Desktop/tesis/audio/manilla.wav"
    sonido8="/home/pi/Desktop/tesis/audio/torta.wav"
    sonido9="/home/pi/Desktop/tesis/audio/teta.wav"
    sonido10="/home/pi/Desktop/tesis/audio/lechuga.wav"
    a = tk.Tk()
    a.title("DTAG AND DTOP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuT6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="T",  height=3, width=10,bg=colorboton,font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
    
def menucuentoT():
    global cuentoT
    cuentoT=tix.Tk()
    vamosacontarcuento()
    cuentoT.geometry("800x480")
    cuentoT.config(bg="white")
    cuentoT.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/CuentoT/1ct.png", master=cuentoT)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/CuentoT/2ct.png", master=cuentoT)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/CuentoT/3ct.png", master=cuentoT)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/CuentoT/4ct.png", master=cuentoT)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/CuentoT/5ct.png", master=cuentoT)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/CuentoT/6ct.png", master=cuentoT)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/CuentoT/7ct.png", master=cuentoT)
    cuento181=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaT/CuentoT/8ct.png", master=cuentoT)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoT)
    cuento1=Label(cuentoT, text="Caminando por el bosque iba la",height=3, width=24,font=("Helvetica",12), bg="white").place(x=20,y=10)
    cuento2=Button(cuentoT, image=cuento111, command=tortuga, height=50, width=50).place(x=250,y=10)
    cuento3=Label(cuentoT, text="a paso lento, muy lento en busca de", height=3, width=27,font=("Helvetica",12), bg="white").place(x=310,y=10)
    cuento4=Button(cuentoT, image=cuento121, command=frutas ,height=50, width=50).place(x=565,y=10)
    cuento5=Label(cuentoT, text="y vegetales.",  height=3, width=9,font=("Helvetica",12), bg="white").place(x=630,y=10)
    cuento31=Label(cuentoT, text="De pronto, encontró unos", height=3, width=21,font=("Helvetica",12), bg="white").place(x=20,y=70)
    cuento6=Button(cuentoT, image=cuento131, command=guineos, height=50, width=50).place(x=220,y=70)
    cuento7=Label(cuentoT, text=", una", height=3, width=3,font=("Helvetica",12), bg="white").place(x=280,y=70)
    cuento8=Button(cuentoT, image=cuento141, command=manzana ,height=50, width=50).place(x=320,y=70)
    cuento71=Label(cuentoT, text=", un", height=3, width=3,font=("Helvetica",12), bg="white").place(x=380,y=70)
    cuento81=Button(cuentoT, image=cuento151, command=tomate ,height=50, width=50).place(x=415,y=70)
    cuento72=Label(cuentoT, text="y una", height=3, width=4,font=("Helvetica",12), bg="white").place(x=475,y=70)
    cuento82=Button(cuentoT, image=cuento161, command=lechuga ,height=50, width=50).place(x=520,y=70)
    cuento9=Label(cuentoT, text=". Son mias- exclamo feliz la", height=3, width=22,font=("Helvetica",12), bg="white").place(x=580,y=70)
    cuento10=Button(cuentoT, image=cuento111, command=tortuga,height=50, width=50).place(x=15,y=130)
    cuento11=Label(cuentoT, text=". Muy cerca de ella se escucho la voz de una", height=3, width=34,font=("Helvetica",12), bg="white").place(x=75,y=130)
    cuento12=Button(cuentoT, image=cuento171 ,command=serpiente ,height=50, width=50).place(x=390,y=130)
    cuento13=Label(cuentoT, text="que decía- esas son mis", height=3, width=20,font=("Helvetica",12), bg="white").place(x=445,y=130)
    cuento14=Button(cuentoT, image=cuento121, command=frutas, height=50, width=50).place(x=625,y=130)
    cuento15=Label(cuentoT, text="y mis vegetales.", height=3,width=12,font=("Helvetica",12), bg="white").place(x=685,y=130)
    cuento16=Label(cuentoT, text="La", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=190)
    cuento17=Button(cuentoT, image=cuento171, command=serpiente, height=50, width=50).place(x=45,y=190)
    cuento18=Label(cuentoT, text="y la", height=3, width=3,font=("Helvetica",12), bg="white").place(x=105,y=190)
    cuento19=Button(cuentoT, image=cuento111, command=tortuga, height=50, width=50).place(x=140,y=190)
    cuento20=Label(cuentoT, text="no paraban de discutir para decidir a quien pertenecian esas frutas y vegetales. En ", height=3, width=65,font=("Helvetica",12), bg="white").place(x=200,y=190)
    cuento21=Label(cuentoT, text="medio de la discusion, escucharon una voz debil y tembolorosa diciendo- tengo mucha hambre y no encuentro", height=3, width=85,font=("Helvetica",12), bg="white").place(x=20,y=240)
    cuento22=Label(cuentoT, text="comida. Era un", height=3, width=12,font=("Helvetica",12), bg="white").place(x=15,y=290)
    cuento23=Button(cuentoT, image=cuento181, command=topo, height=50, width=50).place(x=125,y=290)
    cuento24=Label(cuentoT, text="flaco, muy flaco. La", height=3, width=16,font=("Helvetica",12), bg="white").place(x=180,y=290)
    cuento25=Button(cuentoT, image=cuento171, command=serpiente, height=50, width=50).place(x=325,y=290)
    cuento26=Label(cuentoT, text="y la", height=3, width=3,font=("Helvetica",12), bg="white").place(x=385,y=290)
    cuento27=Button(cuentoT, image=cuento111, command=tortuga, height=50, width=50).place(x=415,y=290)
    cuento28=Label(cuentoT, text="lo miraron y sintieron mucha pena del", height=3, width=29,font=("Helvetica",12), bg="white").place(x=475,y=290)
    cuento29=Button(cuentoT, image=cuento181, command=topo, height=50, width=50).place(x=740,y=290)
    cuento30=Label(cuentoT, text="flaco y hambriento, entonces decidieron entregarle sus", height=3, width=42,font=("Helvetica",12), bg="white").place(x=20,y=350)
    cuento31=Button(cuentoT, image=cuento121, command=frutas ,height=50, width=50).place(x=410,y=350)
    cuento32=Label(cuentoT, text="y vegetales para que asi, ya no pasara",  height=3, width=30,font=("Helvetica",12), bg="white").place(x=480,y=350)
    cuento32=Label(cuentoT, text="más hambre.",  height=3, width=11,font=("Helvetica",12), bg="white").place(x=20,y=400)
    cuento21=Button(cuentoT, text="Regresar", command=regresarmenuT7, height=3, width=10).place(x=500,y=410)
    c50=Button(cuentoT, image=cuento188, command=cuentoTTTTTT, height=50, width=50).place(x=700,y=410)
    cuentoT.mainloop()
def regresarmenuT7():
    cuentoT.destroy()
    pygame.mixer.music.pause()
    menuT1()


#MENU LETLA L

def entrarL():
    menu.destroy()
    menuL2()
def menuL2():
    escuchayrepite()
    global L1
    L1=tix.Tk()
    L1.geometry("800x480")
    L1.config(bg="white")
    L1.attributes("-fullscreen", True)
    imL1=PhotoImage(file="/home/pi/Desktop/tesis/imagen/Llabios.png", master=L1)
    imL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=L1)
    imL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=L1)
    letrar=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/l.png", master=L1)
    letrar2=Label(L1,image=letrar,height=100, width=100, bg="white").place(x=365,y=20)
    botonL1=Button(L1, image=imL1, command=LLLLLL, height=125, width=125).place(x=350,y=120)
    siguienteL1=tix.Button(L1,text="Siguiente",command=entrarmenuL,width=20, height=3).place(x=600,y=300)
    regresarL1=tix.Button(L1,text="Regresar",command=regresarmenuL2,width=20, height=3).place(x=30,y=300)
    siguienteL12=tix.Button(L1,image=imL2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarL12=tix.Button(L1,image=imL3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    L1.mainloop()
def entrarmenuL():
    pygame.mixer.music.pause()
    L1.destroy()
    menuL1()
def menuL1():
    coloraleatorio()
    global menuL
    menuL=tix.Tk()
    menuL.geometry("800x480")
    menuL.config(bg="white")
    menuL.attributes("-fullscreen", True)
    silabaL= tix.Button(menuL,text="Silabas",command=entrarsilabasL,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasL= tix.Button(menuL,text="Palabras",command=entrarpalabrasL,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenL= tix.Button(menuL,text="Discriminacion Fonetica",command=entrarmenuimagenL,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoL= tix.Button(menuL,text="Cuento",command=entrarmenucuentoL,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirL= tix.Button(menuL,text="Regresar",command=regresarmenuL1,width=23, height=3).place(x=600,y=350)
    menuL.mainloop()
def entrarmenucuentoL():
    menuL.destroy()
    menucuentoL()
def entrarsilabasL():
    menuL.destroy()
    SilabaL1()
def SilabaL1():
    escucharsilabas()
    global silabaL
    silabaL=tix.Tk()
    silabaL.geometry("800x480")
    silabaL.config(bg="white")
    silabaL.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/silabas/la.png", master=silabaL)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/silabas/le.png", master=silabaL)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/silabas/li.png", master=silabaL)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/silabas/lo.png", master=silabaL)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/silabas/lu.png", master=silabaL)
    imL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaL)
    imL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaL)
    siguienteL12=tix.Button(silabaL,image=imL2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarL12=tix.Button(silabaL,image=imL3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaL, image=r11, command=la, height=150, width=150).place(x=50,y=50)
    re1=Button(silabaL, image=r12, command=le, height=150, width=150).place(x=250,y=50)
    ri1=Button(silabaL, image=r13, command=li, height=150, width=150).place(x=450,y=50)
    ro1=Button(silabaL, image=r14, command=lo, height=150, width=150).place(x=50,y=250)
    ru1=Button(silabaL, image=r15, command=lu, height=150, width=150).place(x=250,y=250)
    regresarL1=Button(silabaL,text="Regresar",command=regresarmenuL3,width=15, height=10).place(x=450,y=250)
    silabaL.mainloop()
def regresarmenuL3():
    pygame.mixer.music.pause()
    silabaL.destroy()
    menuL1()
def entrarpalabrasL():
    menuL.destroy()
    tocaimagenrepite()
    menupalabrasL1()
def menupalabrasL1():
    global palabrasL1
    palabrasL1=tix.Tk()
    palabrasL1.geometry("800x480")
    palabrasL1.config(bg="white")
    palabrasL1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/1lapiz.png", master=palabrasL1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/2lagartija.png", master=palabrasL1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/2lobo.png", master=palabrasL1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/3lector.png", master=palabrasL1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/4lechuza.png", master=palabrasL1)
    palabrar16=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/5leche.png", master=palabrasL1)
    #palabrar17=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/5leche.png", master=palabrasL1)
    palabrar18=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/6licuadora.png", master=palabrasL1)
    palabrar19=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/8loro.png", master=palabrasL1)
    palabrar110=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/9lupa.png", master=palabrasL1)
    imL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasL1)
    imL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasL1)
    palabrasr11=Button(palabrasL1, image=palabrar11, command=lapiz, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasL1, image=palabrar12, command=lagartija, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasL1, image=palabrar13, command=lobo, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasL1, image=palabrar14, command=lee, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasL1, image=palabrar15, command=lechuza, height=125, width=125,bg="white").place(x=620,y=10)
    palabrasr16=Button(palabrasL1, image=palabrar16, command=leche, height=125, width=125,bg="white").place(x=20,y=145)
    #palabrasr17=Button(palabrasL1, image=palabrar17, command=leche, height=125, width=125,bg="white").place(x=170,y=145)
    palabrasr18=Button(palabrasL1, image=palabrar18, command=licuadora, height=125, width=125,bg="white").place(x=170,y=145)
    palabrasr19=Button(palabrasL1, image=palabrar19, command=loro, height=125, width=125,bg="white").place(x=320,y=145)
    palabrasr110=Button(palabrasL1, image=palabrar110, command=lupa, height=125, width=125,bg="white").place(x=470,y=145)
    siguienteL11=Button(palabrasL1,text="Siguiente",command=entrarpalabrasL1,width=20, height=3).place(x=230,y=420)
    regresarL11=Button(palabrasL1,text="Regresar",command=regresarmenuL4,width=20, height=3).place(x=30,y=420)
    siguienteL12=tix.Button(palabrasL1,image=imL2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarL12=tix.Button(palabrasL1,image=imL3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasL1.mainloop()
def entrarpalabrasL1():
    pygame.mixer.music.pause()
    palabrasL1.destroy()
    menupalabrasL2()
def regresarmenuL4():
    pygame.mixer.music.pause()
    palabrasL1.destroy()
    menuL1()
def menupalabrasL2():
    global palabrasL2
    palabrasL2=tix.Tk()
    palabrasL2.geometry("800x480")
    palabrasL2.config(bg="white")
    palabrasL2.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/15chocolate.png", master=palabrasL2)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/16elefante.png", master=palabrasL2)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/17escalera.png", master=palabrasL2)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/18nose.png", master=palabrasL2)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/19helado.png", master=palabrasL2)
    palabrar111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/10vela.png", master=palabrasL2)
    palabrar112=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/11maleta.png", master=palabrasL2)
    palabrar113=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/12telefono.png", master=palabrasL2)
    palabrar114=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/13peluca.png", master=palabrasL2)
    palabrar115=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/palabras/14caramelo.png", master=palabrasL2)
    imL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasL2)
    imL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasL2)
    palabrasr11=Button(palabrasL2, image=palabrar11, command=chocolate, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasL2, image=palabrar12, command=elefante, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasL2, image=palabrar13, command=escalera, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasL2, image=palabrar14, command=hola, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasL2, image=palabrar15, command=helado, height=125, width=125,bg="white").place(x=620,y=10)
    palabrasr111=Button(palabrasL2, image=palabrar111, command=vela, height=125, width=125,bg="white").place(x=20,y=145)
    palabrasr112=Button(palabrasL2, image=palabrar112, command=mochila, height=125, width=125,bg="white").place(x=170,y=145)
    palabrasr113=Button(palabrasL2, image=palabrar113, command=telefono, height=125, width=125,bg="white").place(x=320,y=145)
    palabrasr114=Button(palabrasL2, image=palabrar114, command=pelo, height=125, width=125,bg="white").place(x=470,y=145)
    palabrasr115=Button(palabrasL2, image=palabrar115, command=caramelo, height=125, width=125,bg="white").place(x=620,y=145)
    siguienteL11=Button(palabrasL2,text="Finalizar",command=regresarmenuL5,width=20, height=3).place(x=230,y=420)
    regresarL11=Button(palabrasL2,text="Regresar",command=regresarpalabrasL2,width=20, height=3).place(x=30,y=420)
    siguienteL12=tix.Button(palabrasL2,image=imL2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarL12=tix.Button(palabrasL2,image=imL3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasL2.mainloop()
def regresarpalabrasL2():
    pygame.mixer.music.pause()
    palabrasL2.destroy()
    menupalabrasL1()
def regresarmenuL5():
    pygame.mixer.music.pause()
    palabrasL2.destroy()
    menuL1()
def intentalodenuevo5():
    global contador5
    a.destroy()
    contador5=2
    menuimagenL()
def entrarmenuimagenL():
    global contador5
    contador5=1
    menuL.destroy()
    menuimagenL()
def regresarmenuL6():
    pygame.mixer.music.pause()
    a.destroy()
    menuL1()
def menuimagenL():
    coloraleatorio()
    if (contador5==1):
        llevaimagenesl()
    if (contador5==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=1
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=12
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaL/imagenes/"
    q="1il.png"
    q2="2il.png"
    q3="3il.png"
    q4="4il.png"
    q5="5il.png"
    q6="6il.png"
    q7="7il.png"
    q8="8il.png"
    q9="9il.png"
    q10="10il.png"
    sonido="/home/pi/Desktop/tesis/audio/helado.wav"
    sonido2="/home/pi/Desktop/tesis/audio/escalera.wav"
    sonido3="/home/pi/Desktop/tesis/audio/pez.wav"
    sonido4="/home/pi/Desktop/tesis/audio/foco.wav"
    sonido5="/home/pi/Desktop/tesis/audio/lechuza.wav"
    sonido6="/home/pi/Desktop/tesis/audio/limon.wav"
    sonido7="/home/pi/Desktop/tesis/audio/tambor.wav"
    sonido8="/home/pi/Desktop/tesis/audio/uva.wav"
    sonido9="/home/pi/Desktop/tesis/audio/lupa.wav"
    sonido10="/home/pi/Desktop/tesis/audio/licuadora.wav"
    a = tk.Tk()
    a.title("DLAG AND DLOP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuL6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="L",  height=3, width=10, bg=colorboton,font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
    
def menucuentoL():
    global cuentoL
    cuentoL=tix.Tk()
    vamosacontarcuento()
    cuentoL.geometry("800x480")
    cuentoL.config(bg="white")
    cuentoL.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/cuentoL/1cl.png", master=cuentoL)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/cuentoL/2cl.png", master=cuentoL)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/cuentoL/3cl.png", master=cuentoL)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/cuentoL/4cl.png", master=cuentoL)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/cuentoL/5cl.png", master=cuentoL)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/cuentoL/6cl.png", master=cuentoL)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/cuentoL/7cl.png", master=cuentoL)
    cuento181=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/cuentoL/8cl.png", master=cuentoL)
    cuento191=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/cuentoL/9cl.png", master=cuentoL)
    cuento112=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaL/cuentoL/10cl.png", master=cuentoL)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoL)
    cuento1=Label(cuentoL, text="La golosa",height=3, width=7,font=("Helvetica",12),bg="white").place(x=20,y=20)
    cuento2=Button(cuentoL, image=cuento111, command=lechuza, height=50, width=50).place(x=95,y=20)
    cuento3=Label(cuentoL, text="se encontró con su amigo el", height=3, width=21,font=("Helvetica",12),bg="white").place(x=150,y=20)
    cuento4=Button(cuentoL, image=cuento121, command=lobo ,height=50, width=50).place(x=350,y=20)
    cuento5=Label(cuentoL, text="a quién invitó a tomar un  delicioso",  height=3, width=28,font=("Helvetica",12),bg="white").place(x=410,y=20)
    cuento6=Button(cuentoL, image=cuento131, command=helado, height=50, width=50).place(x=660,y=20)
    cuento7=Label(cuentoL, text="Luego se encontró con la", height=3, width=19,font=("Helvetica",12),bg="white").place(x=20,y=90)
    cuento8=Button(cuentoL, image=cuento141, command=lagartija, height=50, width=50).place(x=200,y=90)
    cuento9=Label(cuentoL, text="y le dió unos ricos", height=3, width=15,font=("Helvetica",12),bg="white").place(x=255,y=90)
    cuento10=Button(cuentoL, image=cuento151, command=caramelo,height=50, width=50).place(x=395,y=90)
    cuento11=Label(cuentoL, text="A su amigo el", height=3, width=10,font=("Helvetica",12),bg="white").place(x=452,y=90)
    cuento12=Button(cuentoL, image=cuento161,command=loro, height=50, width=50).place(x=550,y=90)
    cuento13=Label(cuentoL, text="le regaló un exquisito", height=3, width=17,font=("Helvetica",12),bg="white").place(x=610,y=90)
    cuento14=Button(cuentoL, image=cuento171, command=chocolate, height=50, width=50).place(x=20,y=160)
    cuento15=Label(cuentoL, text="Pero la  golosa", height=3,width=12,font=("Helvetica",12),bg="white").place(x=80,y=160)
    cuento18=Button(cuentoL, image=cuento111, command=lechuza, height=50, width=50).place(x=190,y=160)
    cuento17=Label(cuentoL, text="se asustó mucho al ver que no tenía una golosina para su amigo el", height=3, width=52,font=("Helvetica",12),bg="white").place(x=255,y=160)
    cuento18=Button(cuentoL, image=cuento181, command=elefante, height=50, width=50).place(x=20,y=230)
    cuento19=Label(cuentoL, text="a él  le dió un pequeño", height=3, width=20,font=("Helvetica",12),bg="white").place(x=80,y=230)
    cuento20=Button(cuentoL, image=cuento191, command=limon, height=50, width=50).place(x=250,y=230)
    cuento21=Label(cuentoL, text="y una", height=3, width=7,font=("Helvetica",12),bg="white").place(x=305,y=230)
    cuento18=Button(cuentoL, image=cuento112, command=leche, height=50, width=50).place(x=360,y=230)
    cuento19=Label(cuentoL, text="de cartón que tenía guardada hace mucho en su cajon.", height=3, width=44,font=("Helvetica",12),bg="white").place(x=405,y=230)
#    cuento20=Label(cuentoL, text="de cartón que tenía guardada hace mucho en su cajon.", height=3, width=45,font=("Helvetica",12),bg="white").place(x=40,y=300)
    cuento21=Button(cuentoL, text="Regresar", command=regresarmenuL7, height=3, width=10).place(x=20,y=410)
    c50=Button(cuentoL, image=cuento188, command=cuentoLLLLLL, height=50, width=50).place(x=700,y=410)
    cuentoL.mainloop()
def regresarmenuL7():
    cuentoL.destroy()
    pygame.mixer.music.pause()
    menuL1()


#MENU LETMA M

def entrarM():
    menu.destroy()
    menuM2()
def menuM2():
    escuchayrepite()
    global M1
    M1=tix.Tk()
    M1.geometry("800x480")
    M1.config(bg="white")
    M1.attributes("-fullscreen", True)
    imM1=PhotoImage(file="/home/pi/Desktop/tesis/imagen/Mlabios.png", master=M1)
    imM2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=M1)
    imM3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=M1)
    letrar=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/m.png", master=M1)
    letrar2=Label(M1,image=letrar,height=100, width=100, bg="white").place(x=365,y=20)
    botonM1=Button(M1, image=imM1, command=MMMMMM, height=125, width=125).place(x=350,y=120)
    siguienteM1=tix.Button(M1,text="Siguiente",command=entrarmenuM,width=20, height=3).place(x=600,y=300)
    regresarM1=tix.Button(M1,text="Regresar",command=regresarmenuM2,width=20, height=3).place(x=30,y=300)
    siguienteM12=tix.Button(M1,image=imM2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarM12=tix.Button(M1,image=imM3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    M1.mainloop()
def entrarmenuM():
    pygame.mixer.music.pause()
    M1.destroy()
    menuM1()
def menuM1():
    coloraleatorio()
    global menuM
    menuM=tix.Tk()
    menuM.geometry("800x480")
    menuM.config(bg="white")
    menuM.attributes("-fullscreen", True)
    silabaM= tix.Button(menuM,text="Silabas",command=entrarsilabasM,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasM= tix.Button(menuM,text="Palabras",command=entrarpalabrasM,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenM= tix.Button(menuM,text="Discriminacion Fonetica",command=entrarmenuimagenM,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoM= tix.Button(menuM,text="Cuento",command=entrarmenucuentoM,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirM= tix.Button(menuM,text="Regresar",command=regresarmenuM1,width=23, height=3).place(x=600,y=350)
    menuM.mainloop()
def entrarmenucuentoM():
    menuM.destroy()
    menucuentoM()
def entrarsilabasM():
    menuM.destroy()
    SilabaM1()
def SilabaM1():
    escucharsilabas()
    global silabaM
    silabaM=tix.Tk()
    silabaM.geometry("800x480")
    silabaM.config(bg="white")
    silabaM.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/silabas/ma.png", master=silabaM)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/silabas/me.png", master=silabaM)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/silabas/mi.png", master=silabaM)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/silabas/mo.png", master=silabaM)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/silabas/mu.png", master=silabaM)
    imM2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaM)
    imM3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaM)
    siguienteM12=tix.Button(silabaM,image=imM2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarM12=tix.Button(silabaM,image=imM3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaM, image=r11, command=ma, height=150, width=150).place(x=50,y=50)
    re1=Button(silabaM, image=r12, command=me, height=150, width=150).place(x=250,y=50)
    ri1=Button(silabaM, image=r13, command=mi, height=150, width=150).place(x=450,y=50)
    ro1=Button(silabaM, image=r14, command=mo, height=150, width=150).place(x=50,y=250)
    ru1=Button(silabaM, image=r15, command=mu, height=150, width=150).place(x=250,y=250)
    regresarM1=Button(silabaM,text="Regresar",command=regresarmenuM3,width=15, height=10).place(x=450,y=250)
    
    silabaM.mainloop()
def regresarmenuM3():
    pygame.mixer.music.pause()
    silabaM.destroy()
    menuM1()
def entrarpalabrasM():
    menuM.destroy()
    tocaimagenrepite()
    menupalabrasM1()
def menupalabrasM1():
    global palabrasM1
    palabrasM1=tix.Tk()
    palabrasM1.geometry("800x480")
    palabrasM1.config(bg="white")
    palabrasM1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/1maleta.png", master=palabrasM1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/2mesa.png", master=palabrasM1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/3melon.png", master=palabrasM1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/4manza.png", master=palabrasM1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/5mono.png", master=palabrasM1)
    palabrar16=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/6moto.png", master=palabrasM1)
    palabrar17=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/7molino.png", master=palabrasM1)
    palabrar18=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/8muñe.png", master=palabrasM1)
    palabrar19=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/9muleta.png", master=palabrasM1)
    imM2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasM1)
    imM3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasM1)
    palabrasr11=Button(palabrasM1, image=palabrar11, command=maleta, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasM1, image=palabrar12, command=mesa, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasM1, image=palabrar13, command=melon, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasM1, image=palabrar14, command=manzana, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasM1, image=palabrar15, command=mono, height=125, width=125,bg="white").place(x=620,y=10)
    palabrasr16=Button(palabrasM1, image=palabrar16, command=moto, height=125, width=125,bg="white").place(x=20,y=145)
    palabrasr17=Button(palabrasM1, image=palabrar17, command=molino, height=125, width=125,bg="white").place(x=170,y=145)
    palabrasr18=Button(palabrasM1, image=palabrar18, command=muñeca, height=125, width=125,bg="white").place(x=320,y=145)
    palabrasr19=Button(palabrasM1, image=palabrar19, command=muleta, height=125, width=125,bg="white").place(x=470,y=145)
    siguienteM11=Button(palabrasM1,text="Siguiente",command=entrarpalabrasM1,width=20, height=3).place(x=230,y=420)
    regresarM11=Button(palabrasM1,text="Regresar",command=regresarmenuM4,width=20, height=3).place(x=30,y=420)
    siguienteM12=tix.Button(palabrasM1,image=imM2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarM12=tix.Button(palabrasM1,image=imM3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    
    palabrasM1.mainloop()
def entrarpalabrasM1():
    pygame.mixer.music.pause()
    palabrasM1.destroy()
    menupalabrasM2()
def regresarmenuM4():
    pygame.mixer.music.pause()
    palabrasM1.destroy()
    menuM1()
def menupalabrasM2():
    global palabrasM2
    palabrasM2=tix.Tk()
    palabrasM2.geometry("800x480")
    palabrasM2.config(bg="white")
    palabrasM2.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/16camisa.png", master=palabrasM2)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/17caramelo.png", master=palabrasM2)
    palabrar110=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/10cama.png", master=palabrasM2)
    palabrar111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/11paloma.png", master=palabrasM2)
    palabrar112=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/12llama.png", master=palabrasM2)
    palabrar113=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/13tomate.png", master=palabrasM2)
    palabrar114=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/14niña.png", master=palabrasM2)
    palabrar115=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/palabras/15dormir.png", master=palabrasM2)
    imM2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasM2)
    imM3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasM2)
    palabrasr11=Button(palabrasM2, image=palabrar11, command=camisa, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasM2, image=palabrar12, command=caramelo, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr110=Button(palabrasM2, image=palabrar110, command=cama, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr111=Button(palabrasM2, image=palabrar111, command=paloma, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr112=Button(palabrasM2, image=palabrar112, command=llama, height=125, width=125,bg="white").place(x=20,y=145)
    palabrasr113=Button(palabrasM2, image=palabrar113, command=tomate, height=125, width=125,bg="white").place(x=170,y=145)
    palabrasr114=Button(palabrasM2, image=palabrar114, command=come, height=125, width=125,bg="white").place(x=320,y=145)
    palabrasr115=Button(palabrasM2, image=palabrar115, command=duerme, height=125, width=125,bg="white").place(x=470,y=145)
    siguienteM11=Button(palabrasM2,text="Finalizar",command=regresarmenuM5,width=20, height=3).place(x=230,y=420)
    regresarM11=Button(palabrasM2,text="Regresar",command=regresarpalabrasM2,width=20, height=3).place(x=30,y=420)
    siguienteM12=tix.Button(palabrasM2,image=imM2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarM12=tix.Button(palabrasM2,image=imM3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasM2.mainloop()
def regresarpalabrasM2():
    pygame.mixer.music.pause()
    palabrasM2.destroy()
    menupalabrasM1()
def regresarmenuM5():
    pygame.mixer.music.pause()
    palabrasM2.destroy()
    menuM1()

def intentalodenuevo6():
    global contador6
    a.destroy()
    contador6=2
    menuimagenM()
def entrarmenuimagenM():
    global contador6
    contador6=1
    menuM.destroy()
    menuimagenM()
def regresarmenuM6():
    pygame.mixer.music.pause()
    a.destroy()
    menuM1()
def menuimagenM():
    coloraleatorio()
    if (contador6==1):
        llevaimagenesm()
    if (contador6==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=1
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global IMAGE_PATH
    numerodeimagenes=9
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaM/imagenes/"
    q="1araña.png"
    q2="2silla.png"
    q3="3payaso.png"
    q4="4piña.png"
    q5="5mesa.png"
    q6="6caramelo.png"
    q7="7manzana.png"
    q8="8molino.png"
    q9="9pera.png"
    sonido="/home/pi/Desktop/tesis/audio/araña.wav"
    sonido2="/home/pi/Desktop/tesis/audio/silla.wav"
    sonido3="/home/pi/Desktop/tesis/audio/payaso.wav"
    sonido4="/home/pi/Desktop/tesis/audio/piña.wav"
    sonido5="/home/pi/Desktop/tesis/audio/mesa.wav"
    sonido6="/home/pi/Desktop/tesis/audio/caramelo.wav"
    sonido7="/home/pi/Desktop/tesis/audio/manzana.wav"
    sonido8="/home/pi/Desktop/tesis/audio/molino.wav"
    sonido9="/home/pi/Desktop/tesis/audio/pera.wav"
    global sonido10
    sonido10="/home/pi/Desktop/tesis/audio/silencio.mp3"
    a = tk.Tk()
    a.title("DMAG AND DMOP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuM6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="M",  height=3, width=10, bg=colorboton,font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
    
def menucuentoM():
    global cuentoM
    cuentoM=tix.Tk()
    vamosacontarcuento()
    cuentoM.geometry("800x480")
    cuentoM.config(bg="white")
    cuentoM.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/cuento/1cuentoma.png", master=cuentoM)
    cuento181=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/cuento/2cuentomanza.png", master=cuentoM)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/cuento/cuentocama.png", master=cuentoM)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/cuento/cuentomanzana.png", master=cuentoM)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/cuento/cuentomelon.png", master=cuentoM)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/cuento/cuentomesa.png", master=cuentoM)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/cuento/cuentomono.png", master=cuentoM)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaM/cuento/cuentopaloma.png", master=cuentoM)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoM)
    cuento1=Button(cuentoM, image=cuento111, command=mama, height=50, width=50).place(x=20,y=20)
    cuento2=Label(cuentoM, text="tenía una", height=3, width=9,font=("Helvetica",12),bg="white").place(x=75,y=20)
    cuento3=Button(cuentoM, image=cuento121, command=manzana, height=50, width=50).place(x=160,y=20)
    cuento4=Label(cuentoM, text="y un", height=3, width=5,font=("Helvetica",12),bg="white").place(x=215,y=20)
    cuento5=Button(cuentoM, image=cuento131, command=melon, height=50, width=50).place(x=275,y=20)
    cuento6=Label(cuentoM, text="muy sabroso para darle a su", height=3, width=22,font=("Helvetica",12),bg="white").place(x=330,y=20)
    cuento7=Button(cuentoM, image=cuento141, command=mono, height=50, width=50).place(x=540,y=20)
    cuento8=Label(cuentoM, text="goloso.", height=3, width=5,font=("Helvetica",12),bg="white").place(x=600,y=20)
    cuento9=Label(cuentoM, text="Puso la", height=3, width=5,font=("Helvetica",12),bg="white").place(x=20,y=90)
    cuento10=Button(cuentoM, image=cuento121, command=manzana, height=50, width=50).place(x=90,y=90)
    cuento11=Label(cuentoM, text="y el", height=3, width=5,font=("Helvetica",12),bg="white").place(x=145,y=90)
    cuento12=Button(cuentoM, image=cuento131, command=melon, height=50, width=50).place(x=205,y=90)
    cuento13=Label(cuentoM, text="sobre la", height=3, width=6,font=("Helvetica",12),bg="white").place(x=260,y=90)
    cuento14=Button(cuentoM, image=cuento151, command=mesa, height=50, width=50).place(x=335,y=90)
    cuento15=Label(cuentoM, text="y se fue a la", height=3, width=10,font=("Helvetica",12),bg="white").place(x=390,y=90)
    cuento16=Button(cuentoM, image=cuento161, command=cama, height=50, width=50).place(x=490,y=90)
    cuento17=Label(cuentoM, text="a descansar.", height=3, width=10,font=("Helvetica",12),bg="white").place(x=555,y=90)
    cuento18=Label(cuentoM, text="De pronto, la", height=3, width=10,font=("Helvetica",12),bg="white").place(x=20,y=160)
    cuento19=Button(cuentoM, image=cuento171, command=paloma, height=50, width=50).place(x=125,y=160)
    cuento20=Label(cuentoM, text="Asiri, entró por la ventana de la cocina y se comió toda la", height=3, width=47,font=("Helvetica",12),bg="white").place(x=180,y=160)
    cuento21=Button(cuentoM, image=cuento121, command=manzana, height=50, width=50).place(x=600,y=160)
    cuento22=Label(cuentoM, text="y el", height=3, width=5,font=("Helvetica",12),bg="white").place(x=660,y=160)
    cuento23=Button(cuentoM, image=cuento131, command=melon, height=50, width=50).place(x=700,y=160)
    cuento24=Label(cuentoM, text="El", height=3, width=2,font=("Helvetica",12),bg="white").place(x=20,y=230)
    cuento25=Button(cuentoM, image=cuento141, command=mono, height=50, width=50).place(x=50,y=230)
    cuento26=Label(cuentoM, text="goloso, se puso muy triste, pues se quedó sin", height=3, width=36,font=("Helvetica",12),bg="white").place(x=115,y=230)
    cuento27=Button(cuentoM, image=cuento131, command=melon, height=50, width=50).place(x=435,y=230)
    cuento28=Label(cuentoM, text="y sin", height=3, width=5,font=("Helvetica",12),bg="white").place(x=495,y=230)
    cuento29=Button(cuentoM, image=cuento121, command=manzana, height=50, width=50).place(x=555,y=230)    
    cuento21=Button(cuentoM, text="Regresar", command=regresarmenuM7, height=3, width=10).place(x=20,y=320)
    c50=Button(cuentoM, image=cuento188, command=cuentoMMMMMM, height=50, width=50).place(x=700,y=320)
    cuentoM.mainloop()
def regresarmenuM7():
    cuentoM.destroy()
    pygame.mixer.music.pause()
    menuM1()
def sonidoaleatorio():
    global numerodefrases23
    v=numerodefrases23
    if(numerodefrases==4):
        
        if (v==1):
            pygame.mixer.music.load(audio4)
            pygame.mixer.music.play(1)
            numerodefrases23=2
        if (v==2):
            pygame.mixer.music.load(audio2)
            pygame.mixer.music.play(1)
            numerodefrases23=3
        if (v==3):
            pygame.mixer.music.load(audio)
            pygame.mixer.music.play(1)
            numerodefrases23=4
        if (v==4):
            pygame.mixer.music.load(audio3)
            pygame.mixer.music.play(1)
            numerodefrases23=1
        
    if(numerodefrases==3):
        
        if (v==1):
            pygame.mixer.music.load(audio2)
            pygame.mixer.music.play(1)
            numerodefrases23=2
        if (v==2):
            pygame.mixer.music.load(audio)
            pygame.mixer.music.play(1)
            numerodefrases23=3
        if (v==3):
            pygame.mixer.music.load(audio3)
            pygame.mixer.music.play(1)
            numerodefrases23=1


#MENU LETRA BL

def entrarBL():
    menu.destroy()
    menuBL2()
def menuBL2():
    escuchayrepite()
    global BL1
    BL1=tix.Tk()
    BL1.geometry("800x480")
    BL1.config(bg="white")
    BL1.attributes("-fullscreen", True)
    imBL1=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/bl.png", master=BL1)
    imBL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=BL1)
    imBL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=BL1)
    botonBL1=Button(BL1, image=imBL1, command=BLBLBLBLBLBL, height=100, width=100).place(x=350,y=75)
    siguienteBL1=tix.Button(BL1,text="Siguiente",command=entrarmenuBL,width=20, height=3).place(x=600,y=300)
    regresarBL1=tix.Button(BL1,text="Regresar",command=regresarmenuBL2,width=20, height=3).place(x=30,y=300)
    siguienteBL12=tix.Button(BL1,image=imBL2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarBL12=tix.Button(BL1,image=imBL3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    BL1.mainloop()
def entrarmenuBL():
    pygame.mixer.music.pause()
    BL1.destroy()
    menuBL1()
def menuBL1():
    
    coloraleatorio()
    global menuBL
    menuBL=tix.Tk()
    menuBL.geometry("800x480")
    menuBL.config(bg="white")
    menuBL.attributes("-fullscreen", True)
    silabaBL= tix.Button(menuBL,text="Silabas",command=entrarsilabasBL,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasBL= tix.Button(menuBL,text="Palabras",command=entrarpalabrasBL,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenBL= tix.Button(menuBL,text="Discriminacion Fonetica",command=entrarmenuimagenBL,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoBL= tix.Button(menuBL,text="Frases",command=entrarmenucuentoBL,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirBL= tix.Button(menuBL,text="Regresar",command=regresarmenuBL1,width=23, height=3).place(x=600,y=350)
    menuBL.mainloop()
def entrarmenucuentoBL():
    menuBL.destroy()
    menucuentoBL()
def entrarsilabasBL():
    menuBL.destroy()
    SilabaBL1()
def SilabaBL1():
    escucharsilabas()
    global silabaBL
    silabaBL=tix.Tk()
    silabaBL.geometry("800x480")
    silabaBL.config(bg="white")
    silabaBL.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/silabas/bla.PNG", master=silabaBL)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/silabas/ble.PNG", master=silabaBL)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/silabas/bli.PNG", master=silabaBL)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/silabas/blo.PNG", master=silabaBL)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/silabas/blu.PNG", master=silabaBL)
    imBL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaBL)
    imBL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaBL)
    siguienteBL12=tix.Button(silabaBL,image=imBL2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarBL12=tix.Button(silabaBL,image=imBL3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaBL, image=r11, command=bla, height=150, width=200).place(x=20,y=50)
    re1=Button(silabaBL, image=r12, command=ble, height=150, width=200).place(x=240,y=50)
    ri1=Button(silabaBL, image=r13, command=bli, height=150, width=200).place(x=460,y=50)
    ro1=Button(silabaBL, image=r14, command=blo, height=150, width=200).place(x=20,y=250)
    ru1=Button(silabaBL, image=r15, command=blu, height=150, width=200).place(x=240,y=250)
    regresarBL1=Button(silabaBL,text="Regresar",command=regresarmenuBL3,width=15, height=10).place(x=460,y=250)
    silabaBL.mainloop()
def regresarmenuBL3():
    pygame.mixer.music.pause()
    silabaBL.destroy()
    menuBL1()
def entrarpalabrasBL():
    menuBL.destroy()
    tocaimagenrepite()
    menupalabrasBL1()
def menupalabrasBL1():
    global palabrasBL1
    palabrasBL1=tix.Tk()
    palabrasBL1.geometry("800x480")
    palabrasBL1.config(bg="white")
    palabrasBL1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/palabras/blusa.png", master=palabrasBL1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/palabras/cable.png", master=palabrasBL1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/palabras/habla.png", master=palabrasBL1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/palabras/nabaja.png", master=palabrasBL1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/palabras/tabla.png", master=palabrasBL1)
    imBL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasBL1)
    imBL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasBL1)
    palabrasr11=Button(palabrasBL1, image=palabrar11, command=blusa, height=125, width=125,bg="white").place(x=245,y=160)
    palabrasr12=Button(palabrasBL1, image=palabrar12, command=cable, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasBL1, image=palabrar13, command=habla, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasBL1, image=palabrar14, command=sable, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasBL1, image=palabrar15, command=tabla, height=125, width=125,bg="white").place(x=395,y=160)
    regresarBL11=Button(palabrasBL1,text="Regresar",command=regresarmenuBL4,width=20, height=3).place(x=30,y=420)
    siguienteBL12=tix.Button(palabrasBL1,image=imBL2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarBL12=tix.Button(palabrasBL1,image=imBL3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasBL1.mainloop()
def regresarmenuBL4():
    pygame.mixer.music.pause()
    palabrasBL1.destroy()
    menuBL1()
def intentalodenuevo7():
    global contador7
    a.destroy()
    contador7=2
    menuimagenBL()
def entrarmenuimagenBL():
    global contador7
    contador7=1
    menuBL.destroy()
    menuimagenBL()
def regresarmenuBL6():
    pygame.mixer.music.pause()
    a.destroy()
    menuBL1()
def menuimagenBL():
    coloraleatorio()
    if (contador7==1):
        llevaimagenesbl()
    if (contador7==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=1
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=13
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaBL/imagenes/"
    q="1ibl.png"
    q2="2ibl.png"
    q3="3ibl.png"
    q4="4ibl.png"
    q5="chancho.png"
    q6="lluvia.png"
    q7="pluma.png"
    sonido="/home/pi/Desktop/tesis/audio/blusa.wav"
    sonido2="/home/pi/Desktop/tesis/audio/tabla.wav"
    sonido3="/home/pi/Desktop/tesis/audio/cable.wav"
    sonido4="/home/pi/Desktop/tesis/audio/tijera.wav"
    sonido5="/home/pi/Desktop/tesis/audio/chancho.wav"
    sonido6="/home/pi/Desktop/tesis/audio/lluvia.wav"
    sonido7="/home/pi/Desktop/tesis/audio/pluma.wav"
    sonido8="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido9="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido10="/home/pi/Desktop/tesis/audio/silencio.mp3"
    a = tk.Tk()
    a.title("DBLAG AND DBLOP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuBL6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="BL",  height=3, width=10, bg=colorboton,font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
    
def menucuentoBL():
    
    global audio
    global audio2
    global audio3
    global audio4
    audio="/home/pi/Desktop/tesis/audio/El-cable-de.wav"
    audio2="/home/pi/Desktop/tesis/audio/corto-el-arbol.wav"
    audio3="/home/pi/Desktop/tesis/audio/la-doctora-tiene.wav"
    global numerodefrases
    numerodefrases=3
    señalalosdibujos()
    global cuentoBL
    cuentoBL=tix.Tk()
    cuentoBL.geometry("800x480")
    cuentoBL.config(bg="white")
    cuentoBL.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/frases/1fbl.png", master=cuentoBL)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/frases/2fbl.png", master=cuentoBL)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/frases/3fbl.png", master=cuentoBL)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/frases/4fbl.png", master=cuentoBL)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/frases/5fbl.png", master=cuentoBL)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBL/frases/6fbl.png", master=cuentoBL)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoBL)
    imBL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=cuentoBL)
    imBL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=cuentoBL)
    siguienteBL12=tix.Button(cuentoBL,image=imBL2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarBL12=tix.Button(cuentoBL,image=imBL3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    cuento1=Label(cuentoBL, text="El",height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=40)
    cuento2=Label(cuentoBL, image=cuento111,  height=50, width=50).place(x=50,y=40)
    cuento3=Label(cuentoBL, text="de la television.", height=3, width=16,font=("Helvetica",12), bg="white").place(x=110,y=40)
    cuento4=Label(cuentoBL, text="Corto el", height=3, width=8,font=("Helvetica",12), bg="white").place(x=20,y=130)
    cuento4=Label(cuentoBL, image=cuento121, height=50, width=50).place(x=110,y=130)
    cuento5=Label(cuentoBL, text="con el",  height=3, width=5,font=("Helvetica",12), bg="white").place(x=170,y=130)
    cuento6=Label(cuentoBL, image=cuento131,  height=50, width=50).place(x=250,y=130)
    cuento7=Label(cuentoBL, text="La", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=220)
    cuento8=Label(cuentoBL, image=cuento141, height=50, width=50).place(x=50,y=220)
    cuento9=Label(cuentoBL, text="tiene una", height=3, width=9,font=("Helvetica",12), bg="white").place(x=110,y=220)
    cuento10=Label(cuentoBL, image=cuento151, height=50, width=50).place(x=220,y=220)
    cuento11=Label(cuentoBL, text="de color", height=3, width=8,font=("Helvetica",12), bg="white").place(x=280,y=220)
    cuento12=Label(cuentoBL, image=cuento161 ,height=50, width=50).place(x=370,y=220)
    cuento21=Button(cuentoBL, text="Regresar", command=regresarmenuBL7, height=3, width=10).place(x=20,y=400)
    c50=Button(cuentoBL, image=cuento188, command=sonidoaleatorio, height=50, width=50).place(x=360,y=400)
    cuento60=Button(cuentoBL,image=cuento188,command=repitelaoracion, height=50, width=50).place(x=700,y=400)
    cuentoBL.mainloop()
def regresarmenuBL7():
    cuentoBL.destroy()
    pygame.mixer.music.pause()
    menuBL1()

#MENU LETCLA CL

def entrarCL():
    menu.destroy()
    menuCL2()
def menuCL2():
    escuchayrepite()
    global CL1
    CL1=tix.Tk()
    CL1.geometry("800x480")
    CL1.config(bg="white")
    CL1.attributes("-fullscreen", True)
    imCL1=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/cl.png", master=CL1)
    imCL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=CL1)
    imCL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=CL1)
    botonCL1=Button(CL1, image=imCL1, command=CLCLCLCLCLCL, height=100, width=100, bg="white").place(x=350,y=75)
    siguienteCL1=tix.Button(CL1,text="Siguiente",command=entrarmenuCL,width=20, height=3).place(x=600,y=300)
    regresarCL1=tix.Button(CL1,text="Regresar",command=regresarmenuCL2,width=20, height=3).place(x=30,y=300)
    siguienteCL12=tix.Button(CL1,image=imCL2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarCL12=tix.Button(CL1,image=imCL3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    CL1.mainloop()
def entrarmenuCL():
    pygame.mixer.music.pause()
    CL1.destroy()
    menuCL1()
def menuCL1():
    coloraleatorio()
    global menuCL
    menuCL=tix.Tk()
    menuCL.geometry("800x480")
    menuCL.config(bg="white")
    menuCL.attributes("-fullscreen", True)
    silabaCL= tix.Button(menuCL,text="Silabas",command=entrarsilabasCL,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasCL= tix.Button(menuCL,text="Palabras",command=entrarpalabrasCL,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenCL= tix.Button(menuCL,text="Discriminacion Fonetica",command=entrarmenuimagenCL,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoCL= tix.Button(menuCL,text="Frases",command=entrarmenucuentoCL,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirCL= tix.Button(menuCL,text="Regresar",command=regresarmenuCL1,width=23, height=3).place(x=600,y=350)
    menuCL.mainloop()
def entrarmenucuentoCL():
    menuCL.destroy()
    menucuentoCL()
def entrarsilabasCL():
    menuCL.destroy()
    SilabaCL1()
def SilabaCL1():
    escucharsilabas()
    global silabaCL
    silabaCL=tix.Tk()
    silabaCL.geometry("800x480")
    silabaCL.config(bg="white")
    silabaCL.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/silabas/cla.PNG", master=silabaCL)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/silabas/cle.PNG", master=silabaCL)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/silabas/cli.PNG", master=silabaCL)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/silabas/clo.PNG", master=silabaCL)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/silabas/clu.PNG", master=silabaCL)
    imCL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaCL)
    imCL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaCL)
    siguienteCL12=tix.Button(silabaCL,image=imCL2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarCL12=tix.Button(silabaCL,image=imCL3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaCL, image=r11, command=cla, height=150, width=200).place(x=20,y=50)
    re1=Button(silabaCL, image=r12, command=cle, height=150, width=200).place(x=240,y=50)
    ri1=Button(silabaCL, image=r13, command=cli, height=150, width=200).place(x=460,y=50)
    ro1=Button(silabaCL, image=r14, command=clo, height=150, width=200).place(x=20,y=250)
    ru1=Button(silabaCL, image=r15, command=clu, height=150, width=200).place(x=240,y=250)
    regresarCL1=Button(silabaCL,text="Regresar",command=regresarmenuCL3,width=15, height=10).place(x=460,y=250)
    silabaCL.mainloop()
def regresarmenuCL3():
    pygame.mixer.music.pause()
    silabaCL.destroy()
    menuCL1()
def entrarpalabrasCL():
    menuCL.destroy()
    tocaimagenrepite()
    menupalabrasCL1()
def menupalabrasCL1():
    global palabrasCL1
    palabrasCL1=tix.Tk()
    palabrasCL1.geometry("800x480")
    palabrasCL1.config(bg="white")
    palabrasCL1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/palabras/bicicleta.png", master=palabrasCL1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/palabras/clavel.png", master=palabrasCL1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/palabras/clavo.png", master=palabrasCL1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/palabras/maestras.png", master=palabrasCL1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/palabras/maquina.png", master=palabrasCL1)
    imCL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasCL1)
    imCL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasCL1)
    palabrasr11=Button(palabrasCL1, image=palabrar11, command=bicicleta, height=125, width=125,bg="white").place(x=245,y=160)
    palabrasr12=Button(palabrasCL1, image=palabrar12, command=clavel, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasCL1, image=palabrar13, command=clavo, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasCL1, image=palabrar14, command=clase, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasCL1, image=palabrar15, command=chicle, height=125, width=125,bg="white").place(x=395,y=160)
    regresarCL11=Button(palabrasCL1,text="Regresar",command=regresarmenuCL4,width=20, height=3).place(x=30,y=420)
    siguienteCL12=tix.Button(palabrasCL1,image=imCL2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarCL12=tix.Button(palabrasCL1,image=imCL3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasCL1.mainloop()
def regresarmenuCL4():
    pygame.mixer.music.pause()
    palabrasCL1.destroy()
    menuCL1()
def intentalodenuevo8():
    global contador8
    a.destroy()
    contador8=2
    menuimagenCL()
def entrarmenuimagenCL():
    global contador8
    contador8=1
    menuCL.destroy()
    menuimagenCL()
def regresarmenuCL6():
    pygame.mixer.music.pause()
    a.destroy()
    menuCL1()
def menuimagenCL():
    coloraleatorio()
    if (contador8==1):
        llevaimagenescl()
    if (contador8==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=1
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=14
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaCL/imagenes/"
    q="1ibl.png"
    q2="1icl.png"
    q3="2icl.png"
    q4="3ibl.png"
    q5="6il.png"
    sonido="/home/pi/Desktop/tesis/audio/blusa.wav"
    sonido2="/home/pi/Desktop/tesis/audio/chicle.wav"
    sonido3="/home/pi/Desktop/tesis/audio/clavo.wav"
    sonido4="/home/pi/Desktop/tesis/audio/cable.wav"
    sonido5="/home/pi/Desktop/tesis/audio/limon.wav"
    sonido6="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido7="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido8="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido9="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido10="/home/pi/Desktop/tesis/audio/silencio.mp3"
    a = tk.Tk()
    a.title("DCLAG AND DCLOP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuCL6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="CL",  height=3, width=10, bg=colorboton,font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
    
def menucuentoCL():
    global audio
    global audio2
    global audio3
    global audio4
    audio="/home/pi/Desktop/tesis/audio/A-claudia-le-gusta-los-girasoles.mp3"
    audio2="/home/pi/Desktop/tesis/audio/el-niño-esta-muy-feliz.wav"
    audio3="/home/pi/Desktop/tesis/audio/los-niños-pelean.wav"
    global numerodefrases
    numerodefrases=3
    señalalosdibujos()
    global cuentoCL
    cuentoCL=tix.Tk()
    cuentoCL.geometry("800x480")
    cuentoCL.config(bg="white")
    cuentoCL.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/frases/1fcl.png", master=cuentoCL)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/frases/2fcl.png", master=cuentoCL)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/frases/3fcl.png", master=cuentoCL)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/frases/4fcl.png", master=cuentoCL)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/frases/5fcl.png", master=cuentoCL)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/frases/6fcl.png", master=cuentoCL)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/frases/7fcl.png", master=cuentoCL)
    cuento181=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCL/frases/8fcl.png", master=cuentoCL)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoCL)
    imCL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=cuentoCL)
    imCL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=cuentoCL)
    siguienteCL12=tix.Button(cuentoCL,image=imCL2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarCL12=tix.Button(cuentoCL,image=imCL3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    cuento0=Label(cuentoCL, text="A",height=3, width=1,font=("Helvetica",12), bg="white").place(x=20,y=40)
    cuento=Button(cuentoCL, image=cuento111, command=doctora, height=50, width=50).place(x=35,y=40)
    cuento1=Label(cuentoCL, text="le gustan los",height=3, width=13,font=("Helvetica",12), bg="white").place(x=90,y=40)
    cuento2=Button(cuentoCL, image=cuento121, command=girasol, height=50, width=50).place(x=210,y=40)
    cuento3=Button(cuentoCL, image=cuento131, command=clavel, height=50, width=50).place(x=270,y=40)
    cuento4=Label(cuentoCL, text="y", height=3, width=1,font=("Helvetica",12), bg="white").place(x=330,y=40)
    cuento5=Button(cuentoCL, image=cuento141, command=girasol, height=50, width=50).place(x=360,y=40)
    cuento6=Button(cuentoCL, image=cuento151, command=arbol ,height=50, width=50).place(x=20,y=130)
    cuento7=Label(cuentoCL, text="esta muy feliz con su nueva", height=3, width=27,font=("Helvetica",12), bg="white").place(x=80,y=130)
    cuento8=Button(cuentoCL, image=cuento161, command=bicicleta ,height=50, width=50).place(x=300,y=130)
    cuento10=Button(cuentoCL, image=cuento171, command=doctora ,height=50, width=50).place(x=20,y=220)
    cuento11=Label(cuentoCL, text="pelean por los", height=3, width=14,font=("Helvetica",12), bg="white").place(x=80,y=220)
    cuento10=Button(cuentoCL, image=cuento181, command=melon,height=50, width=50).place(x=200,y=220)
    cuento21=Button(cuentoCL, text="Regresar", command=regresarmenuCL7, height=3, width=10).place(x=20,y=400)
    c50=Button(cuentoCL, image=cuento188, command=sonidoaleatorio, height=50, width=50).place(x=360,y=400)
    cuento60=Button(cuentoCL,image=cuento188,command=repitelaoracion, height=50, width=50).place(x=700,y=400)
    cuentoCL.mainloop()
def regresarmenuCL7():
    cuentoCL.destroy()
    pygame.mixer.music.pause()
    menuCL1()


#MENU LETFLA FL

def entrarFL():
    menu.destroy()
    menuFL2()
def menuFL2():
    escuchayrepite()
    global FL1
    FL1=tix.Tk()
    FL1.geometry("800x480")
    FL1.config(bg="white")
    FL1.attributes("-fullscreen", True)
    imFL1=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/fl.png", master=FL1)
    imFL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=FL1)
    imFL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=FL1)
    botonFL1=Button(FL1, image=imFL1, command=FLFLFLFLFLFL, height=100, width=100).place(x=350,y=75)
    siguienteFL1=tix.Button(FL1,text="Siguiente",command=entrarmenuFL,width=20, height=3).place(x=600,y=300)
    regresarFL1=tix.Button(FL1,text="Regresar",command=regresarmenuFL2,width=20, height=3).place(x=30,y=300)
    siguienteFL12=tix.Button(FL1,image=imFL2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarFL12=tix.Button(FL1,image=imFL3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    FL1.mainloop()
def entrarmenuFL():
    pygame.mixer.music.pause()
    FL1.destroy()
    menuFL1()
def menuFL1():
    coloraleatorio()
    global menuFL
    menuFL=tix.Tk()
    menuFL.geometry("800x480")
    menuFL.config(bg="white")
    menuFL.attributes("-fullscreen", True)
    silabaFL= tix.Button(menuFL,text="Silabas",command=entrarsilabasFL,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasFL= tix.Button(menuFL,text="Palabras",command=entrarpalabrasFL,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenFL= tix.Button(menuFL,text="Discriminacion Fonetica",command=entrarmenuimagenFL,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoFL= tix.Button(menuFL,text="Frases",command=entrarmenucuentoFL,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirFL= tix.Button(menuFL,text="Regresar",command=regresarmenuFL1,width=23, height=3).place(x=600,y=350)
    menuFL.mainloop()
def entrarmenucuentoFL():
    menuFL.destroy()
    menucuentoFL()
def entrarsilabasFL():
    menuFL.destroy()
    SilabaFL1()
def SilabaFL1():
    escucharsilabas()
    global silabaFL
    silabaFL=tix.Tk()
    silabaFL.geometry("800x480")
    silabaFL.config(bg="white")
    silabaFL.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/silabas/fla.PNG", master=silabaFL)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/silabas/fle.PNG", master=silabaFL)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/silabas/fli.PNG", master=silabaFL)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/silabas/flo.PNG", master=silabaFL)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/silabas/flu.PNG", master=silabaFL)
    imFL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaFL)
    imFL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaFL)
    siguienteFL12=tix.Button(silabaFL,image=imFL2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarFL12=tix.Button(silabaFL,image=imFL3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaFL, image=r11, command=fla, height=150, width=200).place(x=20,y=50)
    re1=Button(silabaFL, image=r12, command=fle, height=150, width=200).place(x=240,y=50)
    ri1=Button(silabaFL, image=r13, command=fli, height=150, width=200).place(x=460,y=50)
    ro1=Button(silabaFL, image=r14, command=flo, height=150, width=200).place(x=20,y=250)
    ru1=Button(silabaFL, image=r15, command=flu, height=150, width=200).place(x=240,y=250)
    regresarFL1=Button(silabaFL,text="Regresar",command=regresarmenuFL3,width=15, height=10).place(x=460,y=250)
    silabaFL.mainloop()
def regresarmenuFL3():
    pygame.mixer.music.pause()
    silabaFL.destroy()
    menuFL1()
def entrarpalabrasFL():
    menuFL.destroy()
    tocaimagenrepite()
    menupalabrasFL1()
def menupalabrasFL1():
    global palabrasFL1
    palabrasFL1=tix.Tk()
    palabrasFL1.geometry("800x480")
    palabrasFL1.config(bg="white")
    palabrasFL1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/palabras/cereales.png", master=palabrasFL1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/palabras/flauta.png", master=palabrasFL1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/palabras/flecha.png", master=palabrasFL1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/palabras/flora.png", master=palabrasFL1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/palabras/flores.png", master=palabrasFL1)
    palabrar16=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/palabras/hombre.png", master=palabrasFL1)
    imFL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasFL1)
    imFL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasFL1)
    palabrasr11=Button(palabrasFL1, image=palabrar11, command=conflex, height=125, width=125,bg="white").place(x=170,y=150)
    palabrasr12=Button(palabrasFL1, image=palabrar12, command=flauta, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasFL1, image=palabrar13, command=flecha, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasFL1, image=palabrar14, command=coliflor, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasFL1, image=palabrar15, command=flores, height=125, width=125,bg="white").place(x=320,y=150)
    palabrasr16=Button(palabrasFL1, image=palabrar16, command=flaco, height=125, width=125,bg="white").place(x=470,y=150)
    regresarFL11=Button(palabrasFL1,text="Regresar",command=regresarmenuFL4,width=20, height=3).place(x=30,y=420)
    siguienteFL12=tix.Button(palabrasFL1,image=imFL2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarFL123=tix.Button(palabrasFL1,image=imFL3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasFL1.mainloop()
def regresarmenuFL4():
    pygame.mixer.music.pause()
    palabrasFL1.destroy()
    menuFL1()
def intentalodenuevo9():
    global contador9
    a.destroy()
    contador9=2
    menuimagenFL()
def entrarmenuimagenFL():
    global contador9
    contador9=1
    menuFL.destroy()
    menuimagenFL()
def regresarmenuFL6():
    pygame.mixer.music.pause()
    a.destroy()
    menuFL1()
def menuimagenFL():
    coloraleatorio()
    if (contador9==1):
        llevaimagenesfl()
    if (contador9==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=1
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=15
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaFL/imagenes/"
    q="1ifl.png"
    q2="2ifl.png"
    q3="3ifl.png"
    q4="4ifl.png"
    q5="5ifl.png"
    q6="6ifl.png"
    sonido="/home/pi/Desktop/tesis/audio/flauta.wav"
    sonido2="/home/pi/Desktop/tesis/audio/clase.wav"
    sonido3="/home/pi/Desktop/tesis/audio/flores.wav"
    sonido4="/home/pi/Desktop/tesis/audio/flecha.wav"
    sonido5="/home/pi/Desktop/tesis/audio/tambor.wav"
    sonido6="/home/pi/Desktop/tesis/audio/peces.wav"
    sonido7="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido8="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido9="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido10="/home/pi/Desktop/tesis/audio/silencio.mp3"
    a = tk.Tk()
    a.title("DFLAG AND DFLOP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuFL6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="FL",  height=3, width=10, bg=colorboton, font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
def menucuentoFL():
    global audio
    global audio2
    global audio3
    global audio4
    audio="/home/pi/Desktop/tesis/audio/el-abuelo-le.wav"
    audio2="/home/pi/Desktop/tesis/audio/la-niña-toca.wav"
    audio3="/home/pi/Desktop/tesis/audio/la-niña-come.wav"
    global numerodefrases
    numerodefrases=3
    señalalosdibujos()
    global cuentoFL
    cuentoFL=tix.Tk()
    cuentoFL.geometry("800x480")
    cuentoFL.config(bg="white")
    cuentoFL.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/frases/1ffl.png", master=cuentoFL)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/frases/2ffl.png", master=cuentoFL)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/frases/3ffl.png", master=cuentoFL)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/frases/4ffl.png", master=cuentoFL)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/frases/5ffl.png", master=cuentoFL)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/frases/6ffl.png", master=cuentoFL)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/frases/7ffl.png", master=cuentoFL)
    cuento181=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/frases/8ffl.png", master=cuentoFL)
    cuento191=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/frases/9ffl.png", master=cuentoFL)
    cuento1101=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFL/frases/10ffl.png", master=cuentoFL)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoFL)
    imFL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=cuentoFL)
    imFL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=cuentoFL)
    siguienteFL12=tix.Button(cuentoFL,image=imFL2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarFL12=tix.Button(cuentoFL,image=imFL3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    cuento1=Label(cuentoFL, text="El",height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=40)
    cuento2=Label(cuentoFL, image=cuento111,  height=50, width=50).place(x=50,y=40)
    cuento3=Label(cuentoFL, text="le regala",height=3, width=9,font=("Helvetica",12), bg="white").place(x=110,y=40)
    cuento4=Label(cuentoFL, image=cuento121,  height=50, width=50).place(x=190,y=40)
    cuento5=Label(cuentoFL, text="a mi",height=3, width=4,font=("Helvetica",12), bg="white").place(x=250,y=40)
    cuento6=Label(cuentoFL, image=cuento131,  height=50, width=50).place(x=310,y=40)
    #primera frase
    cuento7=Label(cuentoFL, text="La", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=130)
    cuento8=Label(cuentoFL, image=cuento141,  height=50, width=50).place(x=50,y=130)
    cuento9=Label(cuentoFL, text="toca el", height=3, width=7,font=("Helvetica",12), bg="white").place(x=110,y=130)
    cuento10=Label(cuentoFL, image=cuento151, height=50, width=50).place(x=190,y=130)
    cuento11=Label(cuentoFL, text=", la", height=3, width=4,font=("Helvetica",12), bg="white").place(x=250,y=130)
    cuento12=Label(cuentoFL, image=cuento161, height=50, width=50).place(x=310,y=130)
    cuento13=Label(cuentoFL, text="y la", height=3, width=4,font=("Helvetica",12), bg="white").place(x=370,y=130)
    cuento14=Label(cuentoFL, image=cuento171, height=50, width=50).place(x=430,y=130)
    #segunda frase
    cuento15=Label(cuentoFL, text="La niña", height=3, width=7,font=("Helvetica",12), bg="white").place(x=20,y=220)
    cuento16=Label(cuentoFL, image=cuento181, height=50, width=50).place(x=100,y=220)
    cuento17=Label(cuentoFL, image=cuento191, height=50, width=50).place(x=160,y=220)
    cuento18=Label(cuentoFL, text="y", height=3, width=1,font=("Helvetica",12), bg="white").place(x=220,y=220)
    cuento19=Label(cuentoFL, image=cuento1101, height=50, width=50).place(x=240,y=220)
    cuento21=Button(cuentoFL, text="Regresar", command=regresarmenuFL7, height=3, width=10).place(x=20,y=400)
    c50=Button(cuentoFL, image=cuento188, command=sonidoaleatorio, height=50, width=50).place(x=360,y=400)
    cuento60=Button(cuentoFL,image=cuento188,command=repitelaoracion, height=50, width=50).place(x=700,y=400)
    cuentoFL.mainloop()
def regresarmenuFL7():
    cuentoFL.destroy()
    pygame.mixer.music.pause()
    menuFL1()

#MENU LETGLA GL

def entrarGL():
    menu.destroy()
    menuGL2()
def menuGL2():
    escuchayrepite()
    global GL1
    GL1=tix.Tk()
    GL1.geometry("800x480")
    GL1.config(bg="white")
    GL1.attributes("-fullscreen", True)
    imGL1=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/gl.png", master=GL1)
    imGL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=GL1)
    imGL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=GL1)
    botonGL1=Button(GL1, image=imGL1, command=GLGLGLGLGLGL, height=100, width=100).place(x=350,y=75)
    siguienteGL1=tix.Button(GL1,text="Siguiente",command=entrarmenuGL,width=20, height=3).place(x=600,y=300)
    regresarGL1=tix.Button(GL1,text="Regresar",command=regresarmenuGL2,width=20, height=3).place(x=30,y=300)
    siguienteGL12=tix.Button(GL1,image=imGL2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarGL12=tix.Button(GL1,image=imGL3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    GL1.mainloop()
def entrarmenuGL():
    pygame.mixer.music.pause()
    GL1.destroy()
    menuGL1()
def menuGL1():
    coloraleatorio()
    global menuGL
    menuGL=tix.Tk()
    menuGL.geometry("800x480")
    menuGL.config(bg="white")
    menuGL.attributes("-fullscreen", True)
    silabaGL= tix.Button(menuGL,text="Silabas",command=entrarsilabasGL,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasGL= tix.Button(menuGL,text="Palabras",command=entrarpalabrasGL,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenGL= tix.Button(menuGL,text="Discriminacion Fonetica",command=entrarmenuimagenGL,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoGL= tix.Button(menuGL,text="Frases",command=entrarmenucuentoGL,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirGL= tix.Button(menuGL,text="Regresar",command=regresarmenuGL1,width=23, height=3).place(x=600,y=350)
    menuGL.mainloop()
def entrarmenucuentoGL():
    menuGL.destroy()
    menucuentoGL()
def entrarsilabasGL():
    menuGL.destroy()
    SilabaGL1()
def SilabaGL1():
    escucharsilabas()
    global silabaGL
    silabaGL=tix.Tk()
    silabaGL.geometry("800x480")
    silabaGL.config(bg="white")
    silabaGL.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/silabas/gla.PNG", master=silabaGL)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/silabas/gle.PNG", master=silabaGL)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/silabas/gli.PNG", master=silabaGL)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/silabas/glo.PNG", master=silabaGL)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/silabas/glu.PNG", master=silabaGL)
    imGL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaGL)
    imGL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaGL)
    siguienteGL12=tix.Button(silabaGL,image=imGL2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarGL12=tix.Button(silabaGL,image=imGL3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaGL, image=r11, command=gla, height=150, width=200).place(x=20,y=50)
    re1=Button(silabaGL, image=r12, command=gle, height=150, width=200).place(x=240,y=50)
    ri1=Button(silabaGL, image=r13, command=gli, height=150, width=200).place(x=460,y=50)
    ro1=Button(silabaGL, image=r14, command=glo, height=150, width=200).place(x=20,y=250)
    ru1=Button(silabaGL, image=r15, command=glu, height=150, width=200).place(x=240,y=250)
    regresarGL1=Button(silabaGL,text="Regresar",command=regresarmenuGL3,width=15, height=10).place(x=460,y=250)
    silabaGL.mainloop()
def regresarmenuGL3():
    pygame.mixer.music.pause()
    silabaGL.destroy()
    menuGL1()
def entrarpalabrasGL():
    menuGL.destroy()
    tocaimagenrepite()
    menupalabrasGL1()
def menupalabrasGL1():
    global palabrasGL1
    palabrasGL1=tix.Tk()
    palabrasGL1.geometry("800x480")
    palabrasGL1.config(bg="white")
    palabrasGL1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/palabras/glaciar.png", master=palabrasGL1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/palabras/globos.png", master=palabrasGL1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/palabras/gordo.png", master=palabrasGL1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/palabras/iglesias.png", master=palabrasGL1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/palabras/regla.png", master=palabrasGL1)
    imGL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasGL1)
    imGL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasGL1)
    palabrasr11=Button(palabrasGL1, image=palabrar11, command=iglu, height=125, width=125,bg="white").place(x=245,y=145)
    palabrasr12=Button(palabrasGL1, image=palabrar12, command=globo, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasGL1, image=palabrar13, command=gloton, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasGL1, image=palabrar14, command=iglesia, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasGL1, image=palabrar15, command=regla, height=125, width=125,bg="white").place(x=395,y=145)
    regresarGL11=Button(palabrasGL1,text="Regresar",command=regresarmenuGL4,width=20, height=3).place(x=30,y=420)
    siguienteGL12=tix.Button(palabrasGL1,image=imGL2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarGL12=tix.Button(palabrasGL1,image=imGL3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasGL1.mainloop()

def regresarmenuGL4():
    pygame.mixer.music.pause()
    palabrasGL1.destroy()
    menuGL1()

def intentalodenuevo10():
    global contador10
    a.destroy()
    contador10=2
    menuimagenGL()
def entrarmenuimagenGL():
    global contador10
    contador10=1
    menuGL.destroy()
    menuimagenGL()
def regresarmenuGL6():
    pygame.mixer.music.pause()
    a.destroy()
    menuGL1()
def menuimagenGL():
    coloraleatorio()
    if (contador10==1):
        llevaimagenesgl()
    if (contador10==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=2
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=16
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaGL/imagenes/"
    q="1igl.png"
    q2="2igl.png"
    q3="3igl.png"
    q4="4igl.png"
    q5="5igl.png"
    q6="6igl.png"
    q7="7igl.png"
    q8="8igl.png"
    sonido="/home/pi/Desktop/tesis/audio/trebol.wav"
    sonido2="/home/pi/Desktop/tesis/audio/helado.wav"
    sonido3="/home/pi/Desktop/tesis/audio/iglesia.wav"
    sonido4="/home/pi/Desktop/tesis/audio/gallina.wav"
    sonido5="/home/pi/Desktop/tesis/audio/iglu.wav"
    sonido6="/home/pi/Desktop/tesis/audio/globo.wav"
    sonido7="/home/pi/Desktop/tesis/audio/fuego.wav"
    sonido8="/home/pi/Desktop/tesis/audio/regla.wav"
    sonido9="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido10="/home/pi/Desktop/tesis/audio/silencio.mp3"
    a = tk.Tk()
    a.title("DGLAG AND DGLOP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="regresar", command=regresarmenuGL6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="GL",  height=3, width=10, bg=colorboton, font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
    
def menucuentoGL():
    global audio
    global audio2
    global audio3
    global audio4
    audio="/home/pi/Desktop/tesis/audio/la-novia-se-caso.wav"
    audio2="/home/pi/Desktop/tesis/audio/en-la-fiesta-hay.wav"
    audio3="/home/pi/Desktop/tesis/audio/el-iglu-es.wav"
    global numerodefrases
    numerodefrases=3
    señalalosdibujos()
    global cuentoGL
    cuentoGL=tix.Tk()
    cuentoGL.geometry("800x480")
    cuentoGL.config(bg="white")
    cuentoGL.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/frases/1fgl.png", master=cuentoGL)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/frases/2fgl.png", master=cuentoGL)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/frases/3fgl.png", master=cuentoGL)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/frases/4fgl.png", master=cuentoGL)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGL/frases/5fgl.png", master=cuentoGL)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoGL)
    imGL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=cuentoGL)
    imGL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=cuentoGL)
    siguienteGL12=tix.Button(cuentoGL,image=imGL2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarGL12=tix.Button(cuentoGL,image=imGL3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    cuento1=Label(cuentoGL, text="La",height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=40)
    cuento2=Label(cuentoGL, image=cuento111,  height=50, width=50).place(x=50,y=40)
    cuento3=Label(cuentoGL, text="se caso en la",height=3, width=13,font=("Helvetica",12), bg="white").place(x=110,y=40)
    cuento4=Label(cuentoGL, image=cuento121, height=50, width=50).place(x=230,y=40)
    #primera frase
    cuento8=Label(cuentoGL, image=cuento131,  height=50, width=50).place(x=20,y=130)
    cuento9=Label(cuentoGL, text="hay muchos", height=3, width=10,font=("Helvetica",12), bg="white").place(x=80,y=130)
    cuento10=Label(cuentoGL, image=cuento141, height=50, width=50).place(x=170,y=130)
    #segunda frase
    cuento15=Label(cuentoGL, text="El", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=220)
    cuento16=Label(cuentoGL, image=cuento151, height=50, width=50).place(x=40,y=220)
    cuento18=Label(cuentoGL, text="es muy pequeño.", height=3, width=15,font=("Helvetica",12), bg="white").place(x=100,y=220)
    cuento21=Button(cuentoGL, text="Regresar", command=regresarmenuGL7, height=3, width=10).place(x=20,y=400)
    c50=Button(cuentoGL, image=cuento188, command=sonidoaleatorio, height=50, width=50).place(x=360,y=400)
    cuento60=Button(cuentoGL,image=cuento188,command=repitelaoracion, height=50, width=50).place(x=700,y=400)
    cuentoGL.mainloop()
def regresarmenuGL7():
    cuentoGL.destroy()
    pygame.mixer.music.pause()
    menuGL1()

#MENU LETPLA PL

def entrarPL():
    menu.destroy()
    menuPL2()
def menuPL2():
    escuchayrepite()
    global PL1
    PL1=tix.Tk()
    PL1.geometry("800x480")
    PL1.config(bg="white")
    PL1.attributes("-fullscreen", True)
    imPL1=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/pl.png", master=PL1)
    imPL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=PL1)
    imPL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=PL1)
    botonPL1=Button(PL1, image=imPL1, command=PLPLPLPLPLPL, height=100, width=100).place(x=350,y=75)
    siguientePL1=tix.Button(PL1,text="Siguiente",command=entrarmenuPL,width=20, height=3).place(x=600,y=300)
    regresarPL1=tix.Button(PL1,text="Regresar",command=regresarmenuPL2,width=20, height=3).place(x=30,y=300)
    siguientePL12=tix.Button(PL1,image=imPL2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarPL12=tix.Button(PL1,image=imPL3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    PL1.mainloop()
def entrarmenuPL():
    pygame.mixer.music.pause()
    PL1.destroy()
    menuPL1()
def menuPL1():
    coloraleatorio()
    global menuPL
    menuPL=tix.Tk()
    menuPL.geometry("800x480")
    menuPL.config(bg="white")
    menuPL.attributes("-fullscreen", True)
    silabaPL= tix.Button(menuPL,text="Silabas",command=entrarsilabasPL,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasPL= tix.Button(menuPL,text="Palabras",command=entrarpalabrasPL,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenPL= tix.Button(menuPL,text="Discriminacion Fonetica",command=entrarmenuimagenPL,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoPL= tix.Button(menuPL,text="Frases",command=entrarmenucuentoPL,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirPL= tix.Button(menuPL,text="Regresar",command=regresarmenuPL1,width=23, height=3).place(x=600,y=350)
    menuPL.mainloop()
def entrarmenucuentoPL():
    menuPL.destroy()
    menucuentoPL()
def entrarsilabasPL():
    menuPL.destroy()
    SilabaPL1()
def SilabaPL1():
    escucharsilabas()
    global silabaPL
    silabaPL=tix.Tk()
    silabaPL.geometry("800x480")
    silabaPL.config(bg="white")
    silabaPL.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/silabas/pla.PNG", master=silabaPL)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/silabas/ple.PNG", master=silabaPL)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/silabas/pli.PNG", master=silabaPL)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/silabas/plo.PNG", master=silabaPL)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/silabas/plu.PNG", master=silabaPL)
    imPL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaPL)
    imPL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaPL)
    siguientePL12=tix.Button(silabaPL,image=imPL2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarPL12=tix.Button(silabaPL,image=imPL3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaPL, image=r11, command=pla, height=150, width=200).place(x=20,y=50)
    re1=Button(silabaPL, image=r12, command=ple, height=150, width=200).place(x=240,y=50)
    ri1=Button(silabaPL, image=r13, command=pli, height=150, width=200).place(x=460,y=50)
    ro1=Button(silabaPL, image=r14, command=plo, height=150, width=200).place(x=20,y=250)
    ru1=Button(silabaPL, image=r15, command=plu, height=150, width=200).place(x=240,y=250)
    regresarPL1=Button(silabaPL,text="Regresar",command=regresarmenuPL3,width=15, height=10).place(x=460,y=250)
    silabaPL.mainloop()
def regresarmenuPL3():
    pygame.mixer.music.pause()
    silabaPL.destroy()
    menuPL1()
def entrarpalabrasPL():
    menuPL.destroy()
    tocaimagenrepite()
    menupalabrasPL1()
def menupalabrasPL1():
    global palabrasPL1
    palabrasPL1=tix.Tk()
    palabrasPL1.geometry("800x480")
    palabrasPL1.config(bg="white")
    palabrasPL1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/palabras/aplaudir.png", master=palabrasPL1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/palabras/plato.png", master=palabrasPL1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/palabras/playa.png", master=palabrasPL1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/palabras/pluma.png", master=palabrasPL1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/palabras/viento.png", master=palabrasPL1)
    imPL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasPL1)
    imPL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasPL1)
    palabrasr11=Button(palabrasPL1, image=palabrar11, command=aplaude, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasPL1, image=palabrar12, command=plato, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasPL1, image=palabrar13, command=playa, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasPL1, image=palabrar14, command=pluma, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasPL1, image=palabrar15, command=sopla, height=125, width=125,bg="white").place(x=620,y=10)
    regresarPL11=Button(palabrasPL1,text="Regresar",command=regresarmenuPL4,width=20, height=3).place(x=30,y=420)
    siguientePL12=tix.Button(palabrasPL1,image=imPL2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarPL12=tix.Button(palabrasPL1,image=imPL3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasPL1.mainloop()
def regresarmenuPL4():
    pygame.mixer.music.pause()
    palabrasPL1.destroy()
    menuPL1()
def intentalodenuevo11():
    global contador11
    a.destroy()
    contador11=2
    menuimagenPL()
def entrarmenuimagenPL():
    global contador11
    contador11=1
    menuPL.destroy()
    menuimagenPL()
def regresarmenuPL6():
    pygame.mixer.music.pause()
    a.destroy()
    menuPL1()
def menuimagenPL():
    coloraleatorio()
    if (contador11==1):
        llevaimagenespl()
    if (contador11==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=2
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=17
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaPL/imagenes/"
    q="1ifl.png"
    q2="2ipl.png"
    q3="3ipl.png"
    q4="4ipl.png"
    q5="5ipl.png"
    q6="6ipl.png"
    q7="7ipl.png"
    q8="8ipl.png"
    sonido="/home/pi/Desktop/tesis/audio/flauta.wav"
    sonido2="/home/pi/Desktop/tesis/audio/sucio.wav"
    sonido3="/home/pi/Desktop/tesis/audio/plato.wav"
    sonido4="/home/pi/Desktop/tesis/audio/cocodrilo.wav"
    sonido5="/home/pi/Desktop/tesis/audio/reloj.wav"
    sonido6="/home/pi/Desktop/tesis/audio/pluma.wav"
    sonido7="/home/pi/Desktop/tesis/audio/aplaude.wav"
    sonido8="/home/pi/Desktop/tesis/audio/manzana.wav"
    sonido9="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido10="/home/pi/Desktop/tesis/audio/silencio.mp3"
    a = tk.Tk()
    a.title("DPLAG AND DPLOP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuPL6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="PL",  height=3, width=10, bg=colorboton, font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
    
def menucuentoPL():
    global audio
    global audio2
    global audio3
    global audio4
    audio="/home/pi/Desktop/tesis/audio/el-viento-sopla.wav"
    audio2="/home/pi/Desktop/tesis/audio/el-plato-es.wav"
    audio3="/home/pi/Desktop/tesis/audio/el-aguila-tiene.wav"
    audio4="/home/pi/Desktop/tesis/audio/aplaudo-al-payaso.wav"
    global numerodefrases
    numerodefrases=4
    señalalosdibujos()
    global cuentoPL
    cuentoPL=tix.Tk()
    cuentoPL.geometry("800x480")
    cuentoPL.config(bg="white")
    cuentoPL.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/frases/1fpl.png", master=cuentoPL)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/frases/2fpl.png", master=cuentoPL)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/frases/3fpl.png", master=cuentoPL)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/frases/4fpl.png", master=cuentoPL)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/frases/5fpl.png", master=cuentoPL)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPL/frases/6fpl.png", master=cuentoPL)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoPL)
    imPL2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=cuentoPL)
    imPL3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=cuentoPL)
    siguientePL12=tix.Button(cuentoPL,image=imPL2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarPL12=tix.Button(cuentoPL,image=imPL3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    cuento1=Label(cuentoPL, text="El",height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=40)
    cuento2=Label(cuentoPL, image=cuento111,  height=50, width=50).place(x=50,y=40)
    cuento3=Label(cuentoPL, text="sopla muy fuerte.",height=3, width=17,font=("Helvetica",12), bg="white").place(x=100,y=40)
    #primera frase
    cuento4=Label(cuentoPL, text="El",height=3, width=4,font=("Helvetica",12), bg="white").place(x=20,y=110)
    cuento5=Label(cuentoPL, image=cuento121,  height=50, width=50).place(x=80,y=110)
    cuento6=Label(cuentoPL, text="es blanco",height=3, width=9,font=("Helvetica",12), bg="white").place(x=140,y=110)
    #segunda frase
    cuento7=Label(cuentoPL, text="El", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=180)
    cuento8=Label(cuentoPL, image=cuento131,  height=50, width=50).place(x=40,y=180)
    cuento9=Label(cuentoPL, text="tiene", height=3, width=5,font=("Helvetica",12), bg="white").place(x=100,y=180)
    cuento10=Label(cuentoPL, image=cuento141, height=50, width=50).place(x=160,y=180)
    #tercera frase
    cuento12=Label(cuentoPL, image=cuento151,height=50, width=50).place(x=20,y=250)
    cuento13=Label(cuentoPL, text="al payaso del", height=3, width=13,font=("Helvetica",12), bg="white").place(x=80,y=250)
    cuento14=Label(cuentoPL, image=cuento161, height=50, width=50).place(x=210,y=250)
    cuento21=Button(cuentoPL, text="Regresar", command=regresarmenuPL7, height=3, width=10).place(x=20,y=400)
    c50=Button(cuentoPL, image=cuento188, command=sonidoaleatorio, height=50, width=50).place(x=360,y=400)
    cuento60=Button(cuentoPL,image=cuento188,command=repitelaoracion, height=50, width=50).place(x=700,y=400)
    cuentoPL.mainloop()
def regresarmenuPL7():
    cuentoPL.destroy()
    pygame.mixer.music.pause()
    menuPL1()


#MENU LETRA BR

def entrarBR():
    menu.destroy()
    menuBR2()
def menuBR2():
    escuchayrepite()
    global BR1
    BR1=tix.Tk()
    BR1.geometry("800x480")
    BR1.config(bg="white")
    BR1.attributes("-fullscreen", True)
    imBR1=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/br.png", master=BR1)
    imBR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=BR1)
    imBR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=BR1)
    botonBR1=Button(BR1, image=imBR1, command=BRBRBRBRBRBR, height=100, width=100).place(x=350,y=75)
    siguienteBR1=tix.Button(BR1,text="Siguiente",command=entrarmenuBR,width=20, height=3).place(x=600,y=300)
    regresarBR1=tix.Button(BR1,text="Regresar",command=regresarmenuBR2,width=20, height=3).place(x=30,y=300)
    siguienteBR12=tix.Button(BR1,image=imBR2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarBR12=tix.Button(BR1,image=imBR3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    BR1.mainloop()
def entrarmenuBR():
    pygame.mixer.music.pause()
    BR1.destroy()
    menuBR1()
def menuBR1():
    coloraleatorio()
    global menuBR
    menuBR=tix.Tk()
    menuBR.geometry("800x480")
    menuBR.config(bg="white")
    menuBR.attributes("-fullscreen", True)
    silabaBR= tix.Button(menuBR,text="Silabas",command=entrarsilabasBR,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasBR= tix.Button(menuBR,text="Palabras",command=entrarpalabrasBR,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenBR= tix.Button(menuBR,text="Discriminacion Fonetica",command=entrarmenuimagenBR,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoBR= tix.Button(menuBR,text="Frases",command=entrarmenucuentoBR,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirBR= tix.Button(menuBR,text="Regresar",command=regresarmenuBR1,width=23, height=3).place(x=600,y=350)
    menuBR.mainloop()
def entrarmenucuentoBR():
    menuBR.destroy()
    menucuentoBR()
def entrarsilabasBR():
    menuBR.destroy()
    SilabaBR1()
def SilabaBR1():
    escucharsilabas()
    global silabaBR
    silabaBR=tix.Tk()
    silabaBR.geometry("800x480")
    silabaBR.config(bg="white")
    silabaBR.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/silabas/bra.PNG", master=silabaBR)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/silabas/bre.PNG", master=silabaBR)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/silabas/bri.PNG", master=silabaBR)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/silabas/bro.PNG", master=silabaBR)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/silabas/bru.PNG", master=silabaBR)
    imBR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaBR)
    imBR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaBR)
    siguienteBR12=tix.Button(silabaBR,image=imBR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarBR12=tix.Button(silabaBR,image=imBR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaBR, image=r11, command=bra, height=150, width=200).place(x=20,y=50)
    re1=Button(silabaBR, image=r12, command=bre, height=150, width=200).place(x=240,y=50)
    ri1=Button(silabaBR, image=r13, command=bri, height=150, width=200).place(x=460,y=50)
    ro1=Button(silabaBR, image=r14, command=bro, height=150, width=200).place(x=20,y=250)
    ru1=Button(silabaBR, image=r15, command=bru, height=150, width=200).place(x=240,y=250)
    regresarBR1=Button(silabaBR,text="Regresar",command=regresarmenuBR3,width=15, height=10).place(x=460,y=250)
    silabaBR.mainloop()
def regresarmenuBR3():
    pygame.mixer.music.pause()
    silabaBR.destroy()
    menuBR1()
def entrarpalabrasBR():
    menuBR.destroy()
    tocaimagenrepite()
    menupalabrasBR1()
def menupalabrasBR1():
    global palabrasBR1
    palabrasBR1=tix.Tk()
    palabrasBR1.geometry("800x480")
    palabrasBR1.config(bg="white")
    palabrasBR1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/palabras/brazo.png", master=palabrasBR1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/palabras/bruja.png", master=palabrasBR1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/palabras/libro.png", master=palabrasBR1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/palabras/sobres.png", master=palabrasBR1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/palabras/timbre.png", master=palabrasBR1)
    imBR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasBR1)
    imBR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasBR1)
    palabrasr11=Button(palabrasBR1, image=palabrar11, command=brazo, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasBR1, image=palabrar12, command=bruja, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasBR1, image=palabrar13, command=libro, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasBR1, image=palabrar14, command=sobre, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasBR1, image=palabrar15, command=timbre, height=125, width=125,bg="white").place(x=620,y=10)
    regresarBR11=Button(palabrasBR1,text="Regresar",command=regresarmenuBR4,width=20, height=3).place(x=30,y=420)
    siguienteBR12=tix.Button(palabrasBR1,image=imBR2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarBR12=tix.Button(palabrasBR1,image=imBR3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasBR1.mainloop()
def regresarmenuBR4():
    pygame.mixer.music.pause()
    palabrasBR1.destroy()
    menuBR1()
def intentalodenuevo12():
    global contador9
    a.destroy()
    contador9=2
    menuimagenBR()
def entrarmenuimagenBR():
    global contador9
    contador9=1
    menuBR.destroy()
    menuimagenBR()
def regresarmenuBR6():
    pygame.mixer.music.pause()
    a.destroy()
    menuBR1()
def menuimagenBR():
    coloraleatorio()
    if (contador9==1):
        llevaimagenesbr()
    if (contador9==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=1
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=18
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaBR/imagenes/"
    q="ibrazo.png"
    q2="ibruja.png"
    q3="idormir.png"
    q4="ifamilia.png"
    q5="ilibro.png"
    q6="isobre.png"
    q7="itimbre.png"
    q8="iuña.png"
    q9="iuva.png"
    sonido="/home/pi/Desktop/tesis/audio/brazo.wav"
    sonido2="/home/pi/Desktop/tesis/audio/bruja.wav"
    sonido3="/home/pi/Desktop/tesis/audio/siesta.wav"
    sonido4="/home/pi/Desktop/tesis/audio/familia.wav"
    sonido5="/home/pi/Desktop/tesis/audio/libro.wav"
    sonido6="/home/pi/Desktop/tesis/audio/sobre.wav"
    sonido7="/home/pi/Desktop/tesis/audio/timbre.wav"
    sonido8="/home/pi/Desktop/tesis/audio/uña.wav"
    sonido9="/home/pi/Desktop/tesis/audio/uva.wav"
    sonido10="/home/pi/Desktop/tesis/audio/silencio.mp3"
    a = tk.Tk()
    a.title("DRAG AND DROP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuBR6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="BR",  height=3, width=10, bg=colorboton, font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
def menucuentoBR():
    global audio
    global audio2
    global audio3
    global audio4
    audio="/home/pi/Desktop/tesis/audio/la-bruja-es-amiga-del-duende.wav"
    audio2="/home/pi/Desktop/tesis/audio/mi-profesora-lee.wav"
    audio3="/home/pi/Desktop/tesis/audio/el-abuelo-toca.wav"
    global numerodefrases
    numerodefrases=3
    señalalosdibujos()
    global cuentoBR
    cuentoBR=tix.Tk()
    cuentoBR.geometry("800x480")
    cuentoBR.config(bg="white")
    cuentoBR.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/frases/fanciano.png", master=cuentoBR)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/frases/fbruja.png", master=cuentoBR)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/frases/fcasa.png", master=cuentoBR)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/frases/fdedo.png", master=cuentoBR)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/frases/fduende.png", master=cuentoBR)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/frases/flibro.png", master=cuentoBR)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/frases/fmaestra.png", master=cuentoBR)
    cuento181=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaBR/frases/ftimbre.png", master=cuentoBR)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoBR)
    imBR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=cuentoBR)
    imBR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=cuentoBR)
    siguienteBR12=tix.Button(cuentoBR,image=imBR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarBR12=tix.Button(cuentoBR,image=imBR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    cuento1=Label(cuentoBR, text="La",height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=40)
    cuento2=Button(cuentoBR, image=cuento121, command=doctora, height=50, width=50).place(x=40,y=40)
    cuento3=Label(cuentoBR, text="es amiga del",height=3, width=12,font=("Helvetica",12), bg="white").place(x=100,y=40)
    cuento4=Button(cuentoBR, image=cuento151, command=clavel, height=50, width=50).place(x=210,y=40)
    #primera frase
    cuento5=Label(cuentoBR, text="Mi",height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=130)
    cuento6=Button(cuentoBR, image=cuento171, command=clavel, height=50, width=50).place(x=40,y=130)
    cuento7=Label(cuentoBR, text="lee el", height=3, width=6,font=("Helvetica",12), bg="white").place(x=100,y=130)
    cuento8=Button(cuentoBR, image=cuento161, command=girasol, height=50, width=50).place(x=160,y=130)
    #segunda frase
    cuento9=Label(cuentoBR, text="El", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=220)
    cuento10=Button(cuentoBR, image=cuento111, command=arbol ,height=50, width=50).place(x=40,y=220)
    cuento12=Button(cuentoBR, image=cuento141, command=bicicleta ,height=50, width=50).place(x=100,y=220)
    cuento13=Label(cuentoBR, text="el", height=3, width=2,font=("Helvetica",12), bg="white").place(x=160,y=220)
    cuento14=Button(cuentoBR, image=cuento181, command=doctora ,height=50, width=50).place(x=180,y=220)
    cuento15=Label(cuentoBR, text="de la", height=3, width=5,font=("Helvetica",12), bg="white").place(x=240,y=220)
    cuento16=Button(cuentoBR, image=cuento131, command=melon,height=50, width=50).place(x=290,y=220)
    cuento21=Button(cuentoBR, text="Regresar", command=regresarmenuBR7, height=3, width=10).place(x=20,y=320)
    c50=Button(cuentoBR, image=cuento188, command=sonidoaleatorio, height=50, width=50).place(x=360,y=400)
    cuento60=Button(cuentoBR,image=cuento188,command=repitelaoracion, height=50, width=50).place(x=700,y=400)
    cuentoBR.mainloop()
def regresarmenuBR7():
    cuentoBR.destroy()
    pygame.mixer.music.pause()
    menuBR1()

#MENU LETRA CR

def entrarCR():
    menu.destroy()
    menuCR2()
def menuCR2():
    escuchayrepite()
    global CR1
    CR1=tix.Tk()
    CR1.geometry("800x480")
    CR1.config(bg="white")
    CR1.attributes("-fullscreen", True)
    imCR1=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/cr.png", master=CR1)
    imCR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=CR1)
    imCR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=CR1)
    botonCR1=Button(CR1, image=imCR1, command=CRCRCRCRCRCR, height=100, width=100).place(x=350,y=75)
    siguienteCR1=tix.Button(CR1,text="Siguiente",command=entrarmenuCR,width=20, height=3).place(x=600,y=300)
    regresarCR1=tix.Button(CR1,text="Regresar",command=regresarmenuCR2,width=20, height=3).place(x=30,y=300)
    siguienteCR12=tix.Button(CR1,image=imCR2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarCR12=tix.Button(CR1,image=imCR3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    CR1.mainloop()
def entrarmenuCR():
    pygame.mixer.music.pause()
    CR1.destroy()
    menuCR1()
def menuCR1():
    coloraleatorio()
    global menuCR
    menuCR=tix.Tk()
    menuCR.geometry("800x480")
    menuCR.config(bg="white")
    menuCR.attributes("-fullscreen", True)
    silabaCR= tix.Button(menuCR,text="Silabas",command=entrarsilabasCR,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasCR= tix.Button(menuCR,text="Palabras",command=entrarpalabrasCR,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenCR= tix.Button(menuCR,text="Discriminacion Fonetica",command=entrarmenuimagenCR,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoCR= tix.Button(menuCR,text="Frases",command=entrarmenucuentoCR,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirCR= tix.Button(menuCR,text="Regresar",command=regresarmenuCR1,width=23, height=3).place(x=600,y=350)
    menuCR.mainloop()
def entrarmenucuentoCR():
    menuCR.destroy()
    menucuentoCR()
def entrarsilabasCR():
    menuCR.destroy()
    SilabaCR1()
def SilabaCR1():
    escucharsilabas()
    global silabaCR
    silabaCR=tix.Tk()
    silabaCR.geometry("800x480")
    silabaCR.config(bg="white")
    silabaCR.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/silabas/cra.PNG", master=silabaCR)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/silabas/cre.PNG", master=silabaCR)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/silabas/cri.PNG", master=silabaCR)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/silabas/cro.PNG", master=silabaCR)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/silabas/cru.PNG", master=silabaCR)
    imCR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaCR)
    imCR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaCR)
    siguienteCR12=tix.Button(silabaCR,image=imCR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarCR12=tix.Button(silabaCR,image=imCR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaCR, image=r11, command=cra, height=150, width=200).place(x=20,y=50)
    re1=Button(silabaCR, image=r12, command=cre, height=150, width=200).place(x=240,y=50)
    ri1=Button(silabaCR, image=r13, command=cri, height=150, width=200).place(x=460,y=50)
    ro1=Button(silabaCR, image=r14, command=cro, height=150, width=200).place(x=20,y=250)
    ru1=Button(silabaCR, image=r15, command=cru, height=150, width=200).place(x=240,y=250)
    regresarCR1=Button(silabaCR,text="Regresar",command=regresarmenuCR3,width=15, height=10).place(x=460,y=250)
    silabaCR.mainloop()
def regresarmenuCR3():
    pygame.mixer.music.pause()
    silabaCR.destroy()
    menuCR1()
def entrarpalabrasCR():
    menuCR.destroy()
    tocaimagenrepite()
    menupalabrasCR1()
def menupalabrasCR1():
    global palabrasCR1
    palabrasCR1=tix.Tk()
    palabrasCR1.geometry("800x480")
    palabrasCR1.config(bg="white")
    palabrasCR1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/palabras/craneo.png", master=palabrasCR1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/palabras/cristo.png", master=palabrasCR1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/palabras/cuadro.png", master=palabrasCR1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/palabras/microfono.png", master=palabrasCR1)
    imCR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasCR1)
    imCR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasCR1)
    palabrasr11=Button(palabrasCR1, image=palabrar11, command=craneo, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasCR1, image=palabrar12, command=cruz, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasCR1, image=palabrar13, command=cromo, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasCR1, image=palabrar14, command=microfono, height=125, width=125,bg="white").place(x=470,y=10)
    regresarCR11=Button(palabrasCR1,text="Regresar",command=regresarmenuCR4,width=20, height=3).place(x=30,y=420)
    siguienteCR12=tix.Button(palabrasCR1,image=imCR2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarCR12=tix.Button(palabrasCR1,image=imCR3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasCR1.mainloop()
def regresarmenuCR4():
    pygame.mixer.music.pause()
    palabrasCR1.destroy()
    menuCR1()
def intentalodenuevo13():
    global contador9
    a.destroy()
    contador9=2
    menuimagenCR()
def entrarmenuimagenCR():
    global contador9
    contador9=1
    menuCR.destroy()
    menuimagenCR()
def regresarmenuCR6():
    pygame.mixer.music.pause()
    a.destroy()
    menuCR1()
def menuimagenCR():
    coloraleatorio()
    if (contador9==1):
        llevaimagenescr()
    if (contador9==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=1
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=19
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaCR/imagenes/"
    q="ialfombra.png"
    q2="iburro.png"
    q3="icama.png"
    q4="icraneo.png"
    q5="icristo.png"
    q6="icuadro.png"
    q7="ilupa.png"
    q8="imicrofono.png"
    q9="inaranja.png"
    q10="iniño.png"
    sonido="/home/pi/Desktop/tesis/audio/bufanda.wav"
    sonido2="/home/pi/Desktop/tesis/audio/burro.wav"
    sonido3="/home/pi/Desktop/tesis/audio/cuna.wav"
    sonido4="/home/pi/Desktop/tesis/audio/craneo.wav"
    sonido5="/home/pi/Desktop/tesis/audio/cruz.wav"
    sonido6="/home/pi/Desktop/tesis/audio/cromo.wav"
    sonido7="/home/pi/Desktop/tesis/audio/lupa.wav"
    sonido8="/home/pi/Desktop/tesis/audio/microfono.wav"
    sonido9="/home/pi/Desktop/tesis/audio/naranjilla.wav"
    sonido10="/home/pi/Desktop/tesis/audio/chino.wav"
    a = tk.Tk()
    a.title("DRAG AND DROP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuCR6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="CR",  height=3, width=10, bg=colorboton, font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
def menucuentoCR():
    global audio
    global audio2
    global audio3
    global audio4
    audio="/home/pi/Desktop/tesis/audio/mis-amigas-cantan.wav"
    audio2="/home/pi/Desktop/tesis/audio/la-doctora.wav"
    audio3="/home/pi/Desktop/tesis/audio/guardo-mis-cromos.wav"
    audio4="/home/pi/Desktop/tesis/audio/mi-abuela-tiene-una.wav"
    global numerodefrases
    numerodefrases=4
    señalalosdibujos()
    global cuentoCR
    cuentoCR=tix.Tk()
    cuentoCR.geometry("800x480")
    cuentoCR.config(bg="white")
    cuentoCR.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/frases/fabuela.png", master=cuentoCR)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/frases/fcaja.png", master=cuentoCR)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/frases/fcraneo.png", master=cuentoCR)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/frases/fcristo.png", master=cuentoCR)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/frases/fcuadro.png", master=cuentoCR)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/frases/fdoctora.png", master=cuentoCR)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/frases/fmaestras.png", master=cuentoCR)
    cuento181=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaCR/frases/fmicrofono.png", master=cuentoCR)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoCR)
    imCR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=cuentoCR)
    imCR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=cuentoCR)
    siguienteCR12=tix.Button(cuentoCR,image=imCR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarCR12=tix.Button(cuentoCR,image=imCR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    cuento1=Label(cuentoCR, text="Mis",height=3, width=3,font=("Helvetica",12), bg="white").place(x=20,y=40)
    cuento2=Label(cuentoCR, image=cuento171,  height=50, width=50).place(x=50,y=40)
    cuento3=Label(cuentoCR, text="cantan con el",height=3, width=13,font=("Helvetica",12), bg="white").place(x=110,y=40)
    cuento4=Label(cuentoCR, image=cuento181, height=50, width=50).place(x=240,y=40)

    cuento5=Label(cuentoCR, text="La",height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=110)
    cuento6=Label(cuentoCR, image=cuento161,  height=50, width=50).place(x=40,y=110)
    cuento7=Label(cuentoCR, text="observa el", height=3, width=10,font=("Helvetica",12), bg="white").place(x=100,y=110)
    cuento8=Label(cuentoCR, image=cuento131,  height=50, width=50).place(x=200,y=110)

    cuento9=Label(cuentoCR, text="Guardo mis", height=3, width=10,font=("Helvetica",12), bg="white").place(x=20,y=180)
    cuento10=Label(cuentoCR, image=cuento151, height=50, width=50).place(x=120,y=180)
    cuento11=Label(cuentoCR, text="en la", height=3, width=5,font=("Helvetica",12), bg="white").place(x=180,y=180)
    cuento12=Label(cuentoCR, image=cuento121, height=50, width=50).place(x=230,y=180)

    cuento13=Label(cuentoCR, text="Mi", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=250)
    cuento14=Label(cuentoCR, image=cuento111, height=50, width=50).place(x=40,y=250)
    cuento15=Label(cuentoCR, text="tiene un", height=3, width=7,font=("Helvetica",12), bg="white").place(x=100,y=250)
    cuento16=Label(cuentoCR, image=cuento141, height=50, width=50).place(x=170,y=250)

    cuento21=Button(cuentoCR, text="Regresar", command=regresarmenuCR7, height=3, width=10).place(x=20,y=320)
    c50=Button(cuentoCR, image=cuento188, command=sonidoaleatorio, height=50, width=50).place(x=360,y=400)
    cuento60=Button(cuentoCR,image=cuento188,command=repitelaoracion, height=50, width=50).place(x=700,y=400)
    cuentoCR.mainloop()
def regresarmenuCR7():
    cuentoCR.destroy()
    pygame.mixer.music.pause()
    menuCR1()


#MENU LETRA DR

def entrarDR():
    menu.destroy()
    menuDR2()
def menuDR2():
    escuchayrepite()
    global DR1
    DR1=tix.Tk()
    DR1.geometry("800x480")
    DR1.config(bg="white")
    DR1.attributes("-fullscreen", True)
    imDR1=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/dr.png", master=DR1)
    imDR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=DR1)
    imDR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=DR1)
    botonDR1=Button(DR1, image=imDR1, command=DRDRDRDRDRDR, height=100, width=100).place(x=350,y=75)
    siguienteDR1=tix.Button(DR1,text="Siguiente",command=entrarmenuDR,width=20, height=3).place(x=600,y=300)
    regresarDR1=tix.Button(DR1,text="Regresar",command=regresarmenuDR2,width=20, height=3).place(x=30,y=300)
    siguienteDR12=tix.Button(DR1,image=imDR2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarDR12=tix.Button(DR1,image=imDR3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    DR1.mainloop()
def entrarmenuDR():
    pygame.mixer.music.pause()
    DR1.destroy()
    menuDR1()
def menuDR1():
    coloraleatorio()
    global menuDR
    menuDR=tix.Tk()
    menuDR.geometry("800x480")
    menuDR.config(bg="white")
    menuDR.attributes("-fullscreen", True)
    silabaDR= tix.Button(menuDR,text="Silabas",command=entrarsilabasDR,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasDR= tix.Button(menuDR,text="Palabras",command=entrarpalabrasDR,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenDR= tix.Button(menuDR,text="Discriminacion Fonetica",command=entrarmenuimagenDR,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoDR= tix.Button(menuDR,text="Frases",command=entrarmenucuentoDR,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirDR= tix.Button(menuDR,text="Regresar",command=regresarmenuDR1,width=23, height=3).place(x=600,y=350)
    menuDR.mainloop()
def entrarmenucuentoDR():
    menuDR.destroy()
    menucuentoDR()
def entrarsilabasDR():
    menuDR.destroy()
    SilabaDR1()
def SilabaDR1():
    escucharsilabas()
    global silabaDR
    silabaDR=tix.Tk()
    silabaDR.geometry("800x480")
    silabaDR.config(bg="white")
    silabaDR.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/silabas/dra.PNG", master=silabaDR)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/silabas/dre.PNG", master=silabaDR)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/silabas/dri.PNG", master=silabaDR)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/silabas/dro.PNG", master=silabaDR)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/silabas/dru.PNG", master=silabaDR)
    imDR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaDR)
    imDR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaDR)
    siguienteDR12=tix.Button(silabaDR,image=imDR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarDR12=tix.Button(silabaDR,image=imDR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaDR, image=r11, command=dra, height=150, width=200).place(x=20,y=50)
    re1=Button(silabaDR, image=r12, command=dre, height=150, width=200).place(x=240,y=50)
    ri1=Button(silabaDR, image=r13, command=dri, height=150, width=200).place(x=460,y=50)
    ro1=Button(silabaDR, image=r14, command=dro, height=150, width=200).place(x=20,y=250)
    ru1=Button(silabaDR, image=r15, command=dru, height=150, width=200).place(x=240,y=250)
    regresarDR1=Button(silabaDR,text="Regresar",command=regresarmenuDR3,width=15, height=10).place(x=460,y=250)
    silabaDR.mainloop()
def regresarmenuDR3():
    pygame.mixer.music.pause()
    silabaDR.destroy()
    menuDR1()
def entrarpalabrasDR():
    menuDR.destroy()
    tocaimagenrepite()
    menupalabrasDR1()
def menupalabrasDR1():
    global palabrasDR1
    palabrasDR1=tix.Tk()
    palabrasDR1.geometry("800x480")
    palabrasDR1.config(bg="white")
    palabrasDR1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/palabras/cocodrilo.png", master=palabrasDR1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/palabras/darmanzana.png", master=palabrasDR1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/palabras/ladrillo.png", master=palabrasDR1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/palabras/piedra.png", master=palabrasDR1)
    imDR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasDR1)
    imDR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasDR1)
    palabrasr11=Button(palabrasDR1, image=palabrar11, command=cocodrilo, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasDR1, image=palabrar12, command=madre, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasDR1, image=palabrar13, command=ladrillo, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasDR1, image=palabrar14, command=piedra, height=125, width=125,bg="white").place(x=470,y=10)
    regresarDR11=Button(palabrasDR1,text="Regresar",command=regresarmenuDR4,width=20, height=3).place(x=30,y=420)
    siguienteDR12=tix.Button(palabrasDR1,image=imDR2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarDR12=tix.Button(palabrasDR1,image=imDR3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasDR1.mainloop()
def regresarmenuDR4():
    pygame.mixer.music.pause()
    palabrasDR1.destroy()
    menuDR1()
def intentalodenuevo14():
    global contador9
    a.destroy()
    contador9=2
    menuimagenDR()
def entrarmenuimagenDR():
    global contador9
    contador9=1
    menuDR.destroy()
    menuimagenDR()
def regresarmenuDR6():
    pygame.mixer.music.pause()
    a.destroy()
    menuDR1()
def menuimagenDR():
    coloraleatorio()
    if (contador9==1):
        llevaimagenesdr()
    if (contador9==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=1
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=20
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaDR/imagenes/"
    q="icaramelo.png"
    q2="icocodrilo.png"
    q3="idarmanzana.png"
    q4="ihablar.png"
    q5="iladrillo.png"
    q6="ilobo.png"
    q7="ioveja.png"
    q8="ipiedra.png"
    q9="isucio.png"
    q10="pelear.png"
    sonido="/home/pi/Desktop/tesis/audio/caramelo.wav"
    sonido2="/home/pi/Desktop/tesis/audio/cocodrilo.wav"
    sonido3="/home/pi/Desktop/tesis/audio/madre.wav"
    sonido4="/home/pi/Desktop/tesis/audio/habla.wav"
    sonido5="/home/pi/Desktop/tesis/audio/ladrillo.wav"
    sonido6="/home/pi/Desktop/tesis/audio/lobo.wav"
    sonido7="/home/pi/Desktop/tesis/audio/borrego.wav"
    sonido8="/home/pi/Desktop/tesis/audio/piedra.wav"
    sonido9="/home/pi/Desktop/tesis/audio/sucio.wav"
    sonido10="/home/pi/Desktop/tesis/audio/pelea.wav"
    a = tk.Tk()
    a.title("DRAG AND DROP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuDR6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="DR",  height=3, width=10, bg=colorboton, font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
def menucuentoDR():
    global audio
    global audio2
    global audio3
    global audio4
    audio="/home/pi/Desktop/tesis/audio/se-rompio-la-cabeza.wav"
    audio2="/home/pi/Desktop/tesis/audio/el-cocodrilo-quiere.wav"
    audio3="/home/pi/Desktop/tesis/audio/madre-tiene-un-gran.wav"
    audio4=""
    global numerodefrases
    numerodefrases=3
    señalalosdibujos()
    global cuentoDR
    cuentoDR=tix.Tk()
    cuentoDR.geometry("800x480")
    cuentoDR.config(bg="white")
    cuentoDR.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/frases/cabeza.png", master=cuentoDR)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/frases/fcocodrilo.png", master=cuentoDR)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/frases/fcorazon.png", master=cuentoDR)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/frases/fdarmanzana.png", master=cuentoDR)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/frases/fniña.png", master=cuentoDR)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/frases/fpeces.png", master=cuentoDR)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaDR/frases/fpiedra.png", master=cuentoDR)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoDR)
    imDR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=cuentoDR)
    imDR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=cuentoDR)
    siguienteDR12=tix.Button(cuentoDR,image=imDR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarDR12=tix.Button(cuentoDR,image=imDR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    cuento1=Label(cuentoDR, text="Se rompio la",height=3, width=12,font=("Helvetica",12), bg="white").place(x=20,y=40)
    cuento2=Label(cuentoDR, image=cuento111,  height=50, width=50).place(x=140,y=40)
    cuento3=Label(cuentoDR, text="con una",height=3, width=7,font=("Helvetica",12), bg="white").place(x=200,y=40)
    cuento4=Label(cuentoDR, image=cuento171,  height=50, width=50).place(x=270,y=40)

    cuento5=Label(cuentoDR, text="El",height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=130)
    cuento6=Label(cuentoDR, image=cuento121,  height=50, width=50).place(x=40,y=130)
    cuento7=Label(cuentoDR, text="quiere comerse a los", height=3, width=20,font=("Helvetica",12), bg="white").place(x=100,y=130)
    cuento8=Label(cuentoDR, image=cuento161,  height=50, width=50).place(x=300,y=130)
    cuento9=Label(cuentoDR, text="de mi", height=3, width=5,font=("Helvetica",12), bg="white").place(x=360,y=130)
    cuento10=Label(cuentoDR, image=cuento151, height=50, width=50).place(x=410,y=130)

    cuento11=Label(cuentoDR, text="Mi", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=220)
    cuento12=Label(cuentoDR, image=cuento141, height=50, width=50).place(x=40,y=220)
    cuento13=Label(cuentoDR, text="tienen un gran", height=3, width=14,font=("Helvetica",12), bg="white").place(x=100,y=220)
    cuento14=Label(cuentoDR, image=cuento131, height=50, width=50).place(x=240,y=220)

    cuento21=Button(cuentoDR, text="Regresar", command=regresarmenuDR7, height=3, width=10).place(x=20,y=400)
    c50=Button(cuentoDR, image=cuento188, command=sonidoaleatorio, height=50, width=50).place(x=360,y=400)
    cuento60=Button(cuentoDR,image=cuento188,command=repitelaoracion, height=50, width=50).place(x=700,y=400)
    cuentoDR.mainloop()
def regresarmenuDR7():
    cuentoDR.destroy()
    pygame.mixer.music.pause()
    menuDR1()

#MENU LETRA FR

def entrarFR():
    menu.destroy()
    menuFR2()
def menuFR2():
    escuchayrepite()
    global FR1
    FR1=tix.Tk()
    FR1.geometry("800x480")
    FR1.config(bg="white")
    FR1.attributes("-fullscreen", True)
    imFR1=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/fr.png", master=FR1)
    imFR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=FR1)
    imFR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=FR1)
    botonFR1=Button(FR1, image=imFR1, command=FRFRFRFRFRFR, height=100, width=100).place(x=350,y=75)
    siguienteFR1=tix.Button(FR1,text="Siguiente",command=entrarmenuFR,width=20, height=3).place(x=600,y=300)
    regresarFR1=tix.Button(FR1,text="Regresar",command=regresarmenuFR2,width=20, height=3).place(x=30,y=300)
    siguienteFR12=tix.Button(FR1,image=imFR2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarFR12=tix.Button(FR1,image=imFR3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    FR1.mainloop()
def entrarmenuFR():
    pygame.mixer.music.pause()
    FR1.destroy()
    menuFR1()
def menuFR1():
    coloraleatorio()
    global menuFR
    menuFR=tix.Tk()
    menuFR.geometry("800x480")
    menuFR.config(bg="white")
    menuFR.attributes("-fullscreen", True)
    silabaFR= tix.Button(menuFR,text="Silabas",command=entrarsilabasFR,width=20, height=3,bg=colorboton).place(x=300,y=40)
    palabrasFR= tix.Button(menuFR,text="Palabras",command=entrarpalabrasFR,width=20, height=3,bg=colorboton2).place(x=300,y=120)
    imagenFR= tix.Button(menuFR,text="Discriminacion Fonetica",command=entrarmenuimagenFR,width=20, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoFR= tix.Button(menuFR,text="Frases",command=entrarmenucuentoFR,width=20, height=3,bg=colorboton4).place(x=300,y=280)
    salirFR= tix.Button(menuFR,text="Regresar",command=regresarmenuFR1,width=20, height=3).place(x=600,y=350)
    menuFR.mainloop()
def entrarmenucuentoFR():
    menuFR.destroy()
    menucuentoFR()
def entrarsilabasFR():
    menuFR.destroy()
    SilabaFR1()
def SilabaFR1():
    escucharsilabas()
    global silabaFR
    silabaFR=tix.Tk()
    silabaFR.geometry("800x480")
    silabaFR.config(bg="white")
    silabaFR.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/silabas/fra.PNG", master=silabaFR)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/silabas/fre.PNG", master=silabaFR)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/silabas/fri.PNG", master=silabaFR)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/silabas/fro.PNG", master=silabaFR)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/silabas/fru.PNG", master=silabaFR)
    imFR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaFR)
    imFR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaFR)
    siguienteFR12=tix.Button(silabaFR,image=imFR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarFR12=tix.Button(silabaFR,image=imFR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaFR, image=r11, command=fra, height=150, width=200).place(x=20,y=50)
    re1=Button(silabaFR, image=r12, command=fre, height=150, width=200).place(x=240,y=50)
    ri1=Button(silabaFR, image=r13, command=fri, height=150, width=200).place(x=460,y=50)
    ro1=Button(silabaFR, image=r14, command=fro, height=150, width=200).place(x=20,y=250)
    ru1=Button(silabaFR, image=r15, command=fru, height=150, width=200).place(x=240,y=250)
    regresarFR1=Button(silabaFR,text="Regresar",command=regresarmenuFR3,width=15, height=10).place(x=460,y=250)
    silabaFR.mainloop()
def regresarmenuFR3():
    pygame.mixer.music.pause()
    silabaFR.destroy()
    menuFR1()
def entrarpalabrasFR():
    menuFR.destroy()
    tocaimagenrepite()
    menupalabrasFR1()
def menupalabrasFR1():
    global palabrasFR1
    palabrasFR1=tix.Tk()
    palabrasFR1.geometry("800x480")
    palabrasFR1.config(bg="white")
    palabrasFR1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/palabras/frasco.png", master=palabrasFR1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/palabras/fresa.png", master=palabrasFR1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/palabras/frio.png", master=palabrasFR1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/palabras/frutas.png", master=palabrasFR1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/palabras/refrigeradora.png", master=palabrasFR1)
    imFR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasFR1)
    imFR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasFR1)
    palabrasr11=Button(palabrasFR1, image=palabrar11, command=frasco, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasFR1, image=palabrar12, command=frutilla, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasFR1, image=palabrar13, command=frio, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasFR1, image=palabrar14, command=frutas, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasFR1, image=palabrar15, command=refrigeradora, height=125, width=125,bg="white").place(x=620,y=10)
    regresarFR11=Button(palabrasFR1,text="Regresar",command=regresarmenuFR4,width=20, height=3).place(x=30,y=420)
    siguienteFR12=tix.Button(palabrasFR1,image=imFR2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarFR12=tix.Button(palabrasFR1,image=imFR3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasFR1.mainloop()
def regresarmenuFR4():
    pygame.mixer.music.pause()
    palabrasFR1.destroy()
    menuFR1()
def intentalodenuevo15():
    global contador9
    a.destroy()
    contador9=2
    menuimagenFR()
def entrarmenuimagenFR():
    global contador9
    contador9=1
    menuFR.destroy()
    menuimagenFR()
def regresarmenuFR6():
    pygame.mixer.music.pause()
    a.destroy()
    menuFR1()
def menuimagenFR():
    coloraleatorio()
    if (contador9==1):
        llevaimagenesfr()
    if (contador9==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=1
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=21
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaFR/imagenes/"
    q="ichancho.png"
    q2="icorazon.png"
    q3="ifrasco.png"
    q4="ifresa.png"
    q5="ifrio.png"
    q6="ifrutas.png"
    q7="iraton.png"
    q8="irefri.png"
    q9="jarra.png"
    q10="columpio.png"
    sonido="/home/pi/Desktop/tesis/audio/chancho.wav"
    sonido2="/home/pi/Desktop/tesis/audio/corazon.wav"
    sonido3="/home/pi/Desktop/tesis/audio/frasco.wav"
    sonido4="/home/pi/Desktop/tesis/audio/frutilla.wav"
    sonido5="/home/pi/Desktop/tesis/audio/frio.wav"
    sonido6="/home/pi/Desktop/tesis/audio/frutas.wav"
    sonido7="/home/pi/Desktop/tesis/audio/raton.wav"
    sonido8="/home/pi/Desktop/tesis/audio/refrigeradora.wav"
    sonido9="/home/pi/Desktop/tesis/audio/jarra.wav"
    sonido10="/home/pi/Desktop/tesis/audio/columpio.wav"
    a = tk.Tk()
    a.title("DRAG AND DROP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuFR6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="FR",  height=3, width=10, bg=colorboton, font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
def menucuentoFR():
    global audio
    global audio2
    global audio3
    global audio4
    audio="/home/pi/Desktop/tesis/audio/el-oso-come.wav"
    audio2="/home/pi/Desktop/tesis/audio/la-princesa-tiene-2.wav"
    audio3="/home/pi/Desktop/tesis/audio/cuando-llueve.wav"
    audio4="/home/pi/Desktop/tesis/audio/mama-guarda-en-la-refrigeradora.wav"
    global numerodefrases
    numerodefrases=4
    señalalosdibujos()
    global cuentoFR
    cuentoFR=tix.Tk()
    cuentoFR.geometry("800x480")
    cuentoFR.config(bg="white")
    cuentoFR.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/frases/cenicienta.png", master=cuentoFR)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/frases/ffresas.png", master=cuentoFR)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/frases/ffrio.png", master=cuentoFR)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/frases/ffrutas.png", master=cuentoFR)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/frases/fllovia.png", master=cuentoFR)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/frases/fmama.png", master=cuentoFR)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/frases/foso.png", master=cuentoFR)
    cuento181=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/frases/frefri.png", master=cuentoFR)
    cuento191=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaFR/frases/fteta.png", master=cuentoFR)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoFR)
    imFR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=cuentoFR)
    imFR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=cuentoFR)
    siguienteFR12=tix.Button(cuentoFR,image=imFR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarFR12=tix.Button(cuentoFR,image=imFR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    cuento1=Label(cuentoFR, text="El",height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=40)
    cuento2=Button(cuentoFR, image=cuento171, command=doctora, height=50, width=50).place(x=40,y=40)
    cuento3=Label(cuentoFR, text="come",height=3, width=4,font=("Helvetica",12), bg="white").place(x=100,y=40)
    cuento4=Button(cuentoFR, image=cuento141, command=girasol, height=50, width=50).place(x=140,y=40)
    cuento5=Label(cuentoFR, text="frescas.",height=3, width=8,font=("Helvetica",12), bg="white").place(x=200,y=40)

    cuento7=Label(cuentoFR, text="La", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=110)
    cuento8=Button(cuentoFR, image=cuento111, command=girasol, height=50, width=50).place(x=40,y=110)
    cuento9=Label(cuentoFR, text="tiene 2", height=3, width=7,font=("Helvetica",12), bg="white").place(x=100,y=110)
    cuento10=Button(cuentoFR, image=cuento121, command=arbol ,height=50, width=50).place(x=170,y=110)

    cuento11=Label(cuentoFR, text="Cuando", height=3, width=6,font=("Helvetica",12), bg="white").place(x=20,y=180)
    cuento12=Button(cuentoFR, image=cuento151, command=bicicleta ,height=50, width=50).place(x=80,y=180)
    cuento13=Label(cuentoFR, text="el niño tiene mucho", height=3, width=19,font=("Helvetica",12), bg="white").place(x=140,y=180)
    cuento14=Button(cuentoFR, image=cuento131, command=doctora ,height=50, width=50).place(x=330,y=180)

    cuento6=Button(cuentoFR, image=cuento161, command=clavel, height=50, width=50).place(x=20,y=250)
    cuento15=Label(cuentoFR, text="guarda en la", height=3, width=12,font=("Helvetica",12), bg="white").place(x=80,y=250)
    cuento16=Button(cuentoFR, image=cuento181, command=melon,height=50, width=50).place(x=200,y=250)
    cuento18=Label(cuentoFR, text="el", height=3, width=2,font=("Helvetica",12), bg="white").place(x=260,y=250)
    cuento19=Button(cuentoFR, image=cuento191, command=melon,height=50, width=50).place(x=280,y=250)
    cuento20=Label(cuentoFR, text="del bebe.", height=3, width=9,font=("Helvetica",12), bg="white").place(x=340,y=250)
    cuento21=Button(cuentoFR, text="Regresar", command=regresarmenuFR7, height=3, width=10).place(x=20,y=320)
    c50=Button(cuentoFR, image=cuento188, command=sonidoaleatorio, height=50, width=50).place(x=360,y=400)
    cuento60=Button(cuentoFR,image=cuento188,command=repitelaoracion, height=50, width=50).place(x=700,y=400)
    cuentoFR.mainloop()
def regresarmenuFR7():
    cuentoFR.destroy()
    pygame.mixer.music.pause()
    menuFR1()

#MENU LETRA GR

def entrarGR():
    menu.destroy()
    menuGR2()
def menuGR2():
    escuchayrepite()
    global GR1
    GR1=tix.Tk()
    GR1.geometry("800x480")
    GR1.config(bg="white")
    GR1.attributes("-fullscreen", True)
    imGR1=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/gr.png", master=GR1)
    imGR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=GR1)
    imGR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=GR1)
    botonGR1=Button(GR1, image=imGR1, command=GRGRGRGRGRGR, height=100, width=100).place(x=350,y=75)
    siguienteGR1=tix.Button(GR1,text="Siguiente",command=entrarmenuGR,width=20, height=3).place(x=600,y=300)
    regresarGR1=tix.Button(GR1,text="Regresar",command=regresarmenuGR2,width=20, height=3).place(x=30,y=300)
    siguienteGR12=tix.Button(GR1,image=imGR2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarGR12=tix.Button(GR1,image=imGR3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    GR1.mainloop()
def entrarmenuGR():
    pygame.mixer.music.pause()
    GR1.destroy()
    menuGR1()
def menuGR1():
    coloraleatorio()
    global menuGR
    menuGR=tix.Tk()
    menuGR.geometry("800x480")
    menuGR.config(bg="white")
    menuGR.attributes("-fullscreen", True)
    silabaGR= tix.Button(menuGR,text="Silabas",command=entrarsilabasGR,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasGR= tix.Button(menuGR,text="Palabras",command=entrarpalabrasGR,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenGR= tix.Button(menuGR,text="Discriminacion Fonetica",command=entrarmenuimagenGR,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoGR= tix.Button(menuGR,text="Frases",command=entrarmenucuentoGR,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirGR= tix.Button(menuGR,text="Regresar",command=regresarmenuGR1,width=23, height=3).place(x=600,y=350)
    menuGR.mainloop()
def entrarmenucuentoGR():
    menuGR.destroy()
    menucuentoGR()
def entrarsilabasGR():
    menuGR.destroy()
    SilabaGR1()
def SilabaGR1():
    escucharsilabas()
    global silabaGR
    silabaGR=tix.Tk()
    silabaGR.geometry("800x480")
    silabaGR.config(bg="white")
    silabaGR.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/silabas/gra.PNG", master=silabaGR)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/silabas/gre.PNG", master=silabaGR)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/silabas/gri.PNG", master=silabaGR)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/silabas/gro.PNG", master=silabaGR)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/silabas/gru.PNG", master=silabaGR)
    imGR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaGR)
    imGR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaGR)
    siguienteGR12=tix.Button(silabaGR,image=imGR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarGR12=tix.Button(silabaGR,image=imGR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaGR, image=r11, command=gra, height=150, width=200).place(x=20,y=50)
    re1=Button(silabaGR, image=r12, command=gre, height=150, width=200).place(x=240,y=50)
    ri1=Button(silabaGR, image=r13, command=gri, height=150, width=200).place(x=460,y=50)
    ro1=Button(silabaGR, image=r14, command=gro, height=150, width=200).place(x=20,y=250)
    ru1=Button(silabaGR, image=r15, command=gru, height=150, width=200).place(x=240,y=250)
    regresarGR1=Button(silabaGR,text="Regresar",command=regresarmenuGR3,width=15, height=10).place(x=460,y=250)
    silabaGR.mainloop()
def regresarmenuGR3():
    pygame.mixer.music.pause()
    silabaGR.destroy()
    menuGR1()
def entrarpalabrasGR():
    menuGR.destroy()
    tocaimagenrepite()
    menupalabrasGR1()
def menupalabrasGR1():
    global palabrasGR1
    palabrasGR1=tix.Tk()
    palabrasGR1.geometry("800x480")
    palabrasGR1.config(bg="white")
    palabrasGR1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/palabras/cangrejo.png", master=palabrasGR1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/palabras/demoler.png", master=palabrasGR1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/palabras/grillo.png", master=palabrasGR1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/palabras/grito.png", master=palabrasGR1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/palabras/tigre.png", master=palabrasGR1)
    imGR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasGR1)
    imGR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasGR1)
    palabrasr11=Button(palabrasGR1, image=palabrar11, command=cangrejo, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasGR1, image=palabrar12, command=grua, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasGR1, image=palabrar13, command=grillo, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasGR1, image=palabrar14, command=grita, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasGR1, image=palabrar15, command=tigre, height=125, width=125,bg="white").place(x=620,y=10)
    regresarGR11=Button(palabrasGR1,text="Regresar",command=regresarmenuGR4,width=20, height=3).place(x=30,y=420)
    siguienteGR12=tix.Button(palabrasGR1,image=imGR2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarGR12=tix.Button(palabrasGR1,image=imGR3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasGR1.mainloop()
def regresarmenuGR4():
    pygame.mixer.music.pause()
    palabrasGR1.destroy()
    menuGR1()
def intentalodenuevo16():
    global contador9
    a.destroy()
    contador9=2
    menuimagenGR()
def entrarmenuimagenGR():
    global contador9
    contador9=1
    menuGR.destroy()
    menuimagenGR()
def regresarmenuGR6():
    pygame.mixer.music.pause()
    a.destroy()
    menuGR1()
def menuimagenGR():
    coloraleatorio()
    if (contador9==1):
        llevaimagenesgr()
    if (contador9==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=2
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=22
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaGR/imagenes/"
    q="icangrejo.png"
    q2="idemoler.png"
    q3="igrillo.png"
    q4="igrito.png"
    q5="imariposa.png"
    q6="isandia.png"
    q7="itigre.png"
    q8="itoro.png"
    sonido="/home/pi/Desktop/tesis/audio/cangrejo.wav"
    sonido2="/home/pi/Desktop/tesis/audio/grua.wav"
    sonido3="/home/pi/Desktop/tesis/audio/grillo.wav"
    sonido4="/home/pi/Desktop/tesis/audio/grita.wav"
    sonido5="/home/pi/Desktop/tesis/audio/mariposa.wav"
    sonido6="/home/pi/Desktop/tesis/audio/sandia.wav"
    sonido7="/home/pi/Desktop/tesis/audio/tigre.wav"
    sonido8="/home/pi/Desktop/tesis/audio/toro.wav"
    sonido9="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido10="/home/pi/Desktop/tesis/audio/silencio.mp3"
    a = tk.Tk()
    a.title("DRAG AND DROP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuGR6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="GR",  height=3, width=10, bg=colorboton, font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
def menucuentoGR():
    global audio
    global audio2
    global audio3
    global audio4
    audio="/home/pi/Desktop/tesis/audio/en-la-playa-estan.wav"
    audio2="/home/pi/Desktop/tesis/audio/pepe-el-grillo.wav"
    audio3="/home/pi/Desktop/tesis/audio/el-tigre-el-oso.wav"
    audio4="/home/pi/Desktop/tesis/audio/ese-niño-grita.wav"
    global numerodefrases
    numerodefrases=4
    señalalosdibujos()
    global cuentoGR
    cuentoGR=tix.Tk()
    cuentoGR.geometry("800x480")
    cuentoGR.config(bg="white")
    cuentoGR.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/frases/fcangrejo.png", master=cuentoGR)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/frases/fgrillo.png", master=cuentoGR)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/frases/fgritar.png", master=cuentoGR)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/frases/fmontaña.png", master=cuentoGR)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/frases/foso.png", master=cuentoGR)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/frases/fpaisaje.png", master=cuentoGR)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/frases/fpantera.png", master=cuentoGR)
    cuento181=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaGR/frases/ftigre.png", master=cuentoGR)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoGR)
    imGR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=cuentoGR)
    imGR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=cuentoGR)
    siguienteGR12=tix.Button(cuentoGR,image=imGR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarGR12=tix.Button(cuentoGR,image=imGR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    cuento1=Label(cuentoGR, text="En la",height=3, width=5,font=("Helvetica",12), bg="white").place(x=20,y=40)
    cuento2=Label(cuentoGR, image=cuento161, height=50, width=50).place(x=70,y=40)
    cuento3=Label(cuentoGR, text="estan los",height=3, width=9,font=("Helvetica",12), bg="white").place(x=130,y=40)
    cuento4=Label(cuentoGR, image=cuento111,  height=50, width=50).place(x=220,y=40)

    cuento5=Label(cuentoGR, text="Pepe el",height=3, width=7,font=("Helvetica",12), bg="white").place(x=20,y=110)
    cuento6=Label(cuentoGR, image=cuento121,  height=50, width=50).place(x=90,y=110)
    cuento7=Label(cuentoGR, text="salta por el", height=3, width=12,font=("Helvetica",12), bg="white").place(x=150,y=110)
    cuento8=Label(cuentoGR, image=cuento141,  height=50, width=50).place(x=270,y=110)

    cuento9=Label(cuentoGR, text="El", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=180)
    cuento10=Label(cuentoGR, image=cuento181, height=50, width=50).place(x=40,y=180)
    cuento11=Label(cuentoGR, text="el", height=3, width=2,font=("Helvetica",12), bg="white").place(x=100,y=180)
    cuento12=Label(cuentoGR, image=cuento151, height=50, width=50).place(x=120,y=180)
    cuento13=Label(cuentoGR, text="y la", height=3, width=4,font=("Helvetica",12), bg="white").place(x=180,y=180)
    cuento14=Label(cuentoGR, image=cuento171, height=50, width=50).place(x=220,y=180)
    cuento15=Label(cuentoGR, text="son animales salvajes.", height=3, width=22,font=("Helvetica",12), bg="white").place(x=280,y=180)
    
    cuento18=Label(cuentoGR, text="Ese niño", height=3, width=8,font=("Helvetica",12), bg="white").place(x=20,y=250)
    cuento19=Label(cuentoGR, image=cuento131, height=50, width=50).place(x=100,y=250)
    cuento20=Label(cuentoGR, text="muy fuerte.", height=3, width=11,font=("Helvetica",12), bg="white").place(x=160,y=250)
    cuento21=Button(cuentoGR, text="Regresar", command=regresarmenuGR7, height=3, width=10).place(x=20,y=320)
    c50=Button(cuentoGR, image=cuento188, command=sonidoaleatorio, height=50, width=50).place(x=360,y=400)
    cuento60=Button(cuentoGR,image=cuento188,command=repitelaoracion, height=50, width=50).place(x=700,y=400)
    cuentoGR.mainloop()
def regresarmenuGR7():
    cuentoGR.destroy()
    pygame.mixer.music.pause()
    menuGR1()

#MENU LETRA PR

def entrarPR():
    menu.destroy()
    menuPR2()
def menuPR2():
    escuchayrepite()
    global PR1
    PR1=tix.Tk()
    PR1.geometry("800x480")
    PR1.config(bg="white")
    PR1.attributes("-fullscreen", True)
    imPR1=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/pr.png", master=PR1)
    imPR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=PR1)
    imPR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=PR1)
    botonPR1=Button(PR1, image=imPR1, command=PRPRPRPRPRPR, height=100, width=100).place(x=350,y=75)
    siguientePR1=tix.Button(PR1,text="Siguiente",command=entrarmenuPR,width=20, height=3).place(x=600,y=300)
    regresarPR1=tix.Button(PR1,text="Regresar",command=regresarmenuPR2,width=20, height=3).place(x=30,y=300)
    siguientePR12=tix.Button(PR1,image=imPR2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarPR12=tix.Button(PR1,image=imPR3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    PR1.mainloop()
def entrarmenuPR():
    pygame.mixer.music.pause()
    PR1.destroy()
    menuPR1()
def menuPR1():
    coloraleatorio()
    global menuPR
    menuPR=tix.Tk()
    menuPR.geometry("800x480")
    menuPR.config(bg="white")
    menuPR.attributes("-fullscreen", True)
    silabaPR= tix.Button(menuPR,text="Silabas",command=entrarsilabasPR,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasPR= tix.Button(menuPR,text="Palabras",command=entrarpalabrasPR,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenPR= tix.Button(menuPR,text="Discriminacion Fonetica",command=entrarmenuimagenPR,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoPR= tix.Button(menuPR,text="Frases",command=entrarmenucuentoPR,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirPR= tix.Button(menuPR,text="Regresar",command=regresarmenuPR1,width=23, height=3).place(x=600,y=350)
    menuPR.mainloop()
def entrarmenucuentoPR():
    menuPR.destroy()
    menucuentoPR()
def entrarsilabasPR():
    menuPR.destroy()
    SilabaPR1()
def SilabaPR1():
    escucharsilabas()
    global silabaPR
    silabaPR=tix.Tk()
    silabaPR.geometry("800x480")
    silabaPR.config(bg="white")
    silabaPR.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/silabas/pra.PNG", master=silabaPR)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/silabas/pre.PNG", master=silabaPR)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/silabas/pri.PNG", master=silabaPR)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/silabas/pro.PNG", master=silabaPR)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/silabas/pru.PNG", master=silabaPR)
    imPR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaPR)
    imPR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaPR)
    siguientePR12=tix.Button(silabaPR,image=imPR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarPR12=tix.Button(silabaPR,image=imPR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaPR, image=r11, command=pra, height=150, width=200).place(x=20,y=50)
    re1=Button(silabaPR, image=r12, command=pre, height=150, width=200).place(x=240,y=50)
    ri1=Button(silabaPR, image=r13, command=pri, height=150, width=200).place(x=460,y=50)
    ro1=Button(silabaPR, image=r14, command=pro, height=150, width=200).place(x=20,y=250)
    ru1=Button(silabaPR, image=r15, command=pru, height=150, width=200).place(x=240,y=250)
    regresarPR1=Button(silabaPR,text="Regresar",command=regresarmenuPR3,width=15, height=10).place(x=460,y=250)
    silabaPR.mainloop()
def regresarmenuPR3():
    pygame.mixer.music.pause()
    silabaPR.destroy()
    menuPR1()
def entrarpalabrasPR():
    menuPR.destroy()
    tocaimagenrepite()
    menupalabrasPR1()
def menupalabrasPR1():
    global palabrasPR1
    palabrasPR1=tix.Tk()
    palabrasPR1.geometry("800x480")
    palabrasPR1.config(bg="white")
    palabrasPR1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/palabras/paisaje.png", master=palabrasPR1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/palabras/premio.png", master=palabrasPR1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/palabras/princesa.png", master=palabrasPR1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/palabras/prision.png", master=palabrasPR1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/palabras/profesora.png", master=palabrasPR1)
    imPR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasPR1)
    imPR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasPR1)
    palabrasr11=Button(palabrasPR1, image=palabrar11, command=pradera, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasPR1, image=palabrar12, command=premio, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasPR1, image=palabrar13, command=princesa, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasPR1, image=palabrar14, command=preso, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasPR1, image=palabrar15, command=profesora, height=125, width=125,bg="white").place(x=620,y=10)
    regresarPR11=Button(palabrasPR1,text="Regresar",command=regresarmenuPR4,width=20, height=3).place(x=30,y=420)
    siguientePR12=tix.Button(palabrasPR1,image=imPR2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarPR12=tix.Button(palabrasPR1,image=imPR3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasPR1.mainloop()
def regresarmenuPR4():
    pygame.mixer.music.pause()
    palabrasPR1.destroy()
    menuPR1()
def intentalodenuevo17():
    global contador9
    a.destroy()
    contador9=2
    menuimagenPR()
def entrarmenuimagenPR():
    global contador9
    contador9=1
    menuPR.destroy()
    menuimagenPR()
def regresarmenuPR6():
    pygame.mixer.music.pause()
    a.destroy()
    menuPR1()
def menuimagenPR():
    coloraleatorio()
    if (contador9==1):
        llevaimagenespr()
    if (contador9==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=2
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=23
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaPR/imagenes/"
    q="ibuo.png"
    q2="icocodrilo.png"
    q3="ijirafa.png"
    q4="ipaisaje.png"
    q5="ipollo.png"
    q6="ipprincesa.png"
    q7="iprision.png"
    q8="iprofe.png"
    #q9="isoga.png"
    sonido="/home/pi/Desktop/tesis/audios/lechuza.mp3"
    sonido2="/home/pi/Desktop/tesis/audio/cocodrilo.wav"
    sonido3="/home/pi/Desktop/tesis/audio/jirafa.wav"
    sonido4="/home/pi/Desktop/tesis/audio/pradera.wav"
    sonido5="/home/pi/Desktop/tesis/audio/pollito.wav"
    sonido6="/home/pi/Desktop/tesis/audio/princesa.wav"
    sonido7="/home/pi/Desktop/tesis/audio/preso.wav"
    sonido8="/home/pi/Desktop/tesis/audio/profesora.wav"
    sonido9="/home/pi/Desktop/tesis/audio/silencio.mp3"
    sonido10="/home/pi/Desktop/tesis/audio/silencio.mp3"
    a = tk.Tk()
    a.title("DRAG AND DROP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuPR6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="PR",  height=3, width=10, bg=colorboton, font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
def menucuentoPR():
    global audio
    global audio2
    global audio3
    global audio4
    audio="/home/pi/Desktop/tesis/audio/la-princesa-come.wav"
    audio2="/home/pi/Desktop/tesis/audio/la-profesora-se-olvido.wav"
    audio3="/home/pi/Desktop/tesis/audio/el-conejo-salta.wav"
    audio4="/home/pi/Desktop/tesis/audio/esta-preso-porque.wav"
    global numerodefrases
    numerodefrases=4
    señalalosdibujos()
    global cuentoPR
    cuentoPR=tix.Tk()
    cuentoPR.geometry("800x480")
    cuentoPR.config(bg="white")
    cuentoPR.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/frases/fconejo.png", master=cuentoPR)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/frases/fdiamante.png", master=cuentoPR)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/frases/fhelados.png", master=cuentoPR)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/frases/fpaisaje.png", master=cuentoPR)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/frases/fprincesa.png", master=cuentoPR)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/frases/fprision.png", master=cuentoPR)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/frases/fprofe.png", master=cuentoPR)
    cuento181=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaPR/frases/fregla.png", master=cuentoPR)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoPR)
    imPR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=cuentoPR)
    imPR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=cuentoPR)
    siguientePR12=tix.Button(cuentoPR,image=imPR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarPR12=tix.Button(cuentoPR,image=imPR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    cuento1=Label(cuentoPR, text="La",height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=40)
    cuento2=Label(cuentoPR, image=cuento151,  height=50, width=50).place(x=40,y=40)
    cuento3=Label(cuentoPR, text="come muchos",height=3, width=11,font=("Helvetica",12), bg="white").place(x=100,y=40)
    cuento4=Label(cuentoPR, image=cuento131,  height=50, width=50).place(x=210,y=40)

    cuento5=Label(cuentoPR, text="La",height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=110)
    cuento6=Label(cuentoPR, image=cuento171,  height=50, width=50).place(x=40,y=110)
    cuento7=Label(cuentoPR, text="se olvido de llevar la", height=3, width=22,font=("Helvetica",12), bg="white").place(x=100,y=110)
    cuento8=Label(cuentoPR, image=cuento181, height=50, width=50).place(x=320,y=110)

    cuento9=Label(cuentoPR, text="El", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=180)
    cuento10=Label(cuentoPR, image=cuento111, height=50, width=50).place(x=40,y=180)
    cuento11=Label(cuentoPR, text="salta por el", height=3, width=12,font=("Helvetica",12), bg="white").place(x=100,y=180)
    cuento12=Label(cuentoPR, image=cuento141, height=50, width=50).place(x=220,y=180)

    cuento13=Label(cuentoPR, text="Esta en", height=3, width=7,font=("Helvetica",12), bg="white").place(x=20,y=250)
    cuento14=Label(cuentoPR, image=cuento161, height=50, width=50).place(x=90,y=250)
    cuento15=Label(cuentoPR, text="porque robo un", height=3, width=14,font=("Helvetica",12), bg="white").place(x=150,y=250)
    cuento16=Label(cuentoPR, image=cuento121, height=50, width=50).place(x=290,y=250)

    cuento21=Button(cuentoPR, text="Regresar", command=regresarmenuPR7, height=3, width=10).place(x=20,y=400)
    c50=Button(cuentoPR, image=cuento188, command=sonidoaleatorio, height=50, width=50).place(x=360,y=400)
    cuento60=Button(cuentoPR,image=cuento188,command=repitelaoracion, height=50, width=50).place(x=700,y=400)
    cuentoPR.mainloop()
def regresarmenuPR7():
    cuentoPR.destroy()
    pygame.mixer.music.pause()
    menuPR1()

#MENU LETRA TR

def entrarTR():
    menu.destroy()
    menuTR2()
def menuTR2():
    escuchayrepite()
    global TR1
    TR1=tix.Tk()
    TR1.geometry("800x480")
    TR1.config(bg="white")
    TR1.attributes("-fullscreen", True)
    imTR1=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/menuletras/tr.png", master=TR1)
    imTR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=TR1)
    imTR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=TR1)
    botonTR1=Button(TR1, image=imTR1, command=TRTRTRTRTRTR, height=100, width=100).place(x=350,y=75)
    siguienteTR1=tix.Button(TR1,text="Siguiente",command=entrarmenuTR,width=20, height=3).place(x=600,y=300)
    regresarTR1=tix.Button(TR1,text="Regresar",command=regresarmenuTR2,width=20, height=3).place(x=30,y=300)
    siguienteTR12=tix.Button(TR1,image=imTR2,command=muybienhecho,width=75, height=75).place(x=650,y=100)
    regresarTR12=tix.Button(TR1,image=imTR3,command=muymalhecho,width=75, height=75).place(x=80,y=100)
    TR1.mainloop()
def entrarmenuTR():
    pygame.mixer.music.pause()
    TR1.destroy()
    menuTR1()
def menuTR1():
    coloraleatorio()
    global menuTR
    menuTR=tix.Tk()
    menuTR.geometry("800x480")
    menuTR.config(bg="white")
    menuTR.attributes("-fullscreen", True)
    silabaTR= tix.Button(menuTR,text="Silabas",command=entrarsilabasTR,width=23, height=3,bg=colorboton).place(x=300,y=40)
    palabrasTR= tix.Button(menuTR,text="Palabras",command=entrarpalabrasTR,width=23, height=3,bg=colorboton2).place(x=300,y=120)
    imagenTR= tix.Button(menuTR,text="Discriminacion Fonetica",command=entrarmenuimagenTR,width=23, height=3,bg=colorboton3).place(x=300,y=200)
    cuentoTR= tix.Button(menuTR,text="Frases",command=entrarmenucuentoTR,width=23, height=3,bg=colorboton4).place(x=300,y=280)
    salirTR= tix.Button(menuTR,text="Regresar",command=regresarmenuTR1,width=23, height=3).place(x=600,y=350)
    menuTR.mainloop()
def entrarmenucuentoTR():
    menuTR.destroy()
    menucuentoTR()
def entrarsilabasTR():
    menuTR.destroy()
    SilabaTR1()
def SilabaTR1():
    escucharsilabas()
    global silabaTR
    silabaTR=tix.Tk()
    silabaTR.geometry("800x480")
    silabaTR.config(bg="white")
    silabaTR.attributes("-fullscreen", True)
    r11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/silabas/tra.PNG", master=silabaTR)
    r12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/silabas/tre.PNG", master=silabaTR)
    r13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/silabas/tri.PNG", master=silabaTR)
    r14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/silabas/tro.PNG", master=silabaTR)
    r15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/silabas/tru.PNG", master=silabaTR)
    imTR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=silabaTR)
    imTR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=silabaTR)
    siguienteTR12=tix.Button(silabaTR,image=imTR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarTR12=tix.Button(silabaTR,image=imTR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    ra1=Button(silabaTR, image=r11, command=tra, height=150, width=200).place(x=20,y=50)
    re1=Button(silabaTR, image=r12, command=tre, height=150, width=200).place(x=240,y=50)
    ri1=Button(silabaTR, image=r13, command=tri, height=150, width=200).place(x=460,y=50)
    ro1=Button(silabaTR, image=r14, command=tro, height=150, width=200).place(x=20,y=250)
    ru1=Button(silabaTR, image=r15, command=tru, height=150, width=200).place(x=240,y=250)
    regresarTR1=Button(silabaTR,text="Regresar",command=regresarmenuTR3,width=15, height=10).place(x=460,y=250)
    silabaTR.mainloop()
def regresarmenuTR3():
    pygame.mixer.music.pause()
    silabaTR.destroy()
    menuTR1()
def entrarpalabrasTR():
    menuTR.destroy()
    tocaimagenrepite()
    menupalabrasTR1()
def menupalabrasTR1():
    global palabrasTR1
    palabrasTR1=tix.Tk()
    palabrasTR1.geometry("800x480")
    palabrasTR1.config(bg="white")
    palabrasTR1.attributes("-fullscreen", True)
    palabrar11=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/palabras/estrella.png", master=palabrasTR1)
    palabrar12=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/palabras/monstruo.png", master=palabrasTR1)
    palabrar13=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/palabras/trebol.png", master=palabrasTR1)
    palabrar14=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/palabras/tren.png", master=palabrasTR1)
    palabrar15=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/palabras/triangulo.png", master=palabrasTR1)
    palabrar16=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/palabras/trompeta.png", master=palabrasTR1)
    imTR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=palabrasTR1)
    imTR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=palabrasTR1)
    palabrasr11=Button(palabrasTR1, image=palabrar11, command=estrella, height=125, width=125,bg="white").place(x=20,y=10)
    palabrasr12=Button(palabrasTR1, image=palabrar12, command=monstruo, height=125, width=125,bg="white").place(x=170,y=10)
    palabrasr13=Button(palabrasTR1, image=palabrar13, command=trebol, height=125, width=125,bg="white").place(x=320,y=10)
    palabrasr14=Button(palabrasTR1, image=palabrar14, command=tren, height=125, width=125,bg="white").place(x=470,y=10)
    palabrasr15=Button(palabrasTR1, image=palabrar15, command=triangulo, height=125, width=125,bg="white").place(x=620,y=10)
    palabrasr16=Button(palabrasTR1, image=palabrar16, command=trompeta, height=125, width=125,bg="white").place(x=20,y=145)
    regresarTR11=Button(palabrasTR1,text="Regresar",command=regresarmenuTR4,width=20, height=3).place(x=30,y=420)
    siguienteTR12=tix.Button(palabrasTR1,image=imTR2,command=muybienhecho,width=75, height=75).place(x=600,y=390)
    regresarTR12=tix.Button(palabrasTR1,image=imTR3,command=muymalhecho,width=75, height=75).place(x=700,y=390)
    palabrasTR1.mainloop()
def regresarmenuTR4():
    pygame.mixer.music.pause()
    palabrasTR1.destroy()
    menuTR1()
def intentalodenuevo19():
    global contador9
    a.destroy()
    contador9=2
    menuimagenTR()
def entrarmenuimagenTR():
    global contador9
    contador9=1
    menuTR.destroy()
    menuimagenTR()
def regresarmenuTR6():
    pygame.mixer.music.pause()
    a.destroy()
    menuTR1()
def menuimagenTR():
    coloraleatorio()
    if (contador9==1):
        llevaimagenestr()
    if (contador9==2):
        intentalootravez()
    global numerodeimagenes
    global numerodeaudios
    numerodeaudios=1
    global a
    global q
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q10
    global sonido
    global sonido2
    global sonido3
    global sonido4
    global sonido5
    global sonido6
    global sonido7
    global sonido8
    global sonido9
    global sonido10
    global IMAGE_PATH
    numerodeimagenes=24
    IMAGE_PATH ="/home/pi/Desktop/tesis/imagenes/FonemaTR/imagenes/"
    q="iaji.png"
    q2="ibruja.png"
    q3="iestrella.png"
    q4="ijirafa.png"
    q5="imonstruo.png"
    q6="itrebol.png"
    q7="itren.png"
    q8="itriangulo.png"
    q9="itrompeta.png"
    q10="navidad.png"
    sonido="/home/pi/Desktop/tesis/audio/aji.wav"
    sonido2="/home/pi/Desktop/tesis/audio/bruja.wav"
    sonido3="/home/pi/Desktop/tesis/audio/estrella.wav"
    sonido4="/home/pi/Desktop/tesis/audio/jirafa.wav"
    sonido5="/home/pi/Desktop/tesis/audio/monstruo.wav"
    sonido6="/home/pi/Desktop/tesis/audio/trebol.wav"
    sonido7="/home/pi/Desktop/tesis/audio/tren.wav"
    sonido8="/home/pi/Desktop/tesis/audio/triangulo.wav"
    sonido9="/home/pi/Desktop/tesis/audio/trompeta.wav"
    sonido10="/home/pi/Desktop/tesis/audio/navidad.wav"
    a = tk.Tk()
    a.title("DRAG AND DROP")
    a.geometry("800x480")
    a.attributes("-fullscreen", True)
    app = Application(a).pack(fill='both', expand=True)
    ap=Button(a, text="Regresar", command=regresarmenuTR6, height=3, width=10).place(x=20,y=350)
    cuento5=Label(a, text="TR",  height=3, width=10, bg=colorboton, font=("Helvetica",30)).place(x=300,y=350)
    a.mainloop()
def menucuentoTR():
    global audio
    global audio2
    global audio3
    global audio4
    audio="/home/pi/Desktop/tesis/audio/al-pirata-le-gusta.wav"
    audio2="/home/pi/Desktop/tesis/audio/la-bruja-es-amiga-del-monstruo.wav"
    audio3="/home/pi/Desktop/tesis/audio/el-policia-paro.wav"
    audio4="/home/pi/Desktop/tesis/audio/en-las-noches-de-luna-llena.wav"
    global numerodefrases
    numerodefrases=4
    señalalosdibujos()
    global cuentoTR
    cuentoTR=tix.Tk()
    cuentoTR.geometry("800x480")
    cuentoTR.config(bg="white")
    cuentoTR.attributes("-fullscreen", True)
    cuento111=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/frases/fbruja.png", master=cuentoTR)
    cuento121=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/frases/festrellas.png", master=cuentoTR)
    cuento131=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/frases/fguitarra.png", master=cuentoTR)
    cuento141=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/frases/flunallena.png", master=cuentoTR)
    cuento151=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/frases/fmonstruo.png", master=cuentoTR)
    cuento161=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/frases/fpirata.png", master=cuentoTR)
    cuento171=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/frases/ftren.png", master=cuentoTR)
    cuento181=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/frases/ftriangulo.png", master=cuentoTR)
    cuento191=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/frases/ftrompeta.png", master=cuentoTR)
    cuento1101=PhotoImage(file="/home/pi/Desktop/tesis/imagenes/FonemaTR/frases/policia.png", master=cuentoTR)
    cuento188=PhotoImage(file="/home/pi/Desktop/tesis/imagen/cuentoparlante.png", master=cuentoTR)
    imTR2=PhotoImage(file="/home/pi/Desktop/tesis/imagen/bien.png", master=cuentoTR)
    imTR3=PhotoImage(file="/home/pi/Desktop/tesis/imagen/mal.png", master=cuentoTR)
    siguienteTR12=tix.Button(cuentoTR,image=imTR2,command=muybienhecho,width=75, height=75).place(x=700,y=100)
    regresarTR12=tix.Button(cuentoTR,image=imTR3,command=muymalhecho,width=75, height=75).place(x=700,y=200)
    cuento1=Label(cuentoTR, text="Al",height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=40)
    cuento2=Label(cuentoTR, image=cuento161,  height=50, width=50).place(x=40,y=40)
    cuento3=Label(cuentoTR, text="le gusta tocar el",height=3, width=17,font=("Helvetica",12), bg="white").place(x=100,y=40)
    cuento4=Label(cuentoTR, image=cuento181,  height=50, width=50).place(x=270,y=40)
    cuento5=Label(cuentoTR, text="la",height=3, width=2,font=("Helvetica",12), bg="white").place(x=330,y=40)
    cuento6=Label(cuentoTR, image=cuento131,  height=50, width=50).place(x=350,y=40)
    cuento7=Label(cuentoTR, text="y la", height=3, width=4,font=("Helvetica",12), bg="white").place(x=410,y=40)
    cuento8=Label(cuentoTR, image=cuento191,  height=50, width=50).place(x=450,y=40)

    cuento9=Label(cuentoTR, text="La", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=110)
    cuento10=Label(cuentoTR, image=cuento111, height=50, width=50).place(x=40,y=110)
    cuento11=Label(cuentoTR, text="es amiga del", height=3, width=12,font=("Helvetica",12), bg="white").place(x=100,y=110)
    cuento12=Label(cuentoTR, image=cuento151, height=50, width=50).place(x=220,y=110)

    cuento13=Label(cuentoTR, text="El", height=3, width=2,font=("Helvetica",12), bg="white").place(x=20,y=180)
    cuento14=Label(cuentoTR, image=cuento1101, height=50, width=50).place(x=40,y=180)
    cuento15=Label(cuentoTR, text="paro la marcha del", height=3, width=17,font=("Helvetica",12), bg="white").place(x=100,y=180)
    cuento16=Label(cuentoTR, image=cuento171, height=50, width=50).place(x=270,y=180)

    cuento17=Label(cuentoTR, text="En las noches de", height=3, width=16,font=("Helvetica",12), bg="white").place(x=20,y=250)
    cuento18=Label(cuentoTR, image=cuento141, height=50, width=50).place(x=180,y=250)
    cuento19=Label(cuentoTR, text="puedo ver muchas", height=3, width=15,font=("Helvetica",12), bg="white").place(x=240,y=250)
    cuento20=Label(cuentoTR, image=cuento121, height=50, width=50).place(x=390,y=250)
    cuento21=Button(cuentoTR, text="Regresar", command=regresarmenuTR7, height=3, width=10).place(x=20,y=400)
    c50=Button(cuentoTR, image=cuento188, command=sonidoaleatorio, height=50, width=50).place(x=360,y=400)
    cuento60=Button(cuentoTR,image=cuento188,command=repitelaoracion, height=50, width=50).place(x=700,y=400)
    cuentoTR.mainloop()
def regresarmenuTR7():
    cuentoTR.destroy()
    pygame.mixer.music.pause()
    menuTR1()

    
global ventana
ventana=tix.Tk()
ventana.geometry("800x480")
ventana.config(bg="gray71")
ventana.title("FONA")
ventana.attributes("-fullscreen", True)

class ImageLabel(tix.Label):
    def load(self, im: object) -> object:
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []
        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)
            
lbl = ImageLabel(ventana)
lbl.bind("<Button-1>", callback3)
lbl.pack()
lbl.load('/home/pi/Desktop/tesis/gestos/charla_ muestra.gif')
pygame.mixer.music.load("/home/pi/Desktop/tesis/audios/saludoinicial.wav")
pygame.mixer.music.play(1)
#men= tix.Button(ventana,text="MENU",command=entrar,width=20, height=3, bg="gray88").place(x=325,y=50)
ventana.mainloop()

