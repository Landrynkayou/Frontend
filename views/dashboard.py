import tkinter as tk
from tkinter import ttk, filedialog
import customtkinter as ctk

class VotingSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting System")
        self.master.geometry("400x400")

        # Header
        self.header_label = tk.Label(master, text="Welcome to Voting System", font=("Helvetica", 16, "bold"))
        self.header_label.pack(pady=10)

        
        # Candidate 1
        self.candidate_frame1 = tk.Frame(master, bd=2, relief=tk.GROOVE)
        self.candidate_frame1.pack(pady=10)

        self.candidate_name1 = tk.Label(self.candidate_frame1, text="Candidate 1:", font=("Helvetica", 12))
        self.candidate_name1.grid(row=0, column=0, padx=10, pady=5)

        self.candidate_name_entry1 = tk.Entry(self.candidate_frame1)
        self.candidate_name_entry1.grid(row=0, column=1, padx=10, pady=5)

        self.upload_button1 = ctk.CTkButton(self.candidate_frame1, text="Upload Photo", command=lambda: self.upload_photo(1), style="yellow_black.TButton")
        self.upload_button1.grid(row=1, columnspan=2, padx=10, pady=5)

        self.vote_button1 = ctk.CTkButton(self.candidate_frame1, text="Vote", command=lambda: self.cast_vote(1), style="yellow_black.TButton")
        self.vote_button1.grid(row=2, columnspan=2, padx=10, pady=5)

        # Candidate 2
        self.candidate_frame2 = tk.Frame(master, bd=2, relief=tk.GROOVE)
        self.candidate_frame2.pack(pady=10)

        self.candidate_name2 = tk.Label(self.candidate_frame2, text="Candidate 2:", font=("Helvetica", 12))
        self.candidate_name2.grid(row=0, column=0, padx=10, pady=5)

        self.candidate_name_entry2 = tk.Entry(self.candidate_frame2)
        self.candidate_name_entry2.grid(row=0, column=1, padx=10, pady=5)

        self.upload_button2 = ctk.CTkButton(self.candidate_frame2, text="Upload Photo", command=lambda: self.upload_photo(2), style="yellow_black.TButton")
        self.upload_button2.grid(row=1, columnspan=2, padx=10, pady=5)

        self.vote_button2 = ctk.CTkButton(self.candidate_frame2, text="Vote", command=lambda: self.cast_vote(2), style="yellow_black.TButton")
        self.vote_button2.grid(row=2, columnspan=2, padx=10, pady=5)

    def upload_photo(self, candidate):
        # Open file dialog to select an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

        # Update candidate's photo based on selected file path
        if candidate == 1:
            # For demonstration, update candidate 1's photo
            pass
        elif candidate == 2:
            # For demonstration, update candidate 2's photo
            pass

    def cast_vote(self, candidate):
        # Logic to cast a vote for the selected candidate
        
        if candidate == 1:
            # For demonstration, increment the vote count for candidate 1
            pass
        elif candidate == 2:
            # For demonstration, increment the vote count for candidate 2
            pass


def main():
    root = tk.Tk()
    app = VotingSystemApp(root)
    root.mainloop()

if __name__ == "__main__":
       main()