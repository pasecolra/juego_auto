from tkinter import*
import random
from tkinter import messagebox


BASE = 460
ALTURA = 280

"""desplazamiento_x = 3
desplazamiento_y = 0
intervalo = 20"""

"""velocidad_x = random.randint(1,2)
velocidad_y = random.randint(1,2)"""


def mover_autos():
    global velocidad_x1, velocidad_x2

    x_actual, y = c.coords(auto1)
    x_actual2, y2 = c.coords(auto2) 
    velocidad_x1 = random.randint(12, 20)
    velocidad_x2 = random.randint(12, 20)
    if x_actual >= 400:
        velocidad_x1 = 0
        velocidad_x2 = 0
        messagebox.showinfo("ganador","gano carro 2")
    elif x_actual2 >= 400:
        messagebox.showinfo("ganador","gano carro 1")
    else:
        c.move(auto1, velocidad_x1, 0)
        c.move(auto2, velocidad_x2, 0)

        ventana_principal.after(60, mover_autos)

"""def mover_autos():
    c.move(auto1,velocidad_x,0)
    ventana_principal.after(100,mover_autos)
    c.move(auto2,velocidad_y,0)
    ventana_principal.after(100,mover_autos)
    c.move(auto1, desplazamiento_x, desplazamiento_y)
    ventana_principal.after(intervalo, mover_autos)
    c.move(auto2, desplazamiento_x, desplazamiento_y)
    ventana_principal.after(intervalo, mover_autos)"""

ventana_principal = Tk()
ventana_principal.title("Juego")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="orange", width=480 , height=320 )
frame_graficacion.place(x=10 , y=10)

c = Canvas (ventana_principal , width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=20,y=20)

#separacion
linea_1=c.create_line(BASE/10,ALTURA,BASE/10,0,fill="yellow",width=4)
linea_2=c.create_line(BASE-50,ALTURA,BASE-50,0,fill="yellow",width=4)
linea_3 = c.create_line(BASE-50,ALTURA/2,BASE/2,ALTURA/2 ,  fill="yellow", width=4)
linea_4 = c.create_line(BASE/10,ALTURA/2,BASE/2,ALTURA/2 ,  fill="yellow", width=4)

#salida
texto_1 = c.create_text(BASE/18,ALTURA-260, anchor="center", text="S" , font=("Arial" , 25 ,"bold"), fill="red",
activefill="blue2")
texto_2 = c.create_text(BASE/18,ALTURA-210, anchor="center", text="A" , font=("Arial" , 25 ,"bold"), fill="red",
activefill="blue2")
texto_3 = c.create_text(BASE/18,ALTURA-160, anchor="center", text="L" , font=("Arial" , 25 ,"bold"), fill="red",
activefill="blue2")
texto_4 = c.create_text(BASE/18,ALTURA-110, anchor="center", text="I" , font=("Arial" , 25 ,"bold"), fill="red",
activefill="blue2")
texto_5 = c.create_text(BASE/18,ALTURA-60, anchor="center", text="D" , font=("Arial" , 25 ,"bold"), fill="red",
activefill="blue2")
texto_6 = c.create_text(BASE/18,ALTURA-10, anchor="center", text="A" , font=("Arial" , 25 ,"bold"), fill="red",
activefill="blue2")

#meta
texto_7 = c.create_text(BASE-20,ALTURA-210, anchor="center", text="M" , font=("Arial" , 25 ,"bold"), fill="red",
activefill="blue2")
texto_8 = c.create_text(BASE-20,ALTURA-160, anchor="center", text="E" , font=("Arial" , 25 ,"bold"), fill="red",
activefill="blue2")
texto_9 = c.create_text(BASE-20,ALTURA-110, anchor="center", text="T" , font=("Arial" , 25 ,"bold"), fill="red",
activefill="blue2")
texto_10 = c.create_text(BASE-20,ALTURA-60, anchor="center", text="A" , font=("Arial" , 25 ,"bold"), fill="red",
activefill="blue2")

#carretera 1
rect_1 = c.create_rectangle(BASE-390,ALTURA/6,BASE/4,ALTURA/4,fill="yellow",outline="yellow")
rect_2 = c.create_rectangle(BASE-305,ALTURA-233,BASE-260,ALTURA/4,fill="yellow",outline="yellow")
rect_3 = c.create_rectangle(BASE-215,ALTURA-233,BASE-170,ALTURA/4,fill="yellow",outline="yellow")
rect_4 = c.create_rectangle(BASE-125,ALTURA-233,BASE-80,ALTURA/4,fill="yellow",outline="yellow")

#carretera 2
rect_5 = c.create_rectangle(BASE-390,ALTURA-50,BASE/4,ALTURA-75,fill="yellow",outline="yellow")
rect_6 = c.create_rectangle(BASE-305,ALTURA-50,BASE-260,ALTURA-75,fill="yellow",outline="yellow")
rect_7 = c.create_rectangle(BASE-215,ALTURA-50,BASE-170,ALTURA-75,fill="yellow",outline="yellow")
rect_8 = c.create_rectangle(BASE-125,ALTURA-50,BASE-80,ALTURA-75,fill="yellow",outline="yellow")



img_auto1=PhotoImage(file="img/auto1.png")
auto1= c.create_image(BASE/60,ALTURA/5,image=img_auto1)

img_auto2=PhotoImage(file="img/auto2.png")
auto2= c.create_image(BASE/60,ALTURA-60,image=img_auto2)

frame_controles=Frame(ventana_principal)
frame_controles.config(bg="orange" , width=480 , height=100)
frame_controles.place(x=10 , y=360)

# boton para sumar
bt_jugar = Button(frame_controles,text="JUGAR",command=mover_autos)
bt_jugar.place(x=160, y=35, width=150, height=40)


ventana_principal.mainloop()