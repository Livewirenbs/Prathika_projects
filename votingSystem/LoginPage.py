from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import voter_Dashboard


class LoginPage:

    def __init__(self):

        self.root = Tk()
        self.root.geometry("1500x900")
        self.root.title("Login Page😀")

        # Background Image
        img = Image.open("C:\\Users\\ELCOT\\Downloads\\bts.jpg")
        img = img.resize((1500, 900))

        self.bg = ImageTk.PhotoImage(img)

        Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1
        )

        # Main Frame
        frame = Frame(self.root, bg="#6A0DAD")
        frame.place(
            relx=0.5,
            rely=0.5,
            anchor=CENTER,
            width=600,
            height=400
        )

        # Title
        title = Label(
            frame,
            text="Smart Voting System",
            font=("Verdana", 26, "bold italic"),
            bg="#6A0DAD",
            fg="white"
        )
        title.grid(row=0, column=0, columnspan=2, pady=30)

        # Name
        Label(
            frame,
            text="Name :",
            font=("Verdana", 20, "bold"),
            bg="#6A0DAD",
            fg="white"
        ).grid(row=1, column=0, padx=20, pady=15)

        self.entry_name = Entry(
            frame,
            width=28,
            font=("Verdana", 16)
        )
        self.entry_name.grid(row=1, column=1)

        # Password
        Label(
            frame,
            text="Password :",
            font=("Verdana", 20, "bold"),
            bg="#6A0DAD",
            fg="white"
        ).grid(row=2, column=0, padx=20, pady=15)

        self.pd = Entry(
            frame,
            width=28,
            font=("Verdana", 16),
            show="*"
        )
        self.pd.grid(row=2, column=1)

        # Login Button
        button = Button(
            frame,
            text="Login",
            command=self.login,
            font=("Verdana", 20, "bold"),
            bg="white",
            fg="#6A0DAD",
            width=15
        )

        button.grid(row=3, column=0,
                    columnspan=2, pady=30)

        self.root.mainloop()

    def login(self):

        name = self.entry_name.get()
        password1 = self.pd.get()

        if name == "ps" and password1 == "555":
            messagebox.showinfo(
                "Login Successful",
                "Login Successful"
            )

            self.root.destroy()

            voter_Dashboard.Dashboard()

        else:
            messagebox.showerror(
                "Error",
                "Invalid Username or Password"
            )

LoginPage()