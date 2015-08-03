#!usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import Tkinter
from Tkinter import *
from tkMessageBox import *
Equipoa=''
Equipob=''
def registro():
	try:
		Equipob=e2.get()
		Equipoa=e1.get()
		if (Equipoa) == '':
			showerror('Chequeo de ingreso', 'El nombre del equipo es necesario')
		if (Equipob) =='':
			showerror('Chequeo de ingreso', 'El nombre del equipo es necesario')
	except ValueError:
		valid = False
"""about windows"""
def acerca_de():
	v1=Tk()
	sal_mensaje1=("Una manera de controlar un juego de Baloncesto\n ")
	sal_mensaje2=("Una aplicación que simula un tablero digital de juego para el Baloncesto estudiantil\n")
	sal_mensaje3=("Creada en y para Software Libre\n")
	sal_mensaje4=("por asleybach@gmail.com")
	mensaje_texto= (sal_mensaje1+sal_mensaje2+sal_mensaje3+sal_mensaje4)
	v1.title("Bienvenidos a Tepbe")
	v1.geometry("400x150+500+200")
	v1.maxsize(700, 700)
	mensaje= Label(v1, bg="white", text= mensaje_texto,anchor="center")
	mensaje.pack()
	v1.config(bg="white")
v2=Tk()
v2.title("Tablero Electrónico para Baloncesto Estudiantil")
v2.geometry("600x600+400+150")
v2.maxsize(700, 700)
titulo=Label(v2,text="Registro de Equipos",fg="blue",bg="white",height=3)
titulo.pack()
l1 = Label(v2,text="registro del Equipo A: ",bg="white") 
l1.pack()
e1 = Entry(v2)
e1.pack()
l2 = Label(v2,text="registro del Equipo B: ",bg="white") 
l2.pack()
e2 = Entry(v2)
e2.pack()
boton_ingreso = Button(v2, text="registrar", width=10, command=registro and v2.quit)
boton_ingreso.pack(pady=10)
menu_bar= Menu(v2)
reg= Menu(menu_bar)
reg.add_command(label="Acerca de Tepbe",command=acerca_de,underline=0)
reg.add_command(label="Salir", command = sys.exit, underline=0)
menu_bar.add_cascade(label="Menu",menu=reg, underline=0)
imagenlogo= PhotoImage(file="/home/asley/proyectos/tebe/logo_en.gif")
lab_imagenlogo=Label(v2,image=imagenlogo,anchor="center").pack()
v2.config(bg="white",menu=menu_bar)
v2.mainloop()

#start tepbe
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
imagen=simplegui.load_image('/home/asley/proyectos/tebe/logo_en.png')
sound=simplegui.load_sound('/home/asley/proyectos/tebe/Buzzer.wav')

counter = 0
points = 0
tries = 0
running = False
Equipoa=e1.get()
Equipob=e2.get()
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
	
	D = str(t%10)
	t //= 10
	C = str(t%10)
	t //= 10
	B = str(t % 6)
	t //= 6
	A = str(t % 10)
	t //= 10
	U =str (t %1)
	
	return U+A + ':' + B + C + '.' + D
def forma(s):
	s = str(s)
	return s
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global running
    running = True
    timer.start()
def stop_handler():
    global running, tries, points    
    timer.stop()    
    if running:
        tries += 1        
        if counter % 10 == 0:
            points += 1    
    running = False    
def reset_handler():
    stop_handler()
    sound.pause()
    global running, tries, points, counter, puntajea, puntajeb
    runnig = False
    tries = 0
    points = 0
    counter = 0
    puntajea= 0
    puntajeb= 0
# define score for each team
puntajea = 0
puntajeb = 0 
def suma_a_uno():
	global running, puntajea
	if running:
		puntajea += 1
#Team a
def suma_a_dos():
	global running, puntajea
	if running:
		puntajea += 2
def suma_a_tres():
	global running, puntajea
	if running:
		puntajea += 3		
#Team b
def suma_b_uno():
	global running, puntajeb
	if running:
		puntajeb += 1
def suma_b_dos():
	global running, puntajeb
	if running:
		puntajeb += 2
def suma_b_tres():
	global running, puntajeb
	if running:
		puntajeb += 3
# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter -= 1
# timeout in a game
def retardo():
	global running, start_handler
	if start_handler:
		if int(A) and int(B) and int(C) and int(D)==0:
			running=False
			raw_input("cierre de cuarto")
			running=True
# define draw handler
def draw(canvas):
    #canvas.draw_text(str(points) + '/' + str(tries),(225, 30), 30, 'Green')
    canvas.draw_text('------------ Tiempo de Juego ------------',(300, 450), 25, 'green')
    canvas.draw_text('------------ Tiempo de Juego ------------',(300, 650), 25, 'green')
    #dibuja una linea canvas.draw_line((200,220),(425,430), 5, 'yellow')
    canvas.draw_text(format(counter), (180, 600), 200, 'Black')
    canvas.draw_text(forma(Equipoa),(175, 175), 40, 'blue')
    canvas.draw_text(str(puntajea),(200, 300), 150, 'blue')
    canvas.draw_text(forma(Equipob),(525, 175), 40, 'red')
    canvas.draw_text(str(puntajeb),(600, 300), 150, 'red')
    canvas.draw_text('**** Tablero Digital para Baloncesto Estudiantil ****',(110, 25), 30, 'green')
    canvas.draw_text('Elaborado por asleybach@gmail.com',(280, 60), 25, 'black')
    canvas.draw_image(imagen, (460/2,380/2), (400, 360),(50,50), (100,100))
    canvas.draw_image(imagen, (460/2,380/2), (400, 360),(850,50), (100,100))
# create frame
frame = simplegui.create_frame('Tablero de Baloncesto Estudiantil', 900, 700,)
frame.set_canvas_background('White')
timer = simplegui.create_timer(100, tick)
def rebo_tempo():
	global running, tries, points, counter
	stop_handler()
	sound.pause()
	runnig = False
	tries = 0
	points = 0
	counter = 0
# register event handlers
frame.add_label('Controles de Tiempo')
frame.add_label('_______________________')
frame.add_label(' ')
frame.add_button('Inicio', start_handler)
frame.add_button('Detener', stop_handler)
frame.add_button('Reiniciar', reset_handler,)
frame.add_label(' ')
frame.add_label('Controles de Score')
frame.add_label('_______________________')
frame.add_label(forma(Equipoa))
frame.add_button('+1', suma_a_uno)
frame.add_button('+2', suma_a_dos)
frame.add_button('+3', suma_a_tres)
frame.add_label('_______________________')
frame.add_label(forma(Equipob))
frame.add_button('+1', suma_b_uno)
frame.add_button('+2', suma_b_dos)
frame.add_button('+3', suma_b_tres)
frame.set_draw_handler(draw)
frame.add_label(' ')
frame.add_label('Controles de Juego')
frame.add_label('_______________________')
frame.add_label(' ')
frame.add_button('rebo', rebo_tempo)
frame.add_button('Chicharra', sound.play)
frame.add_label('_______________________')
frame.add_label(' ')
# start frame
frame.start()
