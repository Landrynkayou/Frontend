
import customtkinter
import tkinter as tk
from tkinter import ttk

class ResultView(customtkinter.CTkFrame):

    def __init__(self, parent, title=""):
        super().__init__(parent)  # Call the parent class constructor
        self.coursePanel_frame = customtkinter.CTkScrollableFrame(parent, height=850,width=950)
        self.coursePanel_frame.grid(row=0, column=1, padx=(10, 0), pady=(10, 0), sticky="nsew")
        if title:
            self.logo_label = customtkinter.CTkLabel(self.coursePanel_frame, text=title,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        table = ttk.Treeview(self.coursePanel_frame, columns=("Column 1", "Column 2", "Column 3","Column 4"))
        table.grid(row=1, column=0, padx=(10, 0), pady=(10, 0), sticky="nsew")
        # Define column headings
        # table.heading("#0", text="ID")  # Optional for automatic row numbering
        table.heading("Column 1", text="Candidate")
        table.heading("Column 2", text="Number of Votes")
        table.heading("Column 3", text="% of Vote")
        # table.heading("Column 4", text="Column 3")

        # Set column widths (optional)
        table.column("#0", width=10)  # Adjust widths as needed
        table.column("Column 1", width=150)
        table.column("Column 2", width=150)
        table.column("Column 3", width=150)
        table.column("Column 4", width=10)

        # Show table headings (optional)
        # table.show("headings")

        # # Insert data (replace with your actual data source)
        table.insert("", tk.END, values=("Data 1.1", "Data 1.2", "Data 1.3"))
        table.insert("", tk.END, values=("Data 2.1", "Data 2.2", "Data 2.3"))

        # # Pack the table into the root window
        # table.pack(fill=tk.BOTH, expand=True)
