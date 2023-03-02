#IMPORTS
import turtle
from turtle import *
import random
import time
from tkinter import *
from tkinter import messagebox
import os
os.system('cls') #clears output window (fresh start)
#variable definitions
projectname = "Adventure Game by Ollie Ricketts"
default_select = False
incomplete_read = False
characters = 0
c1toolong = False
c2toolong = False
c3toolong = False
c4toolong = False
loadyn = 0
invalid_responses = [None, "", " "]
num_of_characters_to_create = 4
character1_hp = 2
character2_hp = 2
character3_hp = 2
character4_hp = 2
import_success = False
challenge1_fatal = False
challenge2_fatal = False
challenge3_fatal = False
challenge4_fatal = False
challenge5_fatal = False
fatigued_characters = []
game_fail = False
dead_characters = []
#subroutine definitions
def characterRepetition(b, c, d): # this subroutine takes in a character to be repeat printed on one line, a specified amount of times with a pause between
    for a in range(0, b):
        print(c, end="", flush=True)
        time.sleep(d)
        a = a+1
    return ""
def flushprint(a): #this subroutine takes a string to be printed, prints it, but does not drop down to the next line
    print(a, end="", flush=True)
    return ""
def attribute_generation():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    dice4 = random.randint(1,6)
    lowestroll = (min(dice1, dice2, dice3, dice4))
    totalrolled = dice1 + dice2 + dice3 + dice4
    attribute = totalrolled - lowestroll
    return attribute
#PROGRAM START
#opening code
characterRepetition(10, "=", 0.1)
flushprint(" WELCOME")
time.sleep(0.2)
flushprint(" TO")
time.sleep(0.2)
flushprint(" THE")
time.sleep(0.2)
flushprint(" GAME ")
characterRepetition(10, "=", 0.1)
time.sleep(1)
ready = 0
turtle.title(projectname) #setup for turtle dialog boxes
turtle.Screen().setup(10,10)
print("\nThis game uses popup dialog boxes throughout. If minimised, they will continue to wait for prompt and can be maximised from your taskbar.")
ready = messagebox.askquestion(projectname, "Are you ready to play?") #dialog box
while ready != "yes":
    quit()
loadyn = messagebox.askquestion(projectname, "Do you want to load a save file? (pressing no will begin a new game)") #asks user load or new save
if loadyn == "no":
    incomplete_read = False
os.system('cls') #clears the output window
print("========== WELCOME TO THE GAME ==========")
check_for_file = False
if loadyn == "yes":
    dir_path = os.path.join(os.path.dirname(__file__), "saves")
    if os.path.exists(dir_path):
        files = os.listdir(dir_path)
        print("Save files that can be loaded:")
        for i in range(len(files)):
            files[i] = os.path.splitext(files[i])[0]
        for x in range(0, len(files)):
            print(files[x])
            x = x + 1
    savefile = None
    check_for_file = None
    while savefile == None or check_for_file == None or check_for_file == False or savefile == "" or savefile == " " or savefile[0] == " ":
        if check_for_file == False:
            savefile = turtle.textinput("Load game", "Game save file not found. Please retry the game save file name: (or enter 'new' for a new game instead)")
            if savefile != None:
                savefile = savefile.replace(" ", "")
        elif check_for_file == None:
            savefile = turtle.textinput("Load game", "Please enter the game save file name you would like to load: (or enter 'new' for a new game instead)")
            savefile = savefile.replace(" ", "")
        savefile_valid = savefile
        if savefile_valid != None:
            if savefile.lower() == "new":
                loadyn = "no"
                break
            dir_path = os.path.join(os.path.dirname(__file__), "saves")
            file_path = os.path.join(dir_path, savefile)
            if os.path.exists(file_path):
                check_for_file = True
            else:
                check_for_file = False
            if savefile_valid == "" or savefile_valid[0] == " ":
                savefile == None
        if savefile_valid != None:
            if "txt" not in savefile and savefile != None and savefile != "" and savefile != " " and savefile[0] != " ":
                savefile = str(savefile) + ".txt"
                dir_path = os.path.join(os.path.dirname(__file__), "saves")
            file_path = os.path.join(dir_path, savefile)
            if os.path.exists(file_path):
                check_for_file = True
            else:
                check_for_file = False
            if savefile == None or savefile == "" or savefile == " " or savefile[0] == " ":
                savefile = savefile.replace(" ", "")
            if savefile.lower() == "new":
                loadyn = "no"
    if savefile.lower() != "new":
        file_path = os.path.join(dir_path, savefile)
        f = open(file_path, "r") #opens save file for reading
        characters_to_create = []
        end_of_file = False
        incomplete_read = False
        while end_of_file == False:
            character1 = f.readline().strip()
            if character1 == "":
                incomplete_read = True
                characters_to_create.append("character1")
                characters_to_create.append("character2")
                characters_to_create.append("character3")
                characters_to_create.append("character4")
                end_of_file = True
                break
            character1_strength = f.readline().strip()
            character1_agility = f.readline().strip()
            character1_magic = f.readline().strip()
            character1_luck = f.readline().strip()
            character1_hp = f.readline().strip()
            character2 = f.readline().strip()
            if character2 == "":
                incomplete_read = True
                characters_to_create.append("character2")
                characters_to_create.append("character3")
                characters_to_create.append("character4")
                end_of_file = True
                break
            character2_strength = f.readline().strip()
            character2_agility = f.readline().strip()
            character2_magic = f.readline().strip()
            character2_luck = f.readline().strip()
            character2_hp = f.readline().strip()
            character3 = f.readline().strip()
            if character3 == "":
                incomplete_read = True
                characters_to_create.append("character3")
                characters_to_create.append("character4")
                end_of_file = True
                break
            character3_strength = f.readline().strip()
            character3_agility = f.readline().strip()
            character3_magic = f.readline().strip()
            character3_luck = f.readline().strip()
            character3_hp = f.readline().strip()
            character4 = f.readline().strip()
            if character4 == "":
                incomplete_read = True
                characters_to_create.append("character4")
                end_of_file = True
                break
            character4_strength = f.readline().strip()
            character4_agility = f.readline().strip()
            character4_magic = f.readline().strip()
            character4_luck = f.readline().strip()
            character4_hp = f.readline().strip()
            end_of_file = True
            num_of_characters_to_create = 0
            import_success = True
        if incomplete_read == True:
            num_of_characters_to_create = len(characters_to_create)
        if num_of_characters_to_create == 4:
            loadyn = "no"
        elif num_of_characters_to_create == 3:
            loadyn = "no"
        elif num_of_characters_to_create == 2:
            loadyn = "no"
        elif num_of_characters_to_create == 1:
            loadyn = "no"

