import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.result_var, width=25, font=('Arial', 16), bd=10, insertwidth=4, bg="powder blue", justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sqrt', 5, 0), ('x^y', 5, 1), ('C', 5, 2)
        ]

        for (text, row, col) in button_texts:
            button = tk.Button(self.master, text=text, padx=20, pady=20, font=('Arial', 14), bd=5, bg="light grey", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        for i in range(6):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set("")
        elif char == '=':
            self.evaluate()
        elif char == 'sqrt':
            self.calculate_sqrt()
        elif char == 'x^y':
            self.result_var.set(self.result_var.get() + '**')
        else:
            self.result_var.set(self.result_var.get() + char)

    def evaluate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero is not allowed")
            self.result_var.set("")
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            self.result_var.set("")

    def calculate_sqrt(self):
        try:
            result = math.sqrt(float(self.result_var.get()))
            self.result_var.set(result)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for square root")
            self.result_var.set("")
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
