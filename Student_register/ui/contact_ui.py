from os import system
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Treeview
from contact_bl import *
# from ui.common.utility import get_input, show_list_dict

def show_error(data: dict) -> None:
    err_list = []

    for field, err in data.items():
        err_list.append(f"Error({field})! {err}.")

    showerror("Error!!!", "\n".join(err_list))


def show_success(data: dict) -> None:
    succ_list = []

    for field, msg in data.items():
        succ_list.append(f"Success({field})! {msg}.")

    showinfo("Success!!!", "\n".join(succ_list))


def contact_main_form():

    def load_contact():
        result = get_contacts()

        if not result["SUCCESS"]:
            show_error((result["ERROR_MESSAGE"]))
            return []
        else:
            return result['RETURN_DATA']



    def add_bt():
        form.withdraw()
        contact_data_entry_form(contact_grid=contact_grid)

        form.deiconify()
        pass

    from tkinter.messagebox import askyesno

    def remove_bt():
        row = contact_grid.selection()
        if not row:
            show_error({"row error": "Please select a row!"})
            return

        for id_ in row:
            # Extract the contact details from the selected row
            value = contact_grid.item(id_, "values")
            phone = value[5]  # PHONE NUMBER COLUMN 6 HAST

            # Confirm deletion with the user
            if askyesno("Warning!", f"Do you want to delete this contact with phone number {phone}?"):
                result = remove_contact(phone=phone)

                # Check the result of the deletion operation
                if not result["SUCCESS"]:
                    show_error(result["ERROR_MESSAGE"])
                else:
                    contact_grid.delete(id_)
                    show_success(result["SUCCESS_MESSAGE"])

    def edit_bt():
        rows_id = contact_grid.selection()

        if not rows_id:
            show_error({"row error": "plz  select a row!!!"})
            return

        if len(rows_id) > 1:
            show_error({"row error": "plz select only one row!!!"})
            return

        # Extract the contact details from the selected row
        values = contact_grid.item(rows_id[0], "values")
        national_id = values[0]
        id_ = values[1]
        student_id = values[2]
        name = values[3]
        family = values[4]
        phone = values[5]
        gender = values[6]
        age = values[7]
        email = values[8]
        address = values[9]
        description = values[10]

        if askyesno("Warning!","Do you want to edit this contact?"):

            form.withdraw()
            contact_edit_form(
                row_id=rows_id[0],
                national_id=national_id,
                id_=id_,
                student_id=student_id,
                name=name,
                family=family,
                phone=phone,
                gender=gender,
                age=age,
                email=email,
                address=address,
                description=description,
                contact_grid=contact_grid
            )
            form.deiconify()





        pass

    def exit_bt():
        form.destroy()

        pass
    get_contact=load_contact()

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
        command=exit_bt,
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
        command=add_bt,
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
        command=edit_bt,
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
        command=remove_bt,
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
    for contact in get_contact:
        contact_grid.insert("", END, values=(contact['National ID'],contact['ID'],contact['Student ID'],contact['First name'],contact['Last name'],contact['Phone number'],contact['Gender'],contact['Age'],contact['Email'],contact['Address'],contact['Description']))

    # endregion

    form .mainloop()




def contact_data_entry_form(contact_grid):

    def exit_bt():
        form.quit()
        form.destroy()
        pass
    def add_bt():
        contact = {
            "National ID": national_id_var.get(),
            "ID": id_var.get(),
            "Student ID": student_id_var.get(),
            "First name": name_var.get(),
            "Last name": family_var.get(),
            "Phone number": phone_var.get(),
            "Gender": gender_var.get(),
            "Email": email_var.get(),
            "Age": age_var.get(),
            "Address": address_var.get(),
            "Description": desc_entry.get("1.0", 'end-1c')
        }

        result = create_contact(contact=contact)

        if not result["SUCCESS"]:

            if "First name" in result["ERROR_MESSAGE"]:
                name_var.set("")

            if "Last name" in result["ERROR_MESSAGE"]:
                family_var.set("")

            if "Phone number" in result["ERROR_MESSAGE"]:
                phone_var.set("")

            if "Gender" in result["ERROR_MESSAGE"]:
                gender_var.set("")

            if "Description" in result["ERROR_MESSAGE"]:
                desc_entry.delete(1.0, "END")
                # desc_entry.insert("END", "")

            show_error(result["ERROR_MESSAGE"])

        else:
            contact_grid.insert("", END, values=(contact['National ID'],contact['ID'],contact['Student ID'],contact['First name'],contact['Last name'],contact['Phone number'],contact['Gender'],contact['Age'],contact['Email'],contact['Address'],contact['Description']))

            exit_bt()

    form = Toplevel()

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
    # description_var = StringVar()
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
        command= exit_bt,
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
        command=add_bt,
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




