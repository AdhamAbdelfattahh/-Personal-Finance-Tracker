import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

class FinanceTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("Personal Finance Tracker")
        
        # Input fields
        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack()

        self.category_label = tk.Label(master, text="Category:")
        self.category_label.pack()
        self.category_entry = tk.Entry(master)
        self.category_entry.pack()

        self.add_button = tk.Button(master, text="Add Transaction", command=self.add_transaction)
        self.add_button.pack()

        self.show_button = tk.Button(master, text="Show Report", command=self.show_report)
        self.show_button.pack()

        # Initialize data storage
        self.transactions = pd.DataFrame(columns=["Amount", "Category"])

    def add_transaction(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            new_transaction = pd.DataFrame([[amount, category]], columns=["Amount", "Category"])
            self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)

            # Clear entries
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Transaction added!")
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid amount.")

    def show_report(self):
        if not self.transactions.empty:
            summary = self.transactions.groupby("Category").sum()
            summary.plot(kind='bar')
            plt.title("Expenses by Category")
            plt.ylabel("Amount")
            plt.show()
        else:
            messagebox.showwarning("No Data", "No transactions to show.")

# Create the main application window
root = tk.Tk()
app = FinanceTrackerApp(root)
root.mainloop()