if loadyn == "no":
    if num_of_characters_to_create == 4:
        savefile = None
        already_exist = False
        while savefile == None or savefile == "" or savefile == " " or savefile[0] == " ":
            if incomplete_read == True:
                savefile = turtle.textinput("New game", "No data in save file you tried to load or all players died. Please enter the name you would like to save this new game as: ")
                savefile = savefile.replace(" ", "")
            if already_exist == True:
                savefile = turtle.textinput("New game", "File already exists. Please enter the name you would like to save this game as: ")
                savefile = savefile.replace(" ", "")
            elif already_exist == False and incomplete_read == False:
                savefile = turtle.textinput("New game", "Please enter the name you would like to save this game as: ")
                if savefile != None:
                    savefile = savefile.replace(" ", "")
            savefile_valid = savefile
            if savefile_valid != None:
                if savefile_valid == "" or savefile_valid[0] == " ":
                    savefile == None
            if savefile_valid != None:
                if "txt" not in savefile and savefile != None and savefile != "" and savefile != " " and savefile[0] != " ":
                    savefile = str(savefile) + ".txt"
                directory_path = os.path.join(os.path.dirname(__file__), "saves")
                file_path1 = os.path.join(directory_path, savefile)
                if os.path.exists(file_path1):
                    already_exist = True
            if already_exist == True:
                savefile = None
        dir_path = os.path.join(os.path.dirname(__file__), "saves")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_path = os.path.join(dir_path, savefile)
        f = open(file_path, "w") #creates the savedata.txt file
    #CHARACTER CREATION
    if num_of_characters_to_create == 4:
        #CHARACTER 1 ---------------------------------------------------------------------------------------------------------------------
        character1 = None #CHARACTER 1
        while character1 == None: #ensures that character name cannot have no value, OR begin with a space etc.
            character1 = turtle.textinput("Create character 1", "Enter the name of your first character: ")
            c1length = len(character1)
            if c1length > 15:
                c1toolong = True
            while c1toolong == True:
                character1 = turtle.textinput("Create character 1", "Character must have a name 15 characters or less. Enter the name of your first character: ")
                c1length = len(character1)
                if c1length > 15:
                    c1toolong = True
                else:
                    c1toolong = False
            character1_valid = character1
            if character1_valid != None:
                if character1_valid == "" or character1_valid[0] == " ":
                    character1 = None
        attribute1 = attribute_generation() #generates attributes
        attribute2 = attribute_generation()
        attribute3 = attribute_generation()
        attribute4 = attribute_generation()
        lowestattribute = min(attribute1, attribute2, attribute3, attribute4) #works out the lowest attribute generated
        #assembles a message to be printed and shown in a dialog box
        attributesmessage = "The following numbers have been rolled for" + " " + str(character1) + " " + "and you will need to choose which value you want to assign to each attribute (Strength, Agility, Magic & Luck):" + "\n" + "\n" + str(attribute1) + " " + str(attribute2) + " " + str(attribute3)+ " " + str(attribute4)
        print(attributesmessage)
        messagebox.showinfo(projectname, attributesmessage)
        rerollmessage = "Do you want to reroll your lowest value, " + str(lowestattribute) + "? " + "(you must stick with the rerolled value if you choose yes)"
        reroll = messagebox.askquestion(projectname, rerollmessage)
        if reroll == "yes": #if REROLL 
            os.system('cls') #clears the output window
            print("========== WELCOME TO THE GAME ==========")
            print("You must assign: strength, agility, magic and luck")
            if attribute1 == lowestattribute:
                attribute1 = attribute_generation()
                newattribute = attribute1
            elif attribute2 == lowestattribute:
                attribute2 = attribute_generation()
                newattribute = attribute2
            elif attribute3 == lowestattribute:
                attribute3 = attribute_generation()
                newattribute = attribute3
            else:
                attribute4 = attribute_generation()
                newattribute = attribute4
            #Outputting new values that the user must stick with
            attributesmessage = "The reroll rolled a " + str(newattribute) + ", meaning your new values are:" + "\n" + "\n" + str(attribute1) + " " + str(attribute2) + " " + str(attribute3)+ " " + str(attribute4)
            print(attributesmessage)
            messagebox.showinfo(projectname, attributesmessage)
        os.system('cls')
        print("========== WELCOME TO THE GAME ==========")
        print("You must assign: strength, agility, magic and luck")
        #proceeds to assign variables from attributes1,2,3,4 to Strength, Agility, Magic and Luck
        attributes = [str(attribute1), str(attribute2), str(attribute3), str(attribute4)]
        assignments_made = []
        #strength
        character1_strength = None
        strength_assignment_message = "Which value do you want to assign to " + character1 + "'s" + " strength?" + "\n" + str(attribute1) + "," + str(attribute2) + "," + str(attribute3) + " OR " + str(attribute4)
        while character1_strength not in attributes:
            character1_strength = (turtle.textinput(projectname, strength_assignment_message))
        character1_strength = int(character1_strength)
        if character1_strength == attribute1:
            attributes.remove(str(attribute1))
            assignments_made.append("attribute1")
        elif character1_strength == attribute2:
            attributes.remove(str(attribute2))
            assignments_made.append("attribute2")
        elif character1_strength == attribute3:
            attributes.remove(str(attribute3))
            assignments_made.append("attribute3")
        else:
            attributes.remove(str(attribute4))
            assignments_made.append("attribute4")
        print(character1 + "'s", " strength: ", character1_strength)
        #agility
        character1_agility = None
        agility_assignment_message = "Which value do you want to assign to " + character1 + "'s" + " agility?" + "\n" + str(attributes[0]) + "," + str(attributes[1]) + " OR " + str(attributes[2])
        while character1_agility not in attributes:
            character1_agility = (turtle.textinput(projectname, agility_assignment_message))
        character1_agility = int(character1_agility)
        if "attribute1" not in assignments_made and character1_agility == attribute1:
            attributes.remove(str(attribute1))
            assignments_made.append("attribute1")
        elif "attribute2" not in assignments_made and character1_agility == attribute2:
            attributes.remove(str(attribute2))
            assignments_made.append("attribute2")
        elif "attribute3" not in assignments_made and character1_agility == attribute3:
            attributes.remove(str(attribute3))
            assignments_made.append("attribute3")
        elif "attribute4" not in assignments_made and character1_agility == attribute4:
            attributes.remove(str(attribute4))
            assignments_made.append("attribute4")
        print(character1 + "'s", " agility: ", character1_agility)
        #magic
        character1_magic = None
        magic_assignment_message = "Which value do you want to assign to " + character1 + "'s" + " magic?" + "\n" + str(attributes[0]) + " OR " + str(attributes[1])
        while character1_magic not in attributes:
            character1_magic = (turtle.textinput(projectname, magic_assignment_message))
        character1_magic = int(character1_magic)
        if "attribute1" not in assignments_made and character1_magic == attribute1:
            attributes.remove(str(attribute1))
            assignments_made.append("attribute1")
        elif "attribute2" not in assignments_made and character1_magic == attribute2:
            attributes.remove(str(attribute2))
            assignments_made.append("attribute2")
        elif "attribute3" not in assignments_made and character1_magic == attribute3:
            attributes.remove(str(attribute3))
            assignments_made.append("attribute3")
        elif "attribute4" not in assignments_made and character1_magic == attribute4:
            attributes.remove(str(attribute4))
            assignments_made.append("attribute4")
        print(character1 + "'s", " magic: ", character1_magic)
        #luck
        #only item in the attributes list becomes the luck value
        character1_luck = int(attributes[0])
        character1_hp = 2
        print(character1 + "'s", " luck: ", character1_luck)
        character1_summary_message = character1 + " has been created. Press OK to move onto the creation of your second character."
        messagebox.showinfo("Character successfully created", character1_summary_message)
        os.system('cls')
        print("========== WELCOME TO THE GAME ==========")
        print("You must assign: strength, agility, magic and luck")
        num_of_characters_to_create =  num_of_characters_to_create - 1
    if num_of_characters_to_create == 3:    
        #CHARACTER 2 ------------------------------------------------------------------------------------------------------------------------------------------------
            #CHARACTER CREATION
        character2 = None #CHARACTER 1
        while character2 == None:#ensures that character name cannot have no value, OR begin with a space etc.
            if incomplete_read == True:
                character2 = turtle.textinput("Create character 2", "The save file you loaded requires more players to be created. Create your second character's name:  ")
            elif incomplete_read == False:
                character2 = turtle.textinput("Create character 2", "Enter the name of your second character: ")
            c2length = len(character2)
            if c2length > 15:
                c2toolong = True
            while c2toolong == True:
                character2 = turtle.textinput("Create character 2", "Character must have a name 15 characters or less. Enter the name of your second character: ")
                c2length = len(character2)
                if c2length > 15:
                    c2toolong = True
                else:
                    c2toolong = False
            character2_valid = character2
            if character2_valid != None:
                if character2_valid == "" or character2_valid[0] == " " or character2 == character1:
                    character2 = None
        attribute1 = attribute_generation() #generates attributes
        attribute2 = attribute_generation()
        attribute3 = attribute_generation()
        attribute4 = attribute_generation()
        lowestattribute = min(attribute1, attribute2, attribute3, attribute4) #works out the lowest attribute generated
        #assembles a message to be printed and shown in a dialog box
        attributesmessage = "The following numbers have been rolled for" + " " + str(character2) + " " + "and you will need to choose which value you want to assign to each attribute (Strength, Agility, Magic & Luck):" + "\n" + "\n" + str(attribute1) + " " + str(attribute2) + " " + str(attribute3)+ " " + str(attribute4)
        print(attributesmessage)
        messagebox.showinfo(projectname, attributesmessage)
        rerollmessage = "Do you want to reroll your lowest value, " + str(lowestattribute) + "? " + "(you must stick with the rerolled value if you choose yes)"
        reroll = messagebox.askquestion(projectname, rerollmessage)
        if reroll == "yes": #if REROLL 
            os.system('cls') #clears the output window
            print("========== WELCOME TO THE GAME ==========")
            if attribute1 == lowestattribute:
                attribute1 = attribute_generation()
                newattribute = attribute1
            elif attribute2 == lowestattribute:
                attribute2 = attribute_generation()
                newattribute = attribute2
            elif attribute3 == lowestattribute:
                attribute3 = attribute_generation()
                newattribute = attribute3
            else:
                attribute4 = attribute_generation()
                newattribute = attribute4
            #Outputting new values that the user must stick with
            attributesmessage = "The reroll rolled a " + str(newattribute) + ", meaning your new values are:" + "\n" + "\n" + str(attribute1) + " " + str(attribute2) + " " + str(attribute3)+ " " + str(attribute4)
            print(attributesmessage)
            messagebox.showinfo(projectname, attributesmessage)
        os.system('cls')
        print("========== WELCOME TO THE GAME ==========")
        print("You must assign: strength, agility, magic and luck")
        #proceeds to assign variables from attributes1,2,3,4 to Strength, Agility, Magic and Luck
        attributes = [str(attribute1), str(attribute2), str(attribute3), str(attribute4)]
        assignments_made = []
        #strength
        character2_strength = None
        strength_assignment_message = "Which value do you want to assign to " + character2 + "'s" + " strength?" + "\n" + str(attribute1) + "," + str(attribute2) + "," + str(attribute3) + " OR " + str(attribute4)
        while character2_strength not in attributes:
            character2_strength = (turtle.textinput(projectname, strength_assignment_message))
        character2_strength = int(character2_strength)
        if character2_strength == attribute1:
            attributes.remove(str(attribute1))
            assignments_made.append("attribute1")
        elif character2_strength == attribute2:
            attributes.remove(str(attribute2))
            assignments_made.append("attribute2")
        elif character2_strength == attribute3:
            attributes.remove(str(attribute3))
            assignments_made.append("attribute3")
        else:
            attributes.remove(str(attribute4))
            assignments_made.append("attribute4")
        print(character2 + "'s", " strength: ", character2_strength)
        #agility
        character2_agility = None
        agility_assignment_message = "Which value do you want to assign to " + character2 + "'s" + " agility?" + "\n" + str(attributes[0]) + "," + str(attributes[1]) + " OR " + str(attributes[2])
        while character2_agility not in attributes:
            character2_agility = (turtle.textinput(projectname, agility_assignment_message))
        character2_agility = int(character2_agility)
        if "attribute1" not in assignments_made and character2_agility == attribute1:
            attributes.remove(str(attribute1))
            assignments_made.append("attribute1")
        elif "attribute2" not in assignments_made and character2_agility == attribute2:
            attributes.remove(str(attribute2))
            assignments_made.append("attribute2")
        elif "attribute3" not in assignments_made and character2_agility == attribute3:
            attributes.remove(str(attribute3))
            assignments_made.append("attribute3")
        elif "attribute4" not in assignments_made and character2_agility == attribute4:
            attributes.remove(str(attribute4))
            assignments_made.append("attribute4")
        print(character2 + "'s", " agility: ", character2_agility)
        #magic
        character2_magic = None
        magic_assignment_message = "Which value do you want to assign to " + character2 + "'s" + " magic?" + "\n" + str(attributes[0]) + " OR " + str(attributes[1])
        while character2_magic not in attributes:
            character2_magic = (turtle.textinput(projectname, magic_assignment_message))
        character2_magic = int(character2_magic)
        if "attribute1" not in assignments_made and character2_magic == attribute1:
            attributes.remove(str(attribute1))
            assignments_made.append("attribute1")
        elif "attribute2" not in assignments_made and character2_magic == attribute2:
            attributes.remove(str(attribute2))
            assignments_made.append("attribute2")
        elif "attribute3" not in assignments_made and character2_magic == attribute3:
            attributes.remove(str(attribute3))
            assignments_made.append("attribute3")
        elif "attribute4" not in assignments_made and character2_magic == attribute4:
            attributes.remove(str(attribute4))
            assignments_made.append("attribute4")
        print(character2 + "'s", " magic: ", character2_magic)
        #luck
        #only item in the attributes list becomes the luck value
        character2_luck = int(attributes[0])
        character2_hp = 2
        print(character2 + "'s", " luck: ", character2_luck)
        character2_summary_message = character2 + " has been created. Press OK to move onto the creation of your third character."
        messagebox.showinfo("Character successfully created", character2_summary_message)
        os.system('cls')
        print("========== WELCOME TO THE GAME ==========")
        print("You must assign: strength, agility, magic and luck")
        num_of_characters_to_create =  num_of_characters_to_create - 1
    if num_of_characters_to_create == 2:
        #CHARACTER 3 -----------------------------------------------------------------------------------------------------------------
            #CHARACTER CREATION
        character3 = None #CHARACTER 1
        while character3 == None: #ensures that character name cannot have no value, OR begin with a space etc.
            if incomplete_read == True:
                character3 = turtle.textinput("Create character 3", "The save file you loaded requires more players to be created. Create your third character's name:  ")
            elif incomplete_read == False:
                character3 = turtle.textinput("Create character 3", "Enter the name of your third character: ")
            c3length = len(character3)
            if c3length > 15:
                c3toolong = True
            while c3toolong == True:
                character1 = turtle.textinput("Create character 3", "Character must have a name 15 characters or less. Enter the name of your third character: ")
                c3length = len(character3)
                if c3length > 15:
                    c3toolong = True
                else:
                    c3toolong = False
            character3_valid = character3
            if character3_valid != None:
                if character3_valid == "" or character3_valid[0] == " " or character3 == character1 or character3 == character2:
                    character3 = None
                    while len(character3) > 15:
                        character3 = turtle.textinput("Create character 3", "Character must have a name 15 characters or less. Enter the name of your third character: ")
        attribute1 = attribute_generation() #generates attributes
        attribute2 = attribute_generation()
        attribute3 = attribute_generation()
        attribute4 = attribute_generation()
        lowestattribute = min(attribute1, attribute2, attribute3, attribute4) #works out the lowest attribute generated
        #assembles a message to be printed and shown in a dialog box
        attributesmessage = "The following numbers have been rolled for" + " " + str(character3) + " " + "and you will need to choose which value you want to assign to each attribute (Strength, Agility, Magic & Luck):" + "\n" + "\n" + str(attribute1) + " " + str(attribute2) + " " + str(attribute3)+ " " + str(attribute4)
        print(attributesmessage)
        messagebox.showinfo(projectname, attributesmessage)
        rerollmessage = "Do you want to reroll your lowest value, " + str(lowestattribute) + "? " + "(you must stick with the rerolled value if you choose yes)"
        reroll = messagebox.askquestion(projectname, rerollmessage)
        if reroll == "yes": #if REROLL 
            os.system('cls') #clears the output window
            print("========== WELCOME TO THE GAME ==========")
            if attribute1 == lowestattribute:
                attribute1 = attribute_generation()
                newattribute = attribute1
            elif attribute2 == lowestattribute:
                attribute2 = attribute_generation()
                newattribute = attribute2
            elif attribute3 == lowestattribute:
                attribute3 = attribute_generation()
                newattribute = attribute3
            else:
                attribute4 = attribute_generation()
                newattribute = attribute4
            #Outputting new values that the user must stick with
            attributesmessage = "The reroll rolled a " + str(newattribute) + ", meaning your new values are:" + "\n" + "\n" + str(attribute1) + " " + str(attribute2) + " " + str(attribute3)+ " " + str(attribute4)
            print(attributesmessage)
            messagebox.showinfo(projectname, attributesmessage)
        os.system('cls')
        print("========== WELCOME TO THE GAME ==========")
        print("You must assign: strength, agility, magic and luck")
        #proceeds to assign variables from attributes1,2,3,4 to Strength, Agility, Magic and Luck
        attributes = [str(attribute1), str(attribute2), str(attribute3), str(attribute4)]
        assignments_made = []
        #strength
        character3_strength = None
        strength_assignment_message = "Which value do you want to assign to " + character3 + "'s" + " strength?" + "\n" + str(attribute1) + "," + str(attribute2) + "," + str(attribute3) + " OR " + str(attribute4)
        while character3_strength not in attributes:
            character3_strength = (turtle.textinput(projectname, strength_assignment_message))
        character3_strength = int(character3_strength)
        if character3_strength == attribute1:
            attributes.remove(str(attribute1))
            assignments_made.append("attribute1")
        elif character3_strength == attribute2:
            attributes.remove(str(attribute2))
            assignments_made.append("attribute2")
        elif character3_strength == attribute3:
            attributes.remove(str(attribute3))
            assignments_made.append("attribute3")
        else:
            attributes.remove(str(attribute4))
            assignments_made.append("attribute4")
        print(character3 + "'s", " strength: ", character3_strength)
        #agility
        character3_agility = None
        agility_assignment_message = "Which value do you want to assign to " + character3 + "'s" + " agility?" + "\n" + str(attributes[0]) + "," + str(attributes[1]) + " OR " + str(attributes[2])
        while character3_agility not in attributes:
            character3_agility = (turtle.textinput(projectname, agility_assignment_message))
        character3_agility = int(character3_agility)
        if "attribute1" not in assignments_made and character3_agility == attribute1:
            attributes.remove(str(attribute1))
            assignments_made.append("attribute1")
        elif "attribute2" not in assignments_made and character3_agility == attribute2:
            attributes.remove(str(attribute2))
            assignments_made.append("attribute2")
        elif "attribute3" not in assignments_made and character3_agility == attribute3:
            attributes.remove(str(attribute3))
            assignments_made.append("attribute3")
        elif "attribute4" not in assignments_made and character3_agility == attribute4:
            attributes.remove(str(attribute4))
            assignments_made.append("attribute4")
        print(character3 + "'s", " agility: ", character3_agility)
        #magic
        character3_magic = None
        magic_assignment_message = "Which value do you want to assign to " + character3 + "'s" + " magic?" + "\n" + str(attributes[0]) + " OR " + str(attributes[1])
        while character3_magic not in attributes:
            character3_magic = (turtle.textinput(projectname, magic_assignment_message))
        character3_magic = int(character3_magic)
        if "attribute1" not in assignments_made and character3_magic == attribute1:
            attributes.remove(str(attribute1))
            assignments_made.append("attribute1")
        elif "attribute2" not in assignments_made and character3_magic == attribute2:
            attributes.remove(str(attribute2))
            assignments_made.append("attribute2")
        elif "attribute3" not in assignments_made and character3_magic == attribute3:
            attributes.remove(str(attribute3))
            assignments_made.append("attribute3")
        elif "attribute4" not in assignments_made and character3_magic == attribute4:
            attributes.remove(str(attribute4))
            assignments_made.append("attribute4")
        print(character3 + "'s", " magic: ", character3_magic)
        #luck
        #only item in the attributes list becomes the luck value
        character3_luck = int(attributes[0])
        character3_hp = 2
        print(character3 + "'s", " luck: ", character3_luck)
        character3_summary_message = character3 + " has been created. Press OK to move onto the creation of your final character."
        messagebox.showinfo("Character successfully created", character3_summary_message)
        os.system('cls')
        print("========== WELCOME TO THE GAME ==========")
        print("You must assign: strength, agility, magic and luck")
        num_of_characters_to_create =  num_of_characters_to_create - 1
    if num_of_characters_to_create == 1:
        #CHARACTER 4 --------------------------------------------------------------------------------
            #CHARACTER CREATION
        character4 = None #CHARACTER 1
        while character4 == None: #ensures that character name cannot have no value, OR begin with a space etc.
            if incomplete_read == True:
                character4 = turtle.textinput("Create character 4", "The save file you loaded requires another player to be created. Create your fourth character's name:  ")
            elif incomplete_read == False:
                character4 = turtle.textinput("Create character 4", "Enter the name of your fourth character: ")
            c4length = len(character4)
            if c4length > 15:
                c4toolong = True
            while c4toolong == True:
                character4 = turtle.textinput("Create character 4", "Character must have a name 15 characters or less. Enter the name of your fourth character: ")
                c4length = len(character4)
                if c4length > 15:
                    c4toolong = True
                else:
                    c4toolong = False
            character4_valid = character4
            if character4_valid != None:
                if character4_valid == "" or character4_valid[0] == " " or character4 == character1 or character4 == character2 or character4 == character3:
                    character4 = None
                    while len(character4) > 15:
                        character4 = turtle.textinput("Create character 4", "Character must have a name 15 characters or less. Enter the name of your fourth character: ")
        attribute1 = attribute_generation() #generates attributes
        attribute2 = attribute_generation()
        attribute3 = attribute_generation()
        attribute4 = attribute_generation()
        lowestattribute = min(attribute1, attribute2, attribute3, attribute4) #works out the lowest attribute generated
        #assembles a message to be printed and shown in a dialog box
        attributesmessage = "The following numbers have been rolled for" + " " + str(character4) + " " + "and you will need to choose which value you want to assign to each attribute (Strength, Agility, Magic & Luck):" + "\n" + "\n" + str(attribute1) + " " + str(attribute2) + " " + str(attribute3)+ " " + str(attribute4)
        print(attributesmessage)
        messagebox.showinfo(projectname, attributesmessage)
        rerollmessage = "Do you want to reroll your lowest value, " + str(lowestattribute) + "? " + "(you must stick with the rerolled value if you choose yes)"
        reroll = messagebox.askquestion(projectname, rerollmessage)
        if reroll == "yes": #if REROLL 
            os.system('cls') #clears the output window
            print("========== WELCOME TO THE GAME ==========")
            if attribute1 == lowestattribute:
                attribute1 = attribute_generation()
                newattribute = attribute1
            elif attribute2 == lowestattribute:
                attribute2 = attribute_generation()
                newattribute = attribute2
            elif attribute3 == lowestattribute:
                attribute3 = attribute_generation()
                newattribute = attribute3
            else:
                attribute4 = attribute_generation()
                newattribute = attribute4
            #Outputting new values that the user must stick with
            attributesmessage = "The reroll rolled a " + str(newattribute) + ", meaning your new values are:" + "\n" + "\n" + str(attribute1) + " " + str(attribute2) + " " + str(attribute3)+ " " + str(attribute4)
            print(attributesmessage)
            messagebox.showinfo(projectname, attributesmessage)
        os.system('cls')
        print("========== WELCOME TO THE GAME ==========")
        print("You must assign: strength, agility, magic and luck")
        #proceeds to assign variables from attributes1,2,3,4 to Strength, Agility, Magic and Luck
        attributes = [str(attribute1), str(attribute2), str(attribute3), str(attribute4)]
        assignments_made = []
        #strength
        character4_strength = None
        strength_assignment_message = "Which value do you want to assign to " + character4 + "'s" + " strength?" + "\n" + str(attribute1) + "," + str(attribute2) + "," + str(attribute3) + " OR " + str(attribute4)
        while character4_strength not in attributes:
            character4_strength = (turtle.textinput(projectname, strength_assignment_message))
        character4_strength = int(character4_strength)
        if character4_strength == attribute1:
            attributes.remove(str(attribute1))
            assignments_made.append("attribute1")
        elif character4_strength == attribute2:
            attributes.remove(str(attribute2))
            assignments_made.append("attribute2")
        elif character4_strength == attribute3:
            attributes.remove(str(attribute3))
            assignments_made.append("attribute3")
        else:
            attributes.remove(str(attribute4))
            assignments_made.append("attribute4")
        print(character4 + "'s", " strength: ", character4_strength)
        #agility
        character4_agility = None
        agility_assignment_message = "Which value do you want to assign to " + character4 + "'s" + " agility?" + "\n" + str(attributes[0]) + "," + str(attributes[1]) + " OR " + str(attributes[2])
        while character4_agility not in attributes:
            character4_agility = (turtle.textinput(projectname, agility_assignment_message))
        character4_agility = int(character4_agility)
        if "attribute1" not in assignments_made and character4_agility == attribute1:
            attributes.remove(str(attribute1))
            assignments_made.append("attribute1")
        elif "attribute2" not in assignments_made and character4_agility == attribute2:
            attributes.remove(str(attribute2))
            assignments_made.append("attribute2")
        elif "attribute3" not in assignments_made and character4_agility == attribute3:
            attributes.remove(str(attribute3))
            assignments_made.append("attribute3")
        elif "attribute4" not in assignments_made and character4_agility == attribute4:
            attributes.remove(str(attribute4))
            assignments_made.append("attribute4")
        print(character4 + "'s", " agility: ", character4_agility)
        #magic
        character4_magic = None
        magic_assignment_message = "Which value do you want to assign to " + character4 + "'s" + " magic?" + "\n" + str(attributes[0]) + " OR " + str(attributes[1])
        while character4_magic not in attributes:
            character4_magic = (turtle.textinput(projectname, magic_assignment_message))
        character4_magic = int(character4_magic)
        if "attribute1" not in assignments_made and character4_magic == attribute1:
            attributes.remove(str(attribute1))
            assignments_made.append("attribute1")
        elif "attribute2" not in assignments_made and character4_magic == attribute2:
            attributes.remove(str(attribute2))
            assignments_made.append("attribute2")
        elif "attribute3" not in assignments_made and character4_magic == attribute3:
            attributes.remove(str(attribute3))
            assignments_made.append("attribute3")
        elif "attribute4" not in assignments_made and character4_magic == attribute4:
            attributes.remove(str(attribute4))
            assignments_made.append("attribute4")
        print(character4 + "'s", " magic: ", character4_magic)
        #luck
        #only item in the attributes list becomes the luck value
        character4_luck = int(attributes[0])
        character4_hp = 2
        print(character4 + "'s", " luck: ", character4_luck)
        character4_summary_message = character4 + " has been created. Press OK to continue."
        messagebox.showinfo("Character successfully created", character4_summary_message)
