#DECLARACION DE LIBRERIAS DEL MODULO TKINTER
from Tkinter import*
from ttk import*
import tkFont
import tkMessageBox
import os
import subprocess
import time
#import mysql.connector
####################  DEFINICION DE LA VENTANA PRINCIPAL (VENTANA PADRE)  ######################
v1=Tk()
v1.geometry("1010x530+0+0")
v1.title("USAP SMARTMILL")

# ----------------------- Definition of method ------------------------------------

def save():

         tab=StringVar()
         hi=horai.get()
         mi=mini.get()
         hf=horaf.get()
         mf=minf.get()
         dia="*"
         mes="*"
         ano="*"
         tab=" "
         user="root"

         path="/home/pi/motoron.sh"
         path2="/home/pi/motoroff.sh"
         cadena=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path))
         print(str(cadena))

         #tkMessageBox.showinfo("Save",message="Horario Programado con Exito")
         os.system("sudo chmod -R 777 /etc/cron.d/tarea")
         pf=open(r'/etc/cron.d/tarea','w')
         pf.write(cadena)
         pf.write("\n")
         pf.close()
         cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2))
         print(str(cadena2))
         os.system("sudo chmod -R 777 /etc/cron.d/tarea2")
         pf2=open(r'/etc/cron.d/tarea2','w')
         pf2.write(cadena2)
         pf2.write("\n")
         pf2.close()
         #pygame.mixer.music.load("/home/pi/PracticasTK/horarioprog.mp3")
         #pygame.mixer.music.play()
         os.system("sudo chmod -R 755 /etc/cron.d/tarea")
         os.system("sudo chmod -R 755 /etc/cron.d/tarea2")
         os.system("sudo /etc/init.d/cron restart")

def toplevel():
    # Las variables Globales siempre deben de declarse al inicio de cada metodo o funcion
    # Para que no generen advertencias o warning ejemplo:syntaxwarning name is assigned to before global declaration
    global horai
    global horaf
    global mini
    global minf
    v1=Toplevel()
    v1.title("Configurar Horarios")
    v1.geometry("450x300+200+200")
    mini=StringVar()
    minf=StringVar()
    horai=StringVar()
    horaf=StringVar()
    # Declarar Variables Globales para ser usadas dentro de cualquier funcion o metodo
    texttop=tkFont.Font(family="Helvetica",size=10,weight="bold")
    texttop2=tkFont.Font(family="Helvetica",size=9,weight="bold")
    label1top=Label(v1,text="HORARIO DE ACTIVACION & DESACTIVACION DE AULA 1",font=texttop).place(x=50,y=10)
    label2top=Label(v1,text="HORA INICIAL :",font=texttop2).place(x=110,y=70)
    caja2=Entry(v1,textvariable=horai,width=20).place(x=215,y=70)
    label3top=Label(v1,text="MINUTO INICIAL :",font=texttop2).place(x=110,y=110)
    TextBox2=Entry(v1,textvariable=mini,width=20).place(x=215,y=110)
    label4top=Label(v1,text="HORA FINAL :",font=texttop2).place(x=110,y=150)
    TextBox3=Entry(v1,textvariable=horaf,width=20).place(x=215,y=150)
    label5top=Label(v1,text="MINUTO FINAL :",font=texttop2).place(x=110,y=190)
    TextBox4=Entry(v1,textvariable=minf,width=20).place(x=215,y=190)
    # Boton Guardar
    imgsave=PhotoImage(file="guardar.gif")
    botosettings=Button(v1,image=imgsave,command=save,width=50).place(x=215,y=220,height=50)
    # Boton Salir 
    botonclose=Button(v1,text="Salir",command=v1.destroy).place (x=295,y=220,height=50)
    # Reloj Time
    def update():
           current=time.strftime("%H:%M:%S")
           labelTiempo=Label(v1,text=" -- Tiempo --").place(x=110,y=230)
           labeltime=Label(v1,text=current).place(x=120,y=250)
           v1.after(1000,update)
    update()     
    v1.mainloop()



######## sensor 1 ########

def save2():

         tab=StringVar()
         hi=horai.get()
         mi=mini.get()
         hf=horaf.get()
         mf=minf.get()
         dia="*"
         mes="*"
         ano="*"
         tab=" "
         user="root"

         path="/home/pi/sensor1on.sh"
         path2="/home/pi/sensor1off.sh"
         cadena=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path))
         print(str(cadena))

         #tkMessageBox.showinfo("Save",message="Horario Programado con Exito")
         os.system("sudo chmod -R 777 /etc/cron.d/sensor1on")
         pf=open(r'/etc/cron.d/sensor1on','w')
         pf.write(cadena)
         pf.write("\n")
         pf.close()
         cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2))
         print(str(cadena2))
         os.system("sudo chmod -R 777 /etc/cron.d/sensor1off")
         pf2=open(r'/etc/cron.d/sensor1off','w')
         pf2.write(cadena2)
         pf2.write("\n")
         pf2.close()
         #pygame.mixer.music.load("/home/pi/PracticasTK/horarioprog.mp3")
         #pygame.mixer.music.play()
         os.system("sudo chmod -R 755 /etc/cron.d/sensor1on")
         os.system("sudo chmod -R 755 /etc/cron.d/sensor1off")
         os.system("sudo /etc/init.d/cron restart")

