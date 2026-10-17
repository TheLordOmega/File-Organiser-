import customtkinter as ctk


def button_callback():
    print("button pressed")
app = ctk.CTk()
app.title("File Organiser")
app.geometry("1980x1080")

button = ctk.CTkButton(app, text="Start Organising", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()