character1_fatigued = False
character2_fatigued = False
character3_fatigued = False
character4_fatigued = False
character1_alive = True
character2_alive = True
character3_alive = True
character4_alive = True
character1_lower = character1.lower()
character2_lower = character2.lower()
character3_lower = character3.lower()
character4_lower = character4.lower()
os.system('cls')
print("========== CHARACTER SUMMARY ==========")
if import_success == True:
    print("Import from file successful.")
    print("")
print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp)
print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp)
print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp)
print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp)
print("")
print("========== THE ADVENTURE BEGINS ==========")
if import_success == True:
    messagebox.showinfo(projectname, "Characters imported. Press OK to begin the game.")
else:
    messagebox.showinfo(projectname, "Characters created. Press OK to begin the game.")

#---------------------------------------------------------------------------------------               - GAME BEGINS
#Once a party has four characters, the adventure begins. The computer will output some text then 
#present the player with a challenge which will have a challenge rating between five and fifteen. The 
#challenge will be linked to one of the four main attributes; Strength, Agility, Magic or Luck. The 
#player will choose one of their characters to accept the challenge. The computer will roll a twenty 
#sided dice (generate a number between one and twenty) and will add the challenge rating to 
#produce a challenge total. The computer will then roll another twenty-sided dice and will add the 
#character’s attribute linked to the challenge to produce the character’s total. The two numbers will 
#then be compared. If the character’s total exceeds or equals the challenge total then that character 
#defeats the challenge. If the character defeats the challenge then they may add a Hit Point to their 
#total up to a maximum of four. If the character is defeated by the challenge then they lose a Hit 
#Point. If they lose their last Hit Point then the character is killed and may not be used again in a 
#future challenge. Whether the character wins or loses the challenge, they become fatigued and may 
#not be used until another challenge has been completed (won or lost). There should be appropriate 
#text output at all stages of the challenge to describe what is going on. 
os.system('cls')
if character1_fatigued == True:
    character1_fatigued_pretty = "Y"
