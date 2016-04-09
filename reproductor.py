# UNEFA Mérida
# Integrantes: eidyyolisbeth, GladysBG, jeanc123
# Profesor: javierri
# Calificación

class reproductor:

# Atributos
    rp_encendido=False
    lector_cerrado=False
    capacidad_cd=3
    capacidad_usb=2
    nro_cd=0
    nro_usb=0
    usb=False
    reproducir_cd=False
    radio_am=True
    radio_fm=False
    volumen=50
    nro_cancion=0
    pausa=False
    

    def encender(self):
        if (self.rp_encendido==False):
            self.rp_encendido=True

    def apagar(self):
        if (self.rp_encendido==True):
            self.rp_encendido=False

    def USB (self):
        if (self.rp_encendido==True):
            self.usb=True
            self.reproducir_cd=False
        print "Leyendo puerto usb"
     
    def CD(self):
        if (self.rp_encendido==True):
            self.usb=False
            self.reproducir_cd=True
        print "leyendo CD"
    
        

    def abrir_lector(self):
        if (self.reproducir_cd==True and self.lector_cerrado==True and self.rp_encendido):
            self.lactor_cerrado=False
        print "abrir lector"
            

    def cerrar_lector(self):
        if (self.reproducir_cd==True and self.lector_cerrado==False and self.rp_encendido):
            self.lector_cerrado=True
        print "cerrar lector"
            

    def ingresar_cd(self):
        if (self.lector_cerrado==False and self.rp_encendido and self.reproducir_cd==True):
            if (self.nro_cd < self.capacidad_cd):
                self.nro_cd = self.nro_cd+1
                print "Ingrese CD", self.nro_cd
            else:
                print "No puede ingresar CD"
        else:
            print "Error al ingresar CD"


    def extraer_cd(self):
        if (self.reproducir_cd==True and self.lector_cerrado==False and self.rp_encendido):
            if (self.nro_cd > 0):
                self.nro_cd = self.nro_cd -1
                print "extraer el CD", self.nro_cd
            else:
                print "No puede extraer el CD"
        else:
            print "Error al extraer el CD"
            

    def subir_vol(self, subir):
        if (self.lector_cerrado==False and self.rp_encendido):
            if (subir < self.volumen and subir > 0 ):
                subir = subir+1
                print "Subir volumen", subir
                

    def bajar_vol(self, bajar):
        if (self.lector_cerrado==False and self.rp_encendido):
            if (bajar < self.volumen and bajar <=50 ):
                bajar = bajar-1
                print "Bajar volumen", bajar
                
    def siguiente(self,adelantar):
        if (self.rp_encendido and self.lector_cerrado==True and self.reproducir_cd==True and self.pausa==True):
            if (adelantar > self.nro_cancion):
                adelantar=adelantar+1
                print "Siguiente"
            print "La melodia que esta oyendo es la numero", adelantar
            

    def anterior(self,retroceder):
        if (self.rp_encendido and self.lector_cerrado==True and self.reproducir_cd==True and self.pausa==True):
            if (retroceder > self.nro_cancion):
                retroceder=retroceder-1
                print "anterior"
                print "La melodia que esta oyendo es la numero", retroceder

    def pausar(self):
        if (self.rp_encendido and self.lector_cerrado==True and self.pausa==False):
                 self.pausa=True
                 print "pausa"
     
    def seguir(self):
        if(self.rp_encendido and self.lector_cerrado==True and self.pausa==False):
                self.pausa=False
                print "play"
            

            
    def reproducir(self, cd):
        if (cd > self.capacidad_cd):
            print "Error al reproducir"
            return
        
        if (self.nro_cd > self.capacidad_cd):
            print "Exceso de CD"
            return
        
        self.abrir_lector()
        #self.cerrar_lector()
    

        if (self.nro_cd < cd):
            for i in range (cd-self.nro_cd):
                self.ingresar_cd()
            print "Cerrar lector"
            print "Reproducir"
    
    
        
        if (self.nro_cd < cd):
            for i in range (self.nro_cd - cd):
                self.extraer_cd()
            print "Extraer CD"
            print "Cerrar lector"
        
     
    
    def insertar_usb(self):
        if (self.rp_encendido and self.usb==True):
            if (self.nro_usb < self.capacidad_usb):
                self.nro_usb = self.nro_usb+1
                print "Inserte usb", self.nro_usb
            else:
                print "No puede insertar usb"  
     
    def reproducir_usb(self, usb):
        if (usb > self.capacidad_usb):
            print "error al ingresar usb"
            return
     
        if (self.nro_usb > self.capacidad_usb):
            print "execeso de usb"
            return
        
        if (self.nro_usb < usb):
            for i in range (usb-self.nro_usb):
                self.insertar_usb()
            print "leer usb"
    
        
     
            

        
# Principal

a= reproductor()
a.encender()
a.CD()
#a.USB()
# cantidad de CD
a.reproducir(2)
a.reproducir(3)
# volumen
a.subir_vol(10)
a.bajar_vol(5)
# musica
a.siguiente(1)    
a.anterior(15)           
a.pausar()            
#USB
#a.reproducir_usb(1) 
#a.reproducir_usb(2)       
