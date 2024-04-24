
import customtkinter
import tkinter as tk
from tkinter import ttk
# from PIL import Image
from customtkinter import CTkLabel


class CandidateView(customtkinter.CTkFrame):

    def __init__(self, parent, title=""):
        super().__init__(parent)  # Call the parent class constructor
        self.coursePanel_frame = customtkinter.CTkScrollableFrame(
            parent, height=850, width=950)
        self.coursePanel_frame.grid(row=0, column=1, padx=(
            10, 0), pady=(10, 0), sticky="nsew")
        if title:
            self.logo_label = customtkinter.CTkLabel(self.coursePanel_frame, text=title,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        candidates = [{
            "id": 1,
            "name": "Test 12"
        }, {
            "id": 2,
            "name": "Test 33"
        },{
            "id": 3,
            "name": "Test 44"
        }, {
            "id": 4,
            "name": "Test 55"
        },{
            "id": 5,
            "name": "Test 01"
        }, {
            "id": 6,
            "name": "Test 66"
        }
        ]
        row = 1
        col = 0
        for candidate in candidates:
            self.voting_frame = customtkinter.CTkFrame(
                self.coursePanel_frame, height=200, width=200)
            self.voting_frame.grid(row=row, column=col, padx=(
                10, 0), pady=(10, 0))
            self.candidate_label = customtkinter.CTkLabel(self.voting_frame, text=candidate["name"],
                                                          font=customtkinter.CTkFont(size=20, weight="bold"))
            self.candidate_label.grid(row=0, column=0, padx=20, pady=(20, 10))
            self.candidate_btn = customtkinter.CTkButton(self.voting_frame, text="Vote",
                                                         font=customtkinter.CTkFont(
                                                             size=18, weight="bold"),
                                                         height=20, width=20)
            self.candidate_btn.grid(row=1, column=1, padx=(
                10, 0), pady=(10, 0))
            col = col + 1
            if col == 3:
                print(row)
                row = row +1
                col = 0