else:
    character1_fatigued_pretty = "N"
if character2_fatigued == True:
    character2_fatigued_pretty = "Y"
else:
    character2_fatigued_pretty = "N"
if character3_fatigued == True:
    character3_fatigued_pretty = "Y"
else:
    character3_fatigued_pretty = "N"
if character4_fatigued == True:
    character4_fatigued_pretty = "Y"
else:
    character4_fatigued_pretty = "N"
print("========== THE ADVENTURE BEGINS ==========")
print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp, " | Fatigued:", character1_fatigued_pretty)
print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp, " | Fatigued:", character2_fatigued_pretty)
print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp, " | Fatigued:", character3_fatigued_pretty)
print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp, " | Fatigued:", character4_fatigued_pretty)
print("")
characters = [character1, character2, character3, character4]
characters_lower = [character1.lower(), character2.lower(), character3.lower(), character4.lower()]
#-----------------------------------------------------------------------------------------------------      CHALLENGE 1 luck
print("Welcome to the game. You and your party set off on your journey and hit a fork in the road ahead. \nYour chosen character will decide whether they go left or right.")
messagebox.showinfo("Challenge 1", "Welcome to the game. You and your party set off on your journey and hit a fork in the road ahead. \n \nYour chosen character will decide whether they go left or right.")
challenge1_player = None
challenge1_rating = random.randint(5,15)
challenge1_roll = random.randint(1,20)
challenge1_total = challenge1_rating + challenge1_roll
character1_luck = int(character1_luck)
character2_luck = int(character2_luck)
character3_luck = int(character3_luck)
character4_luck = int(character4_luck)
challenge1_win = False
while challenge1_player == None:
    challenge1_player = (turtle.textinput("Challenge 1", "Choose the character you wish to accept this first LUCK based challenge:"))
    if challenge1_player != None:
        if challenge1_player not in characters:
            if challenge1_player not in characters_lower:
                challenge1_player = None
challenge1_player = challenge1_player.capitalize()
challenge1_message = "You selected " + challenge1_player + " to accept this challenge. \n \nClick OK to see the outcome of the challenge."
if challenge1_player == characters[0]:
    messagebox.showinfo("Challenge 1", challenge1_message)
    challenge1_playerroll = random.randint(1,20)
    challenge1_playertotal = challenge1_playerroll + character1_luck
    if challenge1_playertotal >= challenge1_total:
        challenge1_win = True
        character1_fatigued = True
        character1_lower = character1.lower()
        if character1.lower() not in fatigued_characters:
            fatigued_characters.append(character1_lower)
        if int(character1_hp) < 4:
            character1_hp = int(character1_hp) + 1
    else:
        if int(character1_hp) > 0:
            character1_fatigued = True
            if character1.lower() not in fatigued_characters:
                fatigued_characters.append(character1_lower)
            character1_hp = int(character1_hp) - 1
        if int(character1_hp) <= 0:
            character1_alive = False
            dead_characters.append(character1_lower)
            if character1.lower() not in fatigued_characters:
                fatigued_characters.append(character1_lower)
            fatigued_characters.remove(character1_lower)
            challenge1_fatal = True
elif challenge1_player == characters[1]:
    messagebox.showinfo("Challenge 1", challenge1_message)
    challenge1_playerroll = random.randint(1,20)
    challenge1_playertotal = challenge1_playerroll + character2_luck
    if challenge1_playertotal >= challenge1_total:
        challenge1_win = True
        character2_fatigued = True
        fatigued_characters.append(character2_lower)
        character2_lower = character2.lower()
        if int(character2_hp) < 4:
            character2_hp = int(character2_hp) + 1
    else:
        if int(character2_hp) > 0:
            character2_fatigued = True
        character2_lower = character2.lower()
        fatigued_characters.append(character2_lower)
        character2_hp = int(character2_hp) - 1
        if int(character2_hp) <= 0:
            character2_alive = False
            dead_characters.append(character2_lower)
            fatigued_characters.remove(character2_lower)
            challenge1_fatal = True
elif challenge1_player == characters[2]:
    messagebox.showinfo("Challenge 1", challenge1_message)
    challenge1_playerroll = random.randint(1,20)
    challenge1_playertotal = challenge1_playerroll + character3_luck
    if challenge1_playertotal >= challenge1_total:
        challenge1_win = True
        character3_fatigued = True
        character3_lower = character3.lower()
        fatigued_characters.append(character3_lower)
        if int(character3_hp) < 4:
            character3_hp = int(character3_hp) + 1
    else:
        if int(character3_hp) > 0:
            character3_fatigued = True
        character3_lower = character3.lower()
        fatigued_characters.append(character3_lower)
        character3_hp = int(character3_hp) - 1
        if int(character3_hp) <= 0:
            character3_alive = False
            dead_characters.append(character3_lower)
            fatigued_characters.remove(character3_lower)
            challenge1_fatal = True
elif challenge1_player == characters[3]:
    messagebox.showinfo("Challenge 1", challenge1_message)
    challenge1_playerroll = random.randint(1,20)
    challenge1_playertotal = challenge1_playerroll + character4_luck
    if challenge1_playertotal >= challenge1_total:
        challenge1_win = True
        character4_fatigued = True
        character4_lower = character4.lower()
        fatigued_characters.append(character4_lower)
        if int(character4_hp) < 4:
            character4_hp = int(character4_hp) + 1
    else:
        if int(character4_hp) > 0:
            character4_fatigued = True
        character4_lower = character4.lower()
        fatigued_characters.append(character4_lower)
        character4_hp = int(character4_hp) - 1
        if int(character4_hp) <= 0:
            character4_alive = False
            dead_characters.append(character4_lower)
            fatigued_characters.remove(character4_lower)
            challenge1_fatal = True
os.system('cls')
print("========== THE ADVENTURE BEGINS ==========")
if character1_fatigued == True:
    character1_fatigued_pretty = "Y"
else:
    character1_fatigued_pretty = "N"
if character2_fatigued == True:
    character2_fatigued_pretty = "Y"
else:
    character2_fatigued_pretty = "N"
if character3_fatigued == True:
    character3_fatigued_pretty = "Y"
else:
    character3_fatigued_pretty = "N"
if character4_fatigued == True:
    character4_fatigued_pretty = "Y"
else:
    character4_fatigued_pretty = "N"
if challenge1_fatal == True:
    if characters.index(challenge1_player) == 0:
        characters[0] = 0
    elif characters.index(challenge1_player) == 1:
        characters[1] = 0
    elif characters.index(challenge1_player) == 2:
        characters[2] = 0
    elif characters.index(challenge1_player) == 3:
        characters[3] = 0
        #make a replacement in the list characters at that posititon then make an exception for entering zero etc.
if character1 in characters:
    print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp, " | Fatigued:", character1_fatigued_pretty)
if character2 in characters:
    print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp, " | Fatigued:", character2_fatigued_pretty)
if character3 in characters:
    print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp, " | Fatigued:", character3_fatigued_pretty)
if character4 in characters:
    print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp, " | Fatigued:", character4_fatigued_pretty)
print("")
leftright = random.randint(1,2)
if leftright == 1:
    challenge1_direction = "left."
else:
    challenge1_direction = "right."
print("")
if challenge1_fatal == False:
    if challenge1_win == True:
        challenge1_win_message = challenge1_player + " chose to go " + challenge1_direction + "\n \n" + "This was the right decision! " + challenge1_player + " defeated the challenge, gaining 1HP but becoming fatigued and cannot play the next challenge." + "\n \n" + "You can see updated character stats in the output window."
        print(challenge1_player, "chose to go", challenge1_direction)
        print("This was the right decision!", challenge1_player, "defeated the challenge, gaining 1HP but becoming fatigued and cannot play the next challenge.")
        print("You can see updated character stats in the output window.")
        messagebox.showinfo("Challenge 1", challenge1_win_message)
    elif challenge1_win == False:
        challenge1_loss_message = challenge1_player + " chose to go " + challenge1_direction + "\n \n" + "This was the wrong decision, " + challenge1_player + " slipped off a cliff and loses 1HP, also becoming fatigued and cannot play the next challenge." + "\n \n" + "You can see updated character stats in the output window."
        print(challenge1_player, "chose to go", challenge1_direction)
        print("This was the wrong decision,", challenge1_player, "slipped off a cliff and loses 1HP, also becoming fatigued so cannot play the next challenge.")
        print("You can see updated character stats in the output window.")
        messagebox.showinfo("Challenge 1", challenge1_loss_message)
