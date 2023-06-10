BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

import pandas as pd
from random import *

x=0

right_list=list()
wrong_words={}
window= Tk()
window.title("Flashy")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)

canvas=Canvas(height=526,width=800)
data=pd.read_csv("data/french_words.csv")

french_word=data.loc[x]["French"]
english_word=data.loc[x]["English"]
x = randint(0, 100)

text1 = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
text2 = canvas.create_text(400, 263, text=french_word, font=("Ariel", 60, "bold"))
temp1=0
temp2=0
def flip():
    global text1
    global text2
    global card_bg
    global data
    global x

    """
    canvas_image = canvas.create_image(400, 263, image=front_card)

    canvas.itemconfig(canvas_image, image=new_image)"""
    """
    text1 = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
    text2 = canvas.create_text(400, 263, text=french_word, font=("Ariel", 60, "bold"))
    """
    canvas.delete(text1)
    canvas.delete(text2)
    text1 = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"),fill="white")

    english_word = data.loc[x]["English"]
    text2 = canvas.create_text(400, 263, text=english_word, font=("Ariel", 60, "bold"),fill="white")
    """
    canvas.itemconfig(text1,text="English",fill="white")
    canvas.itemconfig(text2,text=english_word,fill="white")
    """
    canvas.itemconfig(card_bg,image=new_image)





new_image = PhotoImage(file="C:/Users/PC/Desktop/flash-card-project-start/images/card_back.png")

def start():

    global text1
    global text2

    global x

    x = randint(0, 100)
    canvas.delete(text1)
    canvas.delete(text2)

    data = pd.read_csv("data/french_words.csv")

    french_word = data.loc[x]["French"]
    english_word = data.loc[x]["English"]


    """
    french_word = data.loc[x]["French"]
    english_word = data.loc[x]["English"]
    """
    text1=canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
    text2=canvas.create_text(400, 263, text=french_word, font=("Ariel", 60, "bold"))
    print(data.loc[x]["French"])

    canvas.itemconfig(card_bg,image=front_card)
    window.after(1000, func=flip)
    """
    canvas_image = canvas.create_image(400, 263, image=front_card)
    # To change the image:
    canvas.itemconfig(canvas_image, image=new_image)"""

def show_words():

    global text1
    global text2
    global right_list
    global x
    global french_word
    global english_word

    wrong_words[french_word] = english_word
    print(wrong_words)


    canvas.delete(text1)
    canvas.delete(text2)

    data = pd.read_csv("data/french_words.csv")

    french_word = data.loc[x]["French"]
    english_word = data.loc[x]["English"]


    """
    french_word = data.loc[x]["French"]
    english_word = data.loc[x]["English"]
    """
    text1=canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
    text2=canvas.create_text(400, 263, text=french_word, font=("Ariel", 60, "bold"))


    canvas.itemconfig(card_bg,image=front_card)
    window.after(1000, func=flip)
    """
    canvas_image = canvas.create_image(400, 263, image=front_card)
    # To change the image:
    canvas.itemconfig(canvas_image, image=new_image)"""

def show_new():

    global text1
    global text2
    global wrong_words
    global x
    right_list.append(x)

    x = randint(0, 100)
    while x in right_list:
        x = randint(0, 100)


    canvas.delete(text1)
    canvas.delete(text2)

    data = pd.read_csv("data/french_words.csv")

    french_word = data.loc[x]["French"]
    english_word = data.loc[x]["English"]


    """
    french_word = data.loc[x]["French"]
    english_word = data.loc[x]["English"]
    """
    text1=canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
    text2=canvas.create_text(400, 263, text=french_word, font=("Ariel", 60, "bold"))
    print(data.loc[x]["French"])

    canvas.itemconfig(card_bg,image=front_card)
    window.after(1000, func=flip)
    """
    canvas_image = canvas.create_image(400, 263, image=front_card)
    # To change the image:
    canvas.itemconfig(canvas_image, image=new_image)"""





front_card=PhotoImage(file="C:/Users/PC/Desktop/flash-card-project-start/images/card_front.png")
card_bg=canvas.create_image(400,263,image=front_card)
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
text1=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
text2=canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))

new_image = PhotoImage(file="C:/Users/PC/Desktop/flash-card-project-start/images/card_back.png")
"""
canvas_image = canvas.create_image(400, 263, image=front_card)
#To change the image:
canvas.itemconfig(canvas_image, image=new_image)
"""
canvas.itemconfig(text1,fill="#FAFAEB")
canvas.itemconfig(text2,fill="#FFFFFF")



# apply the tag "red"

"""
back_card=PhotoImage(file="C:/Users/PC/Desktop/flash-card-project-start/images/card_back.png")
canvas.create_image(400,263,image=back_card)
canvas.grid(row=0,column=0)"""

left_card=PhotoImage(file="C:/Users/PC/Desktop/flash-card-project-start/images/right.png")
wrong_button=Button(image=left_card,highlightthickness=0,command=show_new)
wrong_button.grid(row=1,column=0)

right_card=PhotoImage(file="C:/Users/PC/Desktop/flash-card-project-start/images/wrong.png")
right_button=Button(image=right_card,highlightthickness=0,command=show_words)
right_button.grid(row=1,column=1)

start()





window.mainloop()