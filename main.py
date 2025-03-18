from tkinter import *
from tkinter import messagebox
import base64

screen = Tk()
screen.geometry("520x520")
screen.title("Encryption & Decryption")
screen.configure(bg="black")
def encrypt():
    password=code.get()
    if password=="7557":
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("520x350")
        screen1.configure(bg="red")

        message=text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1, text="code is Encrypted", font="impack 10 bold").place(x=7,y=8)
        text2 = Text(screen1, font="30",bd=4, wrap=WORD)
        text2.place(x=2,y=30,width=390,height=140)
        text2.insert(END,encrypt)

    elif(password==""):
        messagebox.showerror("ERROR", "Please enter Secret Key")
    elif(password!="7557"):
        messagebox.showerror("Uh OH!!", "Invalid Secret key")

def decrypt():
    password = code.get()
    if password == "7557":
        screen2 = Toplevel(screen)
        screen2.title("Encryption")
        screen2.geometry("520x350")
        screen2.configure(bg="green")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen2, text="code is Encrypted", font="impack 10 bold").place(x=7, y=8)
        text2 = Text(screen2, font="30", bd=4, wrap=WORD)
        text2.place(x=2, y=30, width=390, height=140)
        text2.insert(END, encrypt)

    elif (password == ""):
        messagebox.showerror("ERROR", "Please enter Secret Key")
    elif (password != "7557"):
        messagebox.showerror("Uh OH!!", "Invalid Secret key")

def reset():
    text1.delete(1.0,END)
    code.det("")




#LAbel
Label(screen, text="Enter the Text for Encrytion & Decryption", font="impack 14 bold").place(x=70, y=4)
#text
text1=Text(screen, font="20")
text1.place(x=50, y=45, width=420, height=130)
#Label
Label(screen, text="Enter Secret key", font="impack 17 bold").place(x=160, y=195)
#entry
code=StringVar()
Entry(textvariable=code,bd=4,font="20",show="*").place(x=155, y=240)
#BUTTON
Button(screen, text="ENCRYPT", font="arial 17 bold", bg="red",fg="white", command=encrypt).place(x=50,y=290,width=170)
Button(screen, text="DECRYPT", font="arial 17 bold", bg="green",fg="white", command=decrypt).place(x=300,y=290,width=170)
Button(screen, text="RESET", font="arial 17 bold", bg="YELLOW",fg="white").place(x=110,y=370,width=270)

mainloop()