elif challenge1_fatal == True:
    challenge1_loss_message = challenge1_player + " chose to go " + challenge1_direction + "\n \n" + "After slipping off a cliff and losing all HP, " + challenge1_player + " is now dead and cannot play on."
    print(challenge1_loss_message)
    messagebox.showinfo("Challenge 1", challenge1_loss_message)
messagebox.showinfo("Challenge 2", "Press OK to continue to challenge 2")
os.system('cls')
print("========== THE ADVENTURE BEGINS ==========")
if character1 in characters:
    print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp, " | Fatigued:", character1_fatigued_pretty)
if character2 in characters:
    print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp, " | Fatigued:", character2_fatigued_pretty)
if character3 in characters:
    print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp, " | Fatigued:", character3_fatigued_pretty)
if character4 in characters:
    print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp, " | Fatigued:", character4_fatigued_pretty)
print("")
#-----------------------------------------------------------------------------------------------------      CHALLENGE 2 strength
print("Welcome to the second challenge. You and your party continue on their journey and are faced with a monster ahead. \n\nYou must fight it.")
messagebox.showinfo("Challenge 2", "Welcome to the second challenge. You and your party continue on their journey and are faced with a monster ahead. \n\nYou must fight it.")
challenge2_player = None
challenge2_rating = random.randint(5,15)
challenge2_roll = random.randint(1,20)
challenge2_total = challenge2_rating + challenge2_roll
character1_strength = int(character1_strength)
character2_strength = int(character2_strength)
character3_strength = int(character3_strength)
character4_strength = int(character4_strength)
challenge2_win = False
while challenge2_player == None:
    challenge2_player = (turtle.textinput("Challenge 2", "Choose the character you wish to accept this strength based, second challenge:"))
    if challenge2_player != None:
        while challenge2_player in fatigued_characters or challenge2_player.lower() in fatigued_characters:
            challenge2_player = (turtle.textinput("Challenge 2", "The character you selected is fatigued and cannot play this challenge. Choose the character you wish to accept this first strength based challenge:"))
        while challenge2_player.lower() in dead_characters:
            challenge2_player = (turtle.textinput("Challenge 2", "The character you selected is dead and no longer exists in your party. Choose the character you wish to accept this first strength based challenge:"))
        if challenge2_player == "0":
            challenge2_player = None
        if challenge2_player.lower() in fatigued_characters:
            challenge2_player = None
        if challenge2_player not in characters:
            if challenge2_player not in characters_lower:
                challenge2_player = None
challenge2_player = challenge2_player.capitalize()
challenge2_message = "You selected " + challenge2_player + " to accept this challenge. \n \nClick OK to see the outcome of the challenge."
if challenge2_player == characters[0]:
    messagebox.showinfo("Challenge 2", challenge2_message)
    challenge2_playerroll = random.randint(1,20)
    challenge2_playertotal = challenge2_playerroll + character1_strength
    if challenge2_playertotal >= challenge2_total:
        challenge2_win = True
        character1_fatigued = True
        fatigued_characters.append(character1_lower)
        if int(character1_hp) < 4:
            character1_hp = int(character1_hp) + 1
    else:
        if int(character1_hp) > 0:
            character1_fatigued = True
            fatigued_characters.append(character1_lower)
            character1_hp = int(character1_hp) - 1
        if int(character1_hp) <= 0:
            character1_alive = False
            dead_characters.append(character1_lower)
            fatigued_characters.remove(character1_lower)
            challenge2_fatal = True
elif challenge2_player == characters[1]:
    messagebox.showinfo("Challenge 2", challenge2_message)
    challenge2_playerroll = random.randint(1,20)
    challenge2_playertotal = challenge2_playerroll + character2_strength
    if challenge2_playertotal >= challenge2_total:
        challenge2_win = True
        character2_fatigued = True
        fatigued_characters.append(character2_lower)
        character2_lower = character2.lower()
        if int(character2_hp) < 4:
            character2_hp = int(character2_hp) + 1
    else:
        if int(character2_hp) > 0:
            character2_fatigued = True
        character2_lower = character2.lower()
        fatigued_characters.append(character2_lower)
        character2_hp = int(character2_hp) - 1
        if int(character2_hp) <= 0:
            character2_alive = False
            dead_characters.append(character2_lower)
            fatigued_characters.remove(character2_lower)
            challenge2_fatal = True
elif challenge2_player == characters[2]:
    messagebox.showinfo("Challenge 2", challenge2_message)
    challenge2_playerroll = random.randint(1,20)
    challenge2_playertotal = challenge2_playerroll + character3_strength
    if challenge2_playertotal >= challenge2_total:
        challenge2_win = True
        character3_fatigued = True
        character3_lower = character3.lower()
        fatigued_characters.append(character3_lower)
        if int(character3_hp) < 4:
            character3_hp = int(character3_hp) + 1
    else:
        if int(character3_hp) > 0:
            character3_fatigued = True
        character3_lower = character3.lower()
        fatigued_characters.append(character3_lower)
        character3_hp = int(character3_hp) - 1
        if int(character3_hp) <= 0:
            character3_alive = False
            dead_characters.append(character3_lower)
            fatigued_characters.remove(character3_lower)
            challenge2_fatal = True
elif challenge2_player == characters[3]:
    messagebox.showinfo("Challenge 2", challenge2_message)
    challenge2_playerroll = random.randint(1,20)
    challenge2_playertotal = challenge2_playerroll + character4_strength
    if challenge2_playertotal >= challenge2_total:
        challenge2_win = True
        character4_fatigued = True
        character4_lower = character4.lower()
        fatigued_characters.append(character4_lower)
        if int(character4_hp) < 4:
            character4_hp = int(character4_hp) + 1
    else:
        if int(character4_hp) > 0:
            character4_fatigued = True
        character4_lower = character4.lower()
        fatigued_characters.append(character4_lower)
        character4_hp = int(character4_hp) - 1
        if int(character4_hp) <= 0:
            character4_alive = False
            dead_characters.append(character4_lower)
            fatigued_characters.remove(character4_lower)
            challenge2_fatal = True
os.system('cls')
print("========== THE ADVENTURE BEGINS ==========")
if challenge1_player == characters[0]:
    character1_fatigued = False
    if character1 in fatigued_characters:
        fatigued_characters.remove(character1_lower)
elif challenge1_player == characters[1]:
    character2_fatigued = False
    if character2 in fatigued_characters:
        fatigued_characters.remove(character2_lower)
elif challenge1_player == characters[2]:
    character3_fatigued = False
    if character3 in fatigued_characters:
        fatigued_characters.remove(character3_lower)
elif challenge1_player == characters[3]:
    character4_fatigued = False
    if character4 in fatigued_characters:
        fatigued_characters.remove(character4_lower)
if character1_fatigued == True:
    character1_fatigued_pretty = "Y"
else:
    character1_fatigued_pretty = "N"
if character2_fatigued == True:
    character2_fatigued_pretty = "Y"
else:
    character2_fatigued_pretty = "N"
if character3_fatigued == True:
    character3_fatigued_pretty = "Y"
else:
    character3_fatigued_pretty = "N"
if character4_fatigued == True:
    character4_fatigued_pretty = "Y"
else:
    character4_fatigued_pretty = "N"
if challenge2_fatal == True:
    pos = characters.index(challenge2_player)
    characters.remove(challenge2_player)
    characters.insert(pos, "0")

if character1 in characters:
    print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp, " | Fatigued:", character1_fatigued_pretty)
if character2 in characters:
    print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp, " | Fatigued:", character2_fatigued_pretty)
if character3 in characters:
    print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp, " | Fatigued:", character3_fatigued_pretty)
if character4 in characters:
    print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp, " | Fatigued:", character4_fatigued_pretty)
print("")
if challenge2_fatal == False:
    if challenge2_win == True:
        challenge2_win_message = challenge2_player + " defeated the monster, beating the challenge, gaining 1HP and becoming fatigued so cannot play the next challenge." + "\n \n" + "You can see updated character stats in the output window."
        print(challenge2_win_message)
        messagebox.showinfo("Challenge 2", challenge2_win_message)
    elif challenge2_win == False:
        challenge2_loss_message = challenge2_player + " did not defeat the monster, narrowly escaping but losing 1HP and becoming fatigued so cannot play the next challenge." + "\n \n" + "You can see updated character stats in the output window."
        print(challenge2_loss_message)
        messagebox.showinfo("Challenge 2", challenge2_loss_message)
elif challenge2_fatal == True:
    challenge2_loss_message = challenge2_player + " did not defeat the monster, and was hurt, losing all HP. " + challenge2_player + " is now dead and cannot play on."
    print(challenge2_loss_message)
    messagebox.showinfo("Challenge 2", challenge2_loss_message)

if challenge1_player == characters[0]:
    character1_fatigued = False
    if character1 in fatigued_characters:
        fatigued_characters.remove(character1_lower)
elif challenge1_player == characters[1]:
    character2_fatigued = False
    if character2 in fatigued_characters:
        fatigued_characters.remove(character2_lower)
elif challenge1_player == characters[2]:
    character3_fatigued = False
    if character3 in fatigued_characters:
        fatigued_characters.remove(character3_lower)
elif challenge1_player == characters[3]:
    character4_fatigued = False
    if character4 in fatigued_characters:
        fatigued_characters.remove(character4_lower)
if character1_fatigued == True:
    character1_fatigued_pretty = "Y"
else:
    character1_fatigued_pretty = "N"
if character2_fatigued == True:
    character2_fatigued_pretty = "Y"
else:
    character2_fatigued_pretty = "N"
if character3_fatigued == True:
    character3_fatigued_pretty = "Y"
else:
    character3_fatigued_pretty = "N"
if character4_fatigued == True:
    character4_fatigued_pretty = "Y"
else:
    character4_fatigued_pretty = "N"
messagebox.showinfo("Challenge 2", "Press OK to continue to challenge 3")
os.system('cls')
print("========== THE ADVENTURE BEGINS ==========")
if character1 in characters:
    print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp, " | Fatigued:", character1_fatigued_pretty)
if character2 in characters:
    print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp, " | Fatigued:", character2_fatigued_pretty)
if character3 in characters:
    print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp, " | Fatigued:", character3_fatigued_pretty)
if character4 in characters:
    print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp, " | Fatigued:", character4_fatigued_pretty)
print("")

#-----------------------------------------------------------------------------------------------------      Challenge 3 agility
print("Welcome to the third challenge. Your party adventurers need to cross a narrow and unstable wooden bridge over a deep and rocky ravine without falling off.\n \nOne of them must go first.")
messagebox.showinfo("Challenge 3", "Welcome to the third challenge. Your party adventurers need to cross a narrow and unstable wooden bridge over a deep and rocky ravine without falling off.\n \nOne of them must go first.")
challenge3_player = None
challenge3_rating = random.randint(5,15)
challenge3_roll = random.randint(1,20)
challenge3_total = challenge3_rating + challenge3_roll
character1_agility = int(character1_agility)
character2_agility = int(character2_agility)
character3_agility = int(character3_agility)
character4_agility = int(character4_agility)
challenge3_win = False
while challenge3_player == None:
    challenge3_player = (turtle.textinput("Challenge 3", "Choose the character you wish to accept this agility based, third challenge:"))
    if challenge3_player != None:
        while challenge3_player in fatigued_characters or challenge3_player.lower() in fatigued_characters:
            challenge3_player = (turtle.textinput("Challenge 3", "The character you selected is fatigued and cannot play this challenge. Choose the character you wish to accept this first agility based challenge:"))
        while challenge3_player.lower() in dead_characters:
            challenge3_player = (turtle.textinput("Challenge 3", "The character you selected is dead and no longer exists in your party. Choose the character you wish to accept this first agility based challenge:"))
        if challenge3_player == "0":
            challenge3_player = None
        if challenge3_player.lower() in fatigued_characters:
            challenge3_player = None
        if challenge3_player not in characters:
            if challenge3_player not in characters_lower:
                challenge3_player = None
