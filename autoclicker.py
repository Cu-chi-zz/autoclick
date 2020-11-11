from pyautogui import *
from os import system
from tkinter import *
from colorama import init, Fore
from PIL import Image 

import pyautogui
import colorama
import time
import keyboard
import random
import json
import win32api, win32con

colorama.init(autoreset=True)

Available_Key_List = [
    'A','B','C','D','E','F',
    'G','H','I','J','K','L',
    'M','N','O','P','Q','R',
    'S','T','U','V','W','X',
    'Y','Z','0','1','2','3',
    '4','5','6','7','8','9',
    '<','>','SPACE_BAR','SHIFT','CTRL','ALT','TAB',
    'a','b','c','d','e','f',
    'g','h','i','j','k','l',
    'm','n','o','p','q','r',
    's','t','u','v','w','x',
    'y','z','0','1','2','3',
    '4','5','6','7','8','9',
    '<','>','space_bar','shift','ctrl','alt','tab',
]

if os.path.exists("i_dependencies.bat"):
    os.remove("i_dependencies.bat")

a = False
Perso_Key_To_Press = ''
Selected_Mode = ''
Response_KP_YN = ''
Random_Rep = ''
SpeedMode_Rdm = ''
Entered_Value_Hold_Down_Delay = False
Entered_Value_Click_Delay = False
show = True
savefile = True
SavedFileProfile = False

system('cls')
system('title AUTO-CLICKER 1.4.9 - [ ! Cuchi\'#1632 ]')

def profile_settings_print():
    global SavedFileProfile
    SavedFileProfile = True
    print(Fore.CYAN + 'Chargement de votre profile :')
    print(' ')
    print(Fore.BLUE + '--> ":" : Quitter l\'auto-clicker')
    print(Fore.BLUE + '--> "'+profile_data["Key"]+'" : Cliquer')
    print(' ')
    print(Fore.YELLOW + 'Astuce : Vous souhaitez changer votre profile ?\nAllez dans ' + Fore.CYAN + 'profile' + Fore.YELLOW + ' et supprimez ' + Fore.CYAN + 'profile.json')

