from tkinter import *
import random
import ttkthemes
from tkinter import ttk
from time import sleep
import threading


totaltime = 60
time = 0
wrongwords = 0
elapsedtimeinminutes = 0


def start_timer():
    startButton.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()

    for time in range(1, 61):
        elapsed_timer_label.config(text=time)
        remainingtime = totaltime - time
        remaining_timer_label.config(text=remainingtime)
        sleep(1)
        root.update()

    textarea.config(state=DISABLED)
    resetButton.config(state=NORMAL)

    
    calculate_statistics()


def count():
    global wrongwords
    while time != totaltime:
        entered_paragraph = textarea.get(1.0, END).split()
        totalwords = len(entered_paragraph)

        totalwords_count_label.config(text=totalwords)

        para_word_list = label_paragraph['text'].split()

        wrongwords = sum(1 for pair in zip(para_word_list, entered_paragraph) if pair[0] != pair[1])

        wrongwords_count_label.config(text=wrongwords)

        root.update()  


def calculate_statistics():
    global time, wrongwords
    elapsedtimeinminutes = totaltime / 60
    totalwords = len(textarea.get(1.0, END).split())

    wpm = (totalwords - wrongwords) / elapsedtimeinminutes
    wpm = round(wpm)
    gross_wpm = totalwords / elapsedtimeinminutes
    accuracy = (totalwords - wrongwords) / totalwords * 100
    accuracy = round(accuracy)

    wpm_count_label.config(text=str(wpm))
    accuracy_percent_label.config(text=str(accuracy) + '%')
    totalwords_count_label.config(text=str(totalwords))


def start():
    t1 = threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()


def reset():
    global time, elapsedtimeinminutes, wrongwords
    time = 0
    elapsedtimeinminutes = 0
    wrongwords = 0
    startButton.config(state=NORMAL)
    resetButton.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0, END)
    textarea.config(state=DISABLED)

    elapsed_timer_label.config(text='0')
    remaining_timer_label.config(text='0')
    wpm_count_label.config(text='0')
    accuracy_percent_label.config(text='0')
    totalwords_count_label.config(text='0')
    wrongwords_count_label.config(text='0')




root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('940x735+200+10')
root.resizable(width=True, height=True) 
root.overrideredirect(True)

mainframe = Frame(root, bd=4, bg='#d9b3ff')
mainframe.grid()

titleframe = Frame(mainframe, bg='#8000ff')
titleframe.grid()

titleLabel = Label(titleframe, text='🆃🆈🅿🅸🅽🅶 🆃🅴🆂🆃', font=('dark text squares', 28, 'bold'), bg='#bf00ff', fg='white',
                  width=38, bd=10)
titleLabel.grid(pady=5)

paragraph_frame = Frame(mainframe, bg='#d9b3ff')
paragraph_frame.grid(row=1, column=0, pady=10)

paragraph_list = [
    ' this is a simple paragraph that is meant to be nice and easy to type which is why there will be mommas no periods or any capital letters so i guess this means that it cannot really be considered a paragraph but just a series of run on sentences this should help you get faster at typing as im trying not to use too many difficult words in it although i think that i might start making it hard by including some more difficult letters Im typing pretty quickly so forgive me for any mistakes i think that i will not just tell you a story about the time i went to the zoo and found a monkey and a fox playing together they were so cute and i think that they were not supposed to be in the same cage but they somehow were and i loved watching them horse around forgive the pun well i hope that it has been highly enjoyable typing this paragraph and i wish you the best of luck getting the best score that you possibly can',


    ' In my junior year of high school, this guy asked me on a date. He rented a Redbox movie and made a pizza. We were watching the movie and the oven beeped so the pizza was done. He looked me dead in the eye and said, “This is the worst part.” I then watched this boy open the oven and pull the pizza out with his bare hands, rack and all, screaming at the top of his lungs. We never had a second date.Ok so then what is i cannot tell you because that didnt happen.',

    

    'One time way back in sixth grade math class I had to fart really bad. Me being the idiot that I am decided that it would be silent. Big surprise it wasn’t. The only person talking was the teacher and she was interrupted by freaking cannon fire farts. She said she was disappointed I couldn’t hold it in and proceeded to tell a story of how she taught a famous athlete who did nearly the same thing.I felt ashamed then everyone laughed and at the end I also laughed.',

    'So a couple weeks ago, me and my friends were sitting on this cement kind of pedestal (as we called it) It’s basically the steps up to the portable. (classroom that no one uses) and this weird supply French teacher comes up to us and says: you shouldn’t be sitting on this ground, it’s too cold and it’s bad for your ovaries. I asked her how or why and she said that if children sit on cold ground their ovaries will freeze and that we won’t be able to have kids.',
    'One of the most valuable possession of human life is its health. With good health, one can attain everything in life. In order to perform an important work effectively, one has to be in sound health. Nowadays, everyone is suffering from some sort of mental, health, chronic or physical illness, which however deprives them. Often bad habits such as smoking have brought upon diseases and weakness upon a person which he is not aware of and are of no value to their family and society.',
    'Alcohol is taken in almost all cool and cold climates, and to a very much less extent in hot ones. It is taken by people who live in the Himalaya Mountains, but not nearly so much by those who live in the plains of India. Alcohol is not necessary in any way to anybody. The regular use of alcohol, even in small quantities, tends to cause mischief in many ways to various organs of the body. It affects the liver, it weakens the mental powers, and lessens the energy of the body.',

    'The Computer is an automatic device that performs mathematical calculations and logical operations. They are being put to use in widely divergent fields such as book-keeping, spaceflight controls, passanger reservation service, language translation etc. There are two categories: analog and digital. The former represents numbers by some physical quantity such as length, angular relation or electric current whereas the latter represent numbers by seperate devices for each digit.'
]

