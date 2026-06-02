from tkinter import *
from tkinter import scrolledtext
from PIL import Image, ImageTk
import requests
from io import BytesIO
import ollama
import threading

import speech_recognition as sr

#WINDOW
root = Tk()
root.title("🚀 Space FunnyBot")
root.geometry("1300x700")
root.resizable(False, False)

#SPACE BACKGROUND 
image_url = "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=1200"

response = requests.get(image_url)
img_data = response.content

img = Image.open(BytesIO(img_data))
img = img.resize((800, 700))

bg_image = ImageTk.PhotoImage(img)

bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# HEADER
header = Frame(root, bg="#4B0082", height=70)
header.pack(fill=X)

title = Label(
    header,
    text="🤖 FunnyBot AI",
    font=("Segoe UI", 18, "bold"),
    fg="white",
    bg="#4B0082"
)
title.pack(side=LEFT, padx=20, pady=15)

status = Label(
    header,
    text="🟢 Online",
    font=("Segoe UI", 10),
    fg="lightgreen",
    bg="#4B0082"
)
status.pack(side=LEFT)

# CHAT FRAME
chat_frame = Frame(root, bg="#000000")
chat_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
chat_area = Text(
    chat_frame,
    font=("Segoe UI", 11),
    wrap=WORD,
    bg="#111827",
    fg="white",
    bd=0,
    padx=10,
    pady=10
)

scrollbar = Scrollbar(chat_frame, command=chat_area.yview)
chat_area.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT, fill=Y)
chat_area.pack(fill=BOTH, expand=True)

#CHAT BUBBLE COLORS
chat_area.tag_config(
    "user",
    background="#7B2CBF",
    foreground="white",
    font=("Segoe UI", 11),
    spacing1=10,
    spacing3=10,
    lmargin1=200,
    lmargin2=200,
    rmargin=20
)

chat_area.tag_config(
    "bot",
    background="#FFFFFF",
    foreground="black",
    font=("Segoe UI", 11),
    spacing1=10,
    spacing3=10,
    lmargin1=20,
    lmargin2=20,
    rmargin=200
)

chat_area.tag_config(
    "thinking",
    foreground="lightgray",
    font=("Segoe UI", 10, "italic")
)



# VOICE INPUT
def voice_input():

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            chat_area.insert(
                END,
                "\n🎤 Listening...\n",
                "thinking"
            )

            chat_area.yview(END)

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

            voice_text = recognizer.recognize_google(audio)

            # Put voice text in entry box
            entry_box.delete(0, END)
            entry_box.insert(0, voice_text)

            # Automatically send
            send_message()

    except sr.UnknownValueError:
        chat_area.insert(
            END,
            "\n❌ Could not understand voice\n",
            "thinking"
        )

    except sr.RequestError:
        chat_area.insert(
            END,
            "\n❌ Internet problem for speech recognition\n",
            "thinking"
        )

    except Exception as e:
        chat_area.insert(
            END,
            f"\n❌ Error: {str(e)}\n",
            "thinking"
        )

#BOT RESPONSE
def get_ai_reply(user_message):

    try:
        response = ollama.chat(
        model="phi3:mini",
        messages=[
        {
            "role": "system",
            "content":
            "You are FunnyBot. "
            "Be funny, smart and friendly. "
            "Reply shortly in 2-3 lines only with emojis."
        },
        {
            "role": "user",
            "content": user_message
        }
    ],
        options={
        "num_predict": 80
    }
)

        bot_reply = response["message"]["content"]

        chat_area.insert(
            END,
            f"\n🤖 {bot_reply}\n",
            "bot"
        )

        chat_area.yview(END)

    except Exception as e:
        chat_area.insert(
            END,
            f"\nError: {str(e)}\n",
            "bot"
        )

#SEND
def send_message():

    user_message = entry_box.get().strip()

    if user_message == "":
        return

    # User bubble
    chat_area.insert(
        END,
        f"\n🧑 {user_message}\n",
        "user"
    )

    entry_box.delete(0, END)

    # Thinking text
    chat_area.insert(
        END,
        "\n🤖 Typing... 🚀\n",
        "thinking"
    )

    chat_area.yview(END)

    threading.Thread(
        target=get_ai_reply,
        args=(user_message,),
        daemon=True
    ).start()

#BOTTOM INPUT BAR
bottom_frame = Frame(root, bg="#1F2937", height=70)
bottom_frame.pack(fill=X, side=BOTTOM)

entry_box = Entry(
    bottom_frame,
    font=("Segoe UI", 13),
    bg="#FFFFFF",
    fg="#4B0082",
    relief=FLAT,
    width=50
)
entry_box.pack(side=LEFT, padx=15, pady=15, ipady=8)


mic_btn = Button(
    bottom_frame,
    text="🎤",
    font=("Segoe UI", 14, "bold"),
    bg="#9333EA",
    fg="white",
    relief=FLAT,
    padx=15,
    pady=8,
    cursor="hand2",
    command=lambda: threading.Thread(
        target=voice_input,
        daemon=True
    ).start()
)

mic_btn.pack(side=RIGHT, padx=10)

send_btn = Button(
    bottom_frame,
    text="🚀 Send",
    font=("Segoe UI", 12, "bold"),
    bg="#7B2CBF",
    fg="white",
    relief=FLAT,
    padx=20,
    pady=8,
    cursor="hand2",
    command=send_message
)
send_btn.pack(side=RIGHT, padx=15)

entry_box.bind("<Return>", lambda event: send_message())
root.mainloop()