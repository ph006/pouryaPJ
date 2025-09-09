
from tkinter import *
import pyautogui
from pynput.keyboard import Key,Listener
# import time
#import threading


run_rapid = False
run_pos = False
run_target= False

window = Tk()
window.title('clicker')
window.minsize(width=800, height=800)

window.wm_resizable(False,False) #note: maximizing the window makes the background act weird

#window.wm_attributes('-transparentcolor','#add123')

back_image= PhotoImage(file='images/ns.png')
back_label=Label(window, image=back_image)
back_label.place(x=0,y=0)

widget_back= PhotoImage(file='images/transparent.png')

def on_press(key):
    # if run_pos==False:
    #     if key == Key.f4:
    #         monitor_mouse_position_stop()
    # elif run_rapid==False:
    #     if key==Key.f4:
    #         stop_rapid_clicking()
    # elif run_target==False:
    #     if key==Key.f4:
    #         stop_target_click()

    if run_pos:
        if key == Key.f4:
            monitor_mouse_position_stop()
    elif run_rapid:
        if key==Key.f4:
            stop_rapid_clicking()
    elif run_target:
        if key==Key.f4:
            stop_target_click()

def monitor_mouse_position():
    global run_pos
    if run_pos:
        posx, posy = pyautogui.position()
        labelx.config(text=f'x= {posx}')
        labely.config(text=f'y= {posy}')
        window.after(1000, monitor_mouse_position)

def monitor_mouse_position_start():
    global run_pos
    run_pos = True
    listener_pos = Listener(on_press=on_press)
    listener_pos.start()
    monitor_mouse_position()

def monitor_mouse_position_stop():
    global run_pos
    run_pos = False

def rapid_click():
    global run_rapid
    button_run.config(state=DISABLED)  # note to self: preventing the button to run the function twice

    try:
        time_sec = int(sec_input.get())
    except ValueError:
        time_sec = 0

    try:
        time_min = int(min_input.get())
    except ValueError:
        time_min= 0
    time=(time_sec*1000)+(time_min*60000)

    if run_rapid and time!=0: # IMPORTANT NOTE: loop runs to fast before time calculation.It needs time!=0 condition
        for i in range(1):
            window.after(100)
            pyautogui.leftClick()
            window.after(time, rapid_click)
    else:
        stop_rapid_clicking()


def start_rapid_clicking():
    global run_rapid
    run_rapid = True
    listener_rapid = Listener(on_press=on_press)
    listener_rapid.start()
    rapid_click()

def stop_rapid_clicking():
    global run_rapid,time
    run_rapid = False
    time = 0
    button_run.config(state=NORMAL)

def target_click():
    global run_target
    try:
        delay = int(target_delay.get())
    except ValueError:
        stop_target_click()

    try:
        pos_x = int(x_input.get())
    except ValueError:
        stop_target_click()

    try:
        pos_y = int(y_input.get())
    except ValueError:
        stop_target_click()
    cal_delay=delay *1000
    if run_target:
        button_target_start.config(state=DISABLED) # note to self: preventing the button to run the function twice
        current_pos = pyautogui.position()
        pyautogui.leftClick(pos_x, pos_y)
        pyautogui.moveTo(current_pos)
        window.after(cal_delay, target_click)

def start_target_click():
    global run_target
    target_time_input=int(target_delay.get())
    run_target=True
    listener_target = Listener(on_press=on_press)
    listener_target.start()
    window.after(target_time_input*1000)
    target_click()

def stop_target_click():
    global run_target,pos_x,pos_y
    run_target=False
    pos_x=0
    pos_y=0
    button_target_start.config(state=NORMAL)



# Labels

custom_font = ("Times New Roman", 10,'bold')

labelpos= Label(text='Press to see your mouse position', font=custom_font)
labelpos.place(relx=0.03, rely=0.05)

labelx = Label(text='')
labelx.place(relx=0.6, rely=0.05)

labely = Label(text='')
labely.place(relx=0.7, rely=0.05)

label_rapid_s= Label(text='Choose how many clicks you want per second/minute')
label_rapid_s.place(relx=0.1, rely=0.2)

label_sec = Label(text='Sec :')
label_sec.place(relx=0.69, rely=0.215)

label_min = Label(text='Min :')
label_min.place(relx=0.69, rely=0.285)

label_target = Label(text='Enter delay time and your desired location to click')
label_target.place(relx=0.1, rely=0.47)

label_target_sec = Label(text='Sec :')
label_target_sec.place(relx=0.64, rely=0.55)

label_target_x = Label(text='X :')
label_target_x.place(relx=0.81, rely=0.5)

label_target_y = Label(text='Y :')
label_target_y.place(relx=0.81, rely=0.6)
# Buttons

# Position Buttons
button_pos = Button(text='start', command=monitor_mouse_position_start)
button_pos.place(relx=0.4, rely=0.04)

button_stop_pos = Button(text='Stop', command=monitor_mouse_position_stop)
button_stop_pos.place(relx=0.48, rely=0.04)

# Rapid Click Buttons
button_run = Button(text='Start Clicking', command=start_rapid_clicking)
button_run.place(relx=0.22, rely=0.27)

button_stop = Button(text='Stop Clicking', command=stop_rapid_clicking)
button_stop.place(relx=0.37, rely=0.27)

# Target Click Buttons
button_target_start = Button(text='Start Clicking', command=start_target_click)
button_target_start.place(relx=0.22, rely=0.54)

button_target_stop = Button(text='Stop Clicking', command=stop_target_click)
button_target_stop.place(relx=0.37, rely=0.54)



# Entry

# Rapid Click Entry
sec_input=Entry(width=5)
sec_input.place(relx=0.75, rely=0.22)

min_input=Entry(width=5)
min_input.place(relx=0.75, rely=0.29)

# Target Click Entry
x_input=Entry(width=5)
x_input.place(relx=0.85, rely=0.5)

y_input=Entry(width=5)
y_input.place(relx=0.85, rely=0.6)

target_delay=Entry(width=5)
target_delay.place(relx=0.7, rely=0.55)



window.mainloop()