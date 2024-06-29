import re
import tkinter as tk
from tkinter import scrolledtext

def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Pattern matching with regex
    if re.search(r"\bhello\b|\bhii\b|\bhi\b", user_input):
        return "Hello! How can I help you today?"
    elif re.search(r"\bhow are you\b|\bhow r u\b", user_input):
        return "I'm just a bunch of code, but I'm here to help you!"
    elif re.search(r"\bohh\b", user_input):
        return "yes yes!"
    elif re.search(r"\bwhat is your name\b|\bwt is ur name\b", user_input):
        return "I am a chatbot created to assist you. You can call me ChatBot."
    elif re.search(r"\bsure,i am happy to call you with your name\b", user_input):
        return "I am glad!"
    elif re.search(r"\bhey chatbot\b", user_input):
        return "supp..how was your day"
    elif re.search(r"\bit was good\b", user_input):
        return "that's great!"
    elif re.search(r"\bwhat can you do for me\b", user_input):
        return "I can answer your questions and help with basic tasks. What do you need help with?"
    elif re.search(r"\bbye\b|\bgoodbye\b|\bbyeee\b", user_input):
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase your question?"

def send_message():
    user_input = user_entry.get()
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    response = chatbot_response(user_input)
    chat_window.insert(tk.END, "ChatBot: " + response + "\n\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)
    user_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("ChatBot")

# Create the chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, width=50, height=20, font=("Helvetica", 14))
chat_window.pack(padx=10, pady=10)

# Create the user entry box
user_entry = tk.Entry(root, font=("Helvetica", 14))
user_entry.pack(padx=10, pady=10, fill=tk.BOTH)
user_entry.bind("<Return>", lambda event: send_message())

# Create the send button
send_button = tk.Button(root, text="Send", font=("Helvetica", 14), command=send_message)
send_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
