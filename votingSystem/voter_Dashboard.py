from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector

# Database Connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ps@123",
    database="voting_system"
)

cursor = con.cursor()


class Dashboard:

    def __init__(self):

        self.root = Tk()
        self.root.title("Voting System")
        self.root.geometry("1500x900")

        # Background Image
        img = Image.open(
            "C:\\Users\\ELCOT\\Downloads\\voting.JPEG"
        )
        img = img.resize((1500, 900))

        self.bg = ImageTk.PhotoImage(img)

        Label(
            self.root,
            image=self.bg
        ).place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        # Main Frame
        frame = Frame(
            self.root,
            bg="#6A0DAD"
        )

        frame.place(
            relx=0.30,
            rely=0.5,
            anchor=CENTER,
            width=700,
            height=600
        )

        # Title
        Label(
            frame,
            text="Choose Your Voter🤩",
            font=("Verdana", 24, "bold"),
            bg="#6A0DAD",
            fg="white"
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=30
        )
        # Student Name
        Label(
            frame,
            text="Student Name :",
            font=("Verdana", 14, "bold"),
            bg="#6A0DAD",
            fg="white"
        ).grid(row=1, column=0, pady=10)

        self.student_name = Entry(
            frame,
            font=("Verdana", 14),
            width=20
        )
        self.student_name.grid(row=1, column=1)

        # Section
        Label(
            frame,
            text="Section :",
            font=("Verdana", 14, "bold"),
            bg="#6A0DAD",
            fg="white"
        ).grid(row=2, column=0, pady=10)

        self.section = Entry(
            frame,
            font=("Verdana", 14),
            width=20
        )
        self.section.grid(row=2, column=1)

        # Register Number
        Label(
            frame,
            text="Register No :",
            font=("Verdana", 14, "bold"),
            bg="#6A0DAD",
            fg="white"
        ).grid(row=3, column=0, pady=10)

        self.reg_no = Entry(
            frame,
            font=("Verdana", 14),
            width=20
        )
        self.reg_no.grid(row=3, column=1)

        # Voter 1
        Button(
            frame,
            text="Voter 1\nNAME : PRATHIKA",
            font=("Verdana", 16, "bold"),
            width=15,
            command=self.voter1
        ).grid(row=4, column=0,
               padx=50, pady=20)

        # Voter 2
        Button(
            frame,
            text="Voter 2\nNAME : PRIYA",
            font=("Verdana", 16, "bold"),
            width=15,
            command=self.voter2
        ).grid(row=4, column=1,
               padx=80, pady=20)

        # Voter 3
        Button(
            frame,
            text="Voter 3\nNAME : SHREE",
            font=("Verdana", 16, "bold"),
            width=15,
            command=self.voter3
        ).grid(row=5, column=0,
               padx=50, pady=40)

        # Voter 4
        Button(
            frame,
            text="Voter 4\nNAME : PAVISHNA",
            font=("Verdana", 16, "bold"),
            width=15,
            command=self.voter4
        ).grid(row=5, column=1,
               padx=70, pady=40)

        # Winner Button
        Button(
            frame,
            text="SHOW WINNER",
            font=("Verdana", 16, "bold"),
            fg="#6A0DAD",
            bg="white",
            command=self.winner
        ).grid(
            row=6,
            column=0,
            columnspan=2,
            pady=20
        )

        self.root.mainloop()

    # Save Vote
    def save_vote(self, name):

        student = self.student_name.get()
        reg_no = self.reg_no.get()
        dept = self.section.get()

        if (
                student == "" or
                reg_no == "" or
                dept == ""
        ):
            messagebox.showerror(
                "Error",
                "Please Enter All Details"
            )
            return

        # Update vote count
        sql1 = """
        UPDATE votes
        SET vote_count = vote_count + 1
        WHERE candidate_name = %s
        """

        cursor.execute(sql1, (name,))

        # Store student details
        sql2 = """
        INSERT INTO student_vote_details(
        student_name,
        register_no,
        department,
        voted_candidate
        )
        VALUES(%s,%s,%s,%s)
        """

        value = (
            student,
            reg_no,
            dept,
            name
        )

        cursor.execute(sql2, value)

        con.commit()

        messagebox.showinfo(
            "Vote Success",
            f"{student}\n"
            f"Voted for {name}"
        )

        # Clear entries
        self.student_name.delete(0, END)
        self.reg_no.delete(0, END)
        self.section.delete(0, END)


    # Show Winner
    def winner(self):

        sql = """
        SELECT candidate_name, vote_count
        FROM votes
        ORDER BY vote_count DESC
        """

        cursor.execute(sql)

        data = cursor.fetchall()

        # Check if table has data
        if len(data) == 0:
            messagebox.showinfo(
                "Result",
                "No Votes Found"
            )

            return

        # Winner
        winner_name = data[0][0]
        winner_votes = data[0][1]

        result = (
            f"🏆 Winner : {winner_name}\n"
            f"🎯 Total Votes : {winner_votes}\n\n"
        )

        result += "📊 Voting Results\n"
        result += "----------------------\n"

        for row in data:
            result += (
                f"{row[0]} = "
                f"{row[1]} Votes\n"
            )

        messagebox.showinfo(
            "Voting Result",
            result
        )

    # Voter 1
    def voter1(self):

        self.save_vote("PRATHIKA")

        top = Toplevel(self.root)
        top.geometry("500x500")
        top.title("Voter 1")

        img = Image.open(
            r"C:\Users\ELCOT\Downloads\prathika.png"
        )

        img = img.resize((500, 500))

        photo = ImageTk.PhotoImage(img)

        label = Label(top, image=photo)
        label.image = photo
        label.pack()

        top.after(2000, top.destroy)

    # Voter 2
    def voter2(self):

        self.save_vote("PRIYA")

        top = Toplevel(self.root)
        top.geometry("500x500")
        top.title("Voter 2")

        img = Image.open(
            r"C:\Users\ELCOT\Downloads\priya.png"
        )

        img = img.resize((500, 500))

        photo = ImageTk.PhotoImage(img)

        label = Label(top, image=photo)
        label.image = photo
        label.pack()

        top.after(2000, top.destroy)

    # Voter 3
    def voter3(self):

        self.save_vote("SHREE")

        top = Toplevel(self.root)
        top.geometry("500x500")
        top.title("Voter 3")

        img = Image.open(
            r"C:\Users\ELCOT\Downloads\shree.png"
        )

        img = img.resize((500, 500))

        photo = ImageTk.PhotoImage(img)

        label = Label(top, image=photo)
        label.image = photo
        label.pack()

        top.after(2000, top.destroy)

    # Voter 4
    def voter4(self):

        self.save_vote("PAVISHNA")

        top = Toplevel(self.root)
        top.geometry("500x500")
        top.title("Voter 4")

        img = Image.open(
            r"C:\Users\ELCOT\Downloads\pavishna.jpeg"
        )

        img = img.resize((500, 500))

        photo = ImageTk.PhotoImage(img)

        label = Label(top, image=photo)
        label.image = photo
        label.pack()

        top.after(2000, top.destroy)
