from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading



engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()




bot = ChatBot('Mybot')

convo = [
    'Hi',
    'Hello, how can I help you?',
    'How are you?',
    'I\'m fine..How are you?',
    'Help.',
    'Sure..How can I help you?',
    'Cisco ASR 903',
    'What would you like to know about Cisco ASR?',
    'Rsp Module in Cisco',
    'There are 2 RSP Modules in Cisco ASR 903',
    'Swtching capacity of RSP-3C',
    'Swtiching Capacity of RSP-RC is 200gbps'

]

trainer = ListTrainer(bot)
trainer.train(convo)

# answer = english_bot.get_response('What do you know about ML?')
# print(answer)
# print("Talk to bot: ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = english_bot.get_response(query)
#     print("Bot: ", answer)
main = Tk()

main.geometry("500x650")


main.title("My Chatbot")
img = PhotoImage(file="images.png")

photoL = Label(main,image=img)

photoL.pack(pady=5)


def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold=1
    print("Your bot is listening..")
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio,language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()
        except EXCEPTION as e:
            print(e)
            print('not recognized')



def ask_from_bot():
    query = textF.get()
    answwer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    msgs.insert(END, "bot : " + str(answwer_from_bot))
    speak(answwer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)

frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame,width = 80, height = 20, yscrollcommand=sc.set)



sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH, pady=10)
frame.pack()

textF = Entry(main,font=("Verdana",20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Send",font = ("Verdana",20),command= ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>',enter_function)


def repeatL():
    while True:
        takeQuery()


t=threading.Thread(target=repeatL)
t.start()


main.mainloop()

