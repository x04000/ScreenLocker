import tkinter as UI
from getpass import getpass

try:
    import os
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')
except:
    print("\n")
try:
    print("""\x1b[38;2;0;255;251m
 ▄▀▀▀▄
 █   █      ____                     __                 __          
███████    / __/__________ ___ ___  / /  ___  ___  ____/ /_____ ____
███████   _\ \/ __/ __/ -_) -_) _ \/ /__/ _ \/ _ \/ __/  '_/ -_) __/
███████  /___/\__/_/  \__/\__/_//_/____/\___/\___/\__/_/\_\\__/_/  

by x04000
    """)

    while(True):
        password = str(getpass("Password: "))
        confirm = str(getpass("Repeat Password: "))

        if password == confirm:
            print("\nPassword has been set sucesfully")
            break
        else:
            print("The passwords doesn't match!\n")

    def lock():
        ui = UI.Tk()
        ui.geometry("250x250")
        ui.title("ScreenLocker by x04000")
        ui.wm_attributes("-topmost", True)
        ui.wm_attributes('-toolwindow', True)
        ui.wm_attributes('-fullscreen', True)
        ui.wm_attributes('-alpha', 0.9)
        ui.configure(bg="black")

        def unhack():
            if str(Password.get()) == password:
                ui.destroy()

        text = UI.Label(ui, text = "ScreenLocker by x04000", bg="red", fg="black")
        text.pack(fill = UI.X)

        text = UI.Label(ui, text = "", bg="black", fg="white")
        text.pack(fill = UI.X)

        text = UI.Label(ui, text = "Password", bg="black", fg="white")
        text.pack()

        Password = UI.Entry(ui, show="*", width = 100, fg="white", bg="black")
        Password.pack()

        Try = UI.Button(ui, text = "Unlock Screen", command = unhack, fg="white", bg="black")
        Try.pack(fill = UI.X)

        ui.mainloop()

    locker = UI.Tk()
    locker.geometry("150x100")
    locker.title("ScreenLocker by x04000")
    locker.wm_attributes("-topmost", True)
    locker.wm_attributes('-toolwindow', True)
    locker.wm_attributes('-alpha', 0.7)
    locker.configure(bg="black")

    text = UI.Label(locker, text = "ScreenLocker by x04000", bg="red", fg="black")
    text.pack(fill = UI.X)

    text = UI.Label(locker, text = "", bg="black", fg="white")
    text.pack(fill = UI.X)

    lockbutton = UI.Button(locker, text = "Lock Screen", command = lock, fg="white", bg="black")
    lockbutton.pack(fill = UI.X)

    locker.mainloop()

except KeyboardInterrupt:
    print("\n[+] Keyboard Interrupt")
except:
    print("\n[-] An Unknow Error Ocurred")