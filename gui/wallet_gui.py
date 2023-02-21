import tkinter as tk
from tkinter import ttk
from core.wallet import Wallet


class WalletGUI:
    def __init__(self, master):
        self.master = master
        master.title("Wallet GUI")

        # Set the size of the window
        master.geometry("400x300")

        # Create a frame with a card-like appearance and a shadow effect
        self.frame = tk.Frame(master, bg="#F0F0F0", bd=1, relief=tk.SOLID)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.frame.configure(width=300, height=200)
        self.frame.pack_propagate(0)

        # Create a label for the full name field
        self.full_name_label = tk.Label(self.frame, text="Full Name:")
        self.full_name_label.pack(pady=(30, 0))

        # Create an entry field for the full name
        self.full_name_entry = ttk.Entry(self.frame, width=30)
        self.full_name_entry.pack()

        # Create a label for the password field
        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.pack(pady=(10, 0))

        # Create an entry field for the password
        self.password_entry = ttk.Entry(self.frame, width=30, show="*")
        self.password_entry.pack()

        # Create a button to create a wallet
        self.create_wallet_button = ttk.Button(self.frame, text="Create Wallet", command=self.create_wallet)
        self.create_wallet_button.pack(pady=(20, 0))

    def create_wallet(self):
        wallet_created = Wallet(self.full_name_entry.get())
        print(wallet_created.to_json())