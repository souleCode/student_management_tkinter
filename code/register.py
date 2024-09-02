from tkinter import *
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont
import re
import random
import sqlite3
import os


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


def draw_student_card(student_pic_path, student_data):
    labels = """
Numero ID:
Nom&Prenom:
Genre:
Age:
Classe:
Numero:
email:
    """
    student_card = Image.open('images/student_card_frame.png')
    pic = Image.open(student_pic_path)
    new_size = (100, 100)
    pic_resized = pic.resize(new_size)
    student_card.paste(pic_resized, (15, 25))
    # draw image

    draw = ImageDraw.Draw(student_card)
    heading_font = ImageFont.truetype('bahnschrift', 18)
    labels_font = ImageFont.truetype('arial', 15)
    data_font = ImageFont.truetype('bahnschrift', 13)

    draw.text(xy=(130, 60), text='La carte de l\'élève', fill=(0, 0, 0),
              font=heading_font)

    draw.multiline_text(xy=(15, 120), text=labels,
                        fill=(0, 0, 0), font=labels_font, spacing=6)

    draw.multiline_text(xy=(120, 120), text=student_data,
                        font=data_font, spacing=10, fill=(0, 0, 0))
    return student_card


def student_card_page(student_card_obj):
    ''' Cette fonction ecris les informations de l'eleve sur la page
        La page est une photo en realite(),
        La fonction prend un obj qui est en realite le return de la fonction draw_student_card()
        On converti l'image retourner en une imageTk
        Cette fonction sera donc appeler dans le add_student() dans la partie ou on a ajouter les datat dans le db
        et remplir la carte. Donc le retour de la fonction draw_student_card()sera notre objet student_card_ob

    '''
    student_card_img = ImageTk.PhotoImage(student_card_obj)

    student_card_page_fm = Frame(
        root, highlightbackground=bg_color, highlightthickness=3)

    heading_lb = Label(student_card_page_fm, text=" La carte de l'élève",
                       bg=bg_color, fg='white', font=('Bold', 18))
    heading_lb.place(x=0, y=0, width=400)

    close_btn = Button(student_card_page_fm, text="X",
                       font=('Bold', 13), bg=bg_color, fg='white', bd=0, command=lambda: student_card_page_fm.destroy())
    close_btn.place(x=370, y=0)

    student_card_lb = Label(student_card_page_fm, image=student_card_img)
    student_card_lb.place(x=50, y=50)
    student_card_lb.image = student_card_img

    save_student_card_btn = Button(
        # borderwidth=1, bordure sera visible
        student_card_page_fm, text='Enregister la carte', bg=bg_color, font=('Bold', 15), fg='white', bd=0)
    save_student_card_btn.place(x=80, y=375)

    student_card_page_fm.place(x=50, y=30, width=400, height=450)

    print_student_card_btn = Button(
        # borderwidth=1, bordure sera visible
        student_card_page_fm, text='🖨', bg=bg_color, font=('Bold', 18), fg='white', bd=0)
    print_student_card_btn.place(x=270, y=370)

    student_card_page_fm.place(x=50, y=30, width=400, height=450)


def init_database():
    if os.path.exists('student_account.db'):
        pass
    else:
        connection = sqlite3.connect('student_account.db')
        cursor = connection.cursor()  # Help to execute sqlite3 query
        query = """
        CREATE TABLE IF NOT EXISTS data (
            id_number text,
            password text,
            name text,
            age text,
            gender text,
            phone text,
            class text,
            email text,
            image blob
        )
        """
        cursor.execute(query)

        connection.commit()
        connection.close()


def check_id_already_exists(id_number):
    connection = sqlite3.connect('student_account.db')
    cursor = connection.cursor()
    cursor.execute(
        f"""
            SELECT id_number FROM data WHERE id_number='{id_number}'
    """)
    connection.commit()
    reponse = cursor.fetchall()
    connection.close()
    return reponse


def add_data(id_number, password, name, age, gender, phone_number, student_class, email, pic_data):
    connection = sqlite3.connect('student_account.db')
    cursor = connection.cursor()
    cursor.execute(
        f"""
        INSERT INTO data VALUES ( '{id_number}','{password}','{name}','{age}','{gender}','{phone_number}','{student_class}','{email}',?)
    """, [pic_data])
    connection.commit()
    connection.close()