random.shuffle(paragraph_list)

label_paragraph = Label(paragraph_frame, text=paragraph_list[0], wraplength=912, justify=LEFT, font=('arial', 14, 'bold'),
                       bg='#d9b3ff')
label_paragraph.grid(row=0, column=0)

textarea_frame = Frame(mainframe, bg='#d9b3ff')
textarea_frame.grid(row=2, column=0)

textarea = Text(textarea_frame, font=('arial', 12, 'bold'), width=100, height=7, bd=4, relief=GROOVE, wrap='word',
                 state=DISABLED)
textarea.grid()

frame_output = Frame(mainframe, bg='#d9b3ff')
frame_output.grid(row=3, column=0)

elapsed_time_label = Label(frame_output, text='Elapsed Time', font=('Tahoma', 12, 'bold'), fg='red', bg='#d9b3ff')
elapsed_time_label.grid(row=0, column=0, padx=5)

elapsed_timer_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'), bg='#d9b3ff')
elapsed_timer_label.grid(row=0, column=1, padx=5)

remaining_time_label = Label(frame_output, text='Remaining Time', font=('Tahoma', 12, 'bold'), fg='red', bg='#d9b3ff')
remaining_time_label.grid(row=0, column=2, padx=5)

remaining_timer_label = Label(frame_output, text='60', font=('Tahoma', 12, 'bold'), bg='#d9b3ff')
remaining_timer_label.grid(row=0, column=3, padx=5)

wpm_label = Label(frame_output, text='WPM', font=('Tahoma', 12, 'bold'), fg='red', bg='#d9b3ff')
wpm_label.grid(row=0, column=4, padx=5)

wpm_count_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'), bg='#d9b3ff')
wpm_count_label.grid(row=0, column=5, padx=5)

totalwords_label = Label(frame_output, text='Total Words', font=('Tahoma', 12, 'bold'), fg='red', bg='#d9b3ff')
totalwords_label.grid(row=0, column=6, padx=5)

totalwords_count_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'), bg='#d9b3ff')
totalwords_count_label.grid(row=0, column=7, padx=5)

wrongwords_label = Label(frame_output, text='Wrong Words', font=('Tahoma', 12, 'bold'), fg='red', bg='#d9b3ff')
wrongwords_label.grid(row=0, column=8, padx=5)

wrongwords_count_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'), bg='#d9b3ff')
wrongwords_count_label.grid(row=0, column=9, padx=5)

accuracy_label = Label(frame_output, text='Accuracy', font=('Tahoma', 12, 'bold'), fg='red', bg='#d9b3ff')
accuracy_label.grid(row=0, column=10, padx=5)

accuracy_percent_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'), bg='#d9b3ff')
accuracy_percent_label.grid(row=0, column=11, padx=5)

buttons_Frame = Frame(mainframe, bg='#d9b3ff')
buttons_Frame.grid(row=4, column=0, pady=10)

startButton = ttk.Button(buttons_Frame, text='Start', command=start)
startButton.grid(row=0, column=0, padx=10)

resetButton = ttk.Button(buttons_Frame, text='Reset', state=DISABLED, command=reset)
resetButton.grid(row=0, column=1, padx=10)

exitButton = ttk.Button(buttons_Frame, text='Exit', command=root.destroy)
exitButton.grid(row=0, column=2, padx=10)

root.mainloop()
