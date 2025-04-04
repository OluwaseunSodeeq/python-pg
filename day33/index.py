import requests
from tkinter import *

response =  requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
data = response.json()["iss_position"]
print(data)


# CHALLENGE


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status()
    kanye_quotes = response.json()["quote"]
    print(f"QUOTES FOR TODAY: {kanye_quotes}")
    canvas.itemconfig(quote_text,text=kanye_quotes)

    # if response.status_code == "404":
    #     print("Unsuccessful ")

window = Tk()
window.title("Kanye says....")
window.config(padx=50,pady=20)


canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)


kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)