if not os.path.exists('profile\\profile.json'):

    gui = Tk()

    def selectedmode():
        global gui
        global Selected_Mode
        global Perso_Key_To_Press
        if var1.get() == 1:
            print('Vous avez séléctionné [', Fore.GREEN + 'Clique Gauche' + Fore.WHITE, ']')
            Selected_Mode = 'CG'
            gui.destroy()
        elif var2.get() == 1:
            print("Vous avez séléctionné [", Fore.GREEN + "Clique Droit" + Fore.WHITE, "]")
            Selected_Mode = 'CD'
            gui.destroy()
        elif var3.get() == 1:
            print("Vous avez séléctionné [", Fore.GREEN + "Touche Personnalisée" + "]")
            Selected_Mode = 'TP'
            Gui_Key_To_Press = pyautogui.prompt('Séléction de la touche à cliquer\n> Lire l\'aide pour voir les touches disponibles', 'Configuration')
            if Gui_Key_To_Press in Available_Key_List:
                Perso_Key_To_Press = Gui_Key_To_Press
                gui.destroy()
            else:
                pyautogui.alert('La touche entrée n\'est pas disponible.', 'Erreur !', 'Recommencer')
                exit()
        else:
            print('Erreur')
            time.sleep(5)
            exit()

    gui.title("Configuration")
    gui.iconbitmap("imgs\\gear.ico")
    gui.configure(bg='#76C2AF')
    Label(gui, text="Que souhaitez-vous utiliser : ", bg='#76C2AF', font='BOLD').grid(row=0)
    var1 = IntVar()
    Checkbutton(gui, text="Clique Gauche", variable=var1, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
    var2 = IntVar()
    Checkbutton(gui, text="Clique Droit", variable=var2, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=2, sticky=W)
    var3 = IntVar()
    Checkbutton(gui, text="Touche Perso.", variable=var3, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=3, sticky=W)
    Button(gui, text='Valider', command=selectedmode, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=4, pady=4)
    gui.mainloop()

    if Selected_Mode == '':
        print(Fore.RED + 'Vous n\'avez rien séléctionné')
        time.sleep(5)
        exit()

    Entered_Value_Clicking_Key = pyautogui.prompt('Touche pour cliquer\n> Lire l\'aide pour voir les touches disponibles', 'Configuration')
    if Entered_Value_Clicking_Key in Available_Key_List:
        Key_To_Click = Entered_Value_Clicking_Key
    else:
        pyautogui.alert('La touche entrée n\'est pas disponible.', 'Erreur !', 'Recommencer')
        exit()

    print(' ')
    print(Fore.BLUE + '--> ":" : Quitter l\'auto-clicker')
    print(Fore.BLUE + '--> "'+Key_To_Click+'" : Cliquer')

    rdmgui = Tk()

    def rdm_ch():
        global rdmgui
        global Random_Rep
        if rep.get() == 1:
            print(' ')
            print(Fore.GREEN + "Vous avez activé le mode de délai aléatoire")
            Random_Rep = "Active"
            rdmgui.destroy()
        else:
            print(' ')
            print(Fore.GREEN + "Vous n'avez pas activé le mode de délai aléatoire")
            Random_Rep = "Inactive"
            rdmgui.destroy()

    def open_dem():
        img = Image.open('imgs\\demo_rdm_cps.jpg')
        img.show()

    rdmgui.title("Mode Aléatoire")
    rdmgui.configure(bg='#76C2AF')
    Label(rdmgui, text="Souhaitez-vous un délai aléatoire entre chaque clique ?", bg='#76C2AF').grid(row=0, sticky=W)
    rep = IntVar()
    Checkbutton(rdmgui, text="Oui", variable=rep, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
    Button(rdmgui, text='Voir la démo', command=open_dem, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='1', width='10', 	bd='5', relief=RIDGE).grid(row=2, pady=4)
    Button(rdmgui, text='TERMINER', command=rdm_ch, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=4, pady=4)
    rdmgui.mainloop()

    if Random_Rep == '':
        print(Fore.RED + 'Vous n\'avez rien séléctionné')
        time.sleep(5)
        exit()

    if Random_Rep == 'Active':
        moderdm = Tk()

        def rdm_ch():
            global moderdm
            global SpeedMode_Rdm
            if rep.get() == 1:
                print('Vous avez séléctionné le mode faible')
                SpeedMode_Rdm = 'Faible'
                moderdm.destroy()
            elif rep2.get() == 1:
                print('Vous avez séléctionné le mode normal')
                SpeedMode_Rdm = 'Normal'
                moderdm.destroy()
            elif rep3.get() == 1:
                print('Vous avez séléctionné le mode rapide')
                SpeedMode_Rdm = 'Rapide'
                moderdm.destroy()
            elif rep4.get() == 1:
                print('Vous avez séléctionné le mode très rapide')
                SpeedMode_Rdm = 'Very_Rapide'
                moderdm.destroy()
            elif rep5.get() == 1:
                print('Vous avez séléctionné le mode inhumain')
                SpeedMode_Rdm = 'Insane_Mode'
                moderdm.destroy()
            else:
                print(Fore.RED + 'Vous n\'avez rien séléctionné')
                time.sleep(2)
                exit()

        moderdm.title("Mode de délai")
        moderdm.configure(bg='#76C2AF')
        Label(moderdm, text="Séléctionnez le type de délai aléatoire :", bg='#76C2AF').grid(row=0, sticky=W)
        rep = IntVar()
        Checkbutton(moderdm, text="Faible", variable=rep, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
        rep2 = IntVar()
        Checkbutton(moderdm, text="Normal", variable=rep2, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=2, sticky=W)
        rep3 = IntVar()
        Checkbutton(moderdm, text="Rapide", variable=rep3, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=3, sticky=W)
        rep4 = IntVar()
        Checkbutton(moderdm, text="Très Rapide", variable=rep4, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=4, sticky=W)
        rep5 = IntVar()
        Checkbutton(moderdm, text="Inhumain", variable=rep5, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=5, sticky=W)
        Button(moderdm, text='TERMINER', command=rdm_ch, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=6, pady=4)
        moderdm.mainloop()

    if Random_Rep == 'Inactive':
        Gui_Value_Click_Delay = pyautogui.prompt('Temps entre chaque clique :\nExemple : 0.5 sera égal à 2 cliques par seconde', 'Configuration')
        Entered_Value_Click_Delay = float(Gui_Value_Click_Delay)
        if Entered_Value_Click_Delay < 0:
            pyautogui.alert('La valeur entrée doit être supérieure à 0 !', 'Erreur !', 'Recommencer')
            exit()
        print(' ')
        print('Vous avez entré', Entered_Value_Click_Delay)

        Entered_Value_Hold_Down_Delay_Prompt = pyautogui.prompt('Contournement (utile pour les jeux qui nécessites un délai entre chaque clique) :\nPour 0.5, le clique sera enfoncé 0.5s\n> Je conseil de mettre au minimum 0.02', 'Configuration')
        Entered_Value_Hold_Down_Delay = float(Entered_Value_Hold_Down_Delay_Prompt)
        if Entered_Value_Hold_Down_Delay < 0:
            pyautogui.alert('La valeur entrée doit être supérieure à 0 !', 'Erreur !', 'Recommencer')
            exit()
        print('Vous avez entré', Entered_Value_Hold_Down_Delay)

        CalculOfCps = Entered_Value_Click_Delay + Entered_Value_Hold_Down_Delay
        print(' ')
        print('Vous effectuerez un clique toutes les', CalculOfCps, 'secondes')

    secgui = Tk()

    def gui_kp_yn():
        global secgui
        global Response_KP_YN
        if resp1.get() == 1:
            print("Vous avez séléctionné lorsque la touche est pressée, auto-click toujours actif.")
            Response_KP_YN = "Always_Active"
            secgui.destroy()
        else:
            print("Vous avez séléctionné lorsque la touche est pressée : auto-click, relachée : stoppé.")
            Response_KP_YN = "On_Key_Active"
            secgui.destroy()

    secgui.title("Mode d'auto-click")
    secgui.configure(bg='#76C2AF')
    Label(secgui, text="Souhaitez-vous que l'auto-click s'active uniquement lorsque\nque la touche est pressée ou alors appuyer une\nseule fois pour qu'il reste activé ?", bg='#76C2AF').grid(row=0, sticky=W)
    resp1 = IntVar()
    Checkbutton(secgui, text="Une seule fois", variable=resp1, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
    Button(secgui, text='TERMINER', command=gui_kp_yn, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=4, pady=4)
    secgui.mainloop()

    print(' ')
    print('Statut :', Fore.GREEN + 'ON')

    if Response_KP_YN == '':
        print(Fore.RED + 'Vous n\'avez rien séléctionné')
        time.sleep(5)
        exit()

    if Response_KP_YN == 'Always_Active':
        pyautogui.alert('Attention, dans ce mode il faudra appuyer plusieurs fois sur / ou : pour fermer le programme !', 'Disclaimer', 'Compris !')

    guisave = Tk()

    if not os.path.exists('profile\\profile.json'):
        profile = { 
            "Show": True,
            "Type" : "", 
            "Key": "",
            "Random_Delay": "",
            "Random_Mode": "",
            "Delay_Down": "",
            "Delay_Up": "",
            "OnActiveKey": "",
        } 

        json_object = json.dumps(profile, indent = 2) 

        with open("profile\\profile.json", "w") as outfile:
            outfile.write(json_object)
        time.sleep(0.25)
        with open('profile\\profile.json') as profile_file:
            profile_data = json.load(profile_file)
    else:
        with open('profile\\profile.json') as profile_file:
            profile_data = json.load(profile_file)

    if profile_data["Show"] == True:
        def response_for_save():
            global guisave
            global savefile
            global Response_KP_YN
            global show
            if save.get() == 1:
                if show.get() == 1:
                    show = False
                    savefile = True
                    save_config()
                    guisave.destroy()
                else:
                    show = True
                    savefile = True
                    save_config()
                    guisave.destroy()
            elif show.get() == 1:
                show = False
                savefile = False
                save_config()
                guisave.destroy()
            else:
                guisave.destroy

        def save_config():
            global savefile
            global show
            global Selected_Mode
            if savefile == True:
                profile = { 
                    "Show": show,
                    "Type" : Selected_Mode, 
                    "Key": Key_To_Click,
                    "To_Press": Perso_Key_To_Press,
                    "Random_Delay": Random_Rep,
                    "Random_Mode": SpeedMode_Rdm,
                    "Delay_Down": Entered_Value_Click_Delay,
                    "Delay_Up": Entered_Value_Hold_Down_Delay,
                    "OnActiveKey": Response_KP_YN
                } 
            elif savefile == False:
                profile = {
                    "Show": show
                }

            json_object = json.dumps(profile, indent = 2) 

            with open("profile\\profile.json", "w") as outfile: 
                outfile.write(json_object)
            print(' ')
            print(Fore.GREEN + "Configuration sauvegardée.")

        guisave.title("Sauvegarde")
        guisave.configure(bg='#76C2AF')
        Label(guisave, text="Souhaitez-vous sauvegarder votre profile ?", bg='#76C2AF').grid(row=0, sticky=W)
        save = IntVar()
        Checkbutton(guisave, text="Oui", variable=save, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
        show = IntVar()
        Checkbutton(guisave, text="Ne plus montrer après", variable=show, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=2, sticky=W)
        Button(guisave, text='Valider', command=response_for_save, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=4, pady=4)
        guisave.mainloop()
elif os.path.exists('profile\\profile.json'):
    with open('profile\\profile.json') as profile_file:
        profile_data = json.load(profile_file)
        if profile_data["Show"] == True:
            if not profile_data["Type"]:
                gui = Tk()

                def selectedmode():
                    global gui
                    global Selected_Mode
                    global Perso_Key_To_Press
                    if var1.get() == 1:
                        print('Vous avez séléctionné [', Fore.GREEN + 'Clique Gauche' + Fore.WHITE, ']')
                        Selected_Mode = 'CG'
                        gui.destroy()
                    elif var2.get() == 1:
                        print("Vous avez séléctionné [", Fore.GREEN + "Clique Droit" + Fore.WHITE, "]")
                        Selected_Mode = 'CD'
                        gui.destroy()
                    elif var3.get() == 1:
                        print("Vous avez séléctionné [", Fore.GREEN + "Touche Personnalisée" + "]")
                        Selected_Mode = 'TP'
                        Gui_Key_To_Press = pyautogui.prompt('Séléction de la touche à cliquer\n> Lire l\'aide pour voir les touches disponibles', 'Configuration')
                        if Gui_Key_To_Press in Available_Key_List:
                            Perso_Key_To_Press = Gui_Key_To_Press
                            gui.destroy()
                        else:
                            pyautogui.alert('La touche entrée n\'est pas disponible.', 'Erreur !', 'Recommencer')
                            exit()
                    else:
                        print('Erreur')
                        time.sleep(5)
                        exit()

                gui.title("Configuration")
                gui.iconbitmap("imgs\\gear.ico")
                gui.configure(bg='#76C2AF')
                Label(gui, text="Que souhaitez-vous utiliser : ", bg='#76C2AF', font='BOLD').grid(row=0)
                var1 = IntVar()
                Checkbutton(gui, text="Clique Gauche", variable=var1, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
                var2 = IntVar()
                Checkbutton(gui, text="Clique Droit", variable=var2, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=2, sticky=W)
                var3 = IntVar()
                Checkbutton(gui, text="Touche Perso.", variable=var3, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=3, sticky=W)
                Button(gui, text='Valider', command=selectedmode, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=4, pady=4)
                gui.mainloop()

                if Selected_Mode == '':
                    print(Fore.RED + 'Vous n\'avez rien séléctionné')
                    time.sleep(5)
                    exit()

                Entered_Value_Clicking_Key = pyautogui.prompt('Touche pour cliquer\n> Lire l\'aide pour voir les touches disponibles', 'Configuration')
                if Entered_Value_Clicking_Key in Available_Key_List:
                    Key_To_Click = Entered_Value_Clicking_Key
                else:
                    pyautogui.alert('La touche entrée n\'est pas disponible.', 'Erreur !', 'Recommencer')
                    exit()

                print(' ')
                print(Fore.BLUE + '--> ":" : Quitter l\'auto-clicker')
                print(Fore.BLUE + '--> "'+Key_To_Click+'" : Cliquer')

                rdmgui = Tk()

                def rdm_ch():
                    global rdmgui
                    global Random_Rep
                    if rep.get() == 1:
                        print(' ')
                        print(Fore.GREEN + "Vous avez activé le mode de délai aléatoire")
                        Random_Rep = "Active"
                        rdmgui.destroy()
                    else:
                        print(' ')
                        print(Fore.GREEN + "Vous n'avez pas activé le mode de délai aléatoire")
                        Random_Rep = "Inactive"
                        rdmgui.destroy()

                def open_dem():
                    img = Image.open('imgs\\demo_rdm_cps.jpg')
                    img.show()

                rdmgui.title("Mode Aléatoire")
                rdmgui.configure(bg='#76C2AF')
                Label(rdmgui, text="Souhaitez-vous un délai aléatoire entre chaque clique ?", bg='#76C2AF').grid(row=0, sticky=W)
                rep = IntVar()
                Checkbutton(rdmgui, text="Oui", variable=rep, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
                Button(rdmgui, text='Voir la démo', command=open_dem, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='1', width='10', 	bd='5', relief=RIDGE).grid(row=2, pady=4)
                Button(rdmgui, text='TERMINER', command=rdm_ch, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=4, pady=4)
                rdmgui.mainloop()

                if Random_Rep == '':
                    print(Fore.RED + 'Vous n\'avez rien séléctionné')
                    time.sleep(5)
                    exit()

                if Random_Rep == 'Active':
                    moderdm = Tk()

                    def rdm_ch():
                        global moderdm
                        global SpeedMode_Rdm
                        if rep.get() == 1:
                            print('Vous avez séléctionné le mode faible')
                            SpeedMode_Rdm = 'Faible'
                            moderdm.destroy()
                        elif rep2.get() == 1:
                            print('Vous avez séléctionné le mode normal')
                            SpeedMode_Rdm = 'Normal'
                            moderdm.destroy()
                        elif rep3.get() == 1:
                            print('Vous avez séléctionné le mode rapide')
                            SpeedMode_Rdm = 'Rapide'
                            moderdm.destroy()
                        elif rep4.get() == 1:
                            print('Vous avez séléctionné le mode très rapide')
                            SpeedMode_Rdm = 'Very_Rapide'
                            moderdm.destroy()
                        elif rep5.get() == 1:
                            print('Vous avez séléctionné le mode inhumain')
                            SpeedMode_Rdm = 'Insane_Mode'
                            moderdm.destroy()
                        else:
                            print(Fore.RED + 'Vous n\'avez rien séléctionné')
                            time.sleep(2)
                            exit()

                    moderdm.title("Mode de délai")
                    moderdm.configure(bg='#76C2AF')
                    Label(moderdm, text="Séléctionnez le type de délai aléatoire :", bg='#76C2AF').grid(row=0, sticky=W)
                    rep = IntVar()
                    Checkbutton(moderdm, text="Faible", variable=rep, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
                    rep2 = IntVar()
                    Checkbutton(moderdm, text="Normal", variable=rep2, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=2, sticky=W)
                    rep3 = IntVar()
                    Checkbutton(moderdm, text="Rapide", variable=rep3, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=3, sticky=W)
                    rep4 = IntVar()
                    Checkbutton(moderdm, text="Très Rapide", variable=rep4, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=4, sticky=W)
                    rep5 = IntVar()
                    Checkbutton(moderdm, text="Inhumain", variable=rep5, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=5, sticky=W)
                    Button(moderdm, text='TERMINER', command=rdm_ch, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=6, pady=4)
                    moderdm.mainloop()

                if Random_Rep == 'Inactive':
                    Gui_Value_Click_Delay = pyautogui.prompt('Temps entre chaque clique :\nExemple : 0.5 sera égal à 2 cliques par seconde', 'Configuration')
                    Entered_Value_Click_Delay = float(Gui_Value_Click_Delay)
                    if Entered_Value_Click_Delay < 0:
                        pyautogui.alert('La valeur entrée doit être supérieure à 0 !', 'Erreur !', 'Recommencer')
                        exit()
                    print(' ')
                    print('Vous avez entré', Entered_Value_Click_Delay)

                    Entered_Value_Hold_Down_Delay_Prompt = pyautogui.prompt('Contournement (utile pour les jeux qui nécessites un délai entre chaque clique) :\nPour 0.5, le clique sera enfoncé 0.5s\n> Je conseil de mettre au minimum 0.02', 'Configuration')
                    Entered_Value_Hold_Down_Delay = float(Entered_Value_Hold_Down_Delay_Prompt)
                    if Entered_Value_Hold_Down_Delay < 0:
                        pyautogui.alert('La valeur entrée doit être supérieure à 0 !', 'Erreur !', 'Recommencer')
                        exit()
                    print('Vous avez entré', Entered_Value_Hold_Down_Delay)

                    CalculOfCps = Entered_Value_Click_Delay + Entered_Value_Hold_Down_Delay
                    print(' ')
                    print('Vous effectuerez un clique toutes les', CalculOfCps, 'secondes')

                secgui = Tk()

                def gui_kp_yn():
                    global secgui
                    global Response_KP_YN
                    if resp1.get() == 1:
                        print("Vous avez séléctionné lorsque la touche est pressée, auto-click toujours actif.")
                        Response_KP_YN = "Always_Active"
                        secgui.destroy()
                    else:
                        print("Vous avez séléctionné lorsque la touche est pressée : auto-click, relachée : stoppé.")
                        Response_KP_YN = "On_Key_Active"
                        secgui.destroy()

                secgui.title("Mode d'auto-click")
                secgui.configure(bg='#76C2AF')
                Label(secgui, text="Souhaitez-vous que l'auto-click s'active uniquement lorsque\nque la touche est pressée ou alors appuyer une\nseule fois pour qu'il reste activé ?", bg='#76C2AF').grid(row=0, sticky=W)
                resp1 = IntVar()
                Checkbutton(secgui, text="Une seule fois", variable=resp1, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
                Button(secgui, text='TERMINER', command=gui_kp_yn, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=4, pady=4)
                secgui.mainloop()

                print(' ')
                print('Statut :', Fore.GREEN + 'ON')

                if Response_KP_YN == '':
                    print(Fore.RED + 'Vous n\'avez rien séléctionné')
                    time.sleep(5)
                    exit()

                if Response_KP_YN == 'Always_Active':
                    pyautogui.alert('Attention, dans ce mode il faudra appuyer plusieurs fois sur / ou : pour fermer le programme !', 'Disclaimer', 'Compris !')

                guisave = Tk()

                if not os.path.exists('profile\\profile.json'):
                    profile = { 
                        "Show": True,
                        "Type" : "", 
                        "Key": "",
                        "Random_Delay": "",
                        "Random_Mode": "",
                        "Delay_Down": "",
                        "Delay_Up": "",
                        "OnActiveKey": "",
                    } 

                    json_object = json.dumps(profile, indent = 2) 

                    with open("profile\\profile.json", "w") as outfile:
                        outfile.write(json_object)
                    time.sleep(0.25)
                    with open('profile\\profile.json') as profile_file:
                        profile_data = json.load(profile_file)
                else:
                    with open('profile\\profile.json') as profile_file:
                        profile_data = json.load(profile_file)

                if profile_data["Show"] == True:
                    def response_for_save():
                        global guisave
                        global savefile
                        global Response_KP_YN
                        global show
                        if save.get() == 1:
                            if show.get() == 1:
                                show = False
                                savefile = True
                                save_config()
                                guisave.destroy()
                            else:
                                show = True
                                savefile = True
                                save_config()
                                guisave.destroy()
                        elif show.get() == 1:
                            show = False
                            savefile = False
                            save_config()
                            guisave.destroy()
                        else:
                            guisave.destroy

                    def save_config():
                        global savefile
                        global show
                        global Selected_Mode
                        if savefile == True:
                            profile = { 
                                "Show": show,
                                "Type" : Selected_Mode, 
                                "Key": Key_To_Click,
                                "To_Press": Perso_Key_To_Press,
                                "Random_Delay": Random_Rep,
                                "Random_Mode": SpeedMode_Rdm,
                                "Delay_Down": Entered_Value_Click_Delay,
                                "Delay_Up": Entered_Value_Hold_Down_Delay,
                                "OnActiveKey": Response_KP_YN
                            } 
                        elif savefile == False:
                            profile = {
                                "Show": show
                            }

                        json_object = json.dumps(profile, indent = 2) 

                        with open("profile\\profile.json", "w") as outfile: 
                            outfile.write(json_object)
                        print(' ')
                        print(Fore.GREEN + "Configuration sauvegardée.")

                    guisave.title("Sauvegarde")
                    guisave.configure(bg='#76C2AF')
                    Label(guisave, text="Souhaitez-vous sauvegarder votre profile ?", bg='#76C2AF').grid(row=0, sticky=W)
                    save = IntVar()
                    Checkbutton(guisave, text="Oui", variable=save, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
                    show = IntVar()
                    Checkbutton(guisave, text="Ne plus montrer après", variable=show, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=2, sticky=W)
                    Button(guisave, text='Valider', command=response_for_save, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=4, pady=4)
                    guisave.mainloop()
                else:
                    SavedFileProfile = 'Yes'
        elif profile_data["Show"] == False:
            if "Type" not in profile_data:
                gui = Tk()

                def selectedmode():
                    global gui
                    global Selected_Mode
                    global Perso_Key_To_Press
                    if var1.get() == 1:
                        print('Vous avez séléctionné [', Fore.GREEN + 'Clique Gauche' + Fore.WHITE, ']')
                        Selected_Mode = 'CG'
                        gui.destroy()
                    elif var2.get() == 1:
                        print("Vous avez séléctionné [", Fore.GREEN + "Clique Droit" + Fore.WHITE, "]")
                        Selected_Mode = 'CD'
                        gui.destroy()
                    elif var3.get() == 1:
                        print("Vous avez séléctionné [", Fore.GREEN + "Touche Personnalisée" + "]")
                        Selected_Mode = 'TP'
                        Gui_Key_To_Press = pyautogui.prompt('Séléction de la touche à cliquer\n> Lire l\'aide pour voir les touches disponibles', 'Configuration')
                        if Gui_Key_To_Press in Available_Key_List:
                            Perso_Key_To_Press = Gui_Key_To_Press
                            gui.destroy()
                        else:
                            pyautogui.alert('La touche entrée n\'est pas disponible.', 'Erreur !', 'Recommencer')
                            exit()
                    else:
                        print('Erreur')
                        time.sleep(5)
                        exit()

                gui.title("Configuration")
                gui.iconbitmap("imgs\\gear.ico")
                gui.configure(bg='#76C2AF')
                Label(gui, text="Que souhaitez-vous utiliser : ", bg='#76C2AF', font='BOLD').grid(row=0)
                var1 = IntVar()
                Checkbutton(gui, text="Clique Gauche", variable=var1, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
                var2 = IntVar()
                Checkbutton(gui, text="Clique Droit", variable=var2, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=2, sticky=W)
                var3 = IntVar()
                Checkbutton(gui, text="Touche Perso.", variable=var3, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=3, sticky=W)
                Button(gui, text='Valider', command=selectedmode, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=4, pady=4)
                gui.mainloop()

                if Selected_Mode == '':
                    print(Fore.RED + 'Vous n\'avez rien séléctionné')
                    time.sleep(5)
                    exit()

                Entered_Value_Clicking_Key = pyautogui.prompt('Touche pour cliquer\n> Lire l\'aide pour voir les touches disponibles', 'Configuration')
                if Entered_Value_Clicking_Key in Available_Key_List:
                    Key_To_Click = Entered_Value_Clicking_Key
                else:
                    pyautogui.alert('La touche entrée n\'est pas disponible.', 'Erreur !', 'Recommencer')
                    exit()

                print(' ')
                print(Fore.BLUE + '--> ":" : Quitter l\'auto-clicker')
                print(Fore.BLUE + '--> "'+Key_To_Click+'" : Cliquer')

                rdmgui = Tk()

                def rdm_ch():
                    global rdmgui
                    global Random_Rep
                    if rep.get() == 1:
                        print(' ')
                        print(Fore.GREEN + "Vous avez activé le mode de délai aléatoire")
                        Random_Rep = "Active"
                        rdmgui.destroy()
                    else:
                        print(' ')
                        print(Fore.GREEN + "Vous n'avez pas activé le mode de délai aléatoire")
                        Random_Rep = "Inactive"
                        rdmgui.destroy()

                def open_dem():
                    img = Image.open('imgs\\demo_rdm_cps.jpg')
                    img.show()

                rdmgui.title("Mode Aléatoire")
                rdmgui.configure(bg='#76C2AF')
                Label(rdmgui, text="Souhaitez-vous un délai aléatoire entre chaque clique ?", bg='#76C2AF').grid(row=0, sticky=W)
                rep = IntVar()
                Checkbutton(rdmgui, text="Oui", variable=rep, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
                Button(rdmgui, text='Voir la démo', command=open_dem, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='1', width='10', 	bd='5', relief=RIDGE).grid(row=2, pady=4)
                Button(rdmgui, text='TERMINER', command=rdm_ch, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=4, pady=4)
                rdmgui.mainloop()

                if Random_Rep == '':
                    print(Fore.RED + 'Vous n\'avez rien séléctionné')
                    time.sleep(5)
                    exit()

                if Random_Rep == 'Active':
                    moderdm = Tk()

                    def rdm_ch():
                        global moderdm
                        global SpeedMode_Rdm
                        if rep.get() == 1:
                            print('Vous avez séléctionné le mode faible')
                            SpeedMode_Rdm = 'Faible'
                            moderdm.destroy()
                        elif rep2.get() == 1:
                            print('Vous avez séléctionné le mode normal')
                            SpeedMode_Rdm = 'Normal'
                            moderdm.destroy()
                        elif rep3.get() == 1:
                            print('Vous avez séléctionné le mode rapide')
                            SpeedMode_Rdm = 'Rapide'
                            moderdm.destroy()
                        elif rep4.get() == 1:
                            print('Vous avez séléctionné le mode très rapide')
                            SpeedMode_Rdm = 'Very_Rapide'
                            moderdm.destroy()
                        elif rep5.get() == 1:
                            print('Vous avez séléctionné le mode inhumain')
                            SpeedMode_Rdm = 'Insane_Mode'
                            moderdm.destroy()
                        else:
                            print(Fore.RED + 'Vous n\'avez rien séléctionné')
                            time.sleep(2)
                            exit()

                    moderdm.title("Mode de délai")
                    moderdm.configure(bg='#76C2AF')
                    Label(moderdm, text="Séléctionnez le type de délai aléatoire :", bg='#76C2AF').grid(row=0, sticky=W)
                    rep = IntVar()
                    Checkbutton(moderdm, text="Faible", variable=rep, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
                    rep2 = IntVar()
                    Checkbutton(moderdm, text="Normal", variable=rep2, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=2, sticky=W)
                    rep3 = IntVar()
                    Checkbutton(moderdm, text="Rapide", variable=rep3, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=3, sticky=W)
                    rep4 = IntVar()
                    Checkbutton(moderdm, text="Très Rapide", variable=rep4, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=4, sticky=W)
                    rep5 = IntVar()
                    Checkbutton(moderdm, text="Inhumain", variable=rep5, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=5, sticky=W)
                    Button(moderdm, text='TERMINER', command=rdm_ch, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=6, pady=4)
                    moderdm.mainloop()

                if Random_Rep == 'Inactive':
                    Gui_Value_Click_Delay = pyautogui.prompt('Temps entre chaque clique :\nExemple : 0.5 sera égal à 2 cliques par seconde', 'Configuration')
                    Entered_Value_Click_Delay = float(Gui_Value_Click_Delay)
                    if Entered_Value_Click_Delay < 0:
                        pyautogui.alert('La valeur entrée doit être supérieure à 0 !', 'Erreur !', 'Recommencer')
                        exit()
                    print(' ')
                    print('Vous avez entré', Entered_Value_Click_Delay)

                    Entered_Value_Hold_Down_Delay_Prompt = pyautogui.prompt('Contournement (utile pour les jeux qui nécessites un délai entre chaque clique) :\nPour 0.5, le clique sera enfoncé 0.5s\n> Je conseil de mettre au minimum 0.02', 'Configuration')
                    Entered_Value_Hold_Down_Delay = float(Entered_Value_Hold_Down_Delay_Prompt)
                    if Entered_Value_Hold_Down_Delay < 0:
                        pyautogui.alert('La valeur entrée doit être supérieure à 0 !', 'Erreur !', 'Recommencer')
                        exit()
                    print('Vous avez entré', Entered_Value_Hold_Down_Delay)

                    CalculOfCps = Entered_Value_Click_Delay + Entered_Value_Hold_Down_Delay
                    print(' ')
                    print('Vous effectuerez un clique toutes les', CalculOfCps, 'secondes')

                secgui = Tk()

                def gui_kp_yn():
                    global secgui
                    global Response_KP_YN
                    if resp1.get() == 1:
                        print("Vous avez séléctionné lorsque la touche est pressée, auto-click toujours actif.")
                        Response_KP_YN = "Always_Active"
                        secgui.destroy()
                    else:
                        print("Vous avez séléctionné lorsque la touche est pressée : auto-click, relachée : stoppé.")
                        Response_KP_YN = "On_Key_Active"
                        secgui.destroy()

                secgui.title("Mode d'auto-click")
                secgui.configure(bg='#76C2AF')
                Label(secgui, text="Souhaitez-vous que l'auto-click s'active uniquement lorsque\nque la touche est pressée ou alors appuyer une\nseule fois pour qu'il reste activé ?", bg='#76C2AF').grid(row=0, sticky=W)
                resp1 = IntVar()
                Checkbutton(secgui, text="Une seule fois", variable=resp1, bg='#76C2AF', activebackground='#76C2AF', font='ITALIC').grid(row=1, sticky=W)
                Button(secgui, text='TERMINER', command=gui_kp_yn, bg='#609E8F', activebackground='#609E8F', font='ITALIC', height='2', width='15', 	bd='5', relief=RIDGE).grid(row=4, pady=4)
                secgui.mainloop()

                print(' ')
                print('Statut :', Fore.GREEN + 'ON')

                if Response_KP_YN == '':
                    print(Fore.RED + 'Vous n\'avez rien séléctionné')
                    time.sleep(5)
                    exit()

                if Response_KP_YN == 'Always_Active':
                    pyautogui.alert('Attention, dans ce mode il faudra appuyer plusieurs fois sur / ou : pour fermer le programme !', 'Disclaimer', 'Compris !')

                guisave = Tk()

                if not os.path.exists('profile\\profile.json'):
                    profile = { 
                        "Show": True,
                        "Type" : "", 
                        "Key": "",
                        "Random_Delay": "",
                        "Random_Mode": "",
                        "Delay_Down": "",
                        "Delay_Up": "",
                        "OnActiveKey": "",
                    } 

                    json_object = json.dumps(profile, indent = 2) 

                    with open("profile\\profile.json", "w") as outfile:
                        outfile.write(json_object)
                    time.sleep(0.25)
                    with open('profile\\profile.json') as profile_file:
                        profile_data = json.load(profile_file)
                else:
                    with open('profile\\profile.json') as profile_file:
                        profile_data = json.load(profile_file)
            else:
                profile_settings_print()
        else:
            profile_settings_print()

while keyboard.is_pressed('/') == False:
    if SavedFileProfile == True:

        if profile_data["Random_Delay"] == 'Active':
            if profile_data["Random_Mode"] == 'Faible': # +/- 5cps
                Random_Gen_Delay = random.randint(2, 200) / 1000
            elif profile_data["Random_Mode"] == 'Normal': # +/- 9cps / 10
                Random_Gen_Delay = random.randint(2, 200) / 2000
            elif profile_data["Random_Mode"] == 'Rapide': # +/- 13cps
                Random_Gen_Delay = random.randint(2, 200) / 3000
            elif profile_data["Random_Mode"] == 'Very_Rapide': # +/- 17cps
                Random_Gen_Delay = random.randint(2, 200) / 4000
            elif profile_data["Random_Mode"] == 'Insane_Mode': # +/- 30cps
                Random_Gen_Delay = random.randint(2, 200) / 7000
            if a:
                print(Random_Gen_Delay)

        Mouse_Pos_X = pyautogui.position().x
        Mouse_Pos_Y = pyautogui.position().y

        if a:
            if(Mouse_Pos_X != pyautogui.position().x):
                if(Mouse_Pos_Y != pyautogui.position().y):
                    print(pyautogui.position().x, pyautogui.position().y)

        if profile_data["OnActiveKey"] == 'On_Key_Active':
            if keyboard.is_pressed(profile_data["Key"]):
                if profile_data["Type"] == 'TP':
                    if profile_data["Random_Delay"] == 'Inactive':
                        pyautogui.keyDown(profile_data["To_Press"])
                        time.sleep(profile_data["Delay_Up"])
                        pyautogui.keyUp(profile_data["To_Press"])
                        time.sleep(profile_data["Delay_Down"])
                    elif profile_data["Random_Delay"] == 'Active':
                        pyautogui.keyDown(profile_data["To_Press"])
                        time.sleep(Random_Gen_Delay)
                        pyautogui.keyUp(profile_data["To_Press"])
                        time.sleep(Random_Gen_Delay)
                    if a:
                        print(profile_data["To_Press"], 'cliquée')
                elif profile_data["Type"] == 'CG':
                    if profile_data["Random_Delay"] == 'Inactive':
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                        time.sleep(profile_data["Delay_Up"])
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        time.sleep(profile_data["Delay_Down"])
                    elif profile_data["Random_Delay"] == 'Active':
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                        time.sleep(Random_Gen_Delay)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        time.sleep(Random_Gen_Delay)
                elif profile_data["Type"] == 'CD':
                    if profile_data["Random_Delay"] == 'Inactive':
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                        time.sleep(profile_data["Delay_Up"])
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
                        time.sleep(profile_data["Delay_Down"])
                    elif profile_data["Random_Delay"] == 'Active':
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                        time.sleep(Random_Gen_Delay)
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
                        time.sleep(Random_Gen_Delay)
        elif Response_KP_YN == 'Always_Active':
            if keyboard.is_pressed(profile_data["Key"]):
                while keyboard.is_pressed('/') == False:
                    if profile_data["Type"] == 'TP':
                        if profile_data["Random_Delay"] == 'Inactive':
                            pyautogui.keyDown(profile_data["To_Press"])
                            time.sleep(profile_data["Delay_Up"])
                            pyautogui.keyUp(profile_data["To_Press"])
                            time.sleep(profile_data["Delay_Down"])
                        elif profile_data["Random_Delay"] == 'Active':
                            pyautogui.keyDown(profile_data["To_Press"])
                            time.sleep(Random_Gen_Delay)
                            pyautogui.keyUp(profile_data["To_Press"])
                            time.sleep(Random_Gen_Delay)
                        if a:
                            print(profile_data["To_Press"], 'cliquée')
                    elif profile_data["Type"] == 'CG':
                        if profile_data["Random_Delay"] == 'Inactive':
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                            time.sleep(profile_data["Delay_Up"])
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                            time.sleep(profile_data["Delay_Down"])
                        elif profile_data["Random_Delay"] == 'Active':
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                            time.sleep(Random_Gen_Delay)
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                            time.sleep(Random_Gen_Delay)
                    elif profile_data["Type"] == 'CD':
                        if profile_data["Random_Delay"] == 'Inactive':
                            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                            time.sleep(profile_data["Delay_Up"])
                            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
                            time.sleep(profile_data["Delay_Down"])
                        elif profile_data["Random_Delay"] == 'Active':
                            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                            time.sleep(Random_Gen_Delay)
                            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
                            time.sleep(Random_Gen_Delay)
        else:
            print(Fore.RED + 'Erreur inattendue.' + Fore.WHITE + '\nContacter : ! Cuchi\'#1632')
            time.sleep(7)
            exit()

        if keyboard.is_pressed('/') == True:
            system('cls')
            print('Statut :', Fore.RED + 'OFF')

    else:
        if Random_Rep == 'Active':
            if SpeedMode_Rdm == 'Faible': # +/- 5cps
                Random_Gen_Delay = random.randint(2, 200) / 1000
            elif SpeedMode_Rdm == 'Normal': # +/- 9cps / 10
                Random_Gen_Delay = random.randint(2, 200) / 2000
            elif SpeedMode_Rdm == 'Rapide': # +/- 13cps
                Random_Gen_Delay = random.randint(2, 200) / 3000
            elif SpeedMode_Rdm == 'Very_Rapide': # +/- 17cps
                Random_Gen_Delay = random.randint(2, 200) / 4000
            elif SpeedMode_Rdm == 'Insane_Mode': # +/- 30cps
                Random_Gen_Delay = random.randint(2, 200) / 7000
            if a:
                print(Random_Gen_Delay)

        Mouse_Pos_X = pyautogui.position().x
        Mouse_Pos_Y = pyautogui.position().y

        if a:
            if(Mouse_Pos_X != pyautogui.position().x):
                if(Mouse_Pos_Y != pyautogui.position().y):
                    print(pyautogui.position().x, pyautogui.position().y)

        if Response_KP_YN == 'On_Key_Active':
            if keyboard.is_pressed(Key_To_Click):
                if Selected_Mode == 'TP':
                    if Random_Rep == 'Inactive':
                        pyautogui.keyDown(Perso_Key_To_Press)
                        time.sleep(Entered_Value_Hold_Down_Delay)
                        pyautogui.keyUp(Perso_Key_To_Press)
                        time.sleep(Entered_Value_Click_Delay)
                    elif Random_Rep == 'Active':
                        pyautogui.keyDown(Perso_Key_To_Press)
                        time.sleep(Random_Gen_Delay)
                        pyautogui.keyUp(Perso_Key_To_Press)
                        time.sleep(Random_Gen_Delay)
                    if a:
                        print(Perso_Key_To_Press, 'cliquée')
                elif Selected_Mode == 'CG':
                    if Random_Rep == 'Inactive':
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                        time.sleep(Entered_Value_Hold_Down_Delay)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        time.sleep(Entered_Value_Click_Delay)
                    elif Random_Rep == 'Active':
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                        time.sleep(Random_Gen_Delay)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                        time.sleep(Random_Gen_Delay)
                elif Selected_Mode == 'CD':
                    if Random_Rep == 'Inactive':
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                        time.sleep(Entered_Value_Hold_Down_Delay)
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
                        time.sleep(Entered_Value_Click_Delay)
                    elif Random_Rep == 'Active':
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                        time.sleep(Random_Gen_Delay)
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
                        time.sleep(Random_Gen_Delay)
        elif Response_KP_YN == 'Always_Active':
            if keyboard.is_pressed(Key_To_Click):
                while keyboard.is_pressed('/') == False:
                    if Selected_Mode == 'TP':
                        if Random_Rep == 'Inactive':
                            pyautogui.keyDown(Perso_Key_To_Press)
                            time.sleep(Entered_Value_Hold_Down_Delay)
                            pyautogui.keyUp(Perso_Key_To_Press)
                            time.sleep(Entered_Value_Click_Delay)
                        elif Random_Rep == 'Active':
                            pyautogui.keyDown(Perso_Key_To_Press)
                            time.sleep(Random_Gen_Delay)
                            pyautogui.keyUp(Perso_Key_To_Press)
                            time.sleep(Random_Gen_Delay)
                        if a:
                            print(Perso_Key_To_Press, 'cliquée')
                    elif Selected_Mode == 'CG':
                        if Random_Rep == 'Inactive':
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                            time.sleep(Entered_Value_Hold_Down_Delay)
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                            time.sleep(Entered_Value_Click_Delay)
                        elif Random_Rep == 'Active':
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                            time.sleep(Random_Gen_Delay)
                            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                            time.sleep(Random_Gen_Delay)
                    elif Selected_Mode == 'CD':
                        if Random_Rep == 'Inactive':
                            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                            time.sleep(Entered_Value_Hold_Down_Delay)
                            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
                            time.sleep(Entered_Value_Click_Delay)
                        elif Random_Rep == 'Active':
                            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                            time.sleep(Random_Gen_Delay)
                            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
                            time.sleep(Random_Gen_Delay)
        else:
            print(Fore.RED + 'Erreur inattendue.' + Fore.WHITE + '\nContacter : ! Cuchi\'#1632')
            time.sleep(7)
            exit()

        if keyboard.is_pressed('/') == True:
            system('cls')
            print('Statut :', Fore.RED + 'OFF')
