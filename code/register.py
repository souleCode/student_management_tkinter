from tkinter import *
from tkinter.ttk import Combobox


root = Tk()
root.geometry('500x600')
root.title('La page d\'enregsitrement')
bg_color = '#273b7a'


login_student_icon = PhotoImage(file="images/login_student_img.png")
login_admin_icon = PhotoImage(file="images/admin_img.png")
add_stud_icon = PhotoImage(file="images/add_student_img.png")
locked_icon = PhotoImage(file="images/locked.png")
unlocked_icon = PhotoImage(file="images/unlocked.png")
add = PhotoImage(file="images/add_image.png")


# Student classes
student_classes = ['6eme', '5e', '4e', '3e', '2ndC', '2ndA',
                   '1ereD', '1ereA', 'TleD', 'TleA']


def welcome_page():
    # Function to call when the user clicks on login student
    def change_student_login_page():
        welcome_page_fm.destroy()
        root.update()
        student_login_page()

    # function to call when user clicks on admin login
    def change_admin_login_page():
        welcome_page_fm.destroy()
        root.update()
        admin_login_page()

    def change_add_account_page():
        welcome_page_fm.destroy()
        root.update()
        add_account_page()

    welcome_page_fm = Frame(
        root, highlightbackground=bg_color, highlightthickness=3)

    heading_label = Label(welcome_page_fm, bg=bg_color, text='Bienvenu sur la page d\'inscription',
                          fg='white', font=('Bold', 18))
    heading_label.place(x=0, y=0, width=400)

    # buttons
    student_login_button = Button(
        welcome_page_fm, text="Connexion Elève", bg=bg_color, fg='white', font=('Bold', 15), bd=0, command=change_student_login_page)
    student_login_button.place(x=120, y=125, width=200)

    admin_login_button = Button(
        welcome_page_fm, text="Connexion Admin", bg=bg_color, fg='white', font=('Bold', 15), bd=0, command=change_admin_login_page)
    admin_login_button.place(x=120, y=225, width=200)

    add_student_button = Button(
        welcome_page_fm, text="Ajouter un élève", bg=bg_color, fg='white', font=('Bold', 15), bd=0, command=change_add_account_page)
    add_student_button.place(x=120, y=325, width=200)

    # icon
    student_login_img = Button(
        welcome_page_fm, image=login_student_icon, bd=0, command=change_student_login_page)
    student_login_img.place(x=60, y=100)

    admin_login_img = Button(
        welcome_page_fm, image=login_admin_icon, bd=0, command=change_admin_login_page)
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
    # function to change to welcome page when click on back

    def change_to_welcome():
        student_login_page_fm.destroy()
        root.update()
        welcome_page()

    student_login_page_fm = Frame(
        root, highlightbackground=bg_color, highlightthickness=3)

    heading_lb = Label(student_login_page_fm, text="Connexion Elève", bg=bg_color, fg='white', font=('bold', 18)
                       )
    heading_lb.place(x=0, y=0, width=400)
    stud_icon_label = Label(student_login_page_fm, image=login_student_icon)
    stud_icon_label.place(x=150, y=40)

    # button pour revenir en arriere sur welcome page
    back_btn = Button(student_login_page_fm, text="<<",
                      font=('bold', 20), fg=bg_color, bd=0, command=change_to_welcome)
    back_btn.place(x=5, y=40)

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


def admin_login_page():
    # function to show or hide password
    def show_hide_password():
        if password_ent['show'] == '*':
            password_ent.config(show='')
            show_hide_btn.config(image=unlocked_icon)
        else:
            password_ent.config(show='*')
            show_hide_btn.config(image=locked_icon)

    def change_to_welcome():
        admin_login_page_fm.destroy()
        root.update()
        welcome_page()
    admin_login_page_fm = Frame(
        root, highlightbackground=bg_color, highlightthickness=3)

    heading_label = Label(admin_login_page_fm, text="Connexion Admin",
                          bg=bg_color, fg='white', font=('bold', 18))
    heading_label.place(x=0, y=0, width=400)
    # button to return to welcome page
    back_btn = Button(admin_login_page_fm, text="<<",
                      fg=bg_color, font=('Bold', 20), bd=0, command=change_to_welcome)
    back_btn.place(x=5, y=40)
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