def contact_edit_form(row_id, national_id, id_, student_id, name, family, phone, gender, age, email, address, description, contact_grid):
    def exit_bt():
        form.quit()
        form.destroy()
        pass

    def edit_btn_onclick():

        contact = {
            "National ID": national_id_var.get(),
            "ID": id_var.get(),
            "Student ID": student_id_var.get(),
            "First name": name_var.get(),
            "Last name": family_var.get(),
            "Phone number": phone_var.get(),
            "Gender": gender_var.get(),
            "Email": email_var.get(),
            "Age": age_var.get(),
            "Address": address_var.get(),
            "Description": desc_entry.get("1.0", 'end-1c')
        }

        result = edit_contact(contact=contact)

        if not result["SUCCESS"]:

            if "name" in result["ERROR_MESSAGE"]:
                name_var.set("")

            if "family" in result["ERROR_MESSAGE"]:
                family_var.set("")

            if "phone" in result["ERROR_MESSAGE"]:
                phone_var.set("")

            if "gender" in result["ERROR_MESSAGE"]:
                gender_var.set("")

            if "description" in result["ERROR_MESSAGE"]:
                desc_entry.delete(1.0, "END")
                # desc_entry.insert("END", "")

            show_error(result["ERROR_MESSAGE"])

        else:
            contact_grid.item(row_id,values=(
            contact['National ID'], contact['ID'], contact['Student ID'], contact['First name'], contact['Last name'],
            contact['Phone number'], contact['Gender'], contact['Age'], contact['Email'], contact['Address'],
            contact['Description']))

            show_success(result["SUCCESS_MESSAGE"])
            exit_bt()

    form = Toplevel()

    # region variables
    national_id_var = StringVar(value=national_id)
    id_var = StringVar(value=id_)
    name_var = StringVar(value=name)
    family_var = StringVar(value=family)
    phone_var = StringVar(value=phone)
    student_id_var = StringVar(value=student_id)
    gender_var = StringVar(value=gender)
    age_var = StringVar(value=age)
    email_var = StringVar(value=email)
    address_var = StringVar(value=address)
    # description= StringVar(value=description)

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
        command=exit_bt,
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

    edit_icon = PhotoImage(file=r"images\edit_icon.png")
    Button(
        command=edit_btn_onclick,
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
    desc_entry.insert("end-1c", description)

    # endregion

    form.mainloop()




# def main_ui():
#
#     def show_error(data: dict) -> None:
#         for field, err in data.items():
#             print(f"Error({field})! {err}.")
#
#     def show_success(data: dict) -> None:
#         for field, msg in data.items():
#             print(f"Success({field})! {msg}.")
#
#     while True:
#
#         # region get menu
#         menu = get_input(
#             filed="""\n\n1. Add contact\n2. Show contact\n3. Remove contact\n4. Edit contact\n5. Search contact\n6. Exit\nmenu""",
#             is_empty=False,
#             valid_range=("1", "2", "3", "4", "5", "6")
#         )
#         # endregion
#
#         match menu:
#             case "1":
#
#                 while True:
#                     system("cls")
#
#                     name = get_input(filed="name", is_empty=False)
#                     family = get_input(filed="family", is_empty=False)
#                     gender = get_input(filed="gender", is_empty=False,
#                                        valid_range=("male", "female", "other"))
#                     description = get_input(filed="description")
#                     phone = get_input(filed="phone", is_empty=False)
#
#                     contact = {
#                         "name": name,
#                         "family": family,
#                         "phone": phone,
#                         "gender": gender,
#                         "description": description
#                     }
#                     while True:
#                         result = create_contact(contact=contact)
#
#                         if not result["SUCCESS"]:
#                             show_error(result["ERROR_MESSAGE"])
#
#                             if "DALERROR" in result["ERROR_MESSAGE"]:
#                                 break
#
#                             if "name" in result["ERROR_MESSAGE"]:
#                                 contact["name"] = get_input(
#                                     filed="name", is_empty=False)
#
#                             if "family" in result["ERROR_MESSAGE"]:
#                                 contact["family"] = get_input(
#                                     filed="family", is_empty=False)
#
#                             if "phone" in result["ERROR_MESSAGE"]:
#                                 contact["phone"] = get_input(
#                                     filed="phone", is_empty=False)
#
#                             if "gender" in result["ERROR_MESSAGE"]:
#                                 contact["gender"] = get_input(filed="gender", is_empty=False,
#                                                               valid_range=("male", "female", "other"))
#
#                             if "description" in result["ERROR_MESSAGE"]:
#                                 contact["description"] = get_input(
#                                     filed="description")
#
#                         else:
#                             show_success(result["SUCCESS_MESSAGE"])
#                             break
#
#                     if input("Do you want to add another contact (yes-etc) : ") != "yes":
#                         system("cls")
#                         break
#
#             case "2":
#
#                 if input("Do yau want to display all column (yes-etc) : ") == "yes":
#                     system("cls")
#                     dispaly_key = ("name", "family", "phone",
#                                    "gender", "description")
#
#                 else:
#                     system("cls")
#
#                     dispaly_key = []
#
#                     for key in ("name", "family", "phone", "gender", "description"):
#
#                         print("Do you want to display",
#                               key, " (yes-etc) : ", end="")
#                         if input() == "yes":
#                             dispaly_key.append(key)
#
#                         system("cls")
#
#                 result = get_contacts(*dispaly_key)
#
#                 if not result["SUCCESS"]:
#                     show_error(result["ERROR_MESSAGE"])
#                 else:
#                     show_list_dict(result["RETURN_DATA"], *dispaly_key,
#                                    word_len=15, is_capital=True, display_row=True)
#
#             case "3":
#
#                 while True:
#
#                     phone = get_input(filed="Phone (exit)", is_empty=False)
#
#                     if phone == "exit":
#                         break
#
#                     result = remove_contact(phone=phone)
#
#                     if not result["SUCCESS"]:
#                         show_error(result["ERROR_MESSAGE"])
#                     else:
#                         show_success(result["SUCCESS_MESSAGE"])
#
#             case "4":
#
#                 while True:
#
#                     phone = get_input(filed="Phone (exit)", is_empty=False)
#
#                     if phone == "exit":
#                         break
#
#                     new_name = get_input(filed="new name", is_empty=False)
#                     new_family = get_input(filed="new family", is_empty=False)
#                     new_gender = get_input(
#                         filed="new gender", is_empty=False, valid_range=("male", "female", "other"))
#                     new_description = get_input(filed="new description")
#
#                     contact = {
#                         "name": new_name,
#                         "family": new_family,
#                         "phone": phone,
#                         "gender": new_gender,
#                         "description": new_description
#                     }
#
#                     result = edit_contact(contact=contact)
#
#                     if not result["SUCCESS"]:
#                         show_error(result["ERROR_MESSAGE"])
#                     else:
#                         show_success(result["SUCCESS_MESSAGE"])
#
#             case "5":
#
#                 while True:
#
#                     search_item = get_input(
#                         filed="\n\nSearch Item (1.Name 2.Family 3.Phone 4.Gender 5.Exit)",
#                         is_empty=False,
#                         valid_range=("1", "2", "3", "4", "5")
#                     )
#
#                     match search_item:
#                         case "1":
#                             val = input("Name : ")
#                             key = "name"
#
#                         case "2":
#                             val = input("Family : ")
#                             key = "family"
#
#                         case "3":
#                             val = input("Phone : ")
#                             key = "phone"
#
#                         case "4":
#                             val = input("Gender : ")
#                             key = "gender"
#
#                         case _:
#                             break
#
#                     system("cls")
#
#
#                     result = search_contact(key=key, val=val)
#
#                     if not result["SUCCESS"]:
#                         show_error(result["ERROR_MESSAGE"])
#                     else:
#                         show_list_dict(result["RETURN_DATA"], "name", "family", "phone", "gender", "description")
#
#
#             case _:
#                 break
