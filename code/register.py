from tkinter import *


root = Tk()
root.geometry('500x600')
root.title('La page d\'enregsitrement')
bg_color = '#273b7a'


login_student_icon = PhotoImage(file="images/login_student_img.png")
login_admin_icon = PhotoImage(file="images/admin_img.png")
add_stud_icon = PhotoImage(file="images/add_student_img.png")
locked_icon = PhotoImage(file="images/locked.png")
unlocked_icon = PhotoImage(file="images/unlocked.png")


def welcome_page():
    welcome_page_fm = Frame(
        root, highlightbackground=bg_color, highlightthickness=3)

    heading_label = Label(welcome_page_fm, bg=bg_color, text='Bienvenu sur la page d\'inscription',
                          fg='white', font=('Bold', 18))
    heading_label.place(x=0, y=0, width=400)

    # buttons
    student_login_button = Button(
        welcome_page_fm, text="Connexion Elève", bg=bg_color, fg='white', font=('Bold', 15), bd=0)
    student_login_button.place(x=120, y=125, width=200)

    admin_login_button = Button(
        welcome_page_fm, text="Connexion Admin", bg=bg_color, fg='white', font=('Bold', 15), bd=0)
    admin_login_button.place(x=120, y=225, width=200)

    add_student_button = Button(
        welcome_page_fm, text="Ajouter un élève", bg=bg_color, fg='white', font=('Bold', 15), bd=0)
    add_student_button.place(x=120, y=325, width=200)

    # icon
    student_login_img = Button(
        welcome_page_fm, image=login_student_icon, bd=0)
    student_login_img.place(x=60, y=100)

    admin_login_img = Button(
        welcome_page_fm, image=login_admin_icon, bd=0)
    admin_login_img.place(x=60, y=200)

    add_student_img = Button(
        welcome_page_fm, image=add_stud_icon, bd=0)
    add_student_img .place(x=60, y=300)

    welcome_page_fm.pack(pady=30)
    welcome_page_fm.pack_propagate(False)
    welcome_page_fm.configure(width=400, height=420)


def student_login_page():

    # function to show or hide password
    def show_hide_password():
        if password_ent['show'] == '*':
            password_ent.config(show='')
            show_hide_btn.config(image=unlocked_icon)
        else:
            password_ent.config(show='*')
            show_hide_btn.config(image=locked_icon)

    student_login_page_fm = Frame(
        root, highlightbackground=bg_color, highlightthickness=3)

    heading_lb = Label(student_login_page_fm, text="Connexion Elève", bg=bg_color, fg='white', font=('bold', 18)
                       )
    heading_lb.place(x=0, y=0, width=400)
    stud_icon_label = Label(student_login_page_fm, image=login_student_icon)
    stud_icon_label.place(x=150, y=40)

    # ID label et Input
    id_num_label = Label(student_login_page_fm,
                         text="Entrer votre ID", fg=bg_color, font=('bold', 15))
    id_num_label.place(x=80, y=140)

    id_num_ent = Entry(student_login_page_fm, font=(
        'bold', 15), justify=CENTER, highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2)
    id_num_ent.place(x=80, y=190)

    # Password field

    password_label = Label(student_login_page_fm,
                           text="Entrer votre mot de passe", fg=bg_color, font=('bold', 15))
    password_label.place(x=80, y=240)

    password_ent = Entry(student_login_page_fm, font=(
        'bold', 15), justify=CENTER, highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2, show='*')
    password_ent.place(x=80, y=290)

    # login button

    login_btn = Button(student_login_page_fm, text="Connexion",
                       font=('bold', 15), bg=bg_color, fg='white')
    login_btn.place(x=95, y=340, width=200, height=40)

    # Forget password btn
    forget_pawwsord_btn = Button(student_login_page_fm, text="Mot de passe oublié",
                                 fg=bg_color, bd=0,)
    forget_pawwsord_btn.place(x=150, y=390)

    # show hid btn

    show_hide_btn = Button(student_login_page_fm,
                           image=locked_icon, bd=0, command=show_hide_password)
    show_hide_btn.place(x=310, y=280)

    student_login_page_fm.pack(pady=30)
    student_login_page_fm.pack_propagate(False)
    student_login_page_fm.configure(width=400, height=450)


# function to show or hide password
def show_hide_password():
    if password_ent['show'] == '*':
        password_ent.config(show='')
        show_hide_btn.config(image=unlocked_icon)
    else:
        password_ent.config(show='*')
        show_hide_btn.config(image=locked_icon)


admin_login_page_fm = Frame(
    root, highlightbackground=bg_color, highlightthickness=3)

heading_label = Label(admin_login_page_fm, text="Connexion Admin",
                      bg=bg_color, fg='white', font=('bold', 18))
heading_label.place(x=0, y=0, width=400)

# Icon for admin
admin_icon_label = Label(admin_login_page_fm, image=login_admin_icon)
admin_icon_label.place(x=150, y=40)

# Labels and entry

# ID label et Input
username_label = Label(admin_login_page_fm,
                       text="Nom d'ultilisateur", fg=bg_color, font=('bold', 15))
username_label.place(x=80, y=140)

username_ent = Entry(admin_login_page_fm, font=(
    'bold', 15), justify=CENTER, highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2)
username_ent.place(x=80, y=190)

# Password field

password_label = Label(admin_login_page_fm,
                       text="Mot de passe Admin", fg=bg_color, font=('bold', 15))
password_label.place(x=80, y=240)

password_ent = Entry(admin_login_page_fm, font=(
    'bold', 15), justify=CENTER, highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2, show='*')
password_ent.place(x=80, y=290)

# login button

login_btn = Button(admin_login_page_fm, text="Connexion",
                   font=('bold', 15), bg=bg_color, fg='white')
login_btn.place(x=95, y=340, width=200, height=40)


# show hid btn

show_hide_btn = Button(admin_login_page_fm,
                       image=locked_icon, bd=0, command=show_hide_password)
show_hide_btn.place(x=310, y=280)


admin_login_page_fm.pack(pady=30)
admin_login_page_fm.pack(pady=30)
admin_login_page_fm.pack_propagate(False)
admin_login_page_fm.configure(width=400, height=430)


root.mainloop()