def toplevel2():
    # Las variables Globales siempre deben de declarse al inicio de cada metodo o funcion
    # Para que no generen advertencias o warning ejemplo:syntaxwarning name is assigned to before global declaration
    global horai
    global horaf
    global mini
    global minf
    v1=Toplevel()
    v1.title("Configurar Horarios")
    v1.geometry("450x300+200+200")
    mini=StringVar()
    minf=StringVar()
    horai=StringVar()
    horaf=StringVar()
    # Declarar Variables Globales para ser usadas dentro de cualquier funcion o metodo
    texttop=tkFont.Font(family="Helvetica",size=10,weight="bold")
    texttop2=tkFont.Font(family="Helvetica",size=9,weight="bold")
    label1top=Label(v1,text="HORARIO DE ACTIVACION & DESACTIVACION DE AULA 1",font=texttop).place(x=50,y=10)
    label2top=Label(v1,text="HORA INICIAL :",font=texttop2).place(x=110,y=70)
    caja2=Entry(v1,textvariable=horai,width=20).place(x=215,y=70)
    label3top=Label(v1,text="MINUTO INICIAL :",font=texttop2).place(x=110,y=110)
    TextBox2=Entry(v1,textvariable=mini,width=20).place(x=215,y=110)
    label4top=Label(v1,text="HORA FINAL :",font=texttop2).place(x=110,y=150)
    TextBox3=Entry(v1,textvariable=horaf,width=20).place(x=215,y=150)
    label5top=Label(v1,text="MINUTO FINAL :",font=texttop2).place(x=110,y=190)
    TextBox4=Entry(v1,textvariable=minf,width=20).place(x=215,y=190)
    # Boton Guardar
    imgsave=PhotoImage(file="guardar.gif")
    botosettings=Button(v1,image=imgsave,command=save2,width=50).place(x=215,y=220,height=50)
    # Boton Salir 
    botonclose=Button(v1,text="Salir",command=v1.destroy).place (x=295,y=220,height=50)
    # Reloj Time
    def update():
           current=time.strftime("%H:%M:%S")
           labelTiempo=Label(v1,text=" -- Tiempo --").place(x=110,y=230)
           labeltime=Label(v1,text=current).place(x=120,y=250)
           v1.after(1000,update)
    update()     
    v1.mainloop()

    

def on():
         text_d1=tkFont.Font(family="Helvetica",size=10)
         label_d1=Label(v1,text="-- ON --",font=text_d1).place(x=350,y=430)
         os.system("sudo /./home/pi/motoron.sh &")
def off():
          text_d2=tkFont.Font(family="Helvetica",size=10)
          label_d2=Label(v1,text="-- OFF --",font=text_d2).place(x=350,y=430)
          os.system("sudo /./home/pi/motoroff.sh &")     
def sensor1on():
                text_s1=tkFont.Font(family="Helvetica",size=10)
                label_s1=Label(v1,text="Actived    ",font=text_s1).place(x=700,y=90)
                label_s1s2=Label(v1,text="Deactived  ",font=text_s1).place(x=700,y=220)
                label_s1s3=Label(v1,text="Deactived  ",font=text_s1).place(x=700,y=350)
                os.system("sudo /./home/pi/sensor1on.sh &")
def sensor2on():
                text_s2=tkFont.Font(family="Helvetica",size=10)
                label_s2=Label(v1,text="Actived    ",font=text_s2).place(x=700,y=220)
                label_s2s1=Label(v1,text="Deactived  ",font=text_s2).place(x=700,y=90)
                label_s2s3=Label(v1,text="Deactived  ",font=text_s2).place(x=700,y=350)
                os.system("sudo /./home/pi/sensor2on.sh &")
                
def sensor3on():
                text_s3=tkFont.Font(family="Helvetica",size=10)
                label_s3=Label(v1,text="Actived    ",font=text_s3).place(x=700,y=350)
                label_s3s1=Label(v1,text="Deactived  ",font=text_s3).place(x=700,y=90)
                label_s3s2=Label(v1,text="Deactived  ",font=text_s3).place(x=700,y=220)
                os.system("sudo /./home/pi/sensor3on.sh &")

def sensor1off():
                 text_s1=tkFont.Font(family="Helvetica",size=10)
                 label_s4=Label(v1,text="Deactived",font=text_s1).place(x=700,y=90)
                 os.system("sudo /./home/pi/sensor1off.sh &") 

