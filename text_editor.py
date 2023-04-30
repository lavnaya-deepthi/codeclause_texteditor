import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
from tkinter import *



def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")

def clear():
    txt_edit.delete("1.0", tk.END)
    window.title("Text Editor")

def edit_file():

    dialog = tk.Toplevel()
    dialog.title("Replace")
    
    lbl_search = tk.Label(dialog, text="Find:")
    lbl_replace = tk.Label(dialog, text="Replace:")
    entry_search = tk.Entry(dialog)
    entry_replace = tk.Entry(dialog)
    btn_find_replace = tk.Button(dialog, text="Replace", command=lambda: find_and_replace(dialog, entry_search.get(), entry_replace.get()))
    
    lbl_search.grid(row=0, column=0, padx=5, pady=5)
    lbl_replace.grid(row=1, column=0, padx=5, pady=5)
    entry_search.grid(row=0, column=1, padx=5, pady=5)
    entry_replace.grid(row=1, column=1, padx=5, pady=5)
    btn_find_replace.grid(row=2, column=1, padx=5, pady=5)
    
def find_and_replace(dialog, search_text, replace_text):

    current_text = txt_edit.get("1.0", tk.END)
    new_text = current_text.replace(search_text, replace_text)
    txt_edit.delete("1.0", tk.END)
    txt_edit.insert(tk.END, new_text)
    dialog.destroy()

def print_file():
    text = txt_edit.get("1.0", tk.END)
    showinfo(title="Print", message=text)


window = tk.Tk()
window.title("Text Editor")

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(1, minsize=0, weight=1)

txt_edit = tk.Text(window)
txt_scroll = tk.Scrollbar(window, orient=tk.VERTICAL, command=txt_edit.yview)
txt_edit.configure(yscrollcommand=txt_scroll.set)



txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)

btn_open = tk.Button(fr_buttons, text="Open", command=open_file, bg="lightgray", fg="black",width=7)
btn_save = tk.Button(fr_buttons, text="Save", command=save_file, bg="lightgray", fg="black",width=7)
btn_clear = tk.Button(fr_buttons, text="clear", command=clear, bg="lightgray", fg="black",width=7)
btn_edit = tk.Button(fr_buttons, text="find/replace ", command=edit_file, bg="lightgray", fg="black",width=12)
btn_print = tk.Button(fr_buttons, text="Print", command=print_file, bg="lightgray", fg="black",width=7)


btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
btn_clear.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
btn_edit.grid(row=0, column=3, sticky="ew", padx=5, pady=5)
btn_print.grid(row=0, column=4, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="nsew")
txt_scroll.grid(row=1, column=1, sticky="nsew")
txt_edit.grid(row=1, column=0, sticky="nsew")


window.configure(bg="lightyellow")
txt_edit.configure(bg="beige", fg="black")




window.mainloop()

