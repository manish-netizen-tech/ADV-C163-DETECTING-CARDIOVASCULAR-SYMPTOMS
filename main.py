from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("DETECTING CARDIOVASCULAR SYMPTOMS")
root.geometry("400x00")

question1_radiobutton = StringVar(value = "0")

label_question01 = Label(root, text="Do you experience shortness of breath during routine activities???")
label_question01.pack()

question1_r1 = Radiobutton(root, text="yes", variable=question1_radiobutton, value="yes")
question1_r1.pack()

question1_r2 = Radiobutton(root, text="no", variable=question1_radiobutton, value="no")
question1_r2.pack()

question2_radiobutton = StringVar(value = "0")

label_question02 = Label(root, text="Do you experience shortness of breath while at rest/lying down?")
label_question02.pack()

question2_r1 = Radiobutton(root, text="yes", variable=question2_radiobutton, value="yes")
question2_r1.pack()

question2_r2 = Radiobutton(root, text="no", variable=question2_radiobutton, value="no")
question2_r2.pack()

question3_radiobutton = StringVar(value = "0")

label_question03 = Label(root, text="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?")
label_question03.pack()

question3_r1 = Radiobutton(root, text="yes", variable=question3_radiobutton, value="yes")
question3_r1.pack()

question3_r2 = Radiobutton(root, text="no", variable=question3_radiobutton, value="no")
question3_r2.pack()

def fever_score():
    score = 0
    if question1_radiobutton.get() == "yes":
        score = score + 20
        print(score)
    if question2_radiobutton.get() == "yes":
        score = score + 20
        print(score)
    if question3_radiobutton.get() == "yes":
        score = score + 20
        print(score)
    if score <= 20:
        messagebox.showinfo("report", "you don't need to visit to doctor")
    elif score > 20 and score <= 40:
        messagebox.showinfo("report", "you might perhaps visit to a doctor")
    else :
        messagebox.showwarning("report", "you are strongly advised to visit a doctor")

btn = Button(root, text="show report", command=fever_score)
btn.pack()

root.mainloop()