import os
import time

stagiaires = [
    {"idS": 1, "nom": "Smith", "prenom": "John", "tel": "123456789", "email": "john.smith@example.com"},
    {"idS": 2, "nom": "Doe", "prenom": "Jane", "tel": "987654321", "email": "jane.doe@example.com"},
    {"idS": 3, "nom": "Johnson", "prenom": "Robert", "tel": "555555555", "email": "robert.johnson@example.com"},
    {"idS": 4, "nom": "Garcia", "prenom": "Maria", "tel": "111111111", "email": "maria.garcia@example.com"}
]


filiers = [
    {'idF': 1, 'namef': 'Informatique'},
    {'idF': 2, 'namef': 'Electronique'},
    {'idF': 3, 'namef': 'Mecanique'},
    {'idF': 4, 'namef': 'Telecommunications'}
]

groupes = [    
    {"idG": 1, "nameg": "Groupe 1"},    
    {"idG": 2, "nameg": "Groupe 2"},    
    {"idG": 3, "nameg": "Groupe 3"},    
    {"idG": 4, "nameg": "Groupe 4"}
]

inscription_list = [
    {"id": 1, "idG": 1, "idS": 1, "idF": 1,'date_ins' :"12-12-2022"}, 
    {"id": 2, "idG": 2, "idS": 2, "idF": 1,'date_ins' :"12-12-2023"}, 
    # {"id": 3, "idG": 1, "idS": 3, "idF": 2,'date_ins' :"12-12-2022"}, 
    # {"id": 4, "idG": 3, "idS": 4, "idF": 2,'date_ins' :"12-12-2001"}, 
]


# Slow print function --------------------------------------
def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# -----------------------------------------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# -----------------------------------------------------------
def add_stagiaire():
    if not stagiaires:
        idS = 1
    else:
        idS = stagiaires[-1]["idS"] + 1  # Auto-increment idS
    
    nom = input("Enter nom: ")
    prenom = input("Enter prenom: ")
    tel = input("Enter tel: ")
    email = input("Enter email: ")

    # Check if required fields are empty
    if nom.strip() == "":
        slow_print("Nom is required.",0.25)
    elif prenom.strip() == "":
        slow_print("Prenom is required.",0.25)
    elif tel.strip() == "":
        slow_print("Tel is required.",0.25)
    elif email.strip() == "":
        slow_print("Email is required.",0.25)
    else:
        # Add the stagiaire to the list of dictionaries
        stagiaire = {"idS": idS, "nom": nom, "prenom": prenom, "tel": tel, "email": email}
        stagiaires.append(stagiaire)
        
# -----------------------------------------------------------
def edit_stagiaire():
    clear()
    print('-----------------------------------------------------------------------------')
    display_stagiaires()
    print('-----------------------------------------------------------------------------')
    idS = int(input("Enter idS of the stagiaire to edit: "))
    stagiaire = next((s for s in stagiaires if s["idS"] == idS), None)
    print(stagiaire)
    if stagiaire is None:
        slow_print("Stagiaire not found.")
    else:
        print(f"Editing stagiaire {idS} :")
        nom = input(f"Enter new nom ({stagiaire['nom']}): ")
        prenom = input(f"Enter new prenom ({stagiaire['prenom']}): ")
        tel = input(f"Enter new tel ({stagiaire['tel']}): ")
        email = input(f"Enter new email ({stagiaire['email']}): ")
        
        # Update stagiaire information if new information is provided
        if nom.strip() != "":
            stagiaire["nom"] = nom
        if prenom.strip() != "":
            stagiaire["prenom"] = prenom
        if tel.strip() != "":
            stagiaire["tel"] = tel
        if email.strip() != "":
            stagiaire["email"] = email
        else:
            slow_print("Stagiaire information updated successfully!",0.25)

# -----------------------------------------------------------
def remove_stagiaire():
    clear()
    print('-----------------------------------------------------------------------------')
    display_stagiaires()
    print('-----------------------------------------------------------------------------')
    idS = int(input("Enter idS of the stagiaire to remove: "))
    stagiaire = next((s for s in stagiaires if s["idS"] == idS), None)
    #Si un tel dictionnaire est trouvé, cet élément de la liste est retourné. Sinon, la valeur None est retournée.
    
    if stagiaire is None:
        slow_print("Stagiaire not found.")
    else:
        stagiaires.remove(stagiaire)
        slow_print("Stagiaire removed successfully!")

# -----------------------------------------------------------
def display_stagiaires():
    if len(stagiaires) == 0:
        print("No stagiaires found.")
    else:
        print("List of stagiaires:")
    for stagiaire in stagiaires:
        print(f"idS: {stagiaire['idS']}, nom: {stagiaire['nom']}, prenom: {stagiaire['prenom']}, tel: {stagiaire['tel']}, email: {stagiaire['email']}")

# -----------------------------------------------------------
def print_inscription_details():
    if len(inscription_list) == 0:
        print("No inscription found.")
    else:
        print("List of Inscription:")
        for inscription in inscription_list:
            filiere = next((f for f in filiers if f['idF'] == inscription['idF']), None)
            groupe = next((g for g in groupes if g['idG'] == inscription['idG']), None)
            stagiaire = next((s for s in stagiaires if s['idS'] == inscription['idS']), None)
            if filiere and groupe and stagiaire:
                print(f"ID: {inscription['id']}, Nom: {stagiaire['nom']}, filiere: {filiere['namef']}, groupe: {groupe['nameg']}, Date_ins: {inscription['date_ins']}")

