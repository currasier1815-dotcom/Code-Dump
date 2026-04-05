#! python3.11

import ttkbootstrap as ttk

def main():
    app = ttk.Window(themename = 'flatly')
    style = app.style

    app.geometry('300x350')
    app.title("Demo")
    app.resizable(False, False)

    # Title and Explanations
    ttk.Label(app, text = 'Demo', font = ("Calibri", 24, "bold")).pack(pady = 10)

    ttk.Label(
        master = app,
        wraplength = 260,
        justify = "center",
        font = ("Calibri", 10),
        text = "This is a Simple Demo made using TTK-Bootstrap, which is a superset and modernized version for the TK-Interface."
    ).pack(pady = 10)

    ttk.Label(
        master = app,
        wraplength = 260,
        justify = "center",
        font = ("Calibri", 10),
        text = "The TK-Interface is a well known python wrapper for the language TCL, which is primarily used for GUI."
    ).pack(pady = 10)


    btn_theme = ttk.Button(
        master = app,
        text = "Toggle Dark/Light Mode",
        command = lambda: style.theme_use('darkly') if style.theme_use() == 'flatly' else style.theme_use('flatly')
    )
    btn_theme.bind("<Enter>", lambda e: btn_theme.configure(bootstyle = "info"))
    btn_theme.bind("<Leave>", lambda e: btn_theme.configure(bootstyle="primary"))

    btn_theme.pack(pady = 20)

    app.mainloop()

if __name__ == '__main__':
    main()
