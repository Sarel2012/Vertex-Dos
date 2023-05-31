import os
def user():
    makeUser()


def separator(name):
    os.system("cls")
    print("+--------------- " + name + " ---------------+")


def edit():
    file = input("Which file do you want to edit? ")
    with open(file, 'w+') as f:
        filetext = ("")
        for line in f:
            filetext += line
        f.write(filetext)

def fopen():
    separator("Opening File")
    file = input("Open: ")
    print("")
    with open(file, 'r') as f:
        for line in f:
            print(line)
            print("")
    editredirect()


def editredirect():
    separator("Editing")
    print("You can edit this file with the 'edit' command.")
    dcmdLvl2()


def cr():
    directoryName = input("Name of directory: ")
    os.mkdir(directoryName)
    if not os.path.exists(directoryName):
        os.mkdir(directoryName)
        dcmdLvl2()


def cd():
    separator("Open Folder")
    changedDIR = input("Directory name: ")
    os.chdir(changedDIR)
    if not os.path.exists(changedDIR):
        print("Directory not found.")
        dcmdLvl2()


def rem():
    separator("Remove File")
    selectFile = input("Which file do you want to delete? ")
    os.remove(selectFile)


def cmdLvl2():
    separator("CMD")
    print(
        "Use the 'leave' command to shut down the system. Use the 'type' command to start a text editor. You can also type 'clear' to clear the screen. Type 'help -a' for more options.")
    tcmdLvl2 = input("~$: ")
    if tcmdLvl2 == ("leave"):
        quit()
    if tcmdLvl2 == ("type"):
        typer()
    if tcmdLvl2 == ("clear"):
        os.system('cls')
    if tcmdLvl2 == (""):
        dcmdLvl2()
    if tcmdLvl2 == ("help -a"):
        print(
            "You can use the command 'cr' to make a new directory. Use the 'cd' command to access this directory. Additionally, use 'list' to show all sub-folders in your current directory or use 'show' to see your current directory. You can also use 'rem' to remove a file.")
        dcmdLvl2()
    if tcmdLvl2 == ("cr"):
        cr()
    if tcmdLvl2 == ("cd"):
        cd()
    if tcmdLvl2 == ("list"):
        os.system('dir')
    if tcmdLvl2 == ("show"):
        print(os.getcwd())
    if tcmdLvl2 == ("rem"):
        rem()
    if tcmdLvl2 == ("open"):
        fopen()
    if tcmdLvl2 == ("edit"):
        edit()
    if tcmdLvl2 == ("help"):
        cmdLvl2()
    if tcmdLvl2 == ("user"):
        user()
    if tcmdLvl2 not in (
    "leave", "type", "clear", "", "help", "help -a", "cr", "cd", "list", "show", "rem", "open", "edit", "user"):
        print("Command not found.")
    dcmdLvl2()


def dcmdLvl2():
    separator("CMD")
    tcmdLvl2 = input("~$: ")
    if tcmdLvl2 == ("leave"):
        quit()
    if tcmdLvl2 == ("type"):
        typer()
    if tcmdLvl2 == ("clear"):
        os.system('cls')
    if tcmdLvl2 == (""):
        dcmdLvl2()
    if tcmdLvl2 == ("help"):
        cmdLvl2()
    if tcmdLvl2 == ("cr"):
        cr()
    if tcmdLvl2 == ("cd"):
        cd()
    if tcmdLvl2 == ("list"):
        os.system('dir')
    if tcmdLvl2 == ("show"):
        print(os.getcwd())
    if tcmdLvl2 == ("rem"):
        rem()
    if tcmdLvl2 == ("open"):
        fopen()
    if tcmdLvl2 == ("edit"):
        edit()
    if tcmdLvl2 == ("user"):
        user()
    if tcmdLvl2 == ("help -a"):
        print(
            "You can use the command 'cr' to make a new directory. Use the 'cd' command to access this directory. Additionally, use 'list' to show all sub-folders in your current directory or use 'show' to see your current directory. You can also use 'rem' to remove a file.")
        dcmdLvl2()
    if tcmdLvl2 not in (
    "leave", "type", "clear", "", "help", "help -a", "cr", "cd", "list", "show", "rem", "open", "edit", "user"):
        print("Command not found.")
    dcmdLvl2()


def typer():
    separator("Typer")
    print("")
    print("Start typing to begin.")
    typerCMD = input("  ")
    saveAs = input("Save file as: ")
    if saveAs == (""):
        dcmdLvl2()
    with open(saveAs, 'w') as f:
        f.write(typerCMD)
    print("")
    print("You can access this file with the 'open' command.")
    print("")
    dcmdLvl2()


def CMDLine():
    separator("CMD")
    print("Hello, and welcome to your new operating system. Type 'help' to get started.")
    cmd = input("~$: ")
    if cmd == ("leave"):
        quit()
    if cmd == ("type"):
        typer()
    if cmd == ("clear"):
        os.system('cls')
    if cmd == (""):
        dcmdLvl2()
    if cmd == ("help"):
        cmdLvl2()
    if cmd == ("cr"):
        cr()
    if cmd == ("cd"):
        cd()
    if cmd == ("list"):
        os.system('dir')
    if cmd == ("show"):
        print(os.getcwd())
    if cmd == ("rem"):
        rem()
    if cmd == ("help -a"):
        print(
            "You can use the command 'cr' to make a new directory. Use the 'cd' command to access this directory. Additionally, use 'list' to show all sub-folders in your current directory or use 'show' to see your current directory. You can also use 'rem' to remove a file.")
    if cmd == ("open"):
        fopen()
    if cmd == ("edit"):
        edit()
    if cmd == ("user"):
        user()
    if cmd not in (
    "leave", "type", "clear", "", "help", "help -a", "cr", "cd", "list", "show", "rem", "open", "edit", "user"):
        print("Command not found.")
    dcmdLvl2()


def redirect():
    signIn()


def mUserRedirect():
    makeUser()


def PwordSignIn():
    rPword = input("Password: ")
    with open('passwords.txt', 'r') as f:
        for line in f:
            if rPword == (line):
                CMDLine()
            else:
                print("Incorrect password.")
                signIn()


def signIn():
    separator("Sign In")
    rUname = input("Username: ")
    with open('usernames.txt', 'r') as f:
        for line in f:
            if rUname == (line):
                PwordSignIn()
            else:
                print("Username not found.")
                mUserRedirect()


def makeUser():
    separator("New User")
    nUname = input("New username: ")
    nPword = input("Create a password for the user: ")

    with open('usernames.txt', 'w') as f:
        f.write(nUname)
    with open('passwords.txt', 'w') as f:
        f.write(nPword)
    signIn()


def start():
    print("Create a new user? Warning: This will delete any other users. (Y/N): ")
    nUser = input(" ")
    if nUser == ("N"):
        signIn()
    if nUser == ("n"):
        signIn()
    if nUser == ("Y"):
        makeUser()
    if nUser == ("y"):
        makeUser()
    elif nUser == ("Sarel"):
        print("Sarel is a really great Dev. He know how tu use perfectly python and he likes Sythwave music ")
        start()
    elif nUser == ("Sfaltrax"):
        print("Sfaltrax is a YouTuber and dev, passionate of video games and Programming languages. He is from the Studio Dev Team")
        start()
    else:
        start()

os.system("cls")
print("\t**********************************************")
print("\t***        VERTEX DOS 0.2 BETA             ***")
print("\t**********************************************")
start()