# -----------------------------------------------------------
def display_groupes():
    print("List of groupes:")
    for groupe in groupes:
        print(f"idG: {groupe['idG']}, nameg: {groupe['nameg']}")

# -----------------------------------------------------------
def print_filiers():
    print("List of filiers:")
    for filier in filiers:
        print(f"idF: {filier['idF']}, namef: {filier['namef']}")

# -----------------------------------------------------------
def add_inscription():
    clear()
    print("Enter the following information to add a new inscription:")
    
    print('-----------------------------------------------------------------------------')
    display_stagiaires()
    print('-----------------------------------------------------------------------------')
    idS = input("Enter the ID of the stagiaire: ")

    print('-----------------------------------------------------------------------------')
    print_filiers()
    print('-----------------------------------------------------------------------------')
    idF = input("Enter the ID of the filiere: ")

    print('-----------------------------------------------------------------------------')
    display_groupes()
    print('-----------------------------------------------------------------------------')
    idG = input("Enter the ID of the groupe: ")

    date_ins = input("Enter the date of inscription (DD-MM-YYYY): ")
    
    # Check if the stagiaire, filiere, and groupe IDs exist
    stagiaire = next((s for s in stagiaires if s['idS'] == int(idS)), None)
    filiere = next((f for f in filiers if f['idF'] == int(idF)), None)
    groupe = next((g for g in groupes if g['idG'] == int(idG)), None)
    
    if not stagiaire:
        print(f"Error: No stagiaire found with ID {idS}")
        return
    
    if not filiere:
        print(f"Error: No filiere found with ID {idF}")
        return
    
    if not groupe:
        print(f"Error: No groupe found with ID {idG}")
        return
    
    # Generate a new ID for the inscription
    max_id = max([i['id'] for i in inscription_list] + [0])
    new_id = max_id + 1
    
    # Add the new inscription to the list
    inscription_list.append({"id": new_id, "idS": int(idS), "idF": int(idF), "idG": int(idG), "date_ins": date_ins})
    
    print("Inscription added successfully.")

# -----------------------------------------------------------
def edit_inscription():
    clear()
    print("Enter the ID of the inscription you want to edit:")
    print('-----------------------------------------------------------------------------')
    print_inscription_details()
    print('-----------------------------------------------------------------------------')
    inscription_id = input("ID: ")
    
    # Find the inscription with the given ID
    inscription = next((i for i in inscription_list if i['id'] == int(inscription_id)), None)
    if not inscription:
        slow_print(f"No inscription found with ID {inscription_id}")

    else:
        print("Enter the new information for the inscription:")
        
        # Prompt the user to update the stagiaire, filiere, groupe, and date of the inscription
        print('-----------------------------------------------------------------------------')
        display_stagiaires()
        print('-----------------------------------------------------------------------------')
        idS = input(f"Enter the new ID of the stagiaire (current: {inscription['idS']}): ")

        print('-----------------------------------------------------------------------------')
        print_filiers()
        print('-----------------------------------------------------------------------------')
        idF = input(f"Enter the new ID of the filiere (current: {inscription['idF']}): ")

        print('-----------------------------------------------------------------------------')
        display_groupes()
        print('-----------------------------------------------------------------------------')
        idG = input(f"Enter the new ID of the groupe (current: {inscription['idG']}): ")

        date_ins = input(f"Enter the new date of inscription (current: {inscription['date_ins']}, DD-MM-YYYY): ")
        
        inscription['idS'] = int(idS)
        inscription['idF'] = int(idF)
        inscription['idG'] = int(idG)
        inscription['date_ins'] = date_ins
            
        print("Inscription updated successfully.")
# -----------------------------------------------------------

def remove_inscription():
    clear()
    print("Enter the ID of the inscription to remove:")
    print('-----------------------------------------------------------------------------')
    print_inscription_details()
    print('-----------------------------------------------------------------------------')
    inscription_id = input("Inscription ID: ")
    
    inscription = next((i for i in inscription_list if i['id'] == int(inscription_id)), None)
    
    if not inscription:
        slow_print(f"No inscription found with ID {inscription_id}")
    else:
        inscription_list.remove(inscription)
        slow_print("Inscription removed successfully.")

# Main menu loop
while True:
    clear()
    print('-----------------------------------------------------------------------------')
    print_inscription_details()
    print('-----------------------------------------------------------------------------')
    print('---------- stagiaire----------')
    print("1 - Show stagiaire")
    print("2 - Add stagiaire")
    print("3 - Edit stagiaire")
    print("4 - Remove stagiaire")
    print('---------- Inscription ----------')
    print("5 - Add Inscription")
    print("6 - Edit Inscription")
    print("7 - Remove Inscription")
    print("8 - Quit")
    choice = input("Enter your choice (1-8): ")
    
    if choice == "2":
        add_stagiaire()
    elif choice == "3":
        edit_stagiaire()
    elif choice == "4":
        remove_stagiaire()
    elif choice == "1":
        clear()
        print('-----------------------------------------------------------------------------')
        display_stagiaires()
        print('-----------------------------------------------------------------------------')
        message = input('go to Menu')
        slow_print('------------>')
    elif choice == "8":
        break  # Exit the loop
    elif choice == "5":
        add_inscription()
    elif choice == "6":
        edit_inscription()
    elif choice == "7":
        remove_inscription()
    else:
        slow_print("Invalid choice. Please enter a number between 1 and 8.")

