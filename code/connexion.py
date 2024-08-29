from tkinter import *
import os

# Obtenez le chemin absolu du dossier courant
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construisez le chemin absolu de l'image
image_path = os.path.join(current_dir, "add_student_img.png")
print(image_path)  # Pour déboguer, vérifier si le chemin est correct

# Création de la fenêtre principale
root = Tk()
root.title("Page de Connexion")

# Variables globales pour stocker les images
login_stud_icon = PhotoImage(file=image_path)

bg_color = "#34495E"  # Exemple de couleur de fond

# Cadre principal
welcome_page_fm = Frame(root, bg=bg_color)
welcome_page_fm.place(x=0, y=0, width=800, height=600)

# Bouton de connexion pour l'étudiant
student_login_button = Button(
    welcome_page_fm, text="Connexion", bg=bg_color, fg='white', font=('Bold', 15), bd=0)
student_login_button.place(x=120, y=125, width=200)

# Image du bouton de connexion
student_login_img = Button(
    welcome_page_fm, image=login_stud_icon, bd=0)
student_login_img.place(x=120, y=100)

# Lancement de la boucle principale de l'interface Tkinter
root.mainloop()