challenge3_player = challenge3_player.capitalize()
challenge3_message = "You selected " + challenge3_player + " to accept this challenge. \n \nClick OK to see the outcome of the challenge."
if challenge3_player == characters[0]:
    messagebox.showinfo("Challenge 3", challenge3_message)
    challenge3_playerroll = random.randint(1,20)
    challenge3_playertotal = challenge3_playerroll + character1_agility
    if challenge3_playertotal >= challenge3_total:
        challenge3_win = True
        character1_fatigued = True
        fatigued_characters.append(character1_lower)
        if int(character1_hp) < 4:
            character1_hp = int(character1_hp) + 1
    else:
        if int(character1_hp) > 0:
            character1_fatigued = True
            fatigued_characters.append(character1_lower)
            character1_hp = int(character1_hp) - 1
        if int(character1_hp) <= 0:
            character1_alive = False
            dead_characters.append(character1_lower)
            fatigued_characters.remove(character1_lower)
            challenge3_fatal = True
elif challenge3_player == characters[1]:
    messagebox.showinfo("Challenge 3", challenge3_message)
    challenge3_playerroll = random.randint(1,20)
    challenge3_playertotal = challenge3_playerroll + character2_agility
    if challenge3_playertotal >= challenge3_total:
        challenge3_win = True
        character2_fatigued = True
        fatigued_characters.append(character2_lower)
        character2_lower = character2.lower()
        if int(character2_hp) < 4:
            character2_hp = int(character2_hp) + 1
    else:
        if int(character2_hp) > 0:
            character2_fatigued = True
        character2_lower = character2.lower()
        fatigued_characters.append(character2_lower)
        character2_hp = int(character2_hp) - 1
        if int(character2_hp) <= 0:
            character2_alive = False
            dead_characters.append(character2_lower)
            fatigued_characters.remove(character2_lower)
            challenge3_fatal = True
elif challenge3_player == characters[2]:
    messagebox.showinfo("Challenge 3", challenge3_message)
    challenge3_playerroll = random.randint(1,20)
    challenge3_playertotal = challenge3_playerroll + character3_agility
    if challenge3_playertotal >= challenge3_total:
        challenge3_win = True
        character3_fatigued = True
        character3_lower = character3.lower()
        fatigued_characters.append(character3_lower)
        if int(character3_hp) < 4:
            character3_hp = int(character3_hp) + 1
    else:
        if int(character3_hp) > 0:
            character3_fatigued = True
        character3_lower = character3.lower()
        fatigued_characters.append(character3_lower)
        character3_hp = int(character3_hp) - 1
        if int(character3_hp) <= 0:
            character3_alive = False
            dead_characters.append(character3_lower)
            fatigued_characters.remove(character3_lower)
            challenge3_fatal = True
elif challenge3_player == characters[3]:
    messagebox.showinfo("Challenge 3", challenge3_message)
    challenge3_playerroll = random.randint(1,20)
    challenge3_playertotal = challenge3_playerroll + character4_agility
    if challenge3_playertotal >= challenge3_total:
        challenge3_win = True
        character4_fatigued = True
        character4_lower = character4.lower()
        fatigued_characters.append(character4_lower)
        if int(character4_hp) < 4:
            character4_hp = int(character4_hp) + 1
    else:
        if int(character4_hp) > 0:
            character4_fatigued = True
        character4_lower = character4.lower()
        fatigued_characters.append(character4_lower)
        character4_hp = int(character4_hp) - 1
        if int(character4_hp) <= 0:
            character4_alive = False
            dead_characters.append(character4_lower)
            fatigued_characters.remove(character4_lower)
            challenge3_fatal = True
os.system('cls')
print("========== THE ADVENTURE BEGINS ==========")
if challenge2_player == characters[0]:
    character1_fatigued = False
    if character1 in fatigued_characters:
        fatigued_characters.remove(character1_lower)
elif challenge2_player == characters[1]:
    character2_fatigued = False
    if character2 in fatigued_characters:
        fatigued_characters.remove(character2_lower)
elif challenge2_player == characters[2]:
    character3_fatigued = False
    if character3 in fatigued_characters:
        fatigued_characters.remove(character3_lower)
elif challenge2_player == characters[3]:
    character4_fatigued = False
    if character4 in fatigued_characters:
        fatigued_characters.remove(character4_lower)
if character1_fatigued == True:
    character1_fatigued_pretty = "Y"
else:
    character1_fatigued_pretty = "N"
if character2_fatigued == True:
    character2_fatigued_pretty = "Y"
else:
    character2_fatigued_pretty = "N"
if character3_fatigued == True:
    character3_fatigued_pretty = "Y"
else:
    character3_fatigued_pretty = "N"
if character4_fatigued == True:
    character4_fatigued_pretty = "Y"
else:
    character4_fatigued_pretty = "N"
if challenge3_fatal == True:
    pos = characters.index(challenge3_player)
    characters.remove(challenge3_player)
    characters.insert(pos, "0")

if character1 in characters:
    print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp, " | Fatigued:", character1_fatigued_pretty)
if character2 in characters:
    print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp, " | Fatigued:", character2_fatigued_pretty)
if character3 in characters:
    print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp, " | Fatigued:", character3_fatigued_pretty)
if character4 in characters:
    print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp, " | Fatigued:", character4_fatigued_pretty)
print("")
if challenge3_fatal == False:
    if challenge3_win == True:
        challenge3_win_message = challenge3_player + " crossed the bridge safely, beating the challenge, gaining 1HP but becoming fatigued so cannot play the next challenge." + "\n \n" + "You can see updated character stats in the output window."
        print(challenge3_win_message)
        messagebox.showinfo("Challenge 3", challenge3_win_message)
    elif challenge3_win == False:
        challenge3_loss_message = challenge3_player + " slipped off the bridge, narrowly avoiding death but reached the other side, losing 1HP and becoming fatigued so cannot play the next challenge." + "\n \n" + "You can see updated character stats in the output window."
        print(challenge3_loss_message)
        messagebox.showinfo("Challenge 3", challenge3_loss_message)
elif challenge3_fatal == True:
    challenge3_loss_message = challenge3_player + " slipped off the bridge and fell. " + challenge3_player + " is now dead and cannot play on."
    print(challenge3_loss_message)
    messagebox.showinfo("Challenge 3", challenge3_loss_message)


if challenge2_player == characters[0]:
    character1_fatigued = False
    if character1 in fatigued_characters:
        fatigued_characters.remove(character1_lower)
elif challenge2_player == characters[1]:
    character2_fatigued = False
    if character2 in fatigued_characters:
        fatigued_characters.remove(character2_lower)
elif challenge2_player == characters[2]:
    character3_fatigued = False
    if character3 in fatigued_characters:
        fatigued_characters.remove(character3_lower)
elif challenge2_player == characters[3]:
    character4_fatigued = False
    if character4 in fatigued_characters:
        fatigued_characters.remove(character4_lower)
if character1_fatigued == True:
    character1_fatigued_pretty = "Y"
else:
    character1_fatigued_pretty = "N"
if character2_fatigued == True:
    character2_fatigued_pretty = "Y"
else:
    character2_fatigued_pretty = "N"
if character3_fatigued == True:
    character3_fatigued_pretty = "Y"
else:
    character3_fatigued_pretty = "N"
if character4_fatigued == True:
    character4_fatigued_pretty = "Y"
else:
    character4_fatigued_pretty = "N"
messagebox.showinfo("Challenge 4", "Press OK to continue to challenge 4")
os.system('cls')
print("========== THE ADVENTURE BEGINS ==========")
if character1 in characters:
    print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp, " | Fatigued:", character1_fatigued_pretty)
if character2 in characters:
    print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp, " | Fatigued:", character2_fatigued_pretty)
if character3 in characters:
    print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp, " | Fatigued:", character3_fatigued_pretty)
if character4 in characters:
    print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp, " | Fatigued:", character4_fatigued_pretty)
print("")

#--------------- END OF CHALLENGE 3

#                                                    SHOULD BE REPEATED FROM HERE
# CHECKING CHARACTERS THAT REMAIN BETWEEN C3 and C4
death_toll = len(dead_characters)
if death_toll == 3:
    default_select = True
if death_toll == 4:
    game_fail = True

#-----------------------------------------------------------------------------------------------------      Challenge 4 magic
#Checks for zero characters remaining
if game_fail == True:
    os.system('cls')
    print("========== GAME OVER ==========")
    game_fail_message = "Your entire party of adventurers have died - no data will be saved. \n\nPress OK to end the game."
    print(game_fail_message)
    messagebox.showinfo("GAME OVER", game_fail_message)
    os.system('cls')
    print("Thanks for playing.")
    messagebox.showinfo("GAME OVER", "Thanks for playing.")
    quit()

print("Welcome to the fourth challenge. One of your adventurers must use a spell to create a diversion or distraction to avoid detection by enemies.")
messagebox.showinfo("Challenge 4", "Welcome to the fourth challenge. One of your adventurers must use a spell to create a diversion or distraction to avoid detection by enemies.")
challenge4_player = None
challenge4_rating = random.randint(5,15)
challenge4_roll = random.randint(1,20)
challenge4_total = challenge4_rating + challenge4_roll
character1_magic = int(character1_magic)
character2_magic = int(character2_magic)
character3_magic = int(character3_magic)
character4_magic = int(character4_magic)
challenge4_win = False
if default_select == True:
    if character1_alive == True:
        challenge4_player = character1
    elif character2_alive == True:
        challenge4_player = character2
    elif character3_alive == True:
        challenge4_player = character3
    elif character4_alive == True:
        challenge4_player = character4
while challenge4_player == None:
    challenge4_player = (turtle.textinput("Challenge 4", "Choose the character you wish to accept this magic based, fourth challenge:"))
    if challenge4_player != None:
        while challenge4_player in fatigued_characters or challenge4_player.lower() in fatigued_characters:
            challenge4_player = (turtle.textinput("Challenge 4", "The character you selected is fatigued and cannot play this challenge. Choose the character you wish to accept this first magic based challenge:"))
        while challenge4_player.lower() in dead_characters:
            challenge4_player = (turtle.textinput("Challenge 4", "The character you selected is dead and no longer exists in your party. Choose the character you wish to accept this first magic based challenge:"))
        if challenge4_player == "0":
            challenge4_player = None
        if challenge4_player.lower() in fatigued_characters:
            challenge4_player = None
        if challenge4_player not in characters:
            if challenge4_player not in characters_lower:
                challenge4_player = None
challenge4_player = challenge4_player.capitalize()
if default_select == True:
    challenge4_message = "You selected your final character remaining, " + challenge4_player + " to accept this challenge. \n \nClick OK to see the outcome of the challenge."