def message_box(message, statut='red'):

    message_box_fm = Frame(
        root, highlightbackground=bg_color, highlightthickness=3)
    message_box_fm.place(x=100, y=120, width=320, height=200)
    message_lb = Label(message_box_fm, text=message,
                       fg=statut, font=('Bold', 15))
    # @..toto
    # icon_avert = Label(message_box_fm, image=avert, bd=0)
    # icon_avert.place(x=50, y=100, width=80, height=80)

    close_btn = Button(message_box_fm, text='X', bd=0, font=(
        'Bold', 13), fg=bg_color, command=lambda: message_box_fm.destroy())
    close_btn.place(x=290, y=5)
    message_lb.pack(pady=50)


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
    pic_path = StringVar()
    pic_path.set(' ')

    def open_pic():
        '''
        Cette fonction est utiliser pour ouvrir le gestionnaire de dossiers et prendre une image pour mettre
        dans le frame de add_image
        Cette fonction sera commander par le button add_pic_btn
        '''
        path = askopenfilename()
        if path:
            # print(path)
            img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
            pic_path.set(path)

            # On fait la mise a jour de l'image
            add_pic_btn.config(image=img)
            add_pic_btn.image = img

    def remove_highlight_warning(entry):
        '''
         Cette fonction permet d'enlever les avertissement sur les entry une fois remplies. Sinon si on
         02 entry vides, et on averti de remplir, le user va remplir le 01 et le quand il essaie de soumettre a nouveau,
         on lui avertira avec les bordure rouge sur l'entry qu'il vient justeb de remplir.
        '''
        if entry['highlightbackground'] != 'gray':
            if entry.get() != '':
                entry.config(highlightbackground='gray', highlightcolor='gray')

    def check_invalid_email(email):
        '''
         verifie email pour avoir la forme john.doe@example.com.
         email invalides: john.doe@com (TLD trop court)
        '''
        pattern = r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$"
        match = re.match(pattern=pattern, string=email)
        return match
    #  @...todo: check_phone number and username and age

    def validate_age(age):
        ''''
        Cette fonction verifie l'age en tenant compte du fait que ca soit 02 digits
        '''
        pattern = r"^\d{1,2}$"
      # Accepte un ou plusieurs chiffres (jusqu'à 3 chiffres)
        match = re.match(pattern, age)
        return match

    def isNameValide(name):
        ''''
        Cette fonction force en fait le user a donner un nom sous forme Nom+Prenom
        '''
        pattern = r"^[A-Z][a-z]+ [A-Z][a-z]+$"
        match = re.match(pattern, name)
        return match

    def isContactValid(contact):
        ''''Verfirie la forme des numero : 08chiffres'''
        pattern = r"^\d{8}$"
        match = re.match(pattern, contact)
        return match

    def generate_id_number():
        '''
         Cette fonction sera appellée chaque fois qu'on essaie de creer un etudiant,
         pour generer automatiquement un ID
         Elle verifie egalement si ID n'existe pas deja dans notre passe de donnée.
         Si ID existe on fait la recursivité pour en generer a nouveau et la verification se fait automatically
        '''
        list_of_elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'k', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        generated_id = ''

        # Définir la longueur souhaitée pour l'ID, par exemple 8 caractères
        id_length = 6

        # Boucle pour générer l'ID
        for _ in range(id_length):
            generated_id += str(random.choice(list_of_elements))

        if not check_id_already_exists(generated_id):
            student_id_ent.config(state=NORMAL)
            student_id_ent.delete(0, END)
            student_id_ent.insert(END, generated_id)
            student_id_ent.config(state='readonly')
        # print(generated_id)
        else:
            generate_id_number()  # la recurisivite ici

    def check_input_validation():
        '''
         Cette fonction verifie chaque entrée et appelle la fonction  message_box au cas ou une entree est vide
         Pour dire de la remplir car elle est obligatoire
        '''
        if student_name_ent.get() == '':
            student_name_ent.config(
                highlightbackground='red', highlightcolor='red')
            student_name_ent.focus()
            message_box(message='Vous devrez remplir\n le nom de l\'élève')
            # Verifie si le nom est complet
        # elif not isNameValide(student_name_ent.get()):
        #     student_name_ent.config(
        #         highlightbackground='red', highlightcolor='red')
        #     student_name_ent.focus()
            message_box(message='Veuillez donner le nom\n et le prenom')
        elif student_age_ent.get() == '':
            student_age_ent.config(
                highlightbackground='red', highlightcolor='red')
            student_age_ent.focus()
            message_box(message="Veuillez renseigner l'âge de l'élève")
            # Verifie si l'age est comforme
        elif not validate_age(age=student_age_ent.get()):
            student_age_ent.config(
                highlightbackground='red', highlightcolor='red')
            student_age_ent.focus()
            message_box(
                message="L'age invalide\n Veuillez utiliser un age\n valide:2 chiffres")
        elif student_contact_ent.get() == '':
            student_contact_ent.config(
                highlightbackground='red', highlightcolor='red')
            student_contact_ent.focus()
            message_box(
                message="Veuillez renseigner votre numero \n joignable")
            # verifie la validite du numero
        elif not isContactValid(student_contact_ent.get()):
            student_contact_ent.config(
                highlightbackground='red', highlightcolor='red')
            student_contact_ent.focus()
            message_box(
                message="Veuillez renseigner un \n numero valide\n Exemple: 65544895 ")
        elif select_class_btn.get() == '':
            # select box n'a pas les attribut highlight, donc on va juste focus
            select_class_btn.focus()
            message_box(
                message="Veuillez choisir la classe\ndans la quelle\n vous allez vous inscrie")
        elif student_email_ent.get() == '':
            student_email_ent.config(
                highlightbackground='red', highlightcolor='red')
            student_email_ent.focus()
            message_box(
                message="Veuillez ajouter un email\n pour recevoir des informations\n la dessus.")
            # Verifie si l'email est comforme
        elif not check_invalid_email(email=student_email_ent.get().lower()):
            student_email_ent.config(
                highlightbackground='red', highlightcolor='red')
            student_email_ent.focus()
            message_box(
                message="Email invalide\n Veuillez utiliser un email\n valide.Le format:\njohn.doe@example.com")
        elif student_password_ent.get() == '':
            student_password_ent.config(
                highlightbackground='red', highlightcolor='red')
            student_password_ent.focus()
            message_box(
                message="Le mot de passe est obligatoire!\n Merci de remplir ce champs")

        else:
            # valide les donnees images avant de les inserer
            pic_data = b''
            if pic_path.get() != '':
                resize_pic = Image.open(pic_path.get()).resize((100, 100))
                resize_pic.save('temp_pic.jpg')
                read_data = open('temp_pic.jpg', 'rb')
                pic_data = read_data.read()
                read_data.close()
            else:
                pass
                # message_box(
                #     message="C'est conseillé d'utiliser votre\n photo de profile.Donc cliquez sur la case\n et choisir une de vos photos")

            # Une fois que tout es ok, on passe a inserer les datat dans notre base de données
            add_data(student_id_ent.get(),
                     student_password_ent.get(),
                     student_name_ent.get(),
                     student_age_ent.get(),
                     student_gender_val.get(),
                     student_contact_ent.get(),
                     select_class_btn.get(),
                     student_email_ent.get(),
                     pic_data
                     )

            data = f"""
{student_id_ent.get()}
{student_name_ent.get()}
{student_gender_val.get()}
{student_age_ent.get()}
{select_class_btn.get()}
{student_contact_ent.get()}
{student_email_ent.get()}

            """
            get_student_card = draw_student_card(
                student_pic_path=pic_path.get(), student_data=data)
            # On appelle la fonction student_card_page() en lui fournissant get_student_card
            student_card_page(get_student_card)
            add_account_page_fm.destroy()
            root.update()
            message_box('Votre compte est bien crée\n avec succès! Merci',
                        statut='green')
     # change de page: register form to home

    def change_page():
        '''
         cette fonction a 2 partie:
           -Basic, elle change de page register a to home.
           -Et comme il faut verifier si l'utilisateur veut vraiment switcher avec le confirmation_box,
                        donc la deuxime partie rente en jeu.
                        Alors la fonction confirmation_box(message) est definie en bas , pour savoir si le user
                        veut vraiment switcher la page ou non
        '''
        ans = confirmation_box(
            message='Vous voulez reellement\n quitter cette page?')
        if ans:
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
    add_pic_btn = Button(add_pic_fm, image=add, bd=0, command=open_pic)
    add_pic_btn.pack()

    # create label and entry bar
    student_name_lb = Label(add_account_page_fm,
                            text="Nom complet de l'élève", font=('Bold', 12))
    student_name_lb.place(x=5, y=130)

    student_name_ent = Entry(add_account_page_fm, font=(
        'Bold', 15), highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2)
    student_name_ent.place(x=5, y=160, width=180)
    student_name_ent.bind(
        # À chaque fois que l'utilisateur tape quelque chose dans la zone de texte student_name_ent et relâche la touche, la fonction remove_highlight_warning est exécutée.
        '<KeyRelease>', lambda e: remove_highlight_warning(entry=student_name_ent))

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
    student_age_ent.bind(
        # À chaque fois que l'utilisateur tape quelque chose dans la zone de texte student_age_ent et relâche la touche, la fonction remove_highlight_warning est exécutée.
        '<KeyRelease>', lambda e: remove_highlight_warning(entry=student_age_ent))

    # create label and entry bar for student contact
    student_contact_lb = Label(add_account_page_fm,
                               text="Le Numero de l'élève", font=('Bold', 12))
    student_contact_lb.place(x=5, y=360)
    student_contact_ent = Entry(add_account_page_fm, font=(
        'Bold', 15), highlightcolor=bg_color, highlightbackground='gray', highlightthickness=2)
    student_contact_ent.place(x=5, y=390, width=180)
    student_contact_ent.bind(
        # À chaque fois que l'utilisateur tape quelque chose dans la zone de texte student_contact_ent et relâche la touche, la fonction remove_highlight_warning est exécutée.
        '<KeyRelease>', lambda e: remove_highlight_warning(entry=student_contact_ent))

    # create label and combobox for student classes
    student_class_lb = Label(add_account_page_fm,
                             text="Choisir votre classe", font=('Bold', 12))
    student_class_lb.place(x=5, y=445)
    select_class_btn = Combobox(
        add_account_page_fm, font=('Bold', 15), state='readonly', values=student_classes)
    select_class_btn.place(x=5, y=475, width=180, height=30)
    select_class_btn.bind(
        # À chaque fois que l'utilisateur tape quelque chose dans la zone de texte student_name_ent et relâche la touche, la fonction remove_highlight_warning est exécutée.
        '<KeyRelease>', lambda e: remove_highlight_warning(entry=select_class_btn))

    # create label and entry bar for student ID number
    student_id_lb = Label(add_account_page_fm,
                          text="ID de l'élève", font=('Bold', 12),)
    student_id_lb.place(x=240, y=35)
    student_id_ent = Entry(
        add_account_page_fm, font=('Bold', 18))
    student_id_ent.place(x=350, y=35, width=100)

    # Insert random number into the id_ent
    student_id_ent.config(state='readonly')
    generate_id_number()  # Generate ID number
    # # info about ID
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
    student_email_ent.bind(
        # À chaque fois que l'utilisateur tape quelque chose dans la zone de texte student_name_ent et relâche la touche, la fonction remove_highlight_warning est exécutée.
        '<KeyRelease>', lambda e: remove_highlight_warning(entry=student_email_ent))
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
    student_password_ent.bind(
        # À chaque fois que l'utilisateur tape quelque chose dans la zone de texte student_name_ent et relâche la touche, la fonction remove_highlight_warning est exécutée.
        '<KeyRelease>', lambda e: remove_highlight_warning(entry=student_password_ent))

    # info about password
    pass_info_lb = Label(add_account_page_fm,
                         text="Il est confidentiel et doit être \nutilisé pour vous connecter", fg='red', justify=LEFT)

    pass_info_lb.place(x=240, y=345)

    # Home and submit button
    home_btn = Button(add_account_page_fm, text='Acceuil',
                      font=('Bold', 15), bg='red', fg='white', bd=0, command=change_page)
    home_btn.place(x=240, y=420)

    submit_btn = Button(add_account_page_fm, text='Envoyer',
                        font=('Bold', 15), bg=bg_color, fg='white', bd=0, command=check_input_validation)
    submit_btn.place(x=360, y=420)

    student_gender_val.set('M')  # Le genre par defaut
    add_account_page_fm.pack(pady=5)
    add_account_page_fm.pack_propagate(False)
    add_account_page_fm.configure(width=480, height=580)


