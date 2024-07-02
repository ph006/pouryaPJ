from tkinter import *
from tkinter.ttk import Treeview

def main_form():

    form = Tk()

    # region config form
    form.title("Contact management system")

    app_icon = PhotoImage(file=r"images\app_icon.png")
    form.iconphoto(False, app_icon)

    form_width = 1000
    form_height = 600
    padding_top = (form.winfo_screenheight()//2) - (form_height//2)
    padding_left = (form.winfo_screenwidth()//2) - (form_width//2)
    form.geometry(f"{form_width}x{form_height}+{padding_left}+{padding_top}")
    # form.resizable(width=False, height=False)
    form.configure(bg="white")
    # endregion

    # region frame

    header = Frame(master=form, height=70, bg="#ebebeb",
                   highlightthickness=1, highlightbackground="#afafaf")
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = Frame(master=form, height=70, bg="#ebebeb",
                   highlightthickness=1, highlightbackground="#afafaf")
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body = Frame(master=form, height=70, bg="white",
                 highlightthickness=1, highlightbackground="#afafaf")
    body.pack(fill=BOTH, expand=True, padx=10, pady=10)
    body.propagate(False)

    # endregion

    # region form title
    title_icon = PhotoImage(file=r"images\title_icon.png")

    Label(
        master=header,
        text="  Contact main form",
        bg="#ebebeb",
        font=("tahoma", 12, "bold"),
        image=title_icon,
        compound=LEFT
    ).pack(side=LEFT, padx=10)

    # endregion

    # region button

    exit_icon = PhotoImage(file=r"images\exit_icon.png")
    Button(
        master=footer,
        text="Exit",
        bg="#212529",
        fg="white",
        padx=5,
        pady=10,
        font=("tahoma", 10, "bold"),
        activebackground="#1c1f23",
        activeforeground="white",
        image=exit_icon,
        compound=LEFT
    ).pack(side=LEFT, padx=10)

    add_icon = PhotoImage(file=r"images\add_icon.png")
    Button(
        master=footer,
        text="Add",
        bg="#198754",
        fg="white",
        padx=5,
        pady=10,
        font=("tahoma", 10, "bold"),
        activebackground="#157347",
        activeforeground="white",
        image=add_icon,
        compound=LEFT
    ).pack(side=RIGHT, padx=(0, 10))

    edit_icon = PhotoImage(file=r"images\edit_icon.png")
    Button(
        master=footer,
        text="Edit",
        bg="#ffc107",
        fg="black",
        padx=5,
        pady=10,
        font=("tahoma", 10, "bold"),
        activebackground="#ffca2c",
        activeforeground="black",
        image=edit_icon,
        compound=LEFT
    ).pack(side=RIGHT, padx=(0, 10))

    delete_icon = PhotoImage(file=r"images\delete_icon.png")
    Button(
        master=footer,
        text="Delete",
        bg="#dc3545",
        fg="white",
        padx=5,
        pady=10,
        font=("tahoma", 10, "bold"),
        activebackground="#bb2d3b",
        activeforeground="white",
        image=delete_icon,
        compound=LEFT
    ).pack(side=RIGHT, padx=(0, 10))
    # endregion

    # region grid, , padx=10, pady=10

    grid_y_scrollbar = Scrollbar(master=body, orient="vertical")
    grid_x_scrollbar = Scrollbar(master=body, orient="horizontal")

    grid_y_scrollbar.pack(side=RIGHT, fill=Y)
    grid_x_scrollbar.pack(side="bottom", fill=X)


    contact_grid = Treeview(master=body, columns=("National ID", "ID", "Student ID", "First name", "Last name",'Phone number','Gender','Age','Email','Address','Description'), show="headings", selectmode="extended")

    col_width = contact_grid.winfo_width()

    contact_grid.heading(column="National ID", text="National ID", anchor=CENTER)
    contact_grid.heading(column="ID", text="ID", anchor=CENTER)
    contact_grid.heading(column="Student ID", text="Student ID", anchor=CENTER)
    contact_grid.heading(column="First name", text="First name", anchor=CENTER)
    contact_grid.heading(column="Last name", text="Last name", anchor=CENTER)
    contact_grid.heading(column="Phone number", text="Phone number", anchor=CENTER)
    contact_grid.heading(column="Gender", text="Gender", anchor=CENTER)
    contact_grid.heading(column="Age", text="Age", anchor=CENTER)
    contact_grid.heading(column="Email", text="Email", anchor=CENTER)
    contact_grid.heading(column="Address", text="Address", anchor=CENTER)
    contact_grid.heading(column="Description", text="Description", anchor=CENTER)

    contact_grid.column(column="National ID", anchor=CENTER, width=col_width)
    contact_grid.column(column="ID", anchor=CENTER, width=col_width)
    contact_grid.column(column="Student ID",  anchor=CENTER, width=col_width)
    contact_grid.column(column="First name",  anchor=CENTER, width=col_width)
    contact_grid.column(column="Last name", anchor=CENTER, width=col_width)
    contact_grid.column(column="Phone number", anchor=CENTER, width=col_width)
    contact_grid.column(column="Gender", anchor=CENTER, width=col_width)
    contact_grid.column(column="Age", anchor=CENTER, width=col_width)
    contact_grid.column(column="Email", anchor=CENTER, width=col_width)
    contact_grid.column(column="Address", anchor=CENTER, width=col_width)
    contact_grid.column(column="Description", anchor=CENTER, width=col_width)

    contact_grid.pack(fill=BOTH, expand=True)

    contact_grid.configure()


    contact_grid.configure(yscrollcommand=grid_y_scrollbar.set, xscrollcommand=grid_x_scrollbar.set)

    grid_y_scrollbar["command"] = contact_grid.yview
    grid_x_scrollbar["command"] = contact_grid.xview


    # endregion

    # region grid dataentry
    for i in range(100):
        contact_grid.insert("", END, values=(i, i+1, i+2, i+3, i+4,i+5,i+6,i+7,i+8,i+9,i+10))

    # endregion

    form .mainloop()