else:
    challenge4_message = "You selected " + challenge4_player + " to accept this challenge. \n \nClick OK to see the outcome of the challenge."
if challenge4_player == characters[0]:
    messagebox.showinfo("Challenge 4", challenge4_message)
    challenge4_playerroll = random.randint(1,20)
    challenge4_playertotal = challenge4_playerroll + character1_magic
    if challenge4_playertotal >= challenge4_total:
        challenge4_win = True
        character1_fatigued = True
        fatigued_characters.append(character1_lower)
        if int(character1_hp) < 4:
            character1_hp = int(character1_hp) + 1
    else:
        if int(character1_hp) > 0:
            character1_fatigued = True
            fatigued_characters.append(character1_lower)
            character1_hp = int(character1_hp) - 1
        if int(character1_hp) <= 0:
            character1_alive = False
            dead_characters.append(character1_lower)
            fatigued_characters.remove(character1_lower)
            challenge4_fatal = True
elif challenge4_player == characters[1]:
    messagebox.showinfo("Challenge 4", challenge4_message)
    challenge4_playerroll = random.randint(1,20)
    challenge4_playertotal = challenge4_playerroll + character2_magic
    if challenge4_playertotal >= challenge4_total:
        challenge4_win = True
        character2_fatigued = True
        character2_lower = character2.lower()
        fatigued_characters.append(character2_lower)
        if int(character2_hp) < 4:
            character2_hp = int(character2_hp) + 1
    else:
        if int(character2_hp) > 0:
            character2_fatigued = True
        character2_lower = character2.lower()
        fatigued_characters.append(character2_lower)
        character2_hp = int(character2_hp) - 1
        if int(character2_hp) <= 0:
            character2_alive = False
            dead_characters.append(character2_lower)
            fatigued_characters.remove(character2_lower)
            challenge4_fatal = True
elif challenge4_player == characters[2]:
    messagebox.showinfo("Challenge 4", challenge4_message)
    challenge4_playerroll = random.randint(1,20)
    challenge4_playertotal = challenge4_playerroll + character3_magic
    if challenge4_playertotal >= challenge4_total:
        challenge4_win = True
        character3_fatigued = True
        character3_lower = character3.lower()
        fatigued_characters.append(character3_lower)
        if int(character3_hp) < 4:
            character3_hp = int(character3_hp) + 1
    else:
        if int(character3_hp) > 0:
            character3_fatigued = True
        character3_lower = character3.lower()
        fatigued_characters.append(character3_lower)
        character3_hp = int(character3_hp) - 1
        if int(character3_hp) <= 0:
            character3_alive = False
            dead_characters.append(character3_lower)
            fatigued_characters.remove(character3_lower)
            challenge4_fatal = True
elif challenge4_player == characters[3]:
    messagebox.showinfo("Challenge 4", challenge4_message)
    challenge4_playerroll = random.randint(1,20)
    challenge4_playertotal = challenge4_playerroll + character4_magic
    if challenge4_playertotal >= challenge4_total:
        challenge4_win = True
        character4_fatigued = True
        character4_lower = character4.lower()
        fatigued_characters.append(character4_lower)
        if int(character4_hp) < 4:
            character4_hp = int(character4_hp) + 1
    else:
        if int(character4_hp) > 0:
            character4_fatigued = True
        character4_lower = character4.lower()
        fatigued_characters.append(character4_lower)
        character4_hp = int(character4_hp) - 1
        if int(character4_hp) <= 0:
            character4_alive = False
            dead_characters.append(character4_lower)
            fatigued_characters.remove(character4_lower)
            challenge4_fatal = True
os.system('cls')
print("========== THE ADVENTURE BEGINS ==========")
if challenge3_player == characters[0]:
    character1_fatigued = False
    if character1 in fatigued_characters:
        fatigued_characters.remove(character1_lower)
elif challenge3_player == characters[1]:
    character2_fatigued = False
    if character2 in fatigued_characters:
        fatigued_characters.remove(character2_lower)
elif challenge3_player == characters[2]:
    character3_fatigued = False
    if character3 in fatigued_characters:
        fatigued_characters.remove(character3_lower)
elif challenge3_player == characters[3]:
    character4_fatigued = False
    if character4 in fatigued_characters:
        fatigued_characters.remove(character4_lower)
if character1_fatigued == True:
    character1_fatigued_pretty = "Y"
else:
    character1_fatigued_pretty = "N"
if character2_fatigued == True:
    character2_fatigued_pretty = "Y"
else:
    character2_fatigued_pretty = "N"
if character3_fatigued == True:
    character3_fatigued_pretty = "Y"
else:
    character3_fatigued_pretty = "N"
if character4_fatigued == True:
    character4_fatigued_pretty = "Y"
else:
    character4_fatigued_pretty = "N"
if challenge4_fatal == True:
    pos = characters.index(challenge4_player)
    characters.remove(challenge4_player)
    characters.insert(pos, "0")

if character1 in characters:
    print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp, " | Fatigued:", character1_fatigued_pretty)
if character2 in characters:
    print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp, " | Fatigued:", character2_fatigued_pretty)
if character3 in characters:
    print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp, " | Fatigued:", character3_fatigued_pretty)
if character4 in characters:
    print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp, " | Fatigued:", character4_fatigued_pretty)
print("")
if challenge4_fatal == False:
    if challenge4_win == True:
        challenge4_win_message = challenge4_player + " completed the spell perfectly, beating the challenge, gaining 1HP but becoming fatigued so cannot play the next challenge." + "\n \n" + "You can see updated character stats in the output window."
        print(challenge4_win_message)
        messagebox.showinfo("Challenge 4", challenge4_win_message)
    elif challenge4_win == False:
        challenge4_loss_message = challenge4_player + " messed up the spell, narrowly avoiding detection and attack by enemies, losing 1HP and becoming fatigued so cannot play the next challenge." + "\n \n" + "You can see updated character stats in the output window."
        print(challenge4_loss_message)
        messagebox.showinfo("Challenge 4", challenge4_loss_message)
elif challenge4_fatal == True:
    challenge4_loss_message = challenge4_player + " messed up the spell and was killed by enemies. " + challenge4_player + " is now dead and cannot play on."
    print(challenge4_loss_message)
    messagebox.showinfo("Challenge 4", challenge4_loss_message)

if challenge3_player == characters[0]:
    if character1 in fatigued_characters:
        fatigued_characters.remove(character1_lower)
    character1_fatigued = False
elif challenge3_player == characters[1]:
    if character2 in fatigued_characters:
        fatigued_characters.remove(character2_lower)
    character2_fatigued = False
elif challenge3_player == characters[2]:
    if character3 in fatigued_characters:
        fatigued_characters.remove(character3_lower)
    character3_fatigued = False
elif challenge3_player == characters[3]:
    if character4 in fatigued_characters:
        fatigued_characters.remove(character4_lower)
    character4_fatigued = False
if character1_fatigued == True:
    character1_fatigued_pretty = "Y"
else:
    character1_fatigued_pretty = "N"
if character2_fatigued == True:
    character2_fatigued_pretty = "Y"
else:
    character2_fatigued_pretty = "N"
if character3_fatigued == True:
    character3_fatigued_pretty = "Y"
else:
    character3_fatigued_pretty = "N"
if character4_fatigued == True:
    character4_fatigued_pretty = "Y"
else:
    character4_fatigued_pretty = "N"
messagebox.showinfo("Challenge 5", "Press OK to continue to challenge 5")
os.system('cls')
print("========== THE ADVENTURE BEGINS ==========")
if character1 in characters:
    print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp, " | Fatigued:", character1_fatigued_pretty)
if character2 in characters:
    print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp, " | Fatigued:", character2_fatigued_pretty)
if character3 in characters:
    print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp, " | Fatigued:", character3_fatigued_pretty)
if character4 in characters:
    print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp, " | Fatigued:", character4_fatigued_pretty)
print("")

#----------------- END OF C4

# CHECKING CHARACTERS THAT REMAIN
death_toll = len(dead_characters)
if death_toll == 3:
    default_select = True
if death_toll == 4:
    game_fail = True

#-----------------------------------------------------------------------------------------------------      Challenge 5 agility
#Checks for zero characters remaining
if game_fail == True:
    os.system('cls')
    print("========== GAME OVER ==========")
    game_fail_message = "Your entire party of adventurers have died - no data will be saved. \n\n Press OK to end the game."
    print(game_fail_message)
    messagebox.showinfo("GAME OVER", game_fail_message)
    os.system('cls')
    print("Thanks for playing.")
    messagebox.showinfo("GAME OVER", "Thanks for playing.")
    quit()

print("Welcome to the fifth challenge. One of your adventurers must climb a tree to get a better view of the path ahead.")
messagebox.showinfo("Challenge 5", "Welcome to the fifth challenge. One of your adventurers must climb a tree to get a better view of the path ahead.")
challenge5_player = None
challenge5_rating = random.randint(5,15)
challenge5_roll = random.randint(1,20)
challenge5_total = challenge5_rating + challenge5_roll
character1_agility = int(character1_agility)
character2_agility = int(character2_agility)
character3_agility = int(character3_agility)
character4_agility = int(character4_agility)
challenge5_win = False
if default_select == True:
    if character1_alive == True:
        challenge5_player = character1
    elif character2_alive == True:
        challenge5_player = character2
    elif character3_alive == True:
        challenge5_player = character3
    elif character4_alive == True:
        challenge5_player = character4
while challenge5_player == None:
    challenge5_player = (turtle.textinput("Challenge 5", "Choose the character you wish to accept this agility based, fifth challenge:"))
    if challenge5_player != None:
        while challenge5_player in fatigued_characters or challenge5_player.lower() in fatigued_characters:
            challenge5_player = (turtle.textinput("Challenge 5", "The character you selected is fatigued and cannot play this challenge. Choose the character you wish to accept this first agility based challenge:"))
        while challenge5_player.lower() in dead_characters:
            challenge5_player = (turtle.textinput("Challenge 5", "The character you selected is dead and no longer exists in your party. Choose the character you wish to accept this first agility based challenge:"))
        if challenge5_player == "0":
            challenge5_player = None
        if challenge5_player.lower() in fatigued_characters:
            challenge5_player = None
        if challenge5_player not in characters:
            if challenge5_player not in characters_lower:
                challenge5_player = None
challenge5_player = challenge5_player.capitalize()
if default_select == True:
    challenge5_message = "You selected your final character remaining, " + challenge5_player + " to accept this challenge. \n \nClick OK to see the outcome of the challenge."
else:
    challenge5_message = "You selected " + challenge5_player + " to accept this challenge. \n \nClick OK to see the outcome of the challenge."
if challenge5_player == characters[0]:
    messagebox.showinfo("Challenge 5", challenge5_message)
    challenge5_playerroll = random.randint(1,20)
    challenge5_playertotal = challenge5_playerroll + character1_agility
    if challenge5_playertotal >= challenge5_total:
        challenge5_win = True
        character1_fatigued = True
        fatigued_characters.append(character1_lower)
        if int(character1_hp) < 4:
            character1_hp = int(character1_hp) + 1
    else:
        if int(character1_hp) > 0:
            character1_fatigued = True
            fatigued_characters.append(character1_lower)
            character1_hp = int(character1_hp) - 1
        if int(character1_hp) <= 0:
            character1_alive = False
            dead_characters.append(character1_lower)
            fatigued_characters.remove(character1_lower)
            challenge5_fatal = True
