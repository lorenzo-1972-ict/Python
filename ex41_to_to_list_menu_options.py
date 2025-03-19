import os
import json

def show_tasks():
    filepath = "agenda.json"
    with open (filepath, "r") as f:
        print(f.read())
        f.close()

def create_agenda(agenda):
    filepath = "agenda.json"
    if os.path.exists(filepath):
        print("Initialisation de la base de données...")
        return
    else:
        print("Agenda.json a bien été créé")
    with open(agenda, "w") as f:
        f.close()        

#def del_task():
    json.load

def add_task():
    titre=input("Entrez le nom de la tâche : ")
    description=input("Entrez la description de la tâche : ")
    filepath="agenda.json"
    dico = {"titre":titre, "description":description}

    with open(filepath, "a") as f:
        dic_str = str(dico)
        f.write(dic_str + "Numéro de tache" + "\n")
        f.close()

def menu():
    while True:
        choix = input("Voulez-vous voir les tâches [1], ajouter une tâche [2], modifier une tâche [3] ou supprimer une tâche [4] ou quitter [5]?")
        if choix == "1":
            show_tasks()
        elif choix == "2":
            add_task()
        elif choix == "3":
            pass
        elif choix == "4":
            del_task()
        elif choix == "5":
            break
        else:
            print("!")