def sensor2off():
                 text_s2=tkFont.Font(family="Helvetica",size=10)
                 label_s5=Label(v1,text="Deactived",font=text_s2).place(x=700,y=220)

def sensor3off():
                 text_s3=tkFont.Font(family="Helvetica",size=10)
                 label_s6=Label(v1,text="Deactived",font=text_s3).place(x=700,y=350)
                 os.system("sudo /./home/pi/sensor3off.sh &")


def time_1():
             text_t1=tkFont.Font(family="Helvetica",size=10)
             label_t1=Label(v1,text="-- Time --",font=text_t1).place(x=700,y=120)

def time_2():
             text_t1=tkFont.Font(family="Helvetica",size=10)
             label_t1=Label(v1,text="-- Time --",font=text_t1).place(x=700,y=250)

def time_3():
             text_t1=tkFont.Font(family="Helvetica",size=10)
             label_t1=Label(v1,text="-- Time --",font=text_t1).place(x=700,y=380)

def time_4():
             text_t4=tkFont.Font(family="Helvetica",size=10)
             label_t4=Label(v1,text="-- Time --",font=text_t4).place(x=350,y=450)
                 
               
title_text=tkFont.Font(family="Helvetica",size=15,weight="bold")
label50=Label(v1,text="SMARTMILL SYSTEM",font=title_text).place(x=275,y=10)
############################### Asignar imagenes a Raspi ######################################
bgtext1 = tkFont.Font(family="Helvetica",size=12,weight="bold")
label=Label(v1,text="--- MILL'S SYSTEM ---",font=bgtext1).place(x=110,y=50)

#------------------------------- Sensor-Mill -----------------------------------------------
label1=Label(v1,text="SENSOR-MILL",font=bgtext1).place(x=450,y=50)
img_on1=PhotoImage(file="on.gif")
button_sensor1on=Button(v1,image=img_on1,command=sensor1on).place(x=400,y=90,width=90,height=80)
img_off1=PhotoImage(file="off.gif")
button_sensoroff=Button(v1,image=img_off1,command=sensor1off).place(x=500,y=90,width=90,height=80)
img_settings1=PhotoImage(file="config.gif")
button_settings=Button(v1,image=img_settings1,command=toplevel2).place(x=600,y=90,width=90,height=80)

# --------------------------------Sensor-Alarma ------------------------------------------------
label2=Label(v1,text="SENSOR-ALARMA",font=bgtext1).place(x=450,y=190)
img_on2=PhotoImage(file="on.gif")
button_sensor2on=Button(v1,image=img_on2,command=sensor2on).place(x=400,y=220,width=90,height=80)
img_off2=PhotoImage(file="off.gif")
button_sensoroff2=Button(v1,image=img_off2,command=sensor2off).place(x=500,y=220,width=90,height=80)
img_settings2=PhotoImage(file="config.gif")
button_settings2=Button(v1,image=img_settings2,command=toplevel2).place(x=600,y=220,width=90,height=80)

# --------------------------------Sensor-Lights-Sirena-Mill ------------------------------------------
label3=Label(v1,text="SENSOR-LIGHT-MILL",font=bgtext1).place(x=450,y=320)
img_on3=PhotoImage(file="on.gif")
button_sensor3on=Button(v1,image=img_on3,command=sensor3on).place(x=400,y=350,width=90,height=80)
img_off3=PhotoImage(file="off.gif")
button_sensor3off=Button(v1,image=img_off3,command=sensor3off).place(x=500,y=350,width=90,height=80)
img_settings3=PhotoImage(file="config.gif")
button_settings3=Button(v1,image=img_settings3,command=time_3).place(x=600,y=350,width=90,height=80)

# --------------------- MILL image --------------------------------------------------------
#imgdoorfinal=PhotoImage(file="doorfinal.png")
imgdoorfinal=PhotoImage(file="molinof2.gif",format="gif -index 2")
button_door=Button(v1,image=imgdoorfinal).place(x=20,y=70,width=300,height=300)
#---------------------------Settings-------------------------------------------------------
imgsettings=PhotoImage(file="config.gif")
button_settings=Button(v1,image=imgsettings,command=toplevel).place(x=240,y=395,width=100,height=100)

imgboton1_on=PhotoImage(file="on.gif")
boton1_on=Button(v1,image=imgboton1_on,command=on,width=100).place(x=20,y=395,height=100)
############################### Asignar imagenes a Security Door  ##############################
bgtext2=tkFont.Font(family="Helvetica",size=12,weight="bold")
imgboton2_off=PhotoImage(file="off.gif")
boton2_off=Button(v1,image=imgboton2_off,command=off,width=100).place(x=130,y=395,height=100)
# ------------------------- Exit Button --------------------------------
quit_image=PhotoImage(file="quit.png")
quit_button=Button(v1,image=quit_image,command=v1.destroy).place(x=880,y=430,height=60,width=60)

v1.mainloop()
 