elif challenge5_player == characters[1]:
    messagebox.showinfo("Challenge 5", challenge5_message)
    challenge5_playerroll = random.randint(1,20)
    challenge5_playertotal = challenge5_playerroll + character2_agility
    if challenge5_playertotal >= challenge5_total:
        challenge5_win = True
        character2_fatigued = True
        character2_lower = character2.lower()
        fatigued_characters.append(character2_lower)
        if int(character2_hp) < 4:
            character2_hp = int(character2_hp) + 1
    else:
        if int(character2_hp) > 0:
            character2_fatigued = True
        character2_lower = character2.lower()
        fatigued_characters.append(character2_lower)
        character2_hp = int(character2_hp) - 1
        if int(character2_hp) <= 0:
            character2_alive = False
            dead_characters.append(character2_lower)
            fatigued_characters.remove(character2_lower)
            challenge5_fatal = True
elif challenge5_player == characters[2]:
    messagebox.showinfo("Challenge 5", challenge5_message)
    challenge5_playerroll = random.randint(1,20)
    challenge5_playertotal = challenge5_playerroll + character3_agility
    if challenge5_playertotal >= challenge5_total:
        challenge5_win = True
        character3_fatigued = True
        character3_lower = character3.lower()
        fatigued_characters.append(character3_lower)
        if int(character3_hp) < 4:
            character3_hp = int(character3_hp) + 1
    else:
        if int(character3_hp) > 0:
            character3_fatigued = True
        character3_lower = character3.lower()
        fatigued_characters.append(character3_lower)
        character3_hp = int(character3_hp) - 1
        if int(character3_hp) <= 0:
            character3_alive = False
            dead_characters.append(character3_lower)
            fatigued_characters.remove(character3_lower)
            challenge5_fatal = True
elif challenge5_player == characters[3]:
    messagebox.showinfo("Challenge 5", challenge5_message)
    challenge5_playerroll = random.randint(1,20)
    challenge5_playertotal = challenge5_playerroll + character4_agility
    if challenge5_playertotal >= challenge5_total:
        challenge5_win = True
        character4_fatigued = True
        character4_lower = character4.lower()
        fatigued_characters.append(character4_lower)
        if int(character4_hp) < 4:
            character4_hp = int(character4_hp) + 1
    else:
        if int(character4_hp) > 0:
            character4_fatigued = True
        character4_lower = character4.lower()
        fatigued_characters.append(character4_lower)
        character4_hp = int(character4_hp) - 1
        if int(character4_hp) <= 0:
            character4_alive = False
            dead_characters.append(character4_lower)
            fatigued_characters.remove(character4_lower)
            challenge5_fatal = True
os.system('cls')
print("========== THE ADVENTURE BEGINS ==========")
if challenge4_player == characters[0]:
    character1_fatigued = False
    if character1 in fatigued_characters:
        fatigued_characters.remove(character1_lower)
elif challenge4_player == characters[1]:
    character2_fatigued = False
    if character2 in fatigued_characters:
        fatigued_characters.remove(character2_lower)
elif challenge4_player == characters[2]:
    character3_fatigued = False
    if character3 in fatigued_characters:
        fatigued_characters.remove(character3_lower)
elif challenge4_player == characters[3]:
    character4_fatigued = False
    if character4 in fatigued_characters:
        fatigued_characters.remove(character4_lower)
if character1_fatigued == True:
    character1_fatigued_pretty = "Y"
else:
    character1_fatigued_pretty = "N"
if character2_fatigued == True:
    character2_fatigued_pretty = "Y"
else:
    character2_fatigued_pretty = "N"
if character3_fatigued == True:
    character3_fatigued_pretty = "Y"
else:
    character3_fatigued_pretty = "N"
if character4_fatigued == True:
    character4_fatigued_pretty = "Y"
else:
    character4_fatigued_pretty = "N"
if challenge5_fatal == True:
    pos = characters.index(challenge5_player)
    characters.remove(challenge5_player)
    characters.insert(pos, "0")

if character1 in characters:
    print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp, " | Fatigued:", character1_fatigued_pretty)
if character2 in characters:
    print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp, " | Fatigued:", character2_fatigued_pretty)
if character3 in characters:
    print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp, " | Fatigued:", character3_fatigued_pretty)
if character4 in characters:
    print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp, " | Fatigued:", character4_fatigued_pretty)
print("")
if challenge5_fatal == False:
    if challenge5_win == True:
        challenge5_win_message = challenge5_player + " made it to the top and back down safely, gaining 1HP but becoming fatigued so cannot play the next challenge." + "\n \n" + "You can see updated character stats in the output window."
        print(challenge5_win_message)
        messagebox.showinfo("Challenge 5", challenge5_win_message)
    elif challenge5_win == False:
        challenge5_loss_message = challenge5_player + " was injured on the way back down, falling part of the way, losing 1HP and becoming fatigued so cannot play the next challenge." + "\n \n" + "You can see updated character stats in the output window."
        print(challenge5_loss_message)
        messagebox.showinfo("Challenge 5", challenge5_loss_message)
elif challenge5_fatal == True:
    challenge5_loss_message = challenge5_player + " slipped from the top of the tree and was killed. " + challenge5_player + " is now dead and cannot play on."
    print(challenge5_loss_message)
    messagebox.showinfo("Challenge 5", challenge5_loss_message)
if challenge4_player == characters[0]:
    if character1 in fatigued_characters:
        fatigued_characters.remove(character1_lower)
    character1_fatigued = False
elif challenge4_player == characters[1]:
    if character2 in fatigued_characters:
        fatigued_characters.remove(character2_lower)
    character2_fatigued = False
elif challenge4_player == characters[2]:
    if character3 in fatigued_characters:
        fatigued_characters.remove(character3_lower)
    character3_fatigued = False
elif challenge4_player == characters[3]:
    if character4 in fatigued_characters:
        fatigued_characters.remove(character4_lower)
    character4_fatigued = False
if character1_fatigued == True:
    character1_fatigued_pretty = "Y"
else:
    character1_fatigued_pretty = "N"
if character2_fatigued == True:
    character2_fatigued_pretty = "Y"
else:
    character2_fatigued_pretty = "N"
if character3_fatigued == True:
    character3_fatigued_pretty = "Y"
else:
    character3_fatigued_pretty = "N"
if character4_fatigued == True:
    character4_fatigued_pretty = "Y"
else:
    character4_fatigued_pretty = "N"
messagebox.showinfo("Challenge 6", "Press OK to continue to challenge 6")
os.system('cls')
print("========== THE ADVENTURE BEGINS ==========")
if character1 in characters:
    print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp, " | Fatigued:", character1_fatigued_pretty)
if character2 in characters:
    print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp, " | Fatigued:", character2_fatigued_pretty)
if character3 in characters:
    print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp, " | Fatigued:", character3_fatigued_pretty)
if character4 in characters:
    print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp, " | Fatigued:", character4_fatigued_pretty)
print("")
#END OF C5


# CHECKING CHARACTERS THAT REMAIN
death_toll = len(dead_characters)
if death_toll == 3:
    default_select = True
if death_toll == 4:
    game_fail = True

if game_fail == True:
    os.system('cls')
    print("========== GAME OVER ==========")
    game_fail_message = "Your entire party of adventurers have died - no data will be saved. \n\n Press OK to end the game."
    print(game_fail_message)
    messagebox.showinfo("GAME OVER", game_fail_message)
    os.system('cls')
    print("Thanks for playing.")
    messagebox.showinfo("GAME OVER", "Thanks for playing.")
    quit()

messagebox.showinfo("Game complete", "Press OK to proceed to complete the game and save your party of adventurers still alive.")
os.system('cls')
print("========== FINISHING STATS ==========")
if character1 in characters:
    print(character1 + ":", "Strength:", character1_strength, " | Agility:", character1_agility, " | Magic:", character1_magic, " | Luck:", character1_luck, " | HP:", character1_hp)
if character2 in characters:
    print(character2 + ":", "Strength:", character2_strength, " | Agility:", character2_agility, " | Magic:", character2_magic, " | Luck:", character2_luck, " | HP:", character2_hp)
if character3 in characters:
    print(character3 + ":", "Strength:", character3_strength, " | Agility:", character3_agility, " | Magic:", character3_magic, " | Luck:", character3_luck, " | HP:", character3_hp)
if character4 in characters:
    print(character4 + ":", "Strength:", character4_strength, " | Agility:", character4_agility, " | Magic:", character4_magic, " | Luck:", character4_luck, " | HP:", character4_hp)
print("")
#C8 over
#proceed to game evaluation screen and saving
alive = 4 - (len(dead_characters))
if alive == 4:
    print("Congratulations! You completed the game with a full party of 4 adventurers!")
    messagebox.showinfo("Well done", "Congratulations! You completed the game with a full party of 4 adventurers!")
elif alive == 3:
    print("Very well done! You completed the game with a party of 3 adventurers making it through!")
    messagebox.showinfo("Well done", "Very well done! You completed the game with a party of 3 adventurers making it through!")
elif alive == 2:
    print("Well done! You completed the game with two of your party making it through!")
    messagebox.showinfo("Well done", "Well done! You completed the game with two of your party making it through!")
elif alive == 1:
    print("Good effort! You completed the game with one of your adventurers making it through!")
    messagebox.showinfo("Well done", "Good effort! You completed the game with one of your adventurers making it through!")
messagebox.showinfo("Continue to save...", "Press OK to save your game.")
os.system('cls')
print("Game saving, please wait...")
time.sleep(1.5)
#saving
f.close()
dir_path2 = os.path.join(os.path.dirname(__file__), "saves")
file_path2 = os.path.join(dir_path, savefile)
f = open(file_path2, "w")
if character1_alive == True:
    f.write(character1 + "\n")
    f.write(str(character1_strength) + "\n")
    f.write(str(character1_agility) + "\n")
    f.write(str(character1_magic) + "\n")
    f.write(str(character1_luck) + "\n")
    f.write(str(character1_hp) + "\n")
if character2_alive == True:
    f.write(character2 + "\n")
    f.write(str(character2_strength) + "\n")
    f.write(str(character2_agility) + "\n")
    f.write(str(character2_magic) + "\n")
    f.write(str(character2_luck) + "\n")
    f.write(str(character2_hp) + "\n")
if character3_alive == True:
    f.write(character3 + "\n")
    f.write(str(character3_strength) + "\n")
    f.write(str(character3_agility) + "\n")
    f.write(str(character3_magic) + "\n")
    f.write(str(character3_luck) + "\n")
    f.write(str(character3_hp) + "\n")
if character4_alive == True:
    f.write(character4 + "\n")
    f.write(str(character4_strength) + "\n")
    f.write(str(character4_agility) + "\n")
    f.write(str(character4_magic) + "\n")
    f.write(str(character4_luck) + "\n")
    f.write(str(character4_hp) + "\n")
f.close()
messagebox.showinfo("Game saved", "Game successfully saved.")
os.system('cls')
print("Thank you for playing.")
print("Oliver Ricketts 2023")
messagebox.showinfo("Game over", "Thank you for playing.")