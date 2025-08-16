import tkinter as tk
import random
from tkinter import messagebox

# Simulate getting weight from a scale
def get_weight():
    return round(random.uniform(0.1, 5.0), 2)  # random weight between 0.1 and 5 kg

class WeighingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Weighing Scale + Calculator")
        self.root.geometry("400x500")
        self.root.config(bg="black")
        
        self.total_bill = 0.0
        
        # Weight Display
        self.weight_var = tk.StringVar()
        self.weight_label = tk.Label(root, textvariable=self.weight_var,
                                     font=("Arial", 30, "bold"), bg="black", fg="lime")
        self.weight_label.pack(pady=10)
        
        # Price per kg
        self.price_label = tk.Label(root, text="Price per kg:", font=("Arial", 14), bg="black", fg="white")
        self.price_label.pack()
        self.price_entry = tk.Entry(root, font=("Arial", 14))
        self.price_entry.pack()
        
        # Cost display
        self.cost_var = tk.StringVar()
        self.cost_label = tk.Label(root, textvariable=self.cost_var,
                                   font=("Arial", 20, "bold"), bg="black", fg="yellow")
        self.cost_label.pack(pady=10)
        
        # Buttons
        btn_frame = tk.Frame(root, bg="black")
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Get Weight", font=("Arial", 14), bg="green", fg="white",
                  command=self.update_weight).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Add to Total", font=("Arial", 14), bg="blue", fg="white",
                  command=self.add_to_total).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Show Total", font=("Arial", 14), bg="orange", fg="white",
                  command=self.show_total).grid(row=0, column=2, padx=5)
        
        # Calculator
        self.calc_entry = tk.Entry(root, font=("Arial", 20), justify="right")
        self.calc_entry.pack(pady=10, fill="x")
        
        self.create_calculator()
    
    def update_weight(self):
        weight = get_weight()
        self.weight_var.set(f"Weight: {weight} kg")
        
        try:
            price = float(self.price_entry.get())
            cost = round(price * weight, 2)
            self.cost_var.set(f"Cost: ₹{cost}")
            self.current_cost = cost
        except ValueError:
            messagebox.showerror("Error", "Enter a valid price per kg")
    
    def add_to_total(self):
        if hasattr(self, 'current_cost'):
            self.total_bill += self.current_cost
            messagebox.showinfo("Added", f"Added ₹{self.current_cost} to total")
        else:
            messagebox.showerror("Error", "Get weight first")
    
    def show_total(self):
        messagebox.showinfo("Total Bill", f"Total: ₹{round(self.total_bill, 2)}")
    
    def click_button(self, value):
        if value == "=":
            try:
                result = eval(self.calc_entry.get())
                self.calc_entry.delete(0, tk.END)
                self.calc_entry.insert(tk.END, str(result))
            except:
                self.calc_entry.delete(0, tk.END)
                self.calc_entry.insert(tk.END, "Error")
        elif value == "C":
            self.calc_entry.delete(0, tk.END)
        else:
            self.calc_entry.insert(tk.END, value)
    
    def create_calculator(self):
        calc_frame = tk.Frame(self.root, bg="black")
        calc_frame.pack()
        
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]
        
        row, col = 0, 0
        for btn in buttons:
            tk.Button(calc_frame, text=btn, font=("Arial", 14), width=5, height=2,
                      command=lambda b=btn: self.click_button(b)).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

root = tk.Tk()
app = WeighingMachine(root)
root.mainloop()
