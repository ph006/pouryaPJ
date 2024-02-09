import tkinter
from tkinter import ttk
import PyPDF2 as pd
from docx import Document
import re
# from langdetect import detect
from tkinter import *
from tkinter import filedialog,messagebox
import os

window = Tk()
window.title('Pdf Converter (Pourya Hedayat)')
window.minsize(width=350, height=50)
window.configure(bg='gray')

converted_file=None
file_select=None

# def select():
#     select = filedialog.askopenfilename()
#     return select


def out():
    global converted_file
    global file_select

    read = pd.PdfReader(file_select)
    my_doc = Document()

    clean_method = dropdown.get()

    for page_number, page in enumerate(read.pages):
        txt = page.extract_text()

        # lang = detect(txt)

        if clean_method == "No space clean":
            clean = re.sub(r'\s+', ' ', txt)

        elif clean_method == "Spaced cleanup":
            clean = re.sub(r'[^\w\s]', '', txt)

        elif clean_method == "Full clean":
            clean = re.sub(r'\s+', ' ', txt)
            clean = re.sub(r'[^\w\s]', '', clean)



        my_doc.add_paragraph(clean)

        converted_file = my_doc

    path= filedialog.asksaveasfilename(defaultextension= ".docx", filetypes =[("Word file", "*.docx"),("All files","*.*")])

    loc=os.path.join(path)

    converted_file.save(loc)
    messagebox.showinfo(' Converted to Docx', f'File generated at{path}')


def convert():
    global converted_file
    global file_select

    file_select = filedialog.askopenfilename()
    text_box = tkinter.Label(window, text=f'Selected file: {file_select}')
    text_box.place(relx=0, rely=0.3)
    text_box['font'] = ('Times', 7)
    messagebox.showinfo('Success', 'Your file has been successfully loaded')


options = ["No space clean", "Spaced cleanup","Full clean"]

dropdown = ttk.Combobox(window, values=options, state="readonly")
dropdown.place(relx=0.5, rely=0.2)

# button_pos = Button(text='Select PDF', command=select)
# button_pos.place(relx=0.2, rely=0.04)

button_pos2 = Button(text='Load', command=convert)
button_pos2.place(relx=0.3, rely=0.04)
button_pos2['font'] = ('Times',10,'bold')
button_pos2['fg'] ='black'
button_pos2['bg'] ='sky blue'
button_pos2['borderwidth'] = 2

button_pos3 = Button(text='Generate', command=out)
button_pos3.place(relx=0.6, rely=0.04)
button_pos3['font'] = ('Times', 10, 'bold')
button_pos3['fg'] = 'black'
button_pos3['bg'] = 'sky blue'
button_pos3['borderwidth'] = 2
# button_pos3['relief'] = 'solid'




window.mainloop()