def confirmation_box(message):

    answer = BooleanVar()
    answer.set(False)

    def action(ans):
        '''
         cette fonction ajoute la valeur ans a notre answer
         afin de decider si c'est true or false
         Cette action sera utilisée sur le button: Oui(avec ans=True) /Non(avec ans=False)
        '''
        answer.set(ans)
        confirmation_box_fm.destroy()

    confirmation_box_fm = Frame(
        root, highlightbackground=bg_color, highlightthickness=3)
    message_lb = Label(confirmation_box_fm, text=message,
                       fg='red', font=('Bold', 15))
    message_lb.pack(pady=20)

    # button on confirmation_message

    no_btn = Button(confirmation_box_fm, text='Non', font=(
        'Bold', 15), bd=0, bg=bg_color, fg='white', command=lambda: action(False))
    no_btn.place(x=50, y=160, width=80)

    yes_btn = Button(confirmation_box_fm, text='Oui', font=(
        'Bold', 15), bd=0, bg=bg_color, fg='white', command=lambda: action(True))
    yes_btn.place(x=190, y=160, width=80)

    confirmation_box_fm.place(x=100, y=120, width=320, height=220)

    root.wait_window(confirmation_box_fm)
    return answer.get()


init_database()
# draw_student_card()
# student_card_page()
welcome_page()
root.mainloop()
