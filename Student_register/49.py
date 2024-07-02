from tkinter import *
from tkinter.ttk import Treeview
def contact_data_entry_form():

    form = Tk()

    # region variables
    national_id_var = StringVar()
    id_var = StringVar()
    name_var = StringVar()
    family_var = StringVar()
    phone_var = StringVar()
    student_id_var = StringVar()
    gender_var = StringVar(value="male")
    age_var = StringVar()
    email_var = StringVar()
    address_var = StringVar()
    description_var = StringVar()
    # endregion

    # region config form
    form.title("Contact Management System")

    app_icon = PhotoImage(file=r"images\app_icon.png")
    form.iconphoto(False, app_icon)

    form_width = 600
    form_height = 800
    padding_top = (form.winfo_screenheight()//2) - (form_height//2)
    padding_left = (form.winfo_screenwidth()//2) - (form_width//2)
    form.geometry(f"{form_width}x{form_height}+{padding_left}+{padding_top}")
    form.configure(bg="#f0f0f0")  # Changed background color
    # endregion

    # region frames

    header = Frame(master=form, height=70, bg="#333333",
                   highlightthickness=1, highlightbackground="#222222")
    header.pack(side=TOP, fill=X)
    header.propagate(False)

    footer = Frame(master=form, height=70, bg="#333333",
                   highlightthickness=1, highlightbackground="#222222")
    footer.pack(side=BOTTOM, fill=X)
    footer.propagate(False)

    body = Frame(master=form, bg="#f0f0f0",
                 highlightthickness=1, highlightbackground="#cccccc")
    body.pack(fill=BOTH, expand=True, padx=10, pady=10)
    body.propagate(False)

    # Create frames for each input field
    frames = {}
    fields = ["national_id", "id", "student_id", "name", "family", "phone", "gender", "age", "email", "address", "description"]
    for field in fields:
        frames[field] = Frame(master=body, height=45, bg="#f0f0f0")
        frames[field].pack(side=TOP, fill=X, pady=(1, 1), padx=10)
        frames[field].propagate(False)

    description_frame = Frame(master=body, height=100, bg="#f0f0f0")
    description_frame.pack(fill=BOTH, expand=True, pady=(0, 5), padx=10)
    description_frame.propagate(False)

    # endregion

    # region form title
    title_icon = PhotoImage(file=r"images\dataentry_icon.png")

    Label(
        master=header,
        text=" Contact Data Entry Form",
        bg="#333333",
        fg="#ffffff",
        font=("Verdana", 14, "bold"),
        image=title_icon,
        compound=LEFT
    ).pack(side=LEFT, padx=10)

    # endregion

    # region button

    back_icon = PhotoImage(file=r"images\back_icon.png")
    Button(
        master=footer,
        text="Back",
        bg="#555555",
        fg="#ffffff",
        padx=5,
        pady=10,
        font=("Verdana", 10, "bold"),
        activebackground="#444444",
        activeforeground="#ffffff",
        image=back_icon,
        compound=LEFT
    ).pack(side=LEFT, padx=10)

    add_icon = PhotoImage(file=r"images\add_icon.png")
    Button(
        master=footer,
        text="Add",
        bg="#28a745",
        fg="#ffffff",
        padx=5,
        pady=10,
        font=("Verdana", 10, "bold"),
        activebackground="#218838",
        activeforeground="#ffffff",
        image=add_icon,
        compound=LEFT
    ).pack(side=RIGHT, padx=(0, 10))
    # endregion

    # region National ID
    Label(
        master=frames["national_id"],
        text="National ID : ",
        bg="#f0f0f0",
        fg="#000000",
        font=("Verdana", 10, "bold"),
        anchor=W,
        width=15
    ).pack(side=LEFT)

    Entry(
        master=frames["national_id"],
        textvariable=national_id_var,
        bg="#ffffff",
        bd=1,
        font=("Verdana", 12, "normal")
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region ID
    Label(
        master=frames["id"],
        text="ID : ",
        bg="#f0f0f0",
        fg="#000000",
        font=("Verdana", 10, "bold"),
        anchor=W,
        width=15
    ).pack(side=LEFT)

    Entry(
        master=frames["id"],
        textvariable=id_var,
        bg="#ffffff",
        bd=1,
        font=("Verdana", 12, "normal")
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region Student ID
    Label(
        master=frames["student_id"],
        text="Student ID : ",
        bg="#f0f0f0",
        fg="#000000",
        font=("Verdana", 10, "bold"),
        anchor=W,
        width=15
    ).pack(side=LEFT)

    Entry(
        master=frames["student_id"],
        textvariable=student_id_var,
        bg="#ffffff",
        bd=1,
        font=("Verdana", 12, "normal")
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region name
    Label(
        master=frames["name"],
        text="First name : ",
        bg="#f0f0f0",
        fg="#000000",
        font=("Verdana", 10, "bold"),
        anchor=W,
        width=15
    ).pack(side=LEFT)

    Entry(
        master=frames["name"],
        textvariable=name_var,
        bg="#ffffff",
        bd=1,
        font=("Verdana", 12, "normal")
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region family
    Label(
        master=frames["family"],
        text="Last name : ",
        bg="#f0f0f0",
        fg="#000000",
        font=("Verdana", 10, "bold"),
        anchor=W,
        width=15
    ).pack(side=LEFT)

    Entry(
        master=frames["family"],
        bg="#ffffff",
        bd=1,
        font=("Verdana", 12, "normal"),
        textvariable=family_var
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region phone
    Label(
        master=frames["phone"],
        text="Phone number : ",
        bg="#f0f0f0",
        fg="#000000",
        font=("Verdana", 10, "bold"),
        anchor=W,
        width=15
    ).pack(side=LEFT)

    Entry(
        master=frames["phone"],
        bg="#ffffff",
        textvariable=phone_var,
        bd=1,
        font=("Verdana", 12, "normal")
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region gender
    Label(
        master=frames["gender"],
        text="Gender : ",
        bg="#f0f0f0",
        fg="#000000",
        font=("Verdana", 10, "bold"),
        anchor=W,
        width=15
    ).pack(side=LEFT)

    Radiobutton(
        master=frames["gender"],
        text="Male",
        variable=gender_var,
        value="male",
        bg="#f0f0f0",
        font=("Verdana", 10)
    ).pack(side=LEFT, padx=(0, 10))

    Radiobutton(
        master=frames["gender"],
        text="Female",
        variable=gender_var,
        value="female",
        bg="#f0f0f0",
        font=("Verdana", 10)
    ).pack(side=LEFT, padx=(0, 10))

    Radiobutton(
        master=frames["gender"],
        text="Other",
        variable=gender_var,
        value="other",
        bg="#f0f0f0",
        font=("Verdana", 10)
    ).pack(side=LEFT, padx=(0, 10))
    # endregion

    # region Age
    Label(
        master=frames["age"],
        text="Age : ",
        bg="#f0f0f0",
        fg="#000000",
        font=("Verdana", 10, "bold"),
        anchor=W,
        width=15
    ).pack(side=LEFT)

    Entry(
        master=frames["age"],
        bg="#ffffff",
        bd=1,
        font=("Verdana", 12, "normal"),
        textvariable=age_var
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region Email
    Label(
        master=frames["email"],
        text="Email : ",
        bg="#f0f0f0",
        fg="#000000",
        font=("Verdana", 10, "bold"),
        anchor=W,
        width=15
    ).pack(side=LEFT)

    Entry(
        master=frames["email"],
        bg="#ffffff",
        bd=1,
        font=("Verdana", 12, "normal"),
        textvariable=email_var
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region Address
    Label(
        master=frames["address"],
        text="Address : ",
        bg="#f0f0f0",
        fg="#000000",
        font=("Verdana", 10, "bold"),
        anchor=W,
        width=15
    ).pack(side=LEFT)

    Entry(
        master=frames["address"],
        bg="#ffffff",
        bd=1,
        font=("Verdana", 12, "normal"),
        textvariable=address_var
    ).pack(fill=BOTH, expand=True)
    # endregion

    # region Description
    Label(
        master=description_frame,
        text="Description : ",
        bg="#f0f0f0",
        fg="#000000",
        font=("Verdana", 10, "bold"),
        anchor=W,
        width=15
    ).pack(side=LEFT)

    desc_entry = Text(
        master=description_frame,
        bg="#ffffff",
        bd=1,
        font=("Verdana", 12, "normal")
    )
    desc_entry.pack(fill=BOTH, expand=True)
    # endregion

    form.mainloop()