def add_account_page():
    """" Cette fonction appelle page de register form avec tout ces
    composants. 
    """

    # change de page: register form to home

    def change_page():
        add_account_page_fm.destroy()
        root.update()
        welcome_page()

    student_gender_val = StringVar()  # variable for student gender

    add_account_page_fm = Frame(
        root, highlightbackground=bg_color, highlightthickness=3)

    add_pic_fm = Frame(add_account_page_fm,
                       highlightbackground=bg_color, highlightthickness=3)
    add_pic_fm.place(x=5, y=5, width=105, height=105)

    # Add student btn
    add_student_btn = Button(add_pic_fm, image=add, bd=0)
    add_student_btn.pack()

    # create label and entry bar
    student_name_lb = Label(add_account_page_fm,
                            text="Nom complet de l'élève", font=('Bold', 12))
    student_name_lb.place(x=5, y=130)

    student_name_ent = Entry(add_account_page_fm, font=(
        'Bold', 15), highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2)
    student_name_ent.place(x=5, y=160, width=180)

    # create label and radiobtn bar for student gender
    student_gender_lb = Label(add_account_page_fm,
                              text="Genre de l'élève", font=('Bold', 12))
    student_gender_lb.place(x=5, y=210)

    male_gender_btn = Radiobutton(
        add_account_page_fm, text='M', font=('Bold', 12), variable=student_gender_val, value='M')
    male_gender_btn.place(x=5, y=235)

    female_gender_btn = Radiobutton(
        add_account_page_fm, text='F', font=('Bold', 12), variable=student_gender_val, value='F')
    female_gender_btn.place(x=75, y=235)

    # create label and entry bar for student age
    student_age_lb = Label(add_account_page_fm,
                           text="Age de l'élève", font=('Bold', 12))
    student_age_lb.place(x=5, y=275)
    student_age_ent = Entry(add_account_page_fm, font=(
        'Bold', 15), highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2)
    student_age_ent.place(x=5, y=305, width=180)

    # create label and entry bar for student contact
    student_contact_lb = Label(add_account_page_fm,
                               text="Le Numero de l'élève", font=('Bold', 12))
    student_contact_lb.place(x=5, y=360)
    student_contact_ent = Entry(add_account_page_fm, font=(
        'Bold', 15), highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2)
    student_contact_ent.place(x=5, y=390, width=180)

    # create label and combobox for student classes
    student_class_lb = Label(add_account_page_fm,
                             text="Choisir votre classe", font=('Bold', 12))
    student_class_lb.place(x=5, y=445)
    select_class_btn = Combobox(
        add_account_page_fm, font=('Bold', 15), state='readonly', values=student_classes)
    select_class_btn.place(x=5, y=475, width=180, height=30)

    # create label and entry bar for student ID number
    student_id_lb = Label(add_account_page_fm,
                          text="ID de l'élève", font=('Bold', 12),)
    student_id_lb.place(x=240, y=35)
    student_id_ent = Entry(
        add_account_page_fm, font=('Bold', 18))
    student_id_ent.place(x=350, y=35, width=80)

    # Insert random number into the id_ent
    student_id_ent.insert(END, '184570')
    student_id_ent.config(state='readonly')
    # info about ID
    id_info_lb = Label(add_account_page_fm,
                       text="ID est unique et généré automatiquement!\nRappelle:C'est l'ID utilisé pour se connecter", fg='red', justify=LEFT)

    id_info_lb.place(x=230, y=65)

    # create label and entry bar for student email address
    student_email_lb = Label(add_account_page_fm,
                             text="Votre adresse email", font=('Bold', 12))
    student_email_lb.place(x=240, y=130)
    student_email_ent = Entry(add_account_page_fm, font=(
        'Bold', 15), highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2)
    student_email_ent.place(x=240, y=160, width=180)
    # info about email addresses
    email_info_lb = Label(add_account_page_fm,
                          text="Vous recevrez des notifications sur\ncet email.En cas d'oublie de \n  Mot de passe vouasallez utiliser cet email\n", fg='red', justify=LEFT)

    email_info_lb.place(x=240, y=200)

    # create label and entry bar for student password
    student_password_lb = Label(add_account_page_fm,
                                text="Votre mot de passe", font=('Bold', 12))
    student_password_lb.place(x=240, y=275)
    student_password_ent = Entry(add_account_page_fm, font=(
        'Bold', 15), highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2)
    student_password_ent.place(x=240, y=307, width=180)

    # info about password
    pass_info_lb = Label(add_account_page_fm,
                         text="Il est confidentiel et doit être \nutilisé pour vous connecter", fg='red', justify=LEFT)

    pass_info_lb.place(x=240, y=345)

    # Home and submit button
    home_btn = Button(add_account_page_fm, text='Acceuil',
                      font=('Bold', 15), bg='red', fg='white', bd=0, command=change_page)
    home_btn.place(x=240, y=420)

    submit_btn = Button(add_account_page_fm, text='Envoyer',
                        font=('Bold', 15), bg=bg_color, fg='white', bd=0)
    submit_btn.place(x=360, y=420)

    student_gender_val.set('M')  # Le genre par defaut
    add_account_page_fm.pack(pady=5)
    add_account_page_fm.pack_propagate(False)
    add_account_page_fm.configure(width=480, height=580)


welcome_page()
root.mainloop()
