from tkinter import *


root = Tk()
root.geometry('500x600')
root.title('La page d\'enregsitrement')
bg_color = '#273b7a'


login_student_icon = PhotoImage(file="images/login_student_img.png")
login_admin_icon = PhotoImage(file="images/admin_img.png")
add_stud_icon = PhotoImage(file="images/add_student_img.png")

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


root.mainloop()
