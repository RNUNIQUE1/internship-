import tkinter as tk
from tkinter import messagebox

class ATMInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Interface")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        # Create frames
        self.header_frame = tk.Frame(self.master, bg="#333")
        self.header_frame.pack(fill="x")

        self.body_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.body_frame.pack(fill="both", expand=True)

        # Create header widgets
        self.header_label = tk.Label(self.header_frame, text="ATM Interface", font=("Arial", 24), fg="#fff", bg="#333")
        self.header_label.pack(pady=10)

        # Create body widgets
        self.account_number_label = tk.Label(self.body_frame, text="Account Number:", font=("Arial", 16))
        self.account_number_label.pack(pady=10)

        self.account_number_value = tk.Label(self.body_frame, text="1234567890", font=("Arial", 16))
        self.account_number_value.pack(pady=10)

        self.account_balance_label = tk.Label(self.body_frame, text="Account Balance:", font=("Arial", 16))
        self.account_balance_label.pack(pady=10)

        self.account_balance_value = tk.Label(self.body_frame, text="$1000.00", font=("Arial", 16))
        self.account_balance_value.pack(pady=10)

        self.transaction_options_frame = tk.Frame(self.body_frame)
        self.transaction_options_frame.pack(pady=10)

        self.withdraw_button = tk.Button(self.transaction_options_frame, text="Withdraw", font=("Arial", 16), command=self.withdraw)
        self.withdraw_button.pack(side="left", padx=10)

        self.deposit_button = tk.Button(self.transaction_options_frame, text="Deposit", font=("Arial", 16), command=self.deposit)
        self.deposit_button.pack(side="left", padx=10)

        self.balance_button = tk.Button(self.transaction_options_frame, text="Check Balance", font=("Arial", 16), command=self.check_balance)
        self.balance_button.pack(side="left", padx=10)

        self.transaction_form_frame = tk.Frame(self.body_frame)
        self.transaction_form_frame.pack(pady=10)

        self.amount_label = tk.Label(self.transaction_form_frame, text="Enter Amount:", font=("Arial", 16))
        self.amount_label.pack(pady=10)

        self.amount_entry = tk.Entry(self.transaction_form_frame, font=("Arial", 16), width=20)
        self.amount_entry.pack(pady=10)

        self.submit_button = tk.Button(self.transaction_form_frame, text="Submit", font=("Arial", 16), command=self.submit_transaction)
        self.submit_button.pack(pady=10)

    def withdraw(self):
        messagebox.showinfo("Withdraw", "Withdrawal successful!")

    def deposit(self):
        messagebox.showinfo("Deposit", "Deposit successful!")

    def check_balance(self):
        messagebox.showinfo("Balance", "Your account balance is $1000.00")

    def submit_transaction(self):
        amount = self.amount_entry.get()
        if amount:
            messagebox.showinfo("Transaction", "Transaction successful!")
        else:
            messagebox.showerror("Error", "Please enter an amount")

root = tk.Tk()
atm_interface = ATMInterface(root)
root.mainloop()