from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = TK()
window.title("Fashy")
window.config(padx=50,pady=50,bg=BAC    KGROUND)

canvas =  Canvas(width=800, height=526)
card_front_img = PhotoImage(file="card_font.png")
canvas.create_image(400,263, image=card_front_img)
canvas.create_text(400,150 text="Title", font=("Ariel", 40,"italic"))
canvas.create_text(400,263 text="word", font=("Ariel", 40,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_image = PhotoImage(file="image/wrong.png")
unknown_button  = Button(image=cross_image)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file = "image/right.png")
known_button = Button(image=check_image)
known_button.grid(row=1, column=1)














window.mainloop