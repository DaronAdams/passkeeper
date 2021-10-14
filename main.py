from tkinter import *

# --------------------------- Save Password ------------------------------------------

# ---------------------------- UI Setup ---------------------------------------------
screen = Tk()
screen.title("PassKeeper")
screen.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
my_img = PhotoImage(file="PassKeeper.png")
canvas.create_image(100, 100, image=my_img)
canvas.grid(row=1, column=2)

# Entry Boxes
website_entry = Entry(width=35)
website_entry.grid(row=2, column=2)
email_entry = Entry(width=35)
email_entry.grid(row=3, column=2)


# Labels
website_label = Label(text="Website", font="Arial")
website_label.config()
website_label.grid(row=2, column=1)
screen.mainloop()