from tkinter import *
import generator_of_words as gen


def check_word():
    word = label["text"]
    translate_word = entry.get()
    result = (gen.dict_of_words[word] == translate_word)
    if result:
        label.configure(fg="green")
        label["text"] = "{} - {}".format(word, gen.dict_of_words[word])
        gen.word_history.append(label["text"])
        gen.answer_history.append("True")
        if gen.dict_of_chance[word] > 1:
            gen.dict_of_chance[word] = int(gen.dict_of_chance[word]) - 1
            gen.count_of_chance = int(gen.count_of_chance) - 1
    else:
        label.configure(fg="red")
        label["text"] = "{} - {}".format(word, gen.dict_of_words[word])
        gen.word_history.append(label["text"])
        gen.answer_history.append("False")
        gen.dict_of_chance[word] = int(gen.dict_of_chance[word]) + 1
        gen.count_of_chance = int(gen.count_of_chance) + 1
    btn_check.grid_forget()
    btn_next.grid(row=2, column=3)


def show_history():
    window_history = Toplevel(root)
    window_history.title("This is history")
    window_history.minsize(600, 600)
    window_history.maxsize(600, 600)
    history = Text(window_history, width=40, height=50, font=("Ubuntu", 15))
    history.grid(row=1, column=1)
    history.delete("1.0", END)
    length = len(gen.word_history)
    for i in range(length):
        stroka = "{} : {}\n".format(gen.word_history[length - i - 1], gen.answer_history[length - i - 1])
        history.insert(END, stroka)


def next_word():
    label.configure(text=gen.get_random_word(), fg="black")
    btn_next.grid_forget()
    btn_check.grid(row=2, column=3)


def end_app():
    gen.save_chance()
    gen.save_history()
    root.destroy()


root = Tk()
root.title("Translate it, please.")
root.minsize(1185, 175)
root.maxsize(1185, 175)
root.protocol("WM_DELETE_WINDOW", end_app)

label = Label(root, width=20, font=("Ubuntu", 50))
label.grid(row=1, columnspan=2)

entry = Entry(root, width=32, font=("Ubuntu", 30))
entry.grid(row=2, columnspan=2)

btn_check = Button(root, text="check", font=("Ubuntu", 30), command=check_word)
btn_show_history = Button(root, text="history", font=("Ubuntu", 30), command=show_history)
btn_next = Button(root, text="next", font=("Ubuntu", 30), command=next_word)
btn_next.grid(row=2, column=3)
btn_show_history.grid(row=1, column=3)

gen.fill_words()
gen.fill_chance()
gen.fill_history()

root.mainloop()
