import json
import requests

# Variable Globale
TASKS_FILE = 'tasks.json'

def load_tasks() -> list:
    with open(TASKS_FILE, 'r') as file:
        data = json.load(file)
        return data.get('tasks', [])

def save_tasks(tasks: list) -> None:
    with open(TASKS_FILE, 'w') as file:
        json.dump({'tasks': tasks}, file, indent=4)

def add_task(title: str, description: str) -> None:
    """
    Ajoute une nouvelle tâche avec une citation inspirante.
    """
    tasks = load_tasks()
    task = {
        'title': title,
        'description': description,
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Tâche '{title}' ajoutée avec succès !")

def delete_task(index: int) -> None:
    tasks = load_tasks() # Récupère les tâches
    if 0 <= index < len(tasks): # Vérifie si l'index est valide
        removed_task = tasks.pop(index) # Supprime la tâche
        save_tasks(tasks) # Enregistre les tâches
        print(f"Tâche '{removed_task['title']}' supprimée.")
    else:
        print("Index invalide.")

def display_tasks() -> None:
    """
    Affiche toutes les tâches enregistrées.
    """
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        print(f"[{i}] {task['title']} - {task['description']}\n")

def main_menu() -> None:
    """
    Affiche le menu principal et gère les interactions utilisateur.
    """
    while True:
        print("\n=== Gestionnaire de Tâches ===")
        print("1. Ajouter une tâche")
        print("2. Supprimer une tâche")
        print("3. Afficher toutes les tâches")
        print("4. Quitter")
        choice = input("Choisissez une option : ")

        if choice == "1":
            title = input("Entrez le titre de la tâche : ")
            description = input("Entrez la description de la tâche : ")
            add_task(title, description)
        elif choice == "2":
            display_tasks()
            index = int(input("Entrez l'index de la tâche à supprimer : "))
            delete_task(index)
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == '__main__':
    main_menu()
