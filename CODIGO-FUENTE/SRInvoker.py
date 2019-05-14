
# author: vlarobbyk


import tkinter as tk
import webbrowser as wb
import subprocess as sp
import random
import os

class SRInvoker:
    
    
    def __init__(self):
        self.root = tk.Tk()
        self.initialize()
        
    def initialize(self,path = 'imagenes'):
        self.root.title('Invoking speech recognizer')

        self.proceso = sp.Popen(['python3','-m','http.server','8000'])

        
        btnIniciar = tk.Button(self.root, text = 'Iniciar', command = self.iniciar)
        btnIniciar.grid(row = 0, column = 0)
        btnIniciar.config(font = ('Arial',15))
        
        self.files = os.listdir(path)
        self.path = path
        self.root.mainloop()

    def on_closing():
        self.proceso.kill()
        self.root.destroy()
        
    def iniciar(self):
        name = self.files[random.randint(0,len(self.files)-1)]
        img = '<img src=\''+self.path+'/'+name+'\' />'

        
        
        text = """
            <html>
            <body>
            <FONT COLOR="#FF0000">D</FONT> <FONT
            <form name=\'f1\' action=\'\' >
                <input type=\'text\' id=\'txtRes\' name=\'txtRes\' value=\' \' />
            </form>
            <div id=\'transcript\'></div>

            <script language='javascript'>
            const recognition = new webkitSpeechRecognition();

            var transcript = document.getElementById('txtRes');
            var objectName = \'"""+name[0:name.index('.')]+"""\';

        
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.onresult = function(event) {
                console.log(event.results[0][0].transcript);
                if (event.results[0][0].transcript){
                    transcript.value = event.results[0][0].transcript;
                    if (event.results[0][0].transcript == objectName){
                        //alert('Muy bien, acertaste!');
                        recognition.stop();
                    }
                }
                if (event.results[0].isFinal) {
                    //console.log(event.results[0][0].transcript);
                
                    //alert('Terminó'+event.results[0][0].transcript);
                    
                    //transcript.innerHTML='<strong>event.results[0][0].transcript</strong>';
                    if (event.results[0][0].transcript == objectName){
                        alert('Muy bien, acertaste!');
                        recognition.stop();
                    }
                
                    recognition.stop();
                }
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
            </script>"""

        text += img+'</body></html>'
        
        
        url = 'http://localhost:8000/SpeechRecognition.html'
        _file = open('SpeechRecognition.html','w')
        _file.write(text)
        _file.close()
        #wb.open_new_tab(url)
        sp.Popen(['/usr/bin/chromium-browser', url])
        
if __name__=="__main__":
    srinvoker = SRInvoker()
