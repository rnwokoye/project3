import os
from flask import Flask, render_template, redirect
#Creating tkinter GUI
# import tkinter
# from tkinter import *


# import nltk
# from nltk.stem import WordNetLemmatizer
# lemmatizer = WordNetLemmatizer()

# import pickle
# import numpy as np
# from keras.models import load_model
# model = load_model('chatbot_model.h5')

# import json
# import random



# from gui_chatbot import getResponse, predict_class, intents

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])


@app.route("/")
def index():

    return render_template("index.html")



# @app.route("/scrape")
#     #Creating tkinter GUI
# # import tkinter
# # from tkinter import *
# def send():
#     msg = EntryBox.get("1.0",'end-1c').strip()
#     EntryBox.delete("0.0",END)
#     if msg != '':
#         ChatBox.config(state=NORMAL)
#         ChatBox.insert(END, "You: " + msg + '\n\n')
#         ChatBox.config(foreground="#446665", font=("Verdana", 12 )) 
#         ints = predict_class(msg)
#         res = getResponse(ints, intents)
        
#         ChatBox.insert(END, "Bot: " + res + '\n\n')           
#         ChatBox.config(state=DISABLED)
#         ChatBox.yview(END)



# root = Tk()
# root.title("Chatbot")
# root.geometry("400x500")
# root.resizable(width=FALSE, height=FALSE)


# #Create Chat window
# ChatBox = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",)
# ChatBox.config(state=DISABLED)
# #Bind scrollbar to Chat window
# scrollbar = Scrollbar(root, command=ChatBox.yview, cursor="heart")
# ChatBox['yscrollcommand'] = scrollbar.set
# #Create Button to send message
# SendButton = Button(root, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
#                     bd=0, bg="#f9a602", activebackground="#3c9d9b",fg='#000000',
#                     command= send )
# #Create the box to enter message
# EntryBox = Text(root, bd=0, bg="white",width="29", height="5", font="Arial")
# #EntryBox.bind("<Return>", send)
# #Place all components on the screen
# scrollbar.place(x=376,y=6, height=386)
# ChatBox.place(x=6,y=6, height=386, width=370)
# EntryBox.place(x=128, y=401, height=90, width=265)
# SendButton.place(x=6, y=401, height=90)
# root.mainloop()

   


if __name__ == "__main__":
    app.run(debug=